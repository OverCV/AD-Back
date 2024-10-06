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


class Queyranne(Sia):
    """Class queyranne is used to solve the mip problem using the edges strategy."""

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

        ic(self.__effect_labels, self.__causes_labels)

        # ! Establecer mejor qué retorna la función (Grafo + ?) [#17] ! #
        # self.__net = self.strategy()
        self.macro()

        # edges = self.__net.edges(data=True)
        # self.integrated_info = min([edge[DATA_IDX][WT_LBL] for edge in edges])

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

    def macro(self) -> None:
        edges_idx: list[tuple[int, int]] = list(it.product(self._actual, self._effect))

        self.set_network_data(edges_idx)

        omega = []
        alpha = edges_idx[:]

        for _ in edges_idx:
            mips = []

            loses = []
            for x in alpha:
                lose = dict()

                emd = np.random.random() - np.random.random()

                trimmed_net = self.remove_edges(
                    self.__net.copy(),
                    omega + [x],
                )

                self.plot_net(trimmed_net)

                lose['edge'], lose['emd'], lose['disconnected'] = (
                    x,
                    emd,
                    net.is_disconnected(trimmed_net),
                )

                loses.append(lose)

            min_lose = min(loses, key=lambda x: x['emd'])
            # mip_iter = min([x for x in loses if x['disconnected']], key=lambda x: x['emd'])
            mip_iter = [x for x in loses if x['disconnected']]
            ic(min_lose, mip_iter)

            if len(mip_iter) > 0:
                # Si es disconexo
                min_mip_iter = min(mip_iter, key=lambda x: x['emd'])
                ic(min_mip_iter)
                return min_mip_iter

            print(min_lose)
            print(omega)

            alpha.remove(min_lose['edge'])
            omega.append(min_lose['edge'])

        print(omega)

    def remove_edges(
        self, net: nx.Graph | nx.DiGraph, edges: list[tuple[int, int]]
    ) -> nx.Graph | nx.DiGraph:
        # self.plot_net(net)
        for u, v in edges:
            net.remove_edge(
                self.actual_edge_by_index(u),
                self.effect_edge_by_index(v),
            )
        return net

    def set_network_data(self, concepts) -> None:
        self.__net.add_nodes_from(self.__effect_labels)
        self.__net.add_nodes_from(self.__causes_labels)
        self.__net.add_edges_from(
            (
                (
                    self.__causes_labels[self._actual.index(j)],
                    self.__effect_labels[self._effect.index(i)],
                )
                for j, i in concepts
            )
        )

    def actual_edge_by_index(self, index):
        return self.__causes_labels[self._actual.index(index)]

    def effect_edge_by_index(self, index):
        return self.__effect_labels[self._effect.index(index)]

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

    def meso(self) -> None:
        """
          # x = (t, t+1)
        ------

        omega = []
        alpha = edges[:]
        for _ in edges:
            loses=[]

            for x in alpha:
                emd = g(omega + [x]) - g([x])

                lose = Lose()
                lose.emd, lose.edge = emd, x
                loses.add(lose)

                # si net es desconexo, guardar como partición

            min_lose = min(loses)
            net.remove_edges(omega[:] + [min_lose.edge])

            alpha.remove(min_lose.edge)
            omega.add(min_lose.edge)


          -------
          se tiene [aA, aB, aC, bA, ..., cB, cC]

          omega = {}
          alpha = [aA, aB, aC, bA, ..., cB, cC]

              grafo eliminando (omega U Xi) - (Xi)

              toma un elem de alpha

              queda (x, alpha) no hay que ¿retomar?

                  g({} + {xi}) - g({xi})



          ciclo:

          por e en alpha:
          ---------

          omega vacio, alpha lleno. por cada elem en alpha, tomar un elemento y add en omega y se quita de alpha. Usar aleph como lista completa, realizar calculo EMD, de todas las iteraciones habrá un mejor, este se añade en omega.

          para la siguiente fase se tiene omega con un elemento (que genero minima perdida) en omega


          si en algún punto hubo bipartición en g(w U xi) se retorna como mejor

          -------
          edges = [x1, x2, ..., xn]
          aleph = [x1, x2, ..., xn] = edges[:]

          # for edge in edges:
          alpha = [x1, x2, ..., xn] = edges[:]
          omega = []

          while len(edges) - len(omega) > 0: | len(alpha) > 0: | for _ in edges:

              mips = dict()
              deletions: dict()

              for i=(0->n):
                  alpha = aleph[:]
                  x = alpha.pop(i)

                  emd = g(omega + [x]) - g([x])

                  for edge in omega+[x]:
                      graph.remove_edge(edge)

                  if is_disconnected(graph):
                      mips[tuple(omega+x)] = emd  # order matter?

                  deletions[x] = emd, alpha[:]

              if mips:
                  return min(mips => mip.value)

              gamma = min(deletions)
              gamma_idx = alpha.index(gamma)

              omega.add( aleph.pop(gamma_idx) )





        """

    def strategy(self) -> nx.DiGraph | nx.Graph:
        """Method margin_n_expand is used to generate the network from the structure."""
        concept_comb = list(it.product(self._actual, self._effect))
        ic(concept_comb)
        ic(self._actual, self._effect)

        alt_struct = copy.deepcopy(self._structure)

        edges_number: int = len(self._actual) * len(self._effect)
        inter_idx: int = 0
        last_idx: int = -1
        omega: list[set[str]] = [{}]

        while len(omega[last_idx]) < edges_number:
            sub_struct_xy: Structure = copy.deepcopy(alt_struct)
            sub_struct_y: Structure = copy.deepcopy(alt_struct)

        # El algoritmo tomará un elemento X futuro y marginalizará un elemento pasado y, esto lo realizará para todo t+1 en cada t.
        # De este listado se hará unión con algún otro elemento Z (totalidad) distinto, tratado en algún w. Sobre este elemento zwXY se aplicará la distancia métrica. Así msimo generamos diferencia con la distancia métrica de wZ, este resultado será almacenado para futuras comparaciones.
        # Del listado de valores de la iteración (IT1) se tomará el mínimo de forma que se pueda reconstruír el zwXY que lo generó. Este proceso se repite hasta que el conjunto de mínimos sea igual al número de aristas.

        """
        Ejemplo:
        (X|y), (Z|w)
        ---------
        omega = {}
        for (Xi, yj) in zip((t+1), (t)):
            # ? Para IT1
            smat_ij = mat[Xi]
            smat_kl = mat[Zk]

            # ! Xi U Zk
            states = all_states
            states -= wl
            smat_ij.margin(states)    # margin mantiene los parámetros
            smat_wl = smat_ij

            states -= yj
            smat_ij.margin(states)    # margin mantiene los parámetros

            smat_ij.expand(all_states)
            save.expand(all_states)

            llenar la lista de muestreo si la arista no está en omega

        """
