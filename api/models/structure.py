from collections import OrderedDict
from typing import Callable
from fastapi import HTTPException
from numpy.typing import NDArray
import numpy as np

from api.models.matrix import Matrix
from api.models.props.structure import StructProps
from constants.structure import BIN_RANGE
from utils.consts import INT_ONE, INT_ZERO, STR_ONE


from utils.funcs import be_product, le_product
from server import conf

from icecream import ic


class Structure:
    """Class Structure is used to easily manage the tensorial operations."""

    def __init__(
        self,
        db_struct: dict[str, int | str],
        istate: str,
        tensor: NDArray[np.float64] | OrderedDict[int, Matrix],
    ) -> None:
        # ! Acá se debería poder marginalizar muy eficientemente!
        self.__title: str = db_struct.get(StructProps.TITLE, 'no title')
        self.__istate: str = istate

        # Setted parameters
        self.__effect: str | None = None
        self.__causes: str | None = None

        self.__tensor: dict[int, Matrix] = (
            OrderedDict((idx, Matrix(arr)) for idx, arr in enumerate(tensor))
            if isinstance(tensor, np.ndarray)
            else tensor
        )
        # (

        #     if isinstance(tensor, list)
        #     else tensor
        # )
        self.__prim_dist: NDArray[np.float64] = None
        self.__dual_dist: NDArray[np.float64] = None

        # self.__nodes = set(range(db_sys.get(SysProps.SIZE, -1)))
        # validate.network(self)

    def create_concept(
        self, effect: str, causes: str, data: bool = False
    ) -> NDArray[np.float64] | None:
        # ! Here may be a validation of the ec inputs, validate effect.size == tensor.size and for all matrices, the effect of its side=(prim|dual) is 2^n == matriz.rows [#00] ! #
        ic(conf.little_endian)
        self.__set_effect(effect)
        self.__set_causes(causes)
        self.__correlate()
        return self.set_dists(data=data)

    def set_dists(self, data: bool = False) -> NDArray[np.float64] | None:
        """Calculates the serie distribution of the system. Precondition is that the system has to be set it's effect and causes correctly depending on the size of the tensor. Then, those matrices are used for the purpose of obtaining the full distribution composed by the primal and dual distributions.

        {set_effect 101 - set_causes 01}:
            effect = {T:[0,1,4], F:[]} causes = {T: [2,4], F: []}

        Args:
            data (bool, optional): When set to true, returns the probability distribution, by default is set as a calculated attribute. Defaults to False.

        Returns:
            NDArray[np.float64]: The probability distribution array.
            None: If the data is set to False, else returns the distribution of the system.
        """

        # if len(effect) != len(causes) and len(effect) != len(self.__tensor):
        #     raise HTTPException(
        #         status_code=400,
        #         detail='Effect and causes must have the same length. Also the tensor

        # Accedemos al primal y dual del sistema
        prim_effect = self.__effect[True]
        dual_effect = self.__effect[False]

        prim_tensor: list[NDArray[np.float64]]
        dual_tensor: list[NDArray[np.float64]]
        unit_matrix: NDArray[np.float64] = np.array([INT_ONE], dtype=np.float64)
        # cout(f'1. prim {prim_effect}, dual {dual_effect}')
        # By definition, is not possible to have both tensors empty
        prim_tensor = (
            unit_matrix
            if len(prim_effect) == INT_ZERO
            else [self.__tensor[idx].at_state(self.__istate) for idx in prim_effect]
        )
        dual_tensor = (
            unit_matrix
            if len(dual_effect) == INT_ZERO
            else [self.__tensor[idx].at_state(self.__istate) for idx in dual_effect]
        )
        # cout(f'2. prim {prim_tensor}, dual {dual_tensor}')

        product: Callable = le_product if conf.little_endian else be_product
        self.__prim_dist = product(prim_tensor)
        self.__dual_dist = product(dual_tensor)
        ic(self.__prim_dist, self.__dual_dist)

        dist = product([self.__prim_dist, self.__dual_dist])

        return dist if data else None

    def __correlate(self) -> None:
        """Sets the tensor matrices to it's primal and dual marginalization. The effect and causes must be setted before calling this function. The effect and causes are used to select the matrices that are going to be marginalized. The marginalization is done by the effect and causes, the effect is used to select the matrices that are going to be marginalized by the causes. The causes are used to select the states that are going to be marginalized."""
        if self.__effect is None or self.__causes is None:
            raise HTTPException(status_code=400, detail='Effect and causes must be setted.')
        for i in range(BIN_RANGE):  # ! Paralelize this ! #
            for idx in self.__effect[bool(i)]:
                ic(bool(i), idx)
                mat: Matrix = self.__tensor[idx]
                mat.margin(self.__causes[bool(i)])
        # for idx in self.__effect[False]:
        #     cout(f'F idx: {idx}')
        #     mat: Matrix = self.__tensor[idx]
        #     mat.margin(self.__causes[False])
        # for idx in self.__effect[True]:
        #     cout(f'T idx: {idx}')
        #     mat: Matrix = self.__tensor[idx]
        #     mat.margin(self.__causes[True])

    def __set_effect(self, effect: str) -> None:
        self.__effect = {True: list(), False: list()}
        for i, b in enumerate(effect):
            self.__effect[b == STR_ONE].append(i)

    def __set_causes(self, causes: str) -> None:
        self.__causes = {True: list(), False: list()}
        for i, b in enumerate(causes):
            self.__causes[b == STR_ONE].append(i)

            # subtensor[idx] = self.__tensor[idx]
        # [
        #     cout(k, m) for k, m in self.__tensor.items()
        # ]

    def get_distribution(self, dual: bool = False) -> NDArray[np.float64]:
        return self.__dual_dist if dual else self.__prim_dist

    def get_istate(self) -> str:
        return self.__istate

    def get_effect(self) -> str:
        return self.__effect

    def get_causes(self) -> str:
        return self.__causes

    def get_tensor(self) -> OrderedDict[int, Matrix]:
        return self.__tensor

    def get_tensor_len(self) -> int:
        return len(self.__tensor)

    def get_title(self) -> str:
        return self.__title

    def __str__(self) -> str:
        return f'{self.__title} : {self.__istate}, {self.__effect}, {self.__causes}, {self.__nodes}'

    # def drop_matrices(self, mat_idxs: list[int]) -> None:
    #     self.__effect = None
    #     self.__causes = None
    #     for elem in mat_idxs:
    #         self.__tensor.pop(elem)

    # # def subsystem(self, dual: bool = False) -> None:
    # #     # Given the effect and causes, this function takes the primal selection for the tensor and returns the subsystem.
    # #     subtensor = dict()

    # #     for idx in self.__effect[dual]:
    # #         cout(f'idx: {idx}')
    # #         mat: Matrix = self.__tensor[idx]
    # #         mat.margin(self.__causes[dual])
    # #         subtensor[idx] = self.__tensor[idx]

    # #     # for idx in self.__effect[not dual]:
    # #     #     cout(f'idx: {idx}')
    # #     #     mat: Matrix = self.__tensor[idx]
    # #     #     mat.margin(self.__causes[not dual])
    # #     #     subtensor[idx] = self.__tensor[idx]

    # #     # Eliminamos los estados del lado elegido
    # #     self.__effect[not dual] = list()
    # #     self.__causes[not dual] = list()
    # #     # Asignamos el tensor reducido
    # #     self.__tensor = subtensor
