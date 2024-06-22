from abc import ABC, abstractmethod
import numpy as np
import networkx as nx
from api.models.system import System
from utils.consts import (
    BEST_DISTRIBUTION, BEST_NETWORK, BEST_PARTITION, MIN_INFO_LOSS
)


class Sia(ABC):
    ''' Class Sia is used as parent class to use it's props in the used strategies. '''

    def __init__(self) -> None:
        self.__system: System = None  # Passed
        self.__serie: np.ndarray = None  # Calculated
        # part: (T T . F F)
        # lbls: {A, B} ; part: ({A, B}, {})
        # { prim: ((A, B), (A)), dual: ((VOID), (B)) } #
        self.__network: nx.Graph | nx.DiGraph = None
        self.__information_loss: float = None
        self.__partition: dict = None
        self.__distribution: dict[str, tuple] = None

    @abstractmethod
    def __analisis(self) -> dict[str, nx.Graph | float | dict]:
        pass

    def set_repertoire(self) -> None:
        self.__network = self.__analisis()[BEST_NETWORK]
        self.__network = self.__analisis()[MIN_INFO_LOSS]
        self.__partition = self.__analisis()[BEST_PARTITION]
        self.__distribution = self.__analisis()[BEST_DISTRIBUTION]

    @property
    def get_reperoire(self) -> dict:
        return {
            BEST_NETWORK: self.__network,
            MIN_INFO_LOSS: self.__information_loss,
            BEST_PARTITION: self.__partition,
            BEST_DISTRIBUTION: self.__distribution
        }
