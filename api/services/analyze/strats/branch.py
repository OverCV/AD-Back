from api.models.bnb.nodum import Nodum
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
from matplotlib import pyplot as plt

from constants.dummy import DUMMY_NET_INT_ID, DUMMY_SUBDIST, DUMMY_MIN_INFO_PARTITION
from constants.structure import BOOL_RANGE, T0_SYM, T1_SYM
from utils.consts import FIRST, FLOAT_ZERO, INFTY_POS, INT_ZERO, U_IDX, V_IDX, DATA_IDX, WT_LBL
from utils.funcs import emd_pyphi, get_labels

import utils.network as net

from icecream import ic

from server import conf


class Branch(Sia):
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
        # self.__net = self.margin_n_expand()
        self.margin_n_expand()

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

        concept_comb: list[tuple[int, int]] = list(it.product(self._actual, self._effect))

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
        for idx_actual, idx_effect in ordered_comb:
            # Iteramos las aristas ya definidas en el producto causa efecto
            # ! Por qué no re-instanciar la matriz (no la clase)? [#15] ! #
            sub_struct: Structure = copy.deepcopy(alt_struct)
            sub_mat: Matrix = sub_struct.get_matrix(idx_effect)

            sub_states: list[int] = copy.deepcopy(self._actual)
            sub_states.remove(idx_actual)

            sub_mat.margin(sub_states)
            sub_mat.expand(self._actual)

            effect = {bin: ([] if self._dual == bin else self._effect) for bin in BOOL_RANGE}
            actual = {bin: ([] if self._dual == bin else self._actual) for bin in BOOL_RANGE}

            ic(effect, actual)

            iter_distrib = sub_struct.create_distrib(effect, actual, data=True)[
                StructProps.DIST_ARRAY
            ]
            origin = self.__causes_labels[self._actual.index(idx_actual)]
            destiny = self.__effect_labels[self._effect.index(idx_effect)]

            emd_as_weight = emd_pyphi(*iter_distrib, *self._target_dist)

            self.__net.remove_edge(origin, destiny)

            # ic(idx_causes, idx_effect)
            # ic(emd_as_weight, net.is_disconnected(self.__net))
            # ic(mips)

            # net.precalculate_adjacencies(self.__net)
            if net.is_disconnected(self.__net):
                # Si es disconexo reestablecemos la arista, la guardamos como logro independiente de si tuvo peso o no.
                # print('Disconnected')
                mips[(origin, destiny, emd_as_weight)] = deleted
                self.__net.add_weighted_edges_from([(origin, destiny, emd_as_weight)])
                # ! Maybe return here if emd is 0 # !

            elif emd_as_weight > FLOAT_ZERO:
                # Si es conexo Y hay pérdida entonces restablecemos la arsita.
                # print('Connected and loss')
                # ic((origin, destiny, emd_as_weight))
                self.__net.add_weighted_edges_from([(origin, destiny, emd_as_weight)])

            else:
                # print('Connected no loss')
                # Si es conexo y no hay pérdida entonces guardamos la arista. A su vez guardamos estas aristas en 0 para la reconstrucción.
                # ic((origin, destiny, emd_as_weight))
                deleted.append((origin, destiny, emd_as_weight))
                alt_struct.set_matrix(idx_effect, sub_mat)
                # ic(deleted)

            # print()

        # self.plot_net(self.__net)

        if len(mips) > INT_ZERO:
            min_key = min(mips.keys(), key=lambda x: x[DATA_IDX])  # x=(u,v,w)
            ic(min_key)
            return self.__net
        else:
            self.branch_and_bound()

    """
    ! ¡
    """

    def branch_and_bound(self):
        # ! -> tuple[tuple[tuple[str], tuple[str]]]
        # edges = [
        #     ('A(0)', 'A(1)', 0.5),
        #     ('B(0)', 'A(1)', 0.9),
        #     ('C(0)', 'A(1)', 0.4),
        #     ('A(0)', 'B(1)', 0.3),
        #     ('B(0)', 'B(1)', 0.8),
        #     ('C(0)', 'B(1)', 0.45),
        #     # ('A(0)', 'C(1)', 0.6),
        #     # ('B(0)', 'C(1)', 0.7),
        #     # ('C(0)', 'C(1)', 0.2),
        # ]
        # test_net = nx.DiGraph() if conf.directed else nx.Graph()
        # test_net.add_weighted_edges_from(edges)
        # self.__net = test_net

        origin: Nodum = Nodum(ub=FLOAT_ZERO, net=self.__net.copy())

        # We create a priority queue to store the nodes
        queue: list[tuple[float, Nodum]] = []
        pq.heappush(queue, (FLOAT_ZERO, origin))
        # ! ic(queue)

        gb: float = INFTY_POS
        minimal_loss: Nodum = Nodum(ub=INFTY_POS, net=self.__net.copy())

        # origin_net = origin.get_net()

        m: int = len(self._effect)
        n: int = len(self._actual)
        limit: int = 2 ** (m + n - 1)
        all_nodes = set()

        ic(self.__net.edges(data=True))
        ic(limit)

        # self.plot_net(self.__net)

        while len(queue) > INT_ZERO:
            # ? Obtenemos el hijo de la cola de prioridad hasta que esté vacía.
            # print()
            # ic(queue)
            _, son = pq.heappop(queue)
            all_nodes.add(son)

            # print(son)

            if any(
                (
                    len(son.get_ignored().keys()) == len(son.get_net().edges()),
                    son.get_ub() >= gb,
                )
            ):
                continue
            left: Nodum = Nodum(
                ub=son.get_ub(),
                net=son.get_net().copy(),
                ignore=son.get_ignored().copy(),
            )
            # print(left)
            # ? Ordenamos las aristas para ignorar la primera (mejor)

            for ledge in left.sorted_edges():
                # Al momento de ignorar es importante iterar las aristas puesto no vale tomar la mejor, esto porque es necesario ignorar todas las que vayan siendo requeridas, de forma que cuando ya se haya tomado la mejor, se continuará para la segunda, tercera, etc... hasta que se toma sale del ciclo.
                if (ledge[U_IDX], ledge[V_IDX]) in left.get_ignored().keys():
                    # print('lmin skip', (ledge[U_IDX], ledge[V_IDX]))
                    continue
                left.ignore_new(
                    (ledge[U_IDX], ledge[V_IDX]),
                    {ledge[V_IDX]},
                )
                break

            if not net.is_disconnected(left.get_net()):
                pq.heappush(queue, (-left.get_ub(), left))
            elif left.get_ub() < gb:
                gb = round(left.get_ub(), 4)
                if left.get_ub() < minimal_loss.get_ub():
                    minimal_loss: Nodum = left

            # ? Ordenamos las aristas para tener la de menor pérdida graduada. Esta será la que vayamos a eliminar.

            right: Nodum = Nodum(
                ub=son.get_ub(),
                net=son.get_net().copy(),
                ignore=son.get_ignored().copy(),
            )

            # rmin_edge: tuple[str, str, dict[float]] = right.sorted_edges()[FIRST]
            for redge in right.sorted_edges():
                # Iteramos de forma ordenada las aristas puesto hemos de validar dos condiciones, si la arista debe ser ignorada entonces continuamos a la siguiente iteración para tomar la siguiente mejor arista, sea el caso entonces rompemos el ciclo para tras tomarla no seguir tomando.
                if (redge[U_IDX], redge[V_IDX]) in right.get_ignored().keys():
                    # print('rmin skip', (redge[U_IDX], redge[V_IDX]))
                    continue
                r_net: nx.DiGraph | nx.Graph = right.get_net()
                right.inc_ub(self.calculate_ub(right, redge))
                right.add_deletion((redge[U_IDX], redge[V_IDX], redge[DATA_IDX]))
                r_net.remove_edge(redge[U_IDX], redge[V_IDX])
                break

            if not net.is_disconnected(right.get_net()):
                pq.heappush(queue, (-right.get_ub(), right))
            elif right.get_ub() < gb:
                gb = round(right.get_ub(), 4)
                if right.get_ub() < minimal_loss.get_ub():
                    minimal_loss: Nodum = right

            # ? Graficar o limitar

            # self.biplot(left.get_net(), right.get_net())
            limit -= 1
            if limit < 0:
                raise HTTPException(
                    status_code=status.HTTP_508_LOOP_DETECTED,
                    detail='Maximal limit has been reached.',
                )
            # print('-' * 37)
        # ic(str(minimal_loss))
        # ic()
        edges_deleted = minimal_loss.get_deletions()
        ic(edges_deleted)
        # self.plot_net(minimal_loss.get_net())
        self.integrated_info = minimal_loss.get_ub()
        return minimal_loss.get_net()

        # for edge in left.order_edges():
        #     if (edge[U_IDX], edge[V_IDX]) in left.get_ignored().keys():
        #         continue
        #     if conf.directed:
        #         left.ignore_new(
        #             (edge[U_IDX], edge[V_IDX]),
        #             {edge[V_IDX]},
        #         )
        #     else:
        #         left.ignore_new(
        #             (edge[U_IDX], edge[V_IDX]),
        #             {edge[U_IDX], edge[V_IDX]},
        #         )
        #     break
        # else:
        #     left.ignore_new(
        #         (edge[U_IDX], edge[V_IDX]),
        #         {edge[U_IDX], edge[V_IDX]},
        #     )

    def calculate_ub(self, right: Nodum, edge: tuple[str, str, float]) -> float:
        # Ocurre que una arista incide a un nodo (supóngase unidireccionalidad). En ese sentido si la arista eliminada hace destino a un nodo cual haga parte de otras arista que incidan al mismo nodo, el peso nuevo será máximo el peso de las aristas incidentes al nodo y mínimo lo que ya se lleve acumulado en el nodo.
        # ? Intentar que sean las aristas que no incidan al nodo las que sumen la base. Esto puesto si la arista eliminada no incide al nodo, el peso total será la suma de lo que se lleve más la nueva arista.

        # Si los nodos ya están ignorados sacamos el peso de las aristas que están asociadas incidentemente al mismo.
        # Se suma el resto de aristas que no estén asociadas al nodo.

        # Se tiene un peso acumulado según el criterio que manejamos, por ende es importante que la nueva arista a tomar como peso realmente adicionará un valor que varía según si incide en un nodo con aristas previamente incidentes o no. Como mínimo tomará el máximo de las aristas incidentes, como máximo la suma de su peso.

        # Para sacar el peso debemos tomar un promedio entre la mayor arista y la suma de las demás aristas incidentes al nodo .

        # actual_w: float = node.get_ub()
        # Obtenemos el grafo
        # network: nx.Graph | nx.DiGraph = node.get_net()

        # tenemos la arista a eliminar

        # destiny: str = edge[1]

        # Obtenemos los nodos sobre los que incide la arista
        # nodes: list[tuple[str, str, float]] = get_adj(node.get_net(), destiny)

        # ic(edge[DATA_IDX][WT_LBL])
        return edge[DATA_IDX][WT_LBL]

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

    def biplot(self, net1: nx.Graph, net2: nx.Graph) -> None:
        """This function is used to plot two networks side by side."""
        _, axs = plt.subplots(1, 2, figsize=(12, 6))

        def plot_single_net(ax, net):
            future_nodes = [node for node in net.nodes if node in self.__effect_labels]
            current_nodes = [node for node in net.nodes if node in self.__causes_labels]
            pos = {}
            try:
                pos.update((node, (1, index)) for index, node in enumerate(future_nodes))
                pos.update((node, (0, index)) for index, node in enumerate(current_nodes))
            except KeyError:
                pass

            # Draw the network with custom node and edge colors
            nx.draw(
                net,
                pos=pos,
                with_labels=True,
                ax=ax,
                node_color='skyblue',
                font_color='black',
                edge_color='gray',
            )

            labels = nx.get_edge_attributes(net, 'weight')
            for (u, v), weight in labels.items():
                offset = np.random.default_rng(seed=1).uniform(-0.2, 0.2)

                # Calculate the position for the label closer to the destination node
                pos_y = pos[v][1] + (pos[u][1] - pos[v][1]) * 0.3 + offset
                pos_x = pos[v][0] + (pos[u][0] - pos[v][0]) * 0.3 + offset

                ax.text(
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

        plot_single_net(axs[0], net1)
        plot_single_net(axs[1], net2)

        plt.show()

    # def test_deletion(self):
    #     concept_comb = list(it.product(self._causes, self._effect))

    #     self.__net.add_nodes_from(self.__effect_labels)
    #     self.__net.add_nodes_from(self.__causes_labels)
    #     self.__net.add_edges_from(
    #         (
    #             (
    #                 self.__causes_labels[self._causes.index(j)],
    #                 self.__effect_labels[self._effect.index(i)],
    #             )
    #             for j, i in concept_comb
    #         )
    #     )
    #     ic(self.__net.edges(data=True))

    #     self.__net.remove_edge('A(0)', 'B(1)')
    #     # self.plot_net(self.__net)
    #     ic(net.is_disconnected(self.__net))

    #     self.__net.remove_edge('B(0)', 'B(1)')
    #     # self.plot_net(self.__net)
    #     ic(net.is_disconnected(self.__net))

    #     self.__net.remove_edge('C(0)', 'B(1)')
    #     # self.plot_net(self.__net)
    #     ic(net.is_disconnected(self.__net))
