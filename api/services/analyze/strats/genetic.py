import networkx as nx
from api.services.analyze.sia import Sia
from utils.consts import (
    BEST_DISTRIBUTION, BEST_NETWORK, BEST_PARTITION, MIN_INFO_LOSS
)
from utils.funcs import cout


class Genetic(Sia):
    ''' Class Zero is used to solve the problem by brute force. '''

    def __init__(self, system) -> None:
        super().__init__(system)

    def analisis(self) -> dict:
        # cout(self._system)
        return {
            # BEST_NETWORK: self.__network,
            MIN_INFO_LOSS: 0.3,
            BEST_PARTITION: 0.3,
            BEST_DISTRIBUTION: 0.3,
        }

    def get_reperoire(self) -> dict[str, nx.Graph | nx.DiGraph | float | dict]:
        return {
            BEST_NETWORK: self._network,
            MIN_INFO_LOSS: self._information_loss,
            BEST_PARTITION: self._partition,
            BEST_DISTRIBUTION: self._distribution,
        }
