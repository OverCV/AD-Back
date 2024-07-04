import numpy as np
from numpy.typing import NDArray


class Individual:
    """Class Individual is used to represent a solution."""

    def __init__(self, cms: NDArray[np.bool_], dist: NDArray[np.float64]) -> None:
        self.__chromosome: NDArray[np.bool_] = cms
        self.__distribution: NDArray[np.float64] = dist
        self.__fitness: float = None

    def set_cms(self, chromosome: NDArray[np.bool_]) -> None:
        self.__chromosome = chromosome

    def get_chr(self) -> NDArray[np.bool_]:
        return self.__chromosome

    def set_dist(self, distribution: NDArray[np.float64]) -> None:
        self.__distribution = distribution

    def get_dist(self) -> NDArray[np.float64]:
        return self.__distribution

    def set_fit(self, fitness: float) -> None:
        self.__fitness = fitness

    def get_fitness(self) -> float:
        return self.__fitness

    def __repr__(self) -> str:
        return f'Individual: {self.__chromosome} - {self.__fitness}\n{self.__distribution}\n'

    # def __str__(self) -> str:
    #     return f'Individual: {self.__chromosome} - {self.__fitness}\n{self.__distribution}\n'
