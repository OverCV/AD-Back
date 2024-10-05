from pyparsing import alphas
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
        """
        # x = (t, t+1)

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




        """

        edges_idx: list[tuple[int, int]] = list(it.product(self._actual, self._effect))

        limit: int = 2 ** (len(self._actual) + len(self._effect)) - 1
        limit: int = 1

        while limit > 0:
            print('Se empieza con un elemento del iterable distinto cada vez')
            betha = edges_idx[:]
            omega = []

            #


            print(betha)
            for i, (u, v) in enumerate(betha):
                alpha = betha[:]
                edge = (u, v)
                print(f'Iteración {i}')
                print(f'Elemento {u, v}')
                print(f'Omega {omega}')
                betha.remove(edge)
                betha.pop()

            # ! Decrement ! #
            limit -= 1

        # print(concepts)

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
