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
from utils.consts import FIRST, FLOAT_ZERO, INFTY_POS, INT_ZERO, U_IDX, V_IDX, DATA_IDX, WT_LBL
from utils.funcs import emd_pyphi, get_labels


import utils.network as net

from icecream import ic

from server import conf


class Queyranne(Sia):
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
        # self.__net = self.strategy()
        partition = self.strategy()

        # edges = self.__net.edges(data=True)
        # self.integrated_info = min([edge[DATA_IDX][WT_LBL] for edge in edges])
        # self.integrated_info = partition.get_minuend_emd()

        # raise NotImplementedError
        # part: None = None
        # mip = self.label_mip(part)
        # ic(
        #     self.integrated_info,
        #     self.min_info_part,
        #     self.sub_distrib,
        #     self.network_id,
        # )

        self.network_id = DUMMY_NET_INT_ID
        # self.sub_distrib = partition.get_subdist()
        # self.min_info_part = partition.get_omega() + [partition.get_edge()]
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

        self.set_network_data(edges_idx)

        omega = []
        alpha = edges_idx[:]
        ic(self.__net.edges)

        for _ in edges_idx:
            iter_dels: list[Deletion] = []
            iter_mips = []
            for x in alpha:
                minuend_emd, subtrahend_emd, subdist = self.calcule_emd(omega, x)

                trimmed_net = self.remove_edges(
                    self.__net.copy(),
                    omega + [x],
                )
                deletion: Deletion = Deletion(
                    x,
                    omega,
                    minuend_emd,
                    subtrahend_emd,
                    minuend_emd - subtrahend_emd,
                    net.is_disconnected(trimmed_net),
                    subdist,
                )

                if net.is_disconnected(trimmed_net):
                    iter_mips.append(deletion)
                    self.__net

                iter_dels.append(deletion)
                ic(str(deletion))
                # print([str(lose) for lose in iter_deletions], end='\n')
                # self.plot_net(self.__net)

                # self.plot_net(trimmed_net)
                # self.plot_net(self.__net)

            min_lose = min(iter_dels, key=lambda x: x.get_emd())
            mip_iter = [x for x in iter_dels if x.is_disconn()]
            str(min_lose)

            if len(mip_iter) > 0:
                min_mip_iter = min(mip_iter, key=lambda x: x.get_emd())
                ic(str(min_mip_iter))
                return min_mip_iter

            print(str(min_lose))

            alpha.remove(min_lose.get_edge())
            omega.append(min_lose.get_edge())

        # print(omega, alpha)

    def calcule_emd(
        self,
        omega: list[tuple[int, int]],
        concept: tuple[int, int],
    ) -> tuple[float, float, NDArray[np.float64]]:
        actual, effect = concept
        struct = copy.deepcopy(self._structure)
        # y_struct = copy.deepcopy(self._structure)

        # Modificar las matrices por referencia altera la estructura
        mat = struct.get_matrix(effect)

        # Marginalizamos sólo el tiempo (t)
        actual_states = self._actual[:]
        actual_states.remove(actual)

        mat.margin(actual_states)
        mat.expand(self._actual)

        # Se define las particiones primales y duales, en este escenario no se ha particionado por mover un estado futuro a su complemento, sino que toda la distribución está en una sección, tal que no requiere complementación
        effect_dist = {bin: ([] if self._dual == bin else self._effect) for bin in BOOL_RANGE}
        actual_dist = {bin: ([] if self._dual == bin else self._actual) for bin in BOOL_RANGE}

        iter_distrib = struct.create_distrib(effect_dist, actual_dist, data=True)[
            StructProps.DIST_ARRAY
        ]
        subtrahend_emd = emd_pyphi(*iter_distrib, *self._target_dist)

        # for loop [o_mat = struct.matrix(effect) -> margin] to remove omegas in struct_x, as they're different of x
        for w_actual, w_effect in omega:
            mat = struct.get_matrix(w_effect)

            w_actual_states = self._actual[:]
            w_actual_states.remove(w_actual)

            mat.margin(w_actual_states)
            mat.expand(self._actual)

        w_iter_distrib: NDArray[np.float64] = struct.create_distrib(
            effect_dist, actual_dist, data=True
        )[StructProps.DIST_ARRAY]
        minuend_emd = emd_pyphi(*w_iter_distrib, *self._target_dist)

        return minuend_emd, subtrahend_emd, w_iter_distrib


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
