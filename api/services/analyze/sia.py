from abc import ABC, abstractmethod
import numpy as np
import networkx as nx
from api.models.system import System
from utils.consts import (
    BEST_DISTRIBUTION, BEST_NETWORK, BEST_PARTITION, MIN_INFO_LOSS
)


class Sia(ABC):
    ''' Class Sia is used as parent class to use it's props in the used strategies. '''

    def __init__(self, system) -> None:
        self._system: System = system  # Passed
        self._serie: np.ndarray = None  # Calculated

        self._network: nx.Graph | nx.DiGraph = None
        self._information_loss: float = None
        self._partition: dict = None
        self._distribution: dict[str, tuple] = None

    @abstractmethod
    def analisis(self) -> dict[str, nx.Graph | nx.DiGraph | float | dict]:
        pass

    def set_repertoire(self) -> None:
        self._network = self.analisis().get(BEST_NETWORK, None)
        self._information_loss = self.analisis().get(MIN_INFO_LOSS, None)
        self._partition = self.analisis().get(BEST_PARTITION, None)
        self._distribution = self.analisis().get(BEST_DISTRIBUTION, None)

    # part: (T T . F F)
    # lbls: {A, B} ; part: ({A, B}, {})
    # { prim: ((A, B), (A)), dual: ((VOID), (B)) } #

    # @property
    # def system(self) -> System:
    #     return self.__system

    # @property
    # def serie(self) -> np.ndarray:
    #     return self.__serie

    # @abstractmethod
    # def get_reperoire(self) -> dict:
    #     pass
