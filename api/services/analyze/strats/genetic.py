import numpy as np
from numpy.typing import NDArray


from api.models.genetic.environ import Environ
from api.models.props.structure import StructProps
from api.models.structure import Structure
from api.schemas.genetic.control import ControlSchema
from api.services.analyze.sia import Sia

from icecream import ic
from constants.dummy import DUMMY_MIN_INFO_PARTITION, DUMMY_NET_INT_ID, DUMMY_SUBDIST
from utils.consts import INFTY_POS, ROWS_IDX, STR_ONE, STR_ZERO


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

        # part=('010', '000')
        # best: Individual: [ True False  True  True  True  True], 0.25
        m: int = len(self._effect)
        # ic(self._actual, self._effect)
        # ind_effect = ''.join([str(int(i)) for i in best.get_chr()[StructProps.DIST_ARRAY][:m]])
        # ind_actual = ''.join([str(int(i)) for i in best.get_chr()[StructProps.DIST_ARRAY][m+1:]])
        print()
        # ic(best.get_chr())
        ind_effect = [STR_ONE if x else STR_ZERO for x in best.get_chr()[:m]]
        ind_actual = [STR_ONE if x else STR_ZERO for x in best.get_chr()[m:]]
        mip = self.label_mip((''.join(ind_effect), ''.join(ind_actual)))
        # ic(ind_effect, ind_actual)
        # ic(mip)
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

        self.integrated_info = best.get_fitness()
        self.min_info_part = mip
        self.sub_distrib = best.get_dist()[StructProps.DIST_ARRAY]
        self.network_id = DUMMY_NET_INT_ID

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
