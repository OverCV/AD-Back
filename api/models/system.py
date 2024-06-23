from numpy.typing import NDArray
import numpy as np

from api.models.matrix import Matrix
from api.models.props.system import SysProps
from utils.consts import STR_ONE


class System:
    ''' Class System is used to easily manage the tensorial operations. '''

    def __init__(
        self, db_sys: dict[str, str],
        effect: str, causes: str, tensor: list[NDArray[np.float64]]
    ) -> None:

        # ! Acá se debería poder marginalizar muy eficientemente!
        self.__title: str = db_sys.get(SysProps.TITLE, 'no title')
        self.__istate: str = db_sys.get(SysProps.ISTATE, 'no istate')
        self.__effect: str = {i for i, b in enumerate(effect) if b == STR_ONE}
        self.__causes: str = {i for i, b in enumerate(causes) if b == STR_ONE}
        self.__tensor: list[Matrix] = [Matrix(arr) for arr in tensor]

    def get_effect(self) -> str:
        return self.__effect

    def get_causes(self) -> str:
        return self.__causes

    def get_tensor(self) -> list[Matrix]:
        return self.__tensor

    def get_tensor_len(self) -> int:
        return len(self.__tensor)

    def __str__(self) -> str:
        return f'{self.__title} - {self.__istate} - {
            self.__effect} - {self.__causes} - {len(self.__tensor)}'
