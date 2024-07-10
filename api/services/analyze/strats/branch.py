from matplotlib import pyplot as plt
from api.services.analyze.sia import Sia

from ctypes import Structure

import networkx as nx
import numpy as np
from numpy.typing import NDArray

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

        self.__effect_labels = get_labels(len(effect))
        self.__cause_labels = get_labels(len(causes))

    def analyze(self) -> bool:
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

    def mar_and_pad(self, partition: tuple[str, str]) -> tuple[tuple[tuple[str], tuple[str]]]:
        pass

    def branch_and_bound(self) -> tuple[tuple[tuple[str], tuple[str]]]:
        pass

    def calculate_ub(self) -> float:
        pass

    def plot_net(self, net: nx.Graph) -> None:
        """This function is used to plot the network."""
        # Separate the nodes into two sets
        future_nodes = [node for node in net.nodes if node in self.__effect_labels]
        current_nodes = [node for node in net.nodes if node in self.__cause_labels]

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

    def biplot_net(self, net1: nx.Graph, net2: nx.Graph) -> None:
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
