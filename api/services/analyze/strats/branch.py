from fastapi import HTTPException
from api.services.analyze.sia import Sia
from api.models.matrix import Matrix
from api.models.structure import Structure

import itertools as it
from matplotlib import pyplot as plt
import copy

import networkx as nx
import numpy as np
from numpy.typing import NDArray

from constants.structure import BOOL_RANGE, T0_SYM, T1_SYM
from utils.consts import INFTY, W_LBL
from utils.funcs import get_labels


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
        part: None = None

        max_len = max(*self._effect, *self._causes) + 1
        labels = get_labels(max_len)
        self.__effect_labels = [f'{labels[i]}{T1_SYM}' for i in self._effect]
        self.__causes_labels = [f'{labels[j]}{T0_SYM}' for j in self._causes]
        ic(self.__effect_labels, self.__causes_labels)

        self.__net = self.mar_and_pad()

        #
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

    def mar_and_pad(self) -> nx.Graph:
        concept_comb = list(it.product(self._causes, self._effect))
        ic(list(concept_comb))

        all_edges = [
            (
                self.__causes_labels[self._causes.index(c)],
                self.__effect_labels[self._effect.index(e)],
                -1,
            )
            for c, e in concept_comb
        ]
        ic(all_edges)

        self.__net.add_weighted_edges_from(all_edges)
        # self.plot_net(self.__net)
        """
        self._effect: [0, 4], self._causes: [0, 2, 4]
        ic| self.__effect_labels: ['A(t=1)', 'E(t=1)']
            self.__causes_labels: ['A(t=0)', 'C(t=0)', 'E(t=0)']"""
        for idx_causes, idx_effect in concept_comb:
            # Iteramos las aristas ya definidas en el producto causa efecto
            # ! Por qué no re-instanciar la matriz (no la clase)? [#15] ! #
            sub_struct: Structure = copy.deepcopy(self._structure)
            sub_mat: Matrix = sub_struct.get_tensor()[idx_effect]
            ic(idx_causes, idx_effect)
            # ic(sub_mat.as_dataframe())

            sub_states: list[int] = copy.deepcopy(self._causes)
            sub_states.remove(idx_causes)
            # prev_causes = sorted(sub_states + [idx_causes])

            sub_mat.margin(sub_states, data=True)
            sub_mat.expand(self._causes, data=True)
            ic(sub_mat.as_dataframe())

            effect = {bin: ([] if self._dual == bin else self._effect) for bin in BOOL_RANGE}
            causes = {bin: ([] if self._dual == bin else self._causes) for bin in BOOL_RANGE}
            # ic(effect, causes)
            iter_distrib = sub_struct.create_distrib(effect, causes, data=True)
            ic(iter_distrib)

        # to_margin = [idx for idx in self.]

    def branch_and_bound(self) -> tuple[tuple[tuple[str], tuple[str]]]:
        pass

    def calculate_ub(self) -> float:
        pass

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

    def T(self, net1: nx.Graph, net2: nx.Graph) -> None:
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
