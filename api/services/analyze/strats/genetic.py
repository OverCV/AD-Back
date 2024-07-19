import numpy as np
from numpy.typing import NDArray


from api.models.genetic.environ import Environ
from api.models.structure import Structure
from api.schemas.genetic.control import ControlSchema
from api.services.analyze.sia import Sia

from icecream import ic
from utils.consts import INFTY_POS


class Genetic(Sia):
    """Class Zero is used to solve the problem by brute force."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        actual: list[int],
        distrib: NDArray[np.float64],
        dual: bool,
        ctrl_params: list[list[dict[str, int | float]]],
    ) -> None:
        super().__init__(structure, effect, actual, distrib, dual)
        # There's an environment for each control parameter
        self.__control_params: list[ControlSchema] = ctrl_params
        #! Use all envs required by ctrl params
        self.__environments: list = []

    def analyze(self) -> bool:
        # Definimos los parámetros de control para cada entorno del algoritmo genético, tal vez pueda paralelizarse #
        ic(self.__control_params)

        # ! Start time measurement ! #
        # ! Finish time measurement ! #

        # best_of_all
        for param in self.__control_params:
            #! rep.report('Creating environment')
            env: Environ = Environ(
                param,
                self._structure,
                self._target_dist,
                (self._effect, self._actual),
                self._dual,
            )
            best = env.evolve()

        ic(best)

        # self.__environments.append(
        #     # Environment
        # )
        #! rep.report(f'Environment {i} created')

        # ! Obtain the best solution from the registers ! #

        # Post obtain solution

        #! mip = self.label_mip()

        # ic(iter_distrib.flatten(), self._target_dist.flatten())
        # 000 100 010 110 001 101 011 111
        # emd_dist = emd(*iter_distrib, *self._target_dist)

        self.network_id = -1
        self.min_info_part = ((('?',), ('¿',)), (('¿',), ('?',)))

        # ic(emd_dist)
        not_std_sln = any(
            [
                # ! Store the network, get the id and return it to invoque in front ! #
                self.integrated_info == INFTY_POS,
                self.min_info_part is None,
                self.sub_distrib is None,
                self.network_id is None,
            ]
        )
        return not_std_sln
