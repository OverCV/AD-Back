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

from constants.dummy import DUMMY_NET_INT_ID, DUMMY_SUBDIST, DUMMY_MIN_INFO_PARTITION
from constants.structure import BOOL_RANGE, T0_SYM, T1_SYM
from utils.consts import (
    EMPTY_STR,
    FIRST,
    FLOAT_ZERO,
    INFTY_POS,
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


class QREdges(Sia):
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

        # ic(self.__effect_labels, self.__causes_labels)

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
        edges_idx: list[tuple[int, int]] = list(it.product(self._actual, self._effect))
        struct = copy.deepcopy(self._structure)

        self.set_network_data(edges_idx)

        omega = []
        alpha = edges_idx[:]
        k_iter = 0
        # for _ in edges_idx:
        while len(alpha) > 0:
          # print(k_iter)
            # ziter_dels: list[Deletion] = []
            uiter_dels: list[Deletion] = []
            iter_part: list[Deletion] = []
            betha: list[tuple[int, int]] = []
            for z in alpha:
                minuend_emd, subtrahend_emd, subdist, substruct = self.calcule_emd(
                    omega, z, copy.deepcopy(struct)
                )
                # Peso 0 -> __net Delete & add omega -> iter_2: remove omega -> crash!
                trimmed_net = self.remove_edges(copy.deepcopy(self.__net), omega + [z])

                zdeletion: Deletion = Deletion(
                    z,
                    omega,
                    minuend_emd,
                    subtrahend_emd,
                    minuend_emd - subtrahend_emd,
                    net.is_disconnected(trimmed_net),
                    subdist,
                )
                # ic(str(zdeletion))
                if self.submodule(omega, z, minuend_emd, subtrahend_emd) == FLOAT_ZERO:
                    struct.set_matrix(z[V_IDX], substruct.get_matrix(z[V_IDX]))

                    if net.is_disconnected(trimmed_net):
                        iter_part.append(zdeletion)

                  # print('Delete:', z)
                    omega.append(z)
                else:
                    # Añadimos las aristas con peso para revisarlas
                    betha.append(z)

                # ziter_dels.append(deletion) #? Iteración para eliminar aristas con peso 0

            for u in betha:
                # Proceso de remuestreo sin aristas peso 0
                # ic(u)
                minuend_emd, subtrahend_emd, subdist, substruct = self.calcule_emd(
                    omega, u, copy.deepcopy(struct)
                )
                trimmed_net = self.remove_edges(copy.deepcopy(self.__net), omega + [u])
                xdeletion: Deletion = Deletion(
                    u,
                    omega,
                    minuend_emd,
                    subtrahend_emd,
                    minuend_emd - subtrahend_emd,
                    net.is_disconnected(trimmed_net),
                    subdist,
                )
                # ic(str(xdeletion))

                if xdeletion.is_disconn():
                    iter_part.append(xdeletion)
                else:
                    uiter_dels.append(xdeletion)

            if len(iter_part) > 0:
                min_iter = min(
                    iter_part,
                    key=lambda x: x.get_minuend_emd(),
                )  # End condition
              # print(str(min_iter))
                return min_iter

            min_lose = min(uiter_dels, key=lambda x: x.get_emd())  # Reduce alpha
          # print(str(min_lose))

            omega.append(min_lose.get_edge())
            # ic(omega)
            alpha = [edge for edge in alpha if edge not in omega]

            k_iter += 1

        # print(omega, alpha)

    def submodule(self, omega, x, minuend, subtrahend) -> float:
        # Si la arista no genera pérdida individual o conjuntamente, se eliminará
        if len(omega) > 0:
            return (
                minuend + subtrahend
                if x[V_IDX] != (omega[LAST_IDX][V_IDX] if omega else EMPTY_STR)
                else max(minuend, subtrahend)
            )
        return subtrahend

    def calcule_emd(
        self,
        omega: list[tuple[int, int]],
        concept: tuple[int, int],
        structure: Structure,
    ) -> tuple[float, float, NDArray[np.float64], Structure]:
        actual, effect = concept
        effect_dist = {bin: ([] if self._dual == bin else self._effect) for bin in BOOL_RANGE}
        actual_dist = {bin: ([] if self._dual == bin else self._actual) for bin in BOOL_RANGE}
        # Modificar las matrices por referencia altera la estructura
        mat_y = structure.get_matrix(effect)

        # Marginalizamos sólo el tiempo (t)
        actual_states = self._actual[:]
        actual_states.remove(actual)

        mat_y.margin(actual_states)
        mat_y.expand(self._actual)

        # Se define las particiones primales y duales, en este escenario no se ha particionado por mover un estado futuro a su complemento, sino que toda la distribución está en una sección, tal que no requiere complementación

        iter_distrib = structure.create_distrib(effect_dist, actual_dist, data=True)[
            StructProps.DIST_ARRAY
        ]
        subtrahend_emd = emd_pyphi(*iter_distrib, *self._target_dist)

        # for loop [o_mat = struct.matrix(effect) -> margin] to remove omegas in struct_x, as they're different of x
        for w_actual, w_effect in omega:
            mat_y = structure.get_matrix(w_effect)

            w_actual_states = self._actual[:]
            w_actual_states.remove(w_actual)

            mat_y.margin(w_actual_states)
            mat_y.expand(self._actual)

        w_iter_distrib: NDArray[np.float64] = structure.create_distrib(
            effect_dist, actual_dist, data=True
        )[StructProps.DIST_ARRAY]
        minuend_emd = emd_pyphi(*w_iter_distrib, *self._target_dist)

        return minuend_emd, subtrahend_emd, w_iter_distrib, structure

    def margin_wu(self, omega, structure):
        # concept_keys: dict[str, list[int]] = {k: [t for t, _ in omega] for _, k in omega}
        # for w_effect, w_actual_states in concept_keys.items():
        #     mat_x = structure.get_matrix(w_effect)

        #     mat_x.margin(w_actual_states)
        #     mat_x.expand(self._actual)

        for w_actual, w_effect in omega:
            mat_x = structure.get_matrix(w_effect)

            w_actual_states = self._actual[:]
            w_actual_states.remove(w_actual)

            mat_x.margin(w_actual_states)
            mat_x.expand(self._actual)

    def remove_edges(
        self, net: nx.Graph | nx.DiGraph, edges: list[tuple[int, int]]
    ) -> nx.Graph | nx.DiGraph:
        for u, v in edges:
            net.remove_edge(
                self.actual_edge_by_index(u),
                self.effect_edge_by_index(v),
            )
        return net

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

    # # self.__net = self.remove_edges(self.__net, [x])

    # if net.is_disconnected(trimmed_net):
    #     # Disconexo => reestablecemos la arista, guardamos la MIP.
    #     # self.__net.add_weighted_edges_from([(*x, subtrahend_emd)])
    #     iter_part.append(deletion)

    # elif minuend_emd > FLOAT_ZERO and subtrahend_emd > FLOAT_ZERO:
    #     # Conexo & hay pérdida => restablecemos la arsita.
    #     # ? self.remove_edges(self.__net, [x])
    #     # self.__net.add_weighted_edges_from([(*x, subtrahend_emd)])
    #     ...

    # else:
    #     # Conexo & no hay pérdida => guardamos la arista. A su vez guardamos estas aristas en 0 para la reconstrucción.
    #     iter_dels.append(deletion)
    #     struct.set_matrix(x[V_IDX], substruct.get_matrix(x[V_IDX]))

    # self.plot_net(self.__net)

    # self.plot_net(trimmed_net)

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
