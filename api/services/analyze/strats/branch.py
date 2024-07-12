from math import e
from matplotlib.font_manager import font_family_aliases
from networkx import is_connected
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

from constants.structure import BOOL_RANGE, T0_SYM, T1_SYM
from utils.consts import FLOAT_ZERO, INFTY, W_LBL
from utils.funcs import emd, get_labels

from icecream import ic

from server import conf


class Branch(Sia):
    """Class Branch is used to solve the mip problem using Branch&Bound strategy."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        causes: list[int],
        distrib: NDArray[np.float64],
        dual: bool,
    ) -> None:
        super().__init__(structure, effect, causes, distrib, dual)

        self.__effect_labels: None | list[str] = None
        self.__causes_labels: None | list[str] = None

        self.__net: nx.DiGraph | nx.Graph = nx.DiGraph() if conf.directed else nx.Graph()

    def analyze(self) -> bool:
        ic(self._effect, self._causes, self._target_dist)
        max_len = max(*self._effect, *self._causes) + 1
        labels = get_labels(max_len)
        self.__effect_labels = [f'{labels[i]}{T1_SYM}' for i in self._effect]
        self.__causes_labels = [f'{labels[j]}{T0_SYM}' for j in self._causes]

        self.__net = self.margin_n_expand()

        #
        raise NotImplementedError
        part: None = None
        mip = self.label_mip(part)
        self.min_info_part = mip
        not_std_sln = any(
            [
                # ! Store the network, generate the id and return it as callback in front ! #
                self.integrated_info == INFTY,
                self.min_info_part is None,
                self.sub_distrib is None,
                self.network_id is None,
            ]
        )

        return not_std_sln

    def margin_n_expand(self):
        concept_comb = list(it.product(self._causes, self._effect))

        self.__net.add_nodes_from(self.__effect_labels)
        self.__net.add_nodes_from(self.__causes_labels)
        self.__net.add_weighted_edges_from(
            (
                (
                    self.__causes_labels[self._causes.index(j)],
                    self.__effect_labels[self._effect.index(i)],
                    -1.0,
                )
                for j, i in concept_comb
            )
        )
        # deleted: dict[int, list[tuple[str, str, float]]] = {idx: [] for idx in self._effect}
        # En deldeted están las aristas eliminadas, tal que si hay una bipartición, pero se tiene un mínimo de infformación, se tenga el trazo.
        # Cual es el problema, si se genera una pérdida entonces es importante 2 cosas, primero tener las aristas que valen cero o elimiadas hasta elmomento y segundo (lo mismo), tener la arista que al eliminarse se generó una bipartición, a pesar que tenga valor de 0, para entonces guardarla (tenga peso o no) y listo, sería esta arista + eliminadas, en un diccionario en el que la clave es la tupla de la arista
        # No obstante la comparación eficiente entonces no es si la EMD es 0, sino si hay o no bipartición
        deleted: list[tuple[str, str, float]] = []
        mips: dict[str, str] = dict()
        """
        self._effect: [0, 4], self._causes: [0, 2, 4]
            self.__causes_labels: ['A(t=0)', 'C(t=0)', 'E(t=0)']
        """
        sub_concepts: list[tuple[int, int]] = []
        alt_struct = copy.deepcopy(self._structure)
        # self.plot_net(self.__net)
        for idx_causes, idx_effect in concept_comb:
            # Iteramos las aristas ya definidas en el producto causa efecto
            # ! Por qué no re-instanciar la matriz (no la clase)? [#15] ! #
            sub_struct: Structure = copy.deepcopy(alt_struct)
            sub_mat: Matrix = sub_struct.get_matrix(idx_effect)

            sub_states: list[int] = copy.deepcopy(self._causes)
            sub_states.remove(idx_causes)

            sub_mat.margin(sub_states)
            sub_mat.expand(self._causes)

            effect = {bin: ([] if self._dual == bin else self._effect) for bin in BOOL_RANGE}
            causes = {bin: ([] if self._dual == bin else self._causes) for bin in BOOL_RANGE}
            iter_distrib = sub_struct.create_distrib(effect, causes, data=True)[
                StructProps.DIST_ARR
            ]
            origin = self.__causes_labels[self._causes.index(idx_causes)]
            destiny = self.__effect_labels[self._effect.index(idx_effect)]

            emd_as_weight = emd(iter_distrib, self._target_dist)

            ic(self.__net.edges(data=True))
            ic(emd_as_weight, nx.is_connected(self.__net))
            ic(mips)

            self.__net.remove_edge(origin, destiny)
            if not nx.is_connected(self.__net):
                # Si es disconexo no reestablecemos la arista, la guardamos como logro independiente de si tuvo peso o no.
                print('No conexo')
                mips[(origin, destiny, emd_as_weight)] = deleted
                self.__net.add_weighted_edges_from([(origin, destiny, emd_as_weight)])

            elif emd_as_weight > FLOAT_ZERO:
                # Si es conexo Y hay pérdida entonces restablecemos la arsita.
                print('Recuperar arista')
                self.__net.add_weighted_edges_from([(origin, destiny, emd_as_weight)])

            else:
                # Si es conexo y no hay pérdida entonces guardamos la arista. A sy vez guardamos estas aristas en 0 para la reconstrucción.
                deleted.append((origin, destiny, emd_as_weight))
                alt_struct.set_matrix(idx_effect, sub_mat)

        if len(mips) > 0:
            info_loss = min(mips.keys(), key=lambda x: x[2])
            ic(info_loss)
            self.plot_net(self.__net)
        else:
            self.branch_and_bound()

    def branch_and_bound(self) -> tuple[tuple[tuple[str], tuple[str]]]:
        origin: Nodum = Nodum(ub=0.0, net=self.__net.copy())

        # We create a priority queue to store the nodes
        queue: list[Nodum] = []
        pq.heappush(queue, (FLOAT_ZERO, origin))

        gb: float = INFTY
        minimal_loss: Nodum = Nodum(ub=INFTY, net=self.__net.copy())

        # origin_net = origin.get_net()

        m: int = len(self._effect)
        n: int = len(self._causes)
        limit: int = 2 ** (m + n - 1)

        while len(queue) > 0:
            _, son = pq.heappop(queue)
            son: Nodum

            if any(
                (
                    len(son.get_ignored().keys()) == len(son.get_ordered_edges()),
                    son.get_ub() >= gb,
                )
            ):
                continue
            left: Nodum = Nodum(
                ub=son.get_ub(),
                net=son.get_net().copy(),
                ignore=son.get_ignored().copy(),
            )
            # Ordenamos las aristas para ignorar la primera
            for edge in left.get_ordered_edges():
                if (edge[0], edge[1]) in left.get_ignored().keys():
                    continue
                left.ignore_new((edge[0], edge[1]), {edge[1]})
                # set((edge[0],) if edge[1] in self.__effect_labels else (edge[1],),)
                break

            right: Nodum = Nodum(
                ub=son.get_ub(),
                net=son.get_net().copy(),
                ignore=son.get_ignored().copy(),
            )
            for edge in right.get_ordered_edges():
                if (edge[0], edge[1]) in right.get_ignored().keys():
                    continue
                r_net: nx.Graph = right.get_net()

                right._ub += self.calculate_ub(right, edge)

                r_net.remove_edge(edge[0], edge[1])
                break

            if nx.is_connected(right.get_net()):
                pq.heappush(queue, (-right.get_ub(), right))
            elif right.get_ub() < gb:
                gb = round(right.get_ub(), 4)
                if right.get_ub() < minimal_loss.get_ub():
                    minimal_loss: Nodum = right

            if nx.is_connected(left.get_net()):
                pq.heappush(queue, (-left.get_ub(), left))
            elif left.get_ub() < gb:
                gb = round(left.get_ub(), 4)
                if left.get_ub() < minimal_loss.get_ub():
                    minimal_loss: Nodum = left

            self.biplot(left.get_net(), right.get_net())
            limit -= 1
            if limit < 0:
                raise HTTPException(
                    # status_code=status.HTTP_406_NOT_ACCEPTABLE,
                    status_code=status.HTTP_508_LOOP_DETECTED,
                    detail='Maximal limit has been reached.',
                )
        self.integrated_info = minimal_loss.get_ub()
        return minimal_loss.get_net()

    def calculate_ub(self, right: Nodum, edge: tuple[str, str, float]) -> float:
        return edge[2][W_LBL]

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

        # Draw the bipartite graph
        nx.draw(net, pos=pos, with_labels=True)

        # Add edge labels
        labels = nx.get_edge_attributes(net, W_LBL)
        # Displace the labels horizontally
        for (u, v), weight in labels.items():
            offset = np.random.default_rng(seed=1).uniform(-0.2, 0.2)
            pos_y = (pos[u][1] + pos[v][1]) / 2 + offset
            pos_x = (pos[u][0] + pos[v][0]) / 2 + offset
            plt.text(pos_x, pos_y, weight, ha='center', va='center')

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
