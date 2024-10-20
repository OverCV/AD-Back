from api.models.props.structure import StructProps
from api.services.analyze.sia import Sia
from api.models.matrix import Matrix
from api.models.structure import Structure

import itertools as it
import copy
import heapq as pq

from fastapi import HTTPException, status
import numpy as np
from numpy.typing import NDArray
import networkx as nx
from matplotlib import pyplot as plt

from api.models.queyranne.deletion import Deletion

from constants.dummy import (
    DUMMY_DELETION,
    DUMMY_NET_INT_ID,
    DUMMY_SUBDIST,
    DUMMY_MIN_INFO_PARTITION,
)
from constants.structure import BIN_RANGE, BOOL_RANGE, T0_SYM, T1_SYM
from utils.consts import (
    EMPTY_STR,
    FIRST,
    FLOAT_ZERO,
    INFTY_POS,
    INT_ONE,
    INT_ZERO,
    LAST_IDX,
    U_IDX,
    V_IDX,
    DATA_IDX,
    WT_LBL,
)
from utils.funcs import emd_pyphi, get_labels


import utils.network as net

from icecream import ic

from server import conf


class QRNodes(Sia):
    """Class queyranne is used to solve the mip problem using the edges strategy."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        actual: list[int],
        distrib: NDArray[np.float64],
        dual: bool,
    ) -> None:
        super().__init__(structure, effect, actual, distrib, dual)

        self.__effect_labels: None | list[str] = None
        self.__causes_labels: None | list[str] = None

        self.__net: nx.DiGraph | nx.Graph = nx.DiGraph() if conf.directed else nx.Graph()

    def analyze(self) -> bool:
        max_len = max(*self._effect, *self._actual) + 1
        labels = get_labels(max_len)
        self.__effect_labels = [f'{labels[i]}{T1_SYM}' for i in self._effect]
        self.__causes_labels = [f'{labels[j]}{T0_SYM}' for j in self._actual]

        ic(self.__effect_labels, self.__causes_labels)

        # ! Establecer mejor qué retorna la función (Grafo + ?) [#17] ! #
        partition: Deletion = self.strategy()

        self.integrated_info = partition.get_minuend_emd()
        self.network_id = DUMMY_NET_INT_ID
        self.sub_distrib = partition.get_subdist()
        self.min_info_part = partition.get_omega() + [partition.get_edge()]

        not_std_sln = any(
            [
                # ! Store the network, generate the id and return it as callback in front ! #
                self.integrated_info == INFTY_POS,
                self.min_info_part is None,
                self.sub_distrib is None,
                self.network_id is None,
            ]
        )

        return not_std_sln

    def strategy(self) -> Deletion:
        actual = [(INT_ZERO, i) for i in self._actual]
        effect = [(INT_ONE, j) for j in self._effect]
        ic(actual, effect)

        rep_one, rep_two = BOOL_RANGE

        MAX_ITER = 4
        iteration = 0
        SEP1 = '\\' * 20 + '/' * 20
        SEP2 = '*' * 40
        SEP3 = '-' * 40

        alpha: set[tuple[int, int]] = set(actual + effect)
        best_deletion: Deletion | None = None

        # Iteramos sobre cada posible punto de inicio
        for t in alpha:
            # Elementos restantes sin t
            t_com = alpha - {t}
            # Iniciamos omega con t
            omega: set[tuple[int, int]] = {t}
            # ic(t, t_com)

            print(SEP1)

            while len(omega) < len(alpha):
                print(SEP2)
                all_mips: list[Deletion] = []
                remaining = t_com - omega

                for u in remaining:
                    # Evaluación de u con omega
                    idx_o_actual = {bin: [] for bin in BOOL_RANGE}
                    idx_o_effect = {bin: [] for bin in BOOL_RANGE}
                    o_concept = (idx_o_actual, idx_o_effect)

                    # Conjunto temporal omega + u
                    betha = omega | {u}

                    # Procesamos los elementos en betha
                    for p, q in betha:
                        o_concept[1 - p][rep_one].append(q)

                    # Procesamos elementos restantes
                    o_com = remaining - {u}
                    for i, j in o_com:
                        o_concept[1 - i][rep_two].append(j)

                    ic(betha, o_com)

                    o_effect, o_actual = o_concept
                    o_effect = {k: sorted(v) for k, v in o_effect.items()}
                    o_actual = {k: sorted(v) for k, v in o_actual.items()}
                    ic(o_effect)
                    ic(o_actual)

                    # Calculamos EMD del conjunto
                    o_dist = copy.deepcopy(self._structure)
                    omega_hist = o_dist.create_distrib(o_effect, o_actual, data=True)
                    omega_dist = omega_hist[StructProps.DIST_ARRAY]
                    o_emd = emd_pyphi(*omega_dist, *self._target_dist)
                    print(f'{o_emd=:.2f}', omega_dist)

                    print(SEP3)

                    # Evaluación individual de u
                    idx_u_actual = {bin: [] for bin in BOOL_RANGE}
                    idx_u_effect = {bin: [] for bin in BOOL_RANGE}
                    u_concept = (idx_u_actual, idx_u_effect)

                    # Procesamos el elemento u
                    p, q = u
                    u_concept[1 - p][rep_one].append(q)

                    # Procesamos los elementos restantes
                    u_com = alpha - {u}
                    for i, j in u_com:
                        u_concept[1 - i][rep_two].append(j)

                    ic(u, u_com)

                    u_effect, u_actual = u_concept
                    u_effect = {k: sorted(v) for k, v in u_effect.items()}
                    u_actual = {k: sorted(v) for k, v in u_actual.items()}
                    ic(u_effect)
                    ic(u_actual)

                    # Calculamos EMD individual
                    u_dist = copy.deepcopy(self._structure)
                    u_hist = u_dist.create_distrib(u_effect, u_actual, data=True)
                    u_dist = u_hist[StructProps.DIST_ARRAY]
                    u_emd = emd_pyphi(*u_dist, *self._target_dist)
                    # print(f'{u_emd=:.2f}', u_dist)

                    # Creamos el objeto Deletion con la información
                    current_mip = Deletion(
                        edge=u,
                        omega=list(o_com.copy()),  # Convertimos el set a lista
                        minuend_emd=o_emd,
                        subtrahend_emd=u_emd,
                        emd=o_emd - u_emd,
                        subdist=omega_dist,  # Tomando la del conjunto
                    )
                    all_mips.append(current_mip)

                    # print(f'{o_emd:.2f} - {u_emd:.2f} = {o_emd - u_emd:.2f}')
                    print(SEP3)

                # Seleccionamos el mejor MIP de esta iteración
                best_mip = min(all_mips, key=lambda x: x.get_emd())
                omega.add(best_mip.get_edge())

                # Actualizamos el mejor global si es necesario
                if best_deletion is None or best_mip.get_emd() < best_deletion.get_emd():
                    best_deletion = best_mip

                ic(str(best_deletion))

            # iteration += 1
            # if iteration == MAX_ITER:
            #     break

        # Siempre retornamos el mejor encontrado
        return best_deletion

    # def strategy(self) -> Deletion:
    #     """

    #     OR1 = {(0, 1)=t, (1, 2)=u} COM OR1 = {(1, 0), (0, 2), (1, 1), (0, 0)}
    #     OR2 = {(1, 2)}             COM OR2 = {(0, 1)=t, (0, 0), (0, 2), (1, 1), (1, 0)}

    #     OR1 = {bC}.                COM OR1 = {AcBa}
    #     o_concept = act{False: [b], True: [ca]}, eff{False: [C], True: [AB]}
    #     o_actual  = {False: [1], True: [2,0]}
    #     o_effect  = {False: [2], True: [0,1]}

    # """
    # ic| t: (0, 1), u: (1, 2), u_com: {(1, 0), (0, 2), (1, 1), (0, 0)}
    # ic| t: (0, 1), u: (0, 0), u_com: {(1, 0), (1, 1), (1, 2), (0, 2)}
    # ic| t: (0, 1), u: (1, 1), u_com: {(1, 0), (0, 2), (1, 2), (0, 0)}
    # ic| t: (0, 1), u: (0, 2), u_com: {(1, 0), (1, 1), (1, 2), (0, 0)}
    # ic| t: (0, 1), u: (1, 0), u_com: {(0, 2), (1, 1), (1, 2), (0, 0)}

    # W = b, u = C, V = AcBa

    # """

    def submodule(self, omega, x, minuend, subtrahend) -> float:
        # Si la arista no genera pérdida individual o conjuntamente, se eliminará
        if len(omega) > 0:
            return (
                minuend + subtrahend
                if x[V_IDX] != (omega[LAST_IDX][V_IDX] if omega else EMPTY_STR)
                else max(minuend, subtrahend)
            )
        return subtrahend

    def set_network_data(self, concepts: list[tuple[int, int]]) -> None:
        self.__net.add_nodes_from(self.__effect_labels)
        self.__net.add_nodes_from(self.__causes_labels)
        self.__net.add_edges_from(
            (
                (
                    self.__causes_labels[self._actual.index(j)],
                    self.__effect_labels[self._effect.index(i)],
                )
                for j, i in concepts
            )
        )

    def actual_edge_by_index(self, index):
        return self.__causes_labels[self._actual.index(index)]

    def effect_edge_by_index(self, index):
        return self.__effect_labels[self._effect.index(index)]


    def plot_net(self, net: nx.Graph) -> None:
        """This function is used to plot the network."""
        # Separate the nodes into two sets
        future_nodes = [node for node in net.nodes if node in self.__effect_labels]
        current_nodes = [node for node in net.nodes if node in self.__causes_labels]

        # Create a bipartite layout
        pos = {}
        try:
            pos.update((node, (1, index)) for index, node in enumerate(future_nodes))
            pos.update((node, (0, index)) for index, node in enumerate(current_nodes))
        except KeyError:
            pass

        # Draw the bipartite graph with custom node and edge colors
        nx.draw(
            net,
            pos=pos,
            with_labels=True,
            node_color='skyblue',
            font_color='black',
            edge_color='gray',
        )

        # Add edge labels with better visibility and consistent styles
        labels = nx.get_edge_attributes(net, 'weight')
        for (u, v), weight in labels.items():
            offset = np.random.default_rng(seed=1).uniform(-0.2, 0.2)

            # Calculate the position for the label closer to the destination node
            pos_y = pos[v][1] + (pos[u][1] - pos[v][1]) * 0.3 + offset
            pos_x = pos[v][0] + (pos[u][0] - pos[v][0]) * 0.3 + offset

            plt.text(
                pos_x,
                pos_y,
                weight,
                ha='center',
                va='center',
                fontsize=8,  # You can adjust the fontsize as needed
                bbox=dict(
                    facecolor='white', edgecolor='none', alpha=0.2
                ),  # Add a background to the text for better visibility
            )

        # Show the plot
        plt.show()
