from fastapi import HTTPException
import networkx as nx
import numpy as np
from api.models.props.sia import SiaType
from api.models.structure import Structure
from api.services.analyze.sia import Sia
from constants.structure import BOOL_RANGE
from utils.funcs import emd

from numpy.typing import NDArray

from utils.consts import BEST_DISTRIBUTION, NET_ID, MIP, SMALL_PHI, STR_ONE
from icecream import ic


class Genetic(Sia):
    """Class Zero is used to solve the problem by brute force."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        causes: list[int],
        distribution: NDArray[np.float64],
        dual: bool,
    ) -> None:
        super().__init__(structure, effect, causes, distribution, dual)
        # There's an environment for each control parameter
        self.control_params: list[dict] = []
        self.environments: list = []

    def analyze(self) -> dict:
        # ! cout('Do some logic to obtain the parameters')

        net_id = lambda x: x + 1

        str_effect = '101'
        str_causes = '111'

        effect = {b: [] for b in BOOL_RANGE}
        for i, e in zip(self._effect, str_effect):
            effect[e == STR_ONE].append(i)

        causes = {b: [] for b in BOOL_RANGE}
        for j, c in zip(self._causes, str_causes):
            causes[c == STR_ONE].append(j)

        ic(effect, causes)

        # Calculate distribution... by algorithm!
        iter_distrib = self.structure.create_concept(effect, causes, data=True)  #! TESTING !#
        # best_dist = self._structure.get_distribution(self._dual).tolist()

        mip = ((('?',), ('¿',)), (('¿',), ('?',)))

        ic(iter_distrib.flatten(), self._target_dist.flatten())
        # 000 100 010 110 001 101 011 111
        emd_dist = emd(*iter_distrib, *self._target_dist)

        ic(emd_dist)

        return {
            # ! Store the network, get the id and return it to invoque in front ! #
            NET_ID: net_id(1),
            SMALL_PHI: emd_dist,
            MIP: mip,
            BEST_DISTRIBUTION: iter_distrib.tolist(),
        }

    def get_reperoire(self) -> SiaType:
        concept: SiaType = {
            NET_ID: self._network,
            SMALL_PHI: self._integrated_info,
            MIP: self._min_info_part,
            BEST_DISTRIBUTION: self.distribution,
        }
        return concept
