from numpy.typing import NDArray
import numpy as np

from api.models.matrix import Matrix
from api.models.props.system import SysProps
from utils.consts import ROWS_IDX, STR_ONE, STR_ZERO

from collections import OrderedDict
from matplotlib.cbook import _OrderedSet


from utils.funcs import cout


class System:
    ''' Class System is used to easily manage the tensorial operations. '''

    def __init__(
        self, db_sys: dict[str, int | str],
        istate: str, tensor: list[NDArray[np.float64]]
    ) -> None:
        # ! Acá se debería poder marginalizar muy eficientemente!
        self.__title: str = db_sys.get(SysProps.TITLE, 'no title')
        self.__istate: str = istate
        self.__effect: str = {True: list(), False: list()}
        self.__causes: str = {True: list(), False: list()}

        # self.__effect: str = {i for i, b in enumerate(effect) if b == STR_ONE}
        # self.__causes: str = {i for i, b in enumerate(causes) if b == STR_ONE}
        self.__tensor: dict[int, Matrix] = OrderedDict(
            (idx, Matrix(arr)) for idx, arr in enumerate(tensor)
        )
        self.__distribution: NDArray[np.float64] = None

        # self.__size = self.get_tensor_len()
        self.__nodes = set(range(db_sys.get(SysProps.SIZE, -1)))
        # validate.network(self)

    def subsystem(self, dual: bool = False):
        # Given the effect and causes, this function takes the primal selection for the tensor and returns the subsystem.
        # R5 : effect 11001, causes: 01101, istate 10000, tensor size 5
        # prim ({A,B,E}, {B,C,E}) ; dual ({C,D}, {A,D}) #

        # R5 : effect: {T: [0, 1, 4], F: [2, 3]}, causes: {T: [1, 2, 4], F: [0, 3]}, istate: 10000, tensor size 5

        # BIN: str = STR_ZERO if dual else STR_ONE

        subtensor = []
        # for idx, e in:
        #     if idx not in self.__tensor.keys():
        #         continue
        #     if e == BIN:
        #         ...

        #     else:
        #         continue
        cout(f'effect: {self.__effect}\n causes: {self.__causes}')

        # Escogemos los tensores a usar y los marginalizamos

        for idx in self.__effect[not dual]:
            cout(f'idx: {idx}')
            mat: Matrix = self.__tensor[idx]
            mat.margin(self.__effect[dual])

        # ! Dada una cadena de binarios y una lista de elementos, las combinaciones binarias de elementos determinan si el elemento se va al True o al False de los canales del efecto o causa que se maneje

        # Eliminamos los estados del lado elegido para

        self.__effect[dual] = list()
        self.__causes[dual] = list()

        cout(f'effect: {self.__effect}\n causes: {self.__causes}')

        return System(
            db_sys={SysProps.TITLE: 'subsystem'},
            istate=[
                {i: None for i in range(5) if i in self.__nodes}
            ],
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

    def set_effect(self, effect: str) -> None:
        for i, b in enumerate(effect):
            self.__effect[bool(int(b))].append(i)

    def set_causes(self, causes: str) -> None:
        for i, b in enumerate(causes):
            self.__causes[bool(int(b))].append(i)

    def get_tensor(self) -> list[Matrix]:
        return self.__tensor

    def get_tensor_len(self) -> int:
        return len(self.__tensor)

    def __str__(self) -> str:
        return f'{self.__title} : {self.__istate}, {self.__effect}, {self.__causes}, {self.__nodes}'
