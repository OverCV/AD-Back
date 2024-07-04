from collections import OrderedDict
import numpy as np
from numpy.typing import NDArray

from fastapi import HTTPException

from api.models.structure import Structure
from api.schemas.genetic.control import ControlSchema
from api.services.analyze.sia import Sia

from icecream import ic

from constants.genetic import DEFAULT_PARAMS
from utils.consts import INFTY


class Genetic(Sia):
    """Class Zero is used to solve the problem by brute force."""

    def __init__(
        self,
        structure: Structure,
        effect: list[int],
        causes: list[int],
        distrib: NDArray[np.float64],
        dual: bool,
        ctrl_params: list[dict],
    ) -> None:
        super().__init__(structure, effect, causes, distrib, dual)
        # There's an environment for each control parameter
        self.__control_params: list[ControlSchema] = ctrl_params
        self.__environments: list = []

    def analyze(self) -> dict:
        # Definimos los parámetros de control para cada entorno del algoritmo genético, tal vez pueda paralelizarse #

        # ctrl_params: OrderedDict[int, dict[str, float | int]]
        # for param in self.__control_params:
        #     if all(value == 0 for value in param.values()):
        #         ctrl_params: dict[int, dict[str, float | int]] = OrderedDict(
        #             (0, DEFAULT_PARAMS),
        #         )
        #         break

        # num_envs = len(ctrl_params)
        #! rep: Reporter = Reporter()

        ic(self.__control_params)


        # ! Start time measurement ! #
        # ! Finish time measurement ! #
        raise HTTPException(status_code=300, detail='STOP TESTING')


        for k, env in ctrl_params.items():
            #! rep.report('Creating environment')
            self.__environments.append(
                # Environment
            )
            #! rep.report(f'Environment {i} created')
            pass

        # Post obtain solution

        mip = self.label_mip()

        # ic(iter_distrib.flatten(), self._target_dist.flatten())
        # 000 100 010 110 001 101 011 111
        # emd_dist = emd(*iter_distrib, *self._target_dist)

        self.network_id = -1
        self.min_info_part = ((('?',), ('¿',)), (('¿',), ('?',)))

        # ic(emd_dist)
        not_std_sln = any(
            [
                # ! Store the network, get the id and return it to invoque in front ! #
                self.integrated_info == INFTY,
                self.min_info_part is None,
                self.sub_distrib is None,
                self.network_id is None,
            ]
        )
        return not_std_sln
