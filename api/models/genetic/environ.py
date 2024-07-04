from numpy import float64
from numpy.typing import NDArray

from api.models.genetic.individual import Individual
from api.models.genetic.population import Population
from api.models.genetic.reporter import Reporter


class Environ:
    """Class Environ is used to evolve a population.
    This is achieved using the genetic algorithm definiton of genetic operators. ."""

    def __init__(
        self,
        ctrl_params: dict[str, float | int],
        sys_config: dict[str, str | list[int]],
        # subtensor: list[Matrix],
        # logs: Logger,
    ) -> None:
        self._population: Population = Population()
        self._target_dist: NDArray[float64] = None

        self._ctrl_params: dict[str, float | int] = ctrl_params
        self._sysconfig: dict[str, list] = sys_config
        # self._subtensor: list[Matrix] = subtensor
        self._logger: Reporter = reps

    def evolve(self) -> Individual:
        """Method evolve is used to evolve the population."""
        pass