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
        self.__net = self.strategy()

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

        print('Hello math!')

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

    def strategy(self) -> nx.DiGraph | nx.Graph:
        """Method margin_n_expand is used to generate the network from the structure."""
        concept_comb = list(it.product(self._actual, self._effect))
        ic(concept_comb)
        ic(self._actual, self._effect)

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
