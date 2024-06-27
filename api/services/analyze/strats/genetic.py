import networkx as nx
from api.services.analyze.sia import Sia
from utils.consts import BEST_DISTRIBUTION, NET_ID, MIP, SMALL_PHI


class Genetic(Sia):
    """Class Zero is used to solve the problem by brute force."""

    def __init__(self, structure) -> None:
        super().__init__(structure)

    def analyze(self) -> dict:
        # cout('Do some logic to obtain the parameters')
        def network(x):
            x *= 2
            y = 2
            return x - y

        target_dist = self._structure.get_distribution()

        def loss():
            return 0.3

        def distribution():
            return {0: (0.3, 0.3), 1: (0.3, 0.3)}

        return {
            # ! Store the network, get the id and return it to invoque in front ! #
            NET_ID: network(1),
            SMALL_PHI: 0.3,
            MIP: 0.3,
            BEST_DISTRIBUTION: 0.3,
        }

    def get_reperoire(self) -> dict[str, nx.Graph | nx.DiGraph | float | dict]:
        return {
            NET_ID: self._network,
            SMALL_PHI: self._integrated_info,
            MIP: self._min_info_part,
            BEST_DISTRIBUTION: self._distribution,
        }
