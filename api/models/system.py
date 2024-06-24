from numpy.typing import NDArray
import numpy as np

from api.models.matrix import Matrix
from api.models.props.system import SysProps
from utils.consts import STR_ONE, STR_ZERO
from collections import OrderedDict


from utils.funcs import cout


class System:
    ''' Class System is used to easily manage the tensorial operations. '''

    def __init__(
        self, db_sys: dict[str, int | str],
        istate: str, effect: str, causes: str, tensor: list[NDArray[np.float64]]
    ) -> None:

        # ! Acá se debería poder marginalizar muy eficientemente!
        self.__title: str = db_sys.get(SysProps.TITLE, 'no title')
        self.__istate: str = istate
        self.__effect: str = effect
        self.__causes: str = causes
        # self.__effect: str = {i for i, b in enumerate(effect) if b == STR_ONE}
        # self.__causes: str = {i for i, b in enumerate(causes) if b == STR_ONE}
        self.__tensor: dict[int, Matrix] = OrderedDict(
            (idx, Matrix(arr)) for idx, arr in enumerate(tensor)
        )
        self.__distribution: NDArray[np.float64] = None
        self.__size = self.get_tensor_len()
        # self.__size = set(range(db_sys.get(SysProps.SIZE, -1)))

    def subsystem(self, effect: str, causes: str, dual: bool = False):
        # Given the effect and causes, this function takes the primal selection for the tensor and returns the subsystem.
        # R5 : effect 11001, causes: 01101, istate 10000, tensor size 5
        # prim ({A,B,E}, {B,C,E}) ; dual ({C,D}, {A,D}) #
        BIN: str = STR_ZERO if dual else STR_ONE

        subtensor = []
        for idx, e in enumerate(effect):
            if idx not in self.__tensor.keys():
                continue
            if e == BIN:
                ...
                
            else:
                continue

        return System(
            db_sys={SysProps.TITLE: 'subsystem'},
            istate=[
                {i: None for i in range(5) if i in self.__size}
            ],
            effect=None,
            causes=None,
            tensor=subtensor
        )

    def obtain_dist(self) -> None:
        ''' Returns the distribution of the system. '''

        # Main logic is to set the effect and causes states to just apply the marginalization over the system

        # R5 : effect 11001, causes: 01101, istate 10000, tensor size 5
        # prim ({A,B,E}, {B,C,E}) ; dual ({C,D}, {A,D}) #

        # effect = {i for i, b in enumerate(self.__effect) if b == STR_ONE}
        # causes = {i for i, b in enumerate(self.__causes) if b == STR_ONE}
        cout(f'Implementing!')

        # Si se pide la distribución original del sistema se debe tener en cuenta la notación utilizada en la configuración del sistema, además de los canales utilizados. Se está haciendo la presuposición de que se tiene un sistema con N matrices, cada una marginalizada a su canal propio, de la forma S2P.
        # Debe aprovecharse el paralelismo, así como la capacidad de marginalizar eficientemente mediante la dualidad del sistema.

        #  np.empty_like

        # Tomamos cada uno de los elementos del tensor, paralelizado cada uno empezamos:

        # La matriz tiene una posición, en el efecto determinamos si es primal (1) o dual (0), en función a esto marginalizamos

        # Para marginalizar si es primal pasamos los índices donde equivalga a 1, para dual pasamos los índices donde equivalga a 0.

        # La Matriz debe ser capaz de marginalizar el arreglo a una forma determinada a la primal y a la par la dual.

        # La primal de la dual pueden diferir en tamaños, por lo que únicamente hasta que se seleccione su estado inicial es que todas se podrán unir.

        # R5 : istate 10000, effect 11001 = {A,B,E}, causes: 01101 = {B,C,E}
        # Marginalizar el efecto es tomar la primal
        # Marginalizar las causas implica tomar la sección primal
        # Posteriormente se selecciona el estado inicial para las matrices de la primal
        # Seleccionadas las series se procede con el producto tensorial de las matrices primales

    def get_distribution(self) -> NDArray[np.float64]:
        pass

    def get_istate(self) -> str:
        return self.__istate

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
