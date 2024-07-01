from abc import ABC, abstractmethod
from fastapi import HTTPException
import numpy as np
import networkx as nx
from api.models.props.sia import SiaType
from api.models.structure import Structure
from utils.consts import DISTRIBUTION, INFTY, SUB_DISTRIBUTION, NET_ID, MIP, SMALL_PHI
from numpy.typing import NDArray

from icecream import ic


class Sia(ABC):
    """Class Sia is used as parent class to use it's props in the used strategies."""

    def __init__(self, structure, effect, causes, distribution, dual) -> None:
        self._structure: Structure = structure
        self._effect: list[int] = effect
        self._causes: list[int] = causes
        self._target_dist: NDArray[np.float64] = distribution
        self._dual: bool = dual

        self.integrated_info: float = None
        self.min_info_part: tuple[tuple[tuple[str], tuple[str]]] = None
        self.sub_distrib: NDArray[np.float64] = None
        self.network_id: nx.Graph | nx.DiGraph = None

    def calculate_concept(self) -> None:
        # Analyze method returns a boolean that indicates if there's NOT a standard parameter solution
        if self.analyze():
            raise HTTPException(
                status_code=500,
                detail=f'One or more of the SIA properties are not calculated: {self.integrated_info}, {self.min_info_part}, {self.sub_distrib}, {self.network_id}',
            )   

    def get_reperoire(self) -> dict:
        concept: SiaType = {
            SMALL_PHI: self.integrated_info,
            MIP: self.min_info_part,
            SUB_DISTRIBUTION: self.sub_distrib.tolist(),
            DISTRIBUTION: self._target_dist.tolist(),
            NET_ID: self.network_id,
        }
        return concept

    @abstractmethod
    def analyze(self) -> SiaType:
        pass
