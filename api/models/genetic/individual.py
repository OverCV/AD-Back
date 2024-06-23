import numpy as np
from numpy.typing import NDArray


class Individual:
    ''' Class Individual is used to represent a solution. '''

    def __init__(
        self, cms: NDArray, dist: NDArray
    ) -> None:
        self._cms: NDArray[np.bool_] = cms
        self._dist: NDArray = dist
        self._fitness: float = None

    def set_cms(self, cms: NDArray) -> None:
        self._cms = cms

    def get_cms(self) -> NDArray[np.bool_]:
        return self._cms

    def set_dist(self, dist: NDArray) -> None:
        self._dist = dist

    def get_dist(self) -> NDArray:
        return self._dist

    def set_fitness(self, fit: float) -> None:
        self._fitness = fit

    def get_fitness(self) -> float:
        return self._fitness

    def __str__(self) -> str:
        return f'Individual: {self._cms} - {self._fitness}\n{self._dist}\n'
