from abc import ABC, abstractmethod
import numpy as np
import networkx as nx
from api.models.system import System
from utils.consts import (
    BEST_DISTRIBUTION, NET_ID, MIP, SMALL_PHI
)


class Sia(ABC):
    ''' Class Sia is used as parent class to use it's props in the used strategies. '''

    def __init__(self, system) -> None:
        self._system: System = system  # Passed
        self._dist_sys: NDArray = None  # Calculated

        self._network: nx.Graph | nx.DiGraph = None
        self._integrated_info: float = None
        self._min_info_part: dict = None
        self._distribution: dict[str, tuple] = None

    @abstractmethod
    def analyze(self) -> dict[str, nx.Graph | nx.DiGraph | float | dict]:
        pass

    def calculate_repertoire(self) -> None:
        analysis: dict[str, nx.Graph | nx.DiGraph | float | dict] \
            = self.analyze()
        self._network = analysis.get(NET_ID, None)
        self._integrated_info = analysis.get(SMALL_PHI, None)
        self._min_info_part = analysis.get(MIP, None)
        self._distribution = analysis.get(BEST_DISTRIBUTION, None)

    # part: (T T . F F)
    # lbls: {A, B} ; part: ({A, B}, {})
    # { prim: ((A, B), (A)), dual: ((VOID), (B)) } #

    # @property
    # def system(self) -> System:
    #     return self.__system

    # @property
    # def serie(self) -> NDArray:
    #     return self.__serie

    # @abstractmethod
    # def get_reperoire(self) -> dict:
    #     pass
