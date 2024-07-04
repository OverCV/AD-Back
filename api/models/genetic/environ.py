from ctypes import Structure
from numpy import float64
from numpy.typing import NDArray

from api.models.genetic.individual import Individual
from api.models.genetic.population import Population
from api.models.genetic.recorder import Recorder
from constants.genetic import INIT_POP_SIZE
from utils.consts import CAUSES, EFFECT

from icecream import ic

class Environ:
    """Class Environ is used to evolve a population.
    This is achieved using the genetic algorithm definiton of genetic operators. ."""

    def __init__(
        self,
        ctrl_params: dict[str, float | int],
        structure: Structure,
        distribution: NDArray[float64],
        concept: tuple[list[int], list[int]],
        dual: bool,
    ) -> None:
        self.__ctrl_params: dict[str, float | int] = ctrl_params
        # self.__structure: Structure = structure
        # self.__distribution: NDArray[float64] = distribution

        # self.__effect: list[int] = concept[EFFECT]
        # self.__causes: list[int] = concept[CAUSES]

        self.__population: Population = Population(distribution, concept, structure)
        self.__target_dist: NDArray[float64] = None
        self.__dual: bool = dual

    def evolve(self) -> Individual:
        """Method evolve is used to evolve the population."""
        # ! Inicialización de la población ! #
        ic(self.__population.get_concept())
        self.__population.generate_individuals(self.__ctrl_params[INIT_POP_SIZE])

        
