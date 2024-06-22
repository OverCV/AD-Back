import numpy as np
import networkx as nx
from api.models.system import System


class Sia:
    ''' Class Sia is used as parent class to use it's props in the used strategies. '''

    def __init__(self) -> None:
        self.__system: System = None
        self.__serie: np.ndarray = None

        self.__network: nx.Graph | nx.DiGraph = None
        self.__information_loss: float = None
        self.__partition: dict = None
        # part: (T T . F F)
        # lbls: {A, B} ; part: ({A, B}, {})
        # { prim: ((A, B), (A)), dual: ((VOID), (B)) } #
        self.__distribution: dict[str, tuple] = None
