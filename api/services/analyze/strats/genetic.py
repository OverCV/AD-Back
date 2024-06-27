import networkx as nx
from api.models.props.sia import SiaType
from api.services.analyze.sia import Sia
from utils.consts import BEST_DISTRIBUTION, NET_ID, MIP, SMALL_PHI


class Genetic(Sia):
    """Class Zero is used to solve the problem by brute force."""

    def __init__(self, structure, effect, causes, distribution, dual) -> None:
        super().__init__(structure, effect, causes, distribution, dual)
        # There's an environment for each control parameter
        self.control_params: list[dict] = []
        self.environments: list = []

    def analyze(self) -> dict:
        # cout('Do some logic to obtain the parameters')
        net_ID = lambda x: x + 1

        target_dist = self._structure.get_distribution(self._dual)

        loss = lambda x: x + 1

        distribution = lambda: {0: (0.3, 0.3), 1: (0.3, 0.3)}

        return {
            # ! Store the network, get the id and return it to invoque in front ! #
            NET_ID: network(1),
            SMALL_PHI: 0.3,
            MIP: 0.3,
            BEST_DISTRIBUTION: 0.3,
        }

    def get_reperoire(self) -> SiaType:
        concept: SiaType = {
            NET_ID: self._network,
            SMALL_PHI: self._integrated_info,
            MIP: self._min_info_part,
            BEST_DISTRIBUTION: self._distribution,
        }
        return concept
