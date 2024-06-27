from abc import ABC, abstractmethod
import numpy as np
import networkx as nx
from api.models.structure import Structure
from utils.consts import BEST_DISTRIBUTION, NET_ID, MIP, SMALL_PHI
from numpy.typing import NDArray


class Sia(ABC):
    """Class Sia is used as parent class to use it's props in the used strategies."""

    def __init__(self, structure) -> None:
        self._structure: Structure = structure  # Passed
        self._dist_sys: NDArray[np.float64] = None  # Calculated

        self._network: nx.Graph | nx.DiGraph = None
        self._integrated_info: float = None
        self._min_info_part: dict = None
        self._distribution: dict[str, tuple] = None

    @abstractmethod
    def analyze(self) -> dict[str, nx.Graph | nx.DiGraph | float | dict]:
        pass

    def calculate_concept(self) -> None:
        analysis: dict[str, nx.Graph | nx.DiGraph | float | dict] = self.analyze()
        self._network = analysis.get(NET_ID, None)
        self._integrated_info = analysis.get(SMALL_PHI, None)
        self._min_info_part = analysis.get(MIP, None)
        self._distribution = analysis.get(BEST_DISTRIBUTION, None)
