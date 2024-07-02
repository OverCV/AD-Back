import copy
import itertools

from api.models.structure import Structure
from api.services.analyze.sia import Sia

import numpy as np
from numpy.typing import NDArray

from constants.structure import BOOL_RANGE, VOID
from utils.consts import (
    INT_ZERO,
    CAUSES,
    EFFECT,
    INFTY,
    STR_ONE,
)
from utils.funcs import dec2bin, emd, get_labels
import concurrent.futures

from server import conf

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

    def analyze(self) -> bool:
        # Declare
        # ic(self._target_dist)
        ic(self._effect, self._causes, self._dual)

        # raise HTTPException(status_code=500, detail='Not implemented')

        bipartitions = self.bipartitionate(len(self._effect), len(self._causes))
        # No usamos la distribución original, es un caso absurdo.
        origin: tuple[str, str] = bipartitions.pop(0)

        # ic(bipartitions)
        # Begin
        part = (
            self.calculate_dists_threaded(bipartitions)
            if conf.threaded
            else self.calculate_dists(bipartitions)
        )
        mip = self.label_mip(part)

        self.network_id = -1
        self.min_info_part = mip

        not_std_sln = any(
            [
                self.integrated_info == INFTY,
                self.min_info_part is None,
                self.sub_distrib is None,
                self.network_id is None,
            ]
        )
        return not_std_sln
        # return {
        #     # ! Store the network, get the id and return it to invoque in front ! #
        #     NET_ID: -1,
        #     SMALL_PHI: self.integrated_info,
        #     MIP: mip,
        #     SUB_DISTRIBUTION: self.sub_distrib.tolist(),
        # }

    def label_mip(self, partition: tuple[str, str]) -> tuple[tuple[tuple[str], tuple[str]]]:
        # Incrementamos uno puesto son índices de arreglo
        max_len = max(*self._effect, *self._causes) + 1
        labels = get_labels(max_len)
        concepts = [self._effect, self._causes]
        mip = [[[], []], [[], []]]

        for k, (part, con) in enumerate(zip(partition, concepts)):
            ic(k, part, con)
            for b, lbl_idx in zip(part, con):
                mip[int(b)][k].append(labels[lbl_idx])

        for con in mip[EFFECT]:
            if len(con) == INT_ZERO:
                con.append(VOID)
        for con in mip[CAUSES]:
            if len(con) == INT_ZERO:
                con.append(VOID)

        return tuple(mip)

    def calculate_dists_threaded(self, bipartitions: tuple[tuple[str, str]]) -> tuple[str, str]:
        self.integrated_info = INFTY
        mip = None

        def process_partition(partition):
            sub_struct = copy.deepcopy(self._structure)
            str_effect = partition[EFFECT]
            str_causes = partition[CAUSES]

            effect = {bin: [] for bin in BOOL_RANGE}
            for j, e in zip(self._effect, str_effect):
                effect[e == STR_ONE].append(j)
            causes = {bin: [] for bin in BOOL_RANGE}
            for i, c in zip(self._causes, str_causes):
                causes[c == STR_ONE].append(i)

            iter_distrib = sub_struct.create_concept(effect, causes, data=True)
            emd_dist = emd(*iter_distrib, *self._target_dist)
            return emd_dist, iter_distrib, (str_effect, str_causes)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(
                    process_partition,
                    partition,
                )
                for partition in bipartitions
            ]
            for future in concurrent.futures.as_completed(futures):
                emd_dist, iter_distrib, current_mip = future.result()
                if emd_dist < self.integrated_info:
                    self.integrated_info = emd_dist
                    self.sub_distrib = iter_distrib
                    mip = current_mip
        return mip

    # Non-Threaded version:
    def calculate_dists(self, bipartitions: tuple[tuple[str, str]]) -> tuple[str, str]:
        self.integrated_info = INFTY
        mip: tuple[str, str] = None

        for partition in bipartitions:
            sub_struct: Structure = copy.deepcopy(self._structure)
            str_effect: str = partition[EFFECT]
            str_causes: str = partition[CAUSES]

            effect = {bin: [] for bin in BOOL_RANGE}
            for j, e in zip(self._effect, str_effect):
                effect[e == STR_ONE].append(j)
            causes = {bin: [] for bin in BOOL_RANGE}
            for i, c in zip(self._causes, str_causes):
                causes[c == STR_ONE].append(i)
            iter_distrib = sub_struct.create_concept(effect, causes, data=True)
            # Comparar con la distribución original (objetivo)
            emd_dist = emd(*iter_distrib, *self._target_dist)
            if emd_dist < self.integrated_info:
                self.integrated_info = emd_dist
                self.sub_distrib = iter_distrib
                mip = partition
        return mip

    def bipartitionate(self, m: int, n: int) -> list[tuple[str, str]]:
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
