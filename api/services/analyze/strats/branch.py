from api.models.bnb.nodum import Nodum
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

from constants.structure import BOOL_RANGE, T0_SYM, T1_SYM
from utils.consts import FLOAT_ZERO, INFTY, W_LBL
from utils.funcs import emd, get_labels

from icecream import ic


class Branch(Sia):
    """Class Branch is used to solve the mip problem using Branch&Bound strategy."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        causes: list[int],
        distrib: NDArray[np.float64],
        dual: bool,
    ) -> None:
        super().__init__(structure, effect, causes, distrib, dual)

        self.__effect_labels: None | list[str] = None
        self.__causes_labels = None

        self.__net: nx.Graph = nx.Graph()

    def analyze(self) -> bool:
        max_len = max(*self._effect, *self._causes) + 1
        labels = get_labels(max_len)
        self.__effect_labels = [f'{labels[i]}{T1_SYM}' for i in self._effect]
        self.__causes_labels = [f'{labels[j]}{T0_SYM}' for j in self._causes]
        ic(self.__causes_labels, self.__effect_labels)

        self.__net = self.margin_n_expand()

        #
        raise NotImplementedError
        part: None = None
        mip = self.label_mip(part)
        self.min_info_part = mip
        not_std_sln = any(
            [
                # ! Store the network, generate the id and return it as callback in front ! #
                self.integrated_info == INFTY,
                self.min_info_part is None,
                self.sub_distrib is None,
                self.network_id is None,
            ]
        )

        return not_std_sln

    def margin_n_expand(self) -> nx.Graph:
        concept_comb = list(it.product(self._causes, self._effect))

        possible_edges: list[tuple[str, str, float]] = []

        # possible_edges = [
        #     (
        #         self.__causes_labels[self._causes.index(c)],
        #         self.__effect_labels[self._effect.index(e)],
        #         -1,
        #     )
        #     for c, e in concept_comb
        # ]

        # self.__net.add_weighted_edges_from(possible_edges)
        # self.plot_net(self.__net)
        """
        self._effect: [0, 4], self._causes: [0, 2, 4]
        ic| self.__effect_labels: ['A(t=1)', 'E(t=1)']
            self.__causes_labels: ['A(t=0)', 'C(t=0)', 'E(t=0)']"""
        sub_concepts: list[tuple[int, int]] = []
        for idx_causes, idx_effect in concept_comb:
            # Iteramos las aristas ya definidas en el producto causa efecto
            # ! Por qué no re-instanciar la matriz (no la clase)? [#15] ! #
            sub_struct: Structure = copy.deepcopy(self._structure)
            sub_mat: Matrix = sub_struct.get_tensor()[idx_effect]

            sub_states: list[int] = copy.deepcopy(self._causes)
            sub_states.remove(idx_causes)

            # ic(sub_mat.as_dataframe())

            sub_mat.margin(sub_states, data=True)
            sub_mat.expand(self._causes, data=True)

            # ic(sub_mat.as_dataframe())

            effect = {bin: ([] if self._dual == bin else self._effect) for bin in BOOL_RANGE}
            causes = {bin: ([] if self._dual == bin else self._causes) for bin in BOOL_RANGE}
            iter_distrib = sub_struct.create_distrib(effect, causes, data=True)[
                StructProps.DIST_ARR
            ]
            # ic(self.__causes_labels, self.__effect_labels)
            origin = self.__causes_labels[self._causes.index(idx_causes)]
            destiny = self.__effect_labels[self._effect.index(idx_effect)]

            edge_emd = emd(iter_distrib, self._target_dist)
            if edge_emd > FLOAT_ZERO:
                # ic(origin, destiny, edge_emd)
                # ! Maybe doesn't have order because the edge is undirected, so the order doesn't matter [#17] ! #
                possible_edges.append((origin, destiny, edge_emd))
            else:
                # ! Por qué no en vez de poner todas las aristas e irlas quitando hasat encontrar una bipartición, mejor no se añaden las que tengan peso y al final valida si el grafo es conexo? [#16] !
                sub_concepts.append((idx_effect, idx_causes))
        # Añadimos los nodos:
        self.__net.add_nodes_from(self.__effect_labels)
        self.__net.add_nodes_from(self.__causes_labels)

        # Añadimos las aristas:
        self.__net.add_weighted_edges_from(possible_edges)
        # self.plot_net(self.__net)
        ic(possible_edges)
        ic(self.__net.edges(data=True))
        # self.plot_net(self.__net)

        if nx.is_connected(self.__net):
            ic('Es conexo')
            self.branch_and_bound()
        else:
            ic('No es conexo')
        ic(self._effect, self._causes, sub_concepts)
        # [self.__causes_labels[self._causes.index(idx_causes)]]
        # [self.__effect_labels[self._effect.index(idx_effect)]]
        # [W_LBL] = edge_emd
        # possible_edges

        # to_margin = [idx for idx in self.]

    def branch_and_bound(self) -> tuple[tuple[tuple[str], tuple[str]]]:
        origin: Nodum = Nodum(ub=0.0, net=self.__net.copy())

        # We create a priority queue to store the nodes
        queue: list[Nodum] = []
        pq.heappush(queue, (FLOAT_ZERO, origin))

        gb: float = INFTY
        minimal_loss: Nodum = Nodum(ub=INFTY, net=self.__net.copy())

        origin_net = origin.get_net()

        m: int = len(self._effect)
        n: int = len(self._causes)
        limit: int = 2 ** (m + n - 1)

        while len(queue) > 0:
            _, son = pq.heappop(queue)
            son: Nodum
            ic(str(son))

            if any(
                (
                    len(son.get_ignored().keys()) == len(son.get_ordered_edges()),
                    son.get_ub() >= gb,
                )
            ):
                continue
            left: Nodum = Nodum(
                ub=son.get_ub(),
                net=son.get_net().copy(),
                ignore=son.get_ignored().copy(),
            )
            # Ordenamos las aristas para ignorar la primera
            for edge in left.get_ordered_edges():
                if (edge[0], edge[1]) in left.get_ignored().keys():
                    continue
                left.ignore_new((edge[0], edge[1]), set(edge[1]))
                break

            right: Nodum = Nodum(
                ub=son.get_ub(),
                net=son.get_net().copy(),
                ignore=son.get_ignored().copy(),
            )
            for edge in right.get_ordered_edges():
                if (edge[0], edge[1]) in right.get_ignored().keys():
                    continue
                r_net: nx.Graph = right.get_net()

                right._ub += self.calculate_ub(right, edge)

                r_net.remove_edge(edge[0], edge[1])
                break

            if nx.is_connected(right.get_net()):
                pq.heappush(queue, (right.get_ub(), right))
            elif right.get_ub() < gb:
                gb = round(right.get_ub(), 4)
                if right.get_ub() < minimal_loss.get_ub():
                    minimal_loss: Nodum = right

            if nx.is_connected(left.get_net()):
                pq.heappush(queue, (right.get_ub(), right))
            elif left.get_ub() < gb:
                gb = round(left.get_ub(), 4)
                if left.get_ub() < minimal_loss.get_ub():
                    minimal_loss: Nodum = left

            #
            limit -= 1
            if limit < 0:
                raise HTTPException(
                    # status_code=status.HTTP_406_NOT_ACCEPTABLE,
                    status_code=status.HTTP_508_LOOP_DETECTED,
                    detail='Maximal limit has been reached.',
                )

        ic()
        ic(minimal_loss.get_ub(), minimal_loss.get_net())

    def calculate_ub(self, right: Nodum, edge: tuple[str, str, float]) -> float:
        return edge[2][W_LBL]

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

        # Draw the bipartite graph
        nx.draw(net, pos=pos, with_labels=True)

        # Add edge labels
        labels = nx.get_edge_attributes(net, W_LBL)
        # Displace the labels horizontally
        for (u, v), weight in labels.items():
            offset = np.random.default_rng(seed=1).uniform(-0.2, 0.2)
            pos_y = (pos[u][1] + pos[v][1]) / 2 + offset
            pos_x = (pos[u][0] + pos[v][0]) / 2 + offset
            plt.text(pos_x, pos_y, weight, ha='center', va='center')

        # Show the plot
        plt.show()

    def biplot(self, net1: nx.Graph, net2: nx.Graph) -> None:
        """This function is used to plot two networks side by side."""
        _, axs = plt.subplots(1, 2, figsize=(12, 6))

        def plot_single_net(ax, net):
            future_nodes = [node for node in net.nodes if node in self._future_labels]
            current_nodes = [node for node in net.nodes if node in self._current_labels]
            pos = {}
            try:
                pos.update((node, (1, index)) for index, node in enumerate(future_nodes))
                pos.update((node, (0, index)) for index, node in enumerate(current_nodes))
            except KeyError:
                pass
            nx.draw(net, pos=pos, with_labels=True, ax=ax)
            labels = nx.get_edge_attributes(net, W_LBL)
            for (u, v), weight in labels.items():
                offset = np.random.default_rng(seed=1).uniform(-0.2, 0.2)
                pos_y = (pos[u][1] + pos[v][1]) / 2 + offset
                pos_x = (pos[u][0] + pos[v][0]) / 2 + offset
                ax.text(pos_x, pos_y, weight, ha='center', va='center')

        plot_single_net(axs[0], net1)
        plot_single_net(axs[1], net2)

        plt.show()
