import math
import networkx as nx

from utils.consts import W_LBL
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
        self._ub: float = ub
        self._lb: float = lb
        self._net: nx.Graph | nx.DiGraph = net
        self._ignore: dict[tuple[str, str, float], set[str]] = ignore

    def set_data(
        self,
        ub: float = 0.0,
        net: nx.Graph | nx.DiGraph = nx.Graph(),
        ignore: dict[tuple[str, str, float], set[str]] = None,
        lb: float = 0.0,
    ):
        self._ub = ub
        self._net = net
        self._ignore = ignore if ignore is not None else self._ignore
        self._lb = lb

    def get_ub(self) -> float:
        return self._ub

    def get_net(self) -> nx.Graph | nx.DiGraph:
        return self._net

    def ignore_new(self, edge: tuple[str, str, int], adjacent: set[str]):
        ic(edge, adjacent)
        if self._ignore[edge] is None:
            self._ignore[edge] = set()
        self._ignore[edge].update(adjacent)

    # def get_ignored(self) -> set[tuple[str]]:
    def get_ignored(self) -> dict[tuple[str, str, int], set[str]]:
        return self._ignore

    def get_lb(self) -> float:
        return self._lb

    def get_ordered_edges(self) -> list[tuple[str, str, float]]:
        return sorted(
            self._net.edges(data=True),
            key=lambda edge: edge[2][W_LBL]
            * math.sqrt(
                self._net.degree(edge[0]) ** 2 + self._net.degree(edge[1]) ** 2,
            ),
        )

    def __str__(self) -> str:
        edges = [(u, v, d[W_LBL]) for u, v, d in self.get_ordered_edges()]
        return f'⟨ub: {self._ub}, edges: {edges}, ignore: {self._ignore}⟩'
