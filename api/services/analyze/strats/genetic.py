import networkx as nx
import numpy as np
from api.models.props.sia import SiaType
from api.services.analyze.sia import Sia
from utils.consts import BEST_DISTRIBUTION, NET_ID, MIP, SMALL_PHI
from utils.funcs import emd

from icecream import ic


class Genetic(Sia):
    """Class Zero is used to solve the problem by brute force."""

    def __init__(self, structure, effect, causes, distribution, dual) -> None:
        super().__init__(structure, effect, causes, distribution, dual)
        # There's an environment for each control parameter
        self.control_params: list[dict] = []
        self.environments: list = []

    def analyze(self) -> dict:
        # ! cout('Do some logic to obtain the parameters')

        net_id = lambda x: x + 1
        mip = (('A', 'B', 'C'), ('B',)), ((), ('A', 'C'))

        # Calculate distribution... by algorithm!
        best_dist = self._structure.create_concept(
            '11100', '11100', data=True
        )  #! TESTING with 11100 11100 !#
        # best_dist = self._structure.get_distribution(self._dual).tolist()

        ic(best_dist, self._target_dist)
        emd_dist = emd(best_dist, self._target_dist)
        ic(emd_dist)

        return {
            # ! Store the network, get the id and return it to invoque in front ! #
            NET_ID: net_id(1),
            SMALL_PHI: emd_dist,
            MIP: mip,
            BEST_DISTRIBUTION: best_dist.tolist(),
        }

    def get_reperoire(self) -> SiaType:
        concept: SiaType = {
            NET_ID: self._network,
            SMALL_PHI: self._integrated_info,
            MIP: self._min_info_part,
            BEST_DISTRIBUTION: self._distribution,
        }
        return concept
