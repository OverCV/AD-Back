from copy import deepcopy

import numpy as np
from numpy.typing import NDArray
from api.models.genetic.individual import Individual
from api.models.structure import Structure
from constants.structure import BOOL_RANGE
from utils.consts import ACTUAL, EFFECT, STR_ONE

from server import conf
from icecream import ic


class Population:
    """Class Population is used to cause effects over the individuals."""

    def __init__(
        self,
        distribution: NDArray[np.float64],
        concept: tuple[list[int], list[int]],
        structure: Structure,
    ) -> None:
        self.__indivis: list[Individual] = []
        self.__struct: Structure = structure
        self.__effect: list[int] = concept[EFFECT]
        self.__actual: list[int] = concept[ACTUAL]
        # self.__distrib: NDArray[np.float64] = distribution

    def get_size(self) -> int:
        return len(self.__indivis)

    def get_concept(self) -> tuple[list[int], list[int]]:
        return (deepcopy(self.__effect), deepcopy(self.__actual))

    def get_individuals(self) -> list[Individual]:
        return deepcopy(self.__indivis)

    def set_individuals(self, individuals: list[Individual]) -> None:
        self.__indivis = individuals

    # def get_distrib(self) -> NDArray[np.float64]:
    #     return self.__distrib

    def generate_individuals(self, pop_size) -> None:
        """
        INPUT:
        cms1 -> ABC|DE
             -> [FVV.FV] = (BC.E)(A.D)
        """
        # Debate: Si el máximo de combinaciones es eg. 32, cómo se le pide una población de eg. 100 individuos?
        chromosomes: NDArray[np.float64] = (
            self.generate_random
            if pop_size == 0
            else self.generate_k_cms(len(self.__effect), len(self.__actual), pop_size)
        )
        ic(len(self.__effect), len(self.__actual))
        # ic(chromosomes)
        validated_cms = self.validate_cms(chromosomes)
        sub_dists = self.update_distribution(validated_cms)

        self.set_individuals(
            [Individual(chr, sub_dist) for chr, sub_dist in zip(validated_cms, sub_dists)]
        )
        # [ic(ind) for ind in self.__indivis]

        # self.__indivis = [Individual(chromosome, self.__struct) for chromosome in chromosomes]

    def update_distribution(self, cms: list[NDArray[np.bool_]]) -> list[NDArray[np.float64]]:
        # ! Check for the duality, also Threading! [#14] ! #
        # self.__distrib = distribution
        sub_distrib: list[tuple[tuple[int, ...], NDArray[np.float64]]] = []
        separator: int = len(self.__effect)
        for chromosome in cms:
            effect = {bin: [] for bin in BOOL_RANGE}
            actual = {bin: [] for bin in BOOL_RANGE}
            for j, e in zip(self.__effect, chromosome[:separator]):
                effect[e].append(j)
            for i, c in zip(self.__actual, chromosome[separator:]):
                actual[c].append(i)
            sub_distrib.append(
                deepcopy(self.__struct).create_distrib(
                    effect,
                    actual,
                    data=True,
                )
            )
        # ic(sub_distrib)
        return sub_distrib

    def validate_cms(self, cms: list[NDArray[np.bool_]]) -> list[NDArray[np.bool_]]:
        for chr in cms:
            all_true = np.all(chr, axis=0)
            all_false = np.all(~chr, axis=0)

            if all_false or all_true:
                rnd_idx = np.random.randint(0, len(chr))
                chr[rnd_idx] = ~chr[rnd_idx]
        return cms

    def generate_random(self, m: int, n: int) -> NDArray[np.bool_]:
        # Creamos un arreglo de flotantes de tamaño n + m
        floating = np.random.randint(0, 2, size=(n + m, n + m))
        # Lo volvemos uno de booleanos con la condición de que el valor > 0.5
        return floating > 0.5

    def generate_cms(self, m: int, n: int) -> NDArray[np.bool_]:
        # Número total de combinaciones binarias para n bits
        total_combinaciones = 2**n
        # Crear un array de enteros que representa los números binarios
        enteros = np.arange(total_combinaciones, dtype=np.uint8)
        # Convertir los enteros a su representación binaria
        binarios = (enteros[:, None] & (1 << np.arange(n))) > 0
        # Crear un array de valores True de tamaño (total_combinaciones, m)
        trues = np.ones((total_combinaciones, m), dtype=bool)
        # Concatenar los valores True al inicio de cada fila del array binario
        return np.hstack((trues, binarios))

    def generate_k_cms(self, m: int, n: int, k: int) -> list[NDArray[np.bool_]]:
        # Crear un array de enteros que representa los números binarios
        total_combinaciones = 2 ** (m + n - 1) - 1
        mini_combs: int = min(k, total_combinaciones)

        if k > total_combinaciones:
            # Si las combinaciones brindadas por el usuario superan el tamaño máximo de combinaciones ofrecidas por fuerza bruta, usamos la primera forma (primera línea de combinaciones)
            return self.generate_cms(m, n)
        else:
            # Crear un arreglo de enteros desde 0 hasta mini_combs - 1
            enteros = np.arange(mini_combs, dtype=np.uint32)
            # Convertir cada entero a una matriz de bits booleana
            combinaciones_binarias = (enteros[:, None] & (1 << np.arange(m + n))) > 0
            return combinaciones_binarias
