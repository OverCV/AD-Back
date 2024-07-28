from api.models.props.structure import StructProps
from api.services.analyze.sia import Sia
from api.models.matrix import Matrix
from api.models.structure import Structure

import itertools as it
import copy
import heapq as pq

from fastapi import HTTPException, status
import numpy as np
from numpy.typing import NDArray
import networkx as nx
from networkx.utils import arbitrary_element
from networkx.utils import BinaryHeap
from matplotlib import pyplot as plt

from constants.dummy import DUMMY_NET_INT_ID, DUMMY_SUBDIST, DUMMY_MIN_INFO_PARTITION
from constants.structure import BOOL_RANGE, T0_SYM, T1_SYM
from utils.consts import FIRST, FLOAT_ZERO, INFTY_POS, INT_ZERO, U_IDX, V_IDX, DATA_IDX, WT_LBL
from utils.funcs import emd, get_labels

import utils.network as net

from icecream import ic

from server import conf


class MSTree(Sia):
    """Class Branch is used to solve the mip problem using Branch&Bound strategy."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        actual: list[int],
        distrib: NDArray[np.float64],
        dual: bool,
    ) -> None:
        super().__init__(structure, effect, actual, distrib, dual)

        self.__effect_labels: None | list[str] = None
        self.__causes_labels: None | list[str] = None

        self.__net: nx.DiGraph | nx.Graph = nx.DiGraph() if conf.directed else nx.Graph()

    def analyze(self) -> bool:
        # ic(self._effect, self._causes, self._target_dist)
        max_len = max(*self._effect, *self._actual) + 1
        labels = get_labels(max_len)
        self.__effect_labels = [f'{labels[i]}{T1_SYM}' for i in self._effect]
        self.__causes_labels = [f'{labels[j]}{T0_SYM}' for j in self._actual]

        # ! Establecer mejor qué retorna la función (Grafo + ?) [#17] ! #
        self.__net = self.margin_n_expand()

        raise HTTPException(344, 'Stop.')

        edges = self.__net.edges(data=True)
        self.integrated_info = min([edge[DATA_IDX][WT_LBL] for edge in edges])
        #
        # raise NotImplementedError
        # part: None = None
        # mip = self.label_mip(part)
        # self.min_info_part = mip
        # ic(
        #     self.integrated_info,
        #     self.min_info_part,
        #     self.sub_distrib,
        #     self.network_id,
        # )
        self.network_id = DUMMY_NET_INT_ID
        self.sub_distrib = DUMMY_SUBDIST
        self.min_info_part = DUMMY_MIN_INFO_PARTITION
        not_std_sln = any(
            [
                # ! Store the network, generate the id and return it as callback in front ! #
                self.integrated_info == INFTY_POS,
                self.min_info_part is None,
                self.sub_distrib is None,
                self.network_id is None,
            ]
        )

        return not_std_sln

    def margin_n_expand(self):
        # deleted: dict[int, list[tuple[str, str, float]]] = {idx: [] for idx in self._effect}
        # En deldeted están las aristas eliminadas, tal que si hay una bipartición, pero se tiene un mínimo de infformación, se tenga el trazo.
        # Cual es el problema, si se genera una pérdida entonces es importante 2 cosas, primero tener las aristas que valen cero o elimiadas hasta elmomento y segundo (lo mismo), tener la arista que al eliminarse se generó una bipartición, a pesar que tenga valor de 0, para entonces guardarla (tenga peso o no) y listo, sería esta arista + eliminadas, en un diccionario en el que la clave es la tupla de la arista
        # No obstante la comparación eficiente entonces no es si la EMD es 0, sino si hay o no bipartición
        """
        self._effect: [0, 4], self._causes: [0, 2, 4]
            self.__causes_labels: ['A(t=0)', 'C(t=0)', 'E(t=0)']
        """

        concept_comb = list(it.product(self._actual, self._effect))

        self.__net.add_nodes_from(self.__effect_labels)
        self.__net.add_nodes_from(self.__causes_labels)
        self.__net.add_edges_from(
            (
                (
                    self.__causes_labels[self._actual.index(j)],
                    self.__effect_labels[self._effect.index(i)],
                )
                for j, i in concept_comb
            )
        )

        deleted: list[tuple[str, str, float]] = []
        mips: dict[str, str] = dict()

        alt_struct = copy.deepcopy(self._structure)
        # ic(self.__net.edges(data=True))
        ordered_comb = sorted(concept_comb, key=lambda tup: tup[1])
        # ic(ordered_comb)
        # self.plot_net(self.__net)
        # for idx_causes, idx_effect in concept_comb:
        for idx_causes, idx_effect in ordered_comb:
            # Iteramos las aristas ya definidas en el producto causa efecto
            # ! Por qué no re-instanciar la matriz (no la clase)? [#15] ! #
            sub_struct: Structure = copy.deepcopy(alt_struct)
            sub_mat: Matrix = sub_struct.get_matrix(idx_effect)

            sub_states: list[int] = copy.deepcopy(self._actual)
            sub_states.remove(idx_causes)

            sub_mat.margin(sub_states)
            sub_mat.expand(self._actual)

            effect = {bin: ([] if self._dual == bin else self._effect) for bin in BOOL_RANGE}
            actual = {bin: ([] if self._dual == bin else self._actual) for bin in BOOL_RANGE}
            iter_distrib = sub_struct.create_distrib(effect, actual, data=True)[
                StructProps.DIST_ARRAY
            ]
            origin = self.__causes_labels[self._actual.index(idx_causes)]
            destiny = self.__effect_labels[self._effect.index(idx_effect)]

            emd_as_weight = emd(iter_distrib, self._target_dist)

            self.__net.remove_edge(origin, destiny)

            # ic(idx_causes, idx_effect)
            # ic(emd_as_weight, net.is_disconnected(self.__net))
            # ic(mips)

            # net.precalculate_adjacencies(self.__net)
            if net.is_disconnected(self.__net):
                # Si es disconexo no reestablecemos la arista, la guardamos como logro independiente de si tuvo peso o no.
                print('Disconnected')
                mips[(origin, destiny, emd_as_weight)] = deleted
                self.__net.add_weighted_edges_from([(origin, destiny, emd_as_weight)])
                # ! Maybe return here if emd is 0 # !

            elif emd_as_weight > FLOAT_ZERO:
                # Si es conexo Y hay pérdida entonces restablecemos la arsita.
                print('Connected and loss')
                ic((origin, destiny, emd_as_weight))
                self.__net.add_weighted_edges_from([(origin, destiny, emd_as_weight)])

            else:
                print('Connected no loss')
                # Si es conexo y no hay pérdida entonces guardamos la arista. A sy vez guardamos estas aristas en 0 para la reconstrucción.
                # ic((origin, destiny, emd_as_weight))
                deleted.append((origin, destiny, emd_as_weight))
                alt_struct.set_matrix(idx_effect, sub_mat)
                # ic(deleted)

            print()

        # self.plot_net(self.__net)

        # if len(mips) > INT_ZERO:
        #     ic()
        #     min_key = min(mips.keys(), key=lambda x: x[DATA_IDX])  # x=(u,v,w) #
        #     ic(min_key)
        #     return self.__net
        # else:
        edges = [
            # ('A(0)', 'A(1)', 10),
            ('B(0)', 'A(1)', 60),
            ('C(0)', 'A(1)', 10),
            ('A(0)', 'B(1)', 10),
            # ('B(0)', 'B(1)', 13),
            ('C(0)', 'B(1)', 50),
            ('A(0)', 'C(1)', 30),
            ('B(0)', 'C(1)', 10),
            # ('C(0)', 'C(1)', 12),
        ]
        # test_net = nx.DiGraph() if conf.directed else nx.Graph()
        test_net = nx.Graph()
        test_net.add_weighted_edges_from(edges)
        # pass
        # self.stoer_wagner(self.__net)
        # self.stoer_wagner(test_net)
        cut_value, partition = self.stoer_wagner(test_net)
        ic(cut_value, partition)
        self.plot_net(test_net)

        self.__net = test_net

        # self.min_span_tree()

    def min_span_tree(self):
        """
        Branch and Bound algorithm to solve the MIP problem.
        """
        # ! Implementar Branch and Bound para la solución del MIP #18 ! #
        raise NotImplementedError

    def stoer_wagner(self, G, weight=WT_LBL, used_heap=BinaryHeap):
        r"""Returns the weighted minimum edge cut using the Stoer-Wagner algorithm.

        Determine the minimum edge cut of a connected graph using the
        Stoer-Wagner algorithm. In weighted cases, all weights must be
        nonnegative.

        The running time of the algorithm depends on the type of heaps used:

        ============== =============================================
        Type of heap   Running time
        ============== =============================================
        Binary heap    $O(n (m + n) \log n)$
        Fibonacci heap $O(nm + n^2 \log n)$
        Pairing heap   $O(2^{2 \sqrt{\log \log n}} nm + n^2 \log n)$
        ============== =============================================

        Parameters
        ----------
        G : NetworkX graph
            Edges of the graph are expected to have an attribute named by the
            weight parameter below. If this attribute is not present, the edge is
            considered to have unit weight.

        weight : string
            Name of the weight attribute of the edges. If the attribute is not
            present, unit weight is assumed. Default value: 'weight'.

        heap : class
            Type of heap to be used in the algorithm. It should be a subclass of
            :class:`MinHeap` or implement a compatible interface.

            If a stock heap implementation is to be used, :class:`BinaryHeap` is
            recommended over :class:`PairingHeap` for Python implementations without
            optimized attribute accesses (e.g., CPython) despite a slower
            asymptotic running time. For Python implementations with optimized
            attribute accesses (e.g., PyPy), :class:`PairingHeap` provides better
            performance. Default value: :class:`BinaryHeap`.

        Returns
        -------
        cut_value : integer or float
            The sum of weights of edges in a minimum cut.

        partition : pair of node lists
            A partitioning of the nodes that defines a minimum cut.

        Raises
        ------
        NetworkXNotImplemented
            If the graph is directed or a multigraph.

        NetworkXError
            If the graph has less than two nodes, is not connected or has a
            negative-weighted edge.

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edge("x", "a", weight=3)
        >>> G.add_edge("x", "b", weight=1)
        >>> G.add_edge("a", "c", weight=3)
        >>> G.add_edge("b", "c", weight=5)
        >>> G.add_edge("b", "d", weight=4)
        >>> G.add_edge("d", "e", weight=2)
        >>> G.add_edge("c", "y", weight=2)
        >>> G.add_edge("e", "y", weight=3)
        >>> cut_value, partition = nx.stoer_wagner(G)
        >>> cut_value
        4
        """
        ic(G)

        n = len(G)
        if n < 2:
            raise nx.NetworkXError('graph has less than two nodes.')
        # if not nx.is_connected(G):
        #     raise nx.NetworkXError('graph is not connected.')

        # Make a copy of the graph for internal use.
        G = nx.Graph(
            (
                u,
                v,
                {WT_LBL: e.get(weight, 1)},
            )
            for u, v, e in G.edges(data=True)
            if u != v
        )
        # G.__networkx_cache__ = None  # Disable caching

        for u, v, e in G.edges(data=True):
            if e[WT_LBL] < 0:
                raise nx.NetworkXError('graph has a negative-weighted edge.')

        cut_value = INFTY_POS
        nodes = set(G)
        contractions: list[tuple[str, str]] = []  # contracted node pairs #

        # Repeatedly pick a pair of nodes to contract until only one node is left.
        for i in range(n - 1):
            # Pick an arbitrary node u and create a set A = {u}.
            u = arbitrary_element(G)
            A = {u}
            # Repeatedly pick the node "most tightly connected" to A and add it to
            # A. The tightness of connectivity of a node not in A is defined by the
            # of edges connecting it to nodes in A.
            heap = used_heap()  # min-heap emulating a max-heap
            for v, e in G[u].items():
                heap.insert(v, -e[WT_LBL])
            # Repeat until all but one node has been added to A.
            for _ in range(n - i - 2):
                u = heap.pop()[0]
                A.add(u)
                for v, e in G[u].items():
                    if v not in A:
                        heap.insert(v, heap.get(v, 0) - e[WT_LBL])
            # A and the remaining node v define a "cut of the phase". There is a
            # minimum cut of the original graph that is also a cut of the phase.
            # Due to contractions in earlier phases, v may in fact represent
            # multiple nodes in the original graph.
            v, w = heap.min()
            w = -w
            if w < cut_value:
                cut_value = w
                best_phase = i
            # Contract v and the last node added to A.
            contractions.append((u, v))
            for w, e in G[v].items():
                if w != u:
                    if w not in G[u]:
                        G.add_edge(u, w, weight=e[WT_LBL])
                    else:
                        G[u][w][WT_LBL] += e[WT_LBL]
            G.remove_node(v)

        # Recover the optimal partitioning from the contractions.
        G = nx.Graph(it.islice(contractions, best_phase))
        v = contractions[best_phase][V_IDX]
        ic(contractions, v)
        G.add_node(v)
        ic(G._adj)
        # reachable = set(nx.single_source_shortest_path_length(G, v))
        reachable = set(self._single_shortest_path_length(G._adj    , v))
        partition = (list(reachable), list(nodes - reachable))

        return cut_value, partition

    def _single_shortest_path_length(self, adj, firstlevel, cutoff=None):
        """Yields (node, level) in a breadth first search

        Shortest Path Length helper function
        Parameters
        ----------
            adj : dict
                Adjacency dict or view
            firstlevel : list
                starting nodes, e.g. [source] or [target]
            cutoff : int or float
                level at which we stop the process
        """
        seen = set(firstlevel)
        nextlevel = firstlevel
        level = 0
        n = len(adj)
        for v in nextlevel:
            yield (v, level)
        while nextlevel and cutoff > level:
            level += 1
            thislevel = nextlevel
            nextlevel = []
            for v in thislevel:
                for w in adj[v]:
                    if w not in seen:
                        seen.add(w)
                        nextlevel.append(w)
                        yield (w, level)
                if len(seen) == n:
                    return

    def plot_net(self, net: nx.Graph) -> None:
        """This function is used to plot the network."""
        # Separate the nodes into two sets
        future_nodes = [node for node in net.nodes if node in self.__effect_labels]
        current_nodes = [node for node in net.nodes if node in self.__causes_labels]

        # Create a bipartite layout
        pos = {}
        try:
            pos.update((node, (1, index)) for index, node in enumerate(future_nodes))
            pos.update((node, (0, index)) for index, node in enumerate(current_nodes))
        except KeyError:
            pass

        # Draw the bipartite graph with custom node and edge colors
        nx.draw(
            net,
            pos=pos,
            with_labels=True,
            node_color='skyblue',
            font_color='black',
            edge_color='gray',
        )

        # Add edge labels with better visibility and consistent styles
        labels = nx.get_edge_attributes(net, 'weight')
        for (u, v), weight in labels.items():
            offset = np.random.default_rng(seed=1).uniform(-0.2, 0.2)

            # Calculate the position for the label closer to the destination node
            pos_y = pos[v][1] + (pos[u][1] - pos[v][1]) * 0.3 + offset
            pos_x = pos[v][0] + (pos[u][0] - pos[v][0]) * 0.3 + offset

            plt.text(
                pos_x,
                pos_y,
                weight,
                ha='center',
                va='center',
                fontsize=8,  # You can adjust the fontsize as needed
                bbox=dict(
                    facecolor='white', edgecolor='none', alpha=0.2
                ),  # Add a background to the text for better visibility
            )

        # Show the plot
        plt.show()
