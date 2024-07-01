import copy
from email.iterators import _structure
import itertools

from fastapi import HTTPException
from api.models.props.sia import SiaType
from api.models.structure import Structure
from api.services.analyze.sia import Sia

import numpy as np
from numpy.typing import NDArray

from constants.structure import BOOL_RANGE
from utils.consts import BEST_DISTRIBUTION, CAUSES, EFFECT, INFTY, MIP, NET_ID, SMALL_PHI, STR_ONE
from utils.funcs import dec2bin, emd

from icecream import ic


class BruteForce(Sia):
    """Class Brute Force is used to solve the problem by brute force."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        causes: list[int],
        distribution: NDArray[np.float64],
        dual: bool,
    ) -> None:
        super().__init__(structure, effect, causes, distribution, dual)

    def analyze(self) -> dict:
        # Declare
        ic(self._target_dist)
        ic(self._effect, self._causes, self._dual)

        # raise HTTPException(status_code=500, detail='Not implemented')

        bipartitions = self.bipartitionate(len(self._effect), len(self._causes))
        origin = bipartitions.pop(0)

        ic(bipartitions)
        min_emd: bool = INFTY
        mip: tuple[tuple[str, str], tuple[str, str]] = None
        best_dist = None

        # Begin
        for part in bipartitions:
            sub_struct = copy.deepcopy(self.structure)
            str_effect: str = part[EFFECT]
            str_causes: str = part[CAUSES]

            effect = {bin: [] for bin in BOOL_RANGE}
            for i, e in zip(self._effect, str_effect):
                effect[e == STR_ONE].append(i)
            causes = {bin: [] for bin in BOOL_RANGE}
            for j, c in zip(self._causes, str_causes):
                causes[c == STR_ONE].append(j)
            ic(effect, causes)
            # Calculate distribution... by algorithm!
            ic(str_effect, str_causes, effect, causes)
            iter_distrib = sub_struct.create_concept(effect, causes, data=True)
            # Comparar con la distribución original
            emd_dist = emd(*iter_distrib, *self._target_dist)
            if emd_dist < min_emd:
                min_emd = emd_dist
                mip = (str_effect, str_causes)
                best_dist = iter_distrib

        return {
            # ! Store the network, get the id and return it to invoque in front ! #
            NET_ID: -1,
            SMALL_PHI: min_emd,
            MIP: mip,
            BEST_DISTRIBUTION: best_dist.tolist(),
        }

    def get_reperoire(self) -> SiaType:
        concept: SiaType = {
            NET_ID: self._network,
            SMALL_PHI: self._integrated_info,
            MIP: self._min_info_part,
            BEST_DISTRIBUTION: self.distribution,
        }
        return concept

    def bipartitionate(self, m: int, n: int) -> list[dict[str, tuple[str, str]]]:
        """Genera las biparticiones binarias para un tamaño m de filas por m columnas, de forma que se genera la mitad de combinaciones para filas pero todas las columnas.

        Args:
            m (int): Número de filas a usar
            n (int): Número de columnas a usar.

        Returns:
            list[dict[str, tuple[str, str]]]: El listado de combinaciones duales en formato de lista de tuplas, donde 0 implica la variable está en la partición dual y 1 que está en la primal.
        """
        future_states: list[str] = [dec2bin(b, m) for b in range(2 ** (m - 1))]
        current_states: list[str] = [dec2bin(b, n) for b in range(2**n)]
        return list(itertools.product(future_states, current_states))
        # return list(
        #     (comb[0], comb[1])
        #     for comb in combinations
        #     if int(f'{comb[0][0]}{comb[1][0]}') != 0
        # )

    # def bipartitionate(self, n: int, m: int) -> list[dict[str, tuple[str, str]]]:
    #     future_states: list[str] = [
    #         (dec2bin(b, n), dec2bin(2**n - (b + 1), n)) for b in range(2 ** (n - 1))
    #     ]
    #     current_states: list[str] = [
    #         (dec2bin(b, m), dec2bin(2**m - (b + 1), m)) for b in range(2**m)
    #     ]
    #     combinations = list(itertools.product(future_states, current_states))
    #     return list(
    #         (
    #             (comb[0][0], comb[1][0]),
    #             (comb[0][1], comb[1][1]),
    #         )
    #         for comb in combinations
    #         if int(f'{comb[0][0]}{comb[1][0]}') != 0
    #     )
