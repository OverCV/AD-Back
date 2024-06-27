from abc import ABC, abstractmethod
import numpy as np
import networkx as nx
from api.models.props.sia import SiaType
from api.models.structure import Structure
from utils.consts import BEST_DISTRIBUTION, NET_ID, MIP, SMALL_PHI
from numpy.typing import NDArray


class Sia(ABC):
    """Class Sia is used as parent class to use it's props in the used strategies."""

    def __init__(self, structure, effect, causes, distribution, dual) -> None:
        self._structure: Structure = structure
        self._effect: str = effect
        self._causes: str = causes
        self._target_dist: NDArray[np.float64] = distribution
        self._dual: bool = dual

        self._network: nx.Graph | nx.DiGraph = None
        self._integrated_info: float = None
        self._min_info_part: tuple[tuple[tuple[str], tuple[str]], tuple[tuple[str], tuple[str]]] = (
            None
        )
        self._distribution: NDArray[np.float64] = None

    @abstractmethod
    def analyze(self) -> SiaType:
        pass

    def calculate_concept(self) -> None:
        analysis: SiaType = self.analyze()
        self._network = analysis.get(NET_ID, None)
        self._integrated_info = analysis.get(SMALL_PHI, None)
        self._min_info_part = analysis.get(MIP, None)
        self._distribution = analysis.get(BEST_DISTRIBUTION, None)
