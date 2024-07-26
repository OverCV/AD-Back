import math
import networkx as nx

from utils.consts import FIRST, INT_ZERO, U_IDX, V_IDX, DATA_IDX, WT_LBL
from server import conf
from icecream import ic


class Nodum:
    """Class Nodum is used in the branch and bound process."""

    def __init__(
        self,
        ub: float = 0.0,
        lb: float = 0.0,
        net: nx.Graph | nx.DiGraph = nx.DiGraph() if conf.directed else nx.Graph(),
        ignore: dict[tuple[str, str, float], set[str]] = dict(),
    ) -> None:
        """El nodum es un modelo para almacenar las iteraciones consiguientes a la ramificación y poda.

        Args:
            ub (float, optional): Upper Bound o cota superior, es lo que se ha tomado (pérdida de información). Defaults to 0.0.
            lb (float, optional): Lower Bound o cota inferior, es lo mejor que se puede aspirar a obtener con el nodo, siempre que no se tomen aristas ya ignoradas. Defaults to 0.0.
            net (nx.Graph, optional): Contiene la información de la lista de adyacencia que permite el re-ordenamiento para seleccionar el mejor criterio al tomar cada arco. Defaults to nx.Graph().
            ignore (list[tuple[str]], optional): Aristas que debemos ignorar, en el proceso de ramificación tomamos o no la arista, al iterar sobre la lista re-ordenadad debemos ignorar tomar estas aristas puesto se fue por una rama que no las toma y, las aristas que fueron tomadas pues no están presentes en el grafo del que surge la lista. Defaults to list().
        """
        self.__ub: float = ub
        self.__lb: float = lb
        self.__net: nx.Graph | nx.DiGraph = net
        self.__ignore: dict[tuple[str, str, float], set[str]] = ignore
        self.__deletions: list[tuple[str, str, dict[str, float]]] = []

    def set_data(
        self,
        ub: float = 0.0,
        net: nx.Graph | nx.DiGraph = nx.Graph(),
        ignore: dict[tuple[str, str, float], set[str]] = None,
        lb: float = 0.0,
    ):
        self.__ub = ub
        self.__net = net
        self.__ignore = ignore if ignore is not None else self.__ignore
        self.__lb = lb

    def inc_ub(self, inc: float):
        self.__ub += inc

    def add_deletion(self, edge: tuple[str, str, dict[str, float]]):
        self.__deletions.append(edge)

    def get_deletions(self) -> list[tuple[str, str, dict[str, float]]]:
        return self.__deletions

    def get_ub(self) -> float:
        return self.__ub

    def get_net(self) -> nx.DiGraph | nx.Graph:
        return self.__net

    def ignore_new(self, edge: tuple[str, str], adjacent: set[str]):
        if edge not in self.__ignore:
            self.__ignore[edge] = set()
        self.__ignore[edge].update(adjacent)

    # def get_ignored(self) -> set[tuple[str]]:
    def get_ignored(self) -> dict[tuple[str, str, int], set[str]]:
        return self.__ignore

    def get_lb(self) -> float:
        return self.__lb

    def sorted_edges(self) -> list[tuple[str, str, float]]:
        return sorted(
            self.__net.edges(data=True),
            key=lambda edge: edge[DATA_IDX][WT_LBL]
            * math.sqrt(
                self.__net.degree(edge[U_IDX]) ** 2 + self.__net.degree(edge[V_IDX]) ** 2,
            ),
        )

    # def order_edges(
    #     self, minimal: bool = False, all: bool = False
    # ) -> tuple[str, str, float] | list[tuple[str, str, float]]:
    #     edges = sorted(
    #         self.__net.edges(data=True),
    #         key=lambda edge: edge[W_IDX][W_LBL]
    #         * math.sqrt(
    #             self.__net.degree(edge[U_IDX]) ** 2 + self.__net.degree(edge[V_IDX]) ** 2,
    #         ),
    #     )
    #     return edges if all else edges[FIRST] if minimal else None

    def __str__(self) -> str:
        edges = [(u, v, data[WT_LBL]) for u, v, data in self.sorted_edges()]
        return f'⟨ub: {self.__ub}, lb: {self.__lb}, edges: {edges}, ignore: {self.__ignore}⟩'
