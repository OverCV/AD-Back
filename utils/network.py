import networkx as nx
from networkx.utils import arbitrary_element
from typing import FrozenSet, Set, Union

# from functools import lru_cache
import concurrent.futures

import utils.network as net

from server import conf


# @lru_cache(maxsize=None)
def get_adj(G: Union[nx.Graph, nx.DiGraph], node: str) -> FrozenSet[str]:
    """Obtiene los nodos adyacentes a un nodo dado en un grafo."""
    if isinstance(G, nx.DiGraph):
        return frozenset(G._pred[node]) | frozenset(G._succ[node])
    return frozenset(G._adj[node])


def is_disconnected(G: Union[nx.Graph, nx.DiGraph]) -> bool:
    """Returns True if the graph is not connected, False otherwise."""
    if len(G) == 0:
        raise nx.NetworkXPointlessConcept('Connectivity is undefined for the null graph.')
    return (
        len(threaded_bfs(G, arbitrary_element(G))) != len(G)
        if conf.threaded
        else len(sequential_bfs(G, arbitrary_element(G))) != len(G)
    )


def threaded_bfs(G: Union[nx.Graph, nx.DiGraph], source: str) -> Set[str]:
    """Threaded BFS implementation."""
    num_threads = min(32, len(G))
    seen = set()
    to_visit = {source}

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        while to_visit:
            futures = [executor.submit(bfs_worker, G, node, seen) for node in to_visit]
            to_visit = set()
            for future in concurrent.futures.as_completed(futures):
                new_nodes = future.result()
                seen.update(new_nodes)
                to_visit.update(new_nodes - seen)
            if len(seen) == len(G):
                return seen

    return seen


def bfs_worker(G, node, seen):
    """Worker function for parallel BFS."""
    return get_adj(G, node) - seen


def sequential_bfs(G: Union[nx.Graph, nx.DiGraph], source: str) -> Set[str]:
    """A fast BFS node generator for a graph using get_adj() function."""
    seen = {source}
    to_visit = {source}
    while to_visit:
        node = to_visit.pop()
        neighbors = get_adj(G, node)
        new_nodes = neighbors - seen
        seen.update(new_nodes)
        to_visit.update(new_nodes)
    return seen
