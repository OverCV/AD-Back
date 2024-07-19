from collections import OrderedDict
from fastapi import HTTPException
from numpy.typing import NDArray
import numpy as np

from api.models.matrix import Matrix

from api.models.props.structure import StructProps
from constants.structure import BOOL_RANGE
from server import conf

from icecream import ic

import concurrent.futures
from utils.funcs import product


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
        # Effect & Causes implies the actual working bipartition
        self.__effect: dict[bool, list[int]] | None = None
        self.__actual: dict[bool, list[int]] | None = None
        # Tensor composed by primal and dual matrices #
        self.__tensor: dict[int, Matrix] = (
            OrderedDict((idx, Matrix(arr)) for idx, arr in enumerate(tensor))
            if isinstance(tensor, np.ndarray)
            else tensor
        )
        self.__prim_dist: tuple[tuple[int, ...], NDArray[np.float64]] = None
        self.__dual_dist: tuple[tuple[int, ...], NDArray[np.float64]] = None

    def create_distrib(
        self, effect: dict[bool, list[int]], actual: dict[bool, list[int]], data: bool = False
    ):
        # ! Here may be a validation of the ec inputs, validate effect.size == tensor.size and for all matrices, the effect of its side=(prim|dual) is 2^n == matriz.rows [#00] ! #
        self.__set_effect(effect)
        self.__set_causes(actual)
        self.__correlate()
        return self.prod_dual_primal(data=data)

    def prod_dual_primal(self, data: bool = False, le: bool = conf.little_endian):
        """Calculates the serie distribution of the system. Precondition is that the system has to be set it's effect and actual correctly depending on the size of the tensor. Then, those matrices are used for the purpose of obtaining the full distribution composed by the primal and dual distributions.

        {set_effect 101 - set_causes 01}:
            effect = {T:[0,1,4], F:[]} actual = {T: [2,4], F: []}

        Args:
            data (bool, optional): When set to true, returns the probability distribution, by default is set as a calculated attribute. Defaults to False.

        Returns:
            NDArray[np.float64]: The probability distribution array.
            None: If the data is set to False, else returns the distribution of the system.
        """

        # if len(effect) != len(actual) and len(effect) != len(self.__tensor):
        #     raise HTTPException(
        #         status_code=400,
        #         detail='Effect and actual must have the same length. Also the tensor

        # Accedemos al primal y dual del sistema
        prim_effect = self.__effect[True]
        dual_effect = self.__effect[False]

        # pimr o dual pueden no ((idx,...), mat[idx,...])

        prim_tensor: tuple[tuple[int, ...], NDArray[np.float64]]
        dual_tensor: tuple[tuple[int, ...], NDArray[np.float64]]

        # cout(f'1. prim {prim_effect}, dual {dual_effect}')
        # By definition, is not possible to have both tensors empty
        prim_tensor = [((idx,), self.__tensor[idx].on_state(self.__istate)) for idx in prim_effect]
        dual_tensor = [((idx,), self.__tensor[idx].on_state(self.__istate)) for idx in dual_effect]
        # ic(prim_tensor, dual_tensor)
        # None
        # if len(dual_effect) == INT_ZERO
        # else [self.__tensor[idx].at_state(self.__istate) for idx in dual_effect]
        # cout(f'2. prim {prim_tensor}, dual {dual_tensor}')

        # endian_product: Callable = product if le else be_prod
        self.__prim_dist: tuple[tuple[int, ...], NDArray[np.float64]] = (
            product(prim_tensor) if len(prim_tensor) > 0 else None
        )
        self.__dual_dist: tuple[tuple[int, ...], NDArray[np.float64]] = (
            product(dual_tensor) if len(dual_tensor) > 0 else None
        )

        # ic(self.__prim_dist, self.__dual_dist)
        # self.__dual_dist = endian_product(dual_tensor)
        # How to know if a list is empty? An empty list has a boolean value of False, so we can use the following code to check if the list is empty:
        dist: tuple[tuple[int, ...], NDArray[np.float64]]
        if self.__prim_dist is None:
            dist = self.__dual_dist
        elif self.__dual_dist is None:
            dist = self.__prim_dist
        else:
            dist = product([self.__prim_dist, self.__dual_dist])
        # = (
        #     self.__dual_dist
        #     if prim_tensor is None
        #     else self.__prim_dist
        #     if dual_tensor is None
        #     else product([self.__prim_dist, self.__dual_dist])
        # )
        # ic(dist)
        return dist if data else None

    def __correlate(self) -> None:
        """Sets the tensor matrices to it's primal and dual marginalization. The effect and actual must be setted before calling this function. The effect and actual are used to select the matrices that are going to be marginalized. The marginalization is done by the effect and actual, the effect is used to select the matrices that are going to be marginalized by the actual. The actual are used to select the states that are going to be marginalized."""
        if self.__effect is None or self.__actual is None:
            raise HTTPException(status_code=400, detail='Effect and actual must be setted.')

        if conf.threaded:
            # Threaded version
            def process_matrices(b: bool) -> None:
                for idx in self.__effect[b]:
                    # ic(b, idx)
                    mat: Matrix = self.__tensor[idx]
                    mat.margin(self.__actual[b])

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [executor.submit(process_matrices, b) for b in BOOL_RANGE]
                # Esperar a que todas las tareas completen
                concurrent.futures.wait(futures)
        else:
            # Non-Threaded version
            for b in BOOL_RANGE:
                for idx in self.__effect[b]:
                    # ic(b, idx)
                    mat: Matrix = self.__tensor[idx]
                    mat.margin(self.__actual[b])

    def __set_effect(self, effect: dict[bool, list[int]]) -> None:
        self.__effect = effect

    def __set_causes(self, actual: dict[bool, list[int]]) -> None:
        self.__actual = actual

    def set_bg_cond(self, bg_cond: dict[bool, list[int]]) -> None:
        """
        Las condiciones de fondo implican que dada una cadena se va a manejar una parte del sistema de forma que para evitar pérdida de información el futuro mantiene las matrices, no obstante estas pueden perder sus causas.
        No se eliminan los futuros puesto simplifica operaciones, no obstante esto está regido a cambio puesto la implementación dicta una serie de selecciones basado en las matrices con su índice de existencia.
        """

        # self.init_concepts(effect)
        # self.__set_effect(effect)
        # self.__set_causes(effect)
        for b in BOOL_RANGE:
            for idx in bg_cond[b]:
                mat: Matrix = self.__tensor[idx]
                mat.at_states(self.__istate, bg_cond[b], bg_cond[not b])
                # ic(b, idx, bg_cond)
                # ic(idx, mat.as_dataframe())

    def set_matrix(self, index: int, mat: Matrix) -> None:
        self.__tensor[index] = mat

    def get_distrib(self, dual: bool = False) -> NDArray[np.float64]:
        return (
            self.__dual_dist[StructProps.DIST_ARR]
            if dual
            else self.__prim_dist[StructProps.DIST_ARR]
        )

    def get_istate(self) -> str:
        return self.__istate

    def get_effect(self) -> str:
        return self.__effect

    def get_causes(self) -> str:
        return self.__actual

    def get_matrix(self, idx: int) -> Matrix:
        return self.__tensor[idx]

    def get_tensor(self) -> OrderedDict[int, Matrix]:
        return self.__tensor

    def get_tensor_len(self) -> int:
        return len(self.__tensor)

    def get_title(self) -> str:
        return self.__title

    def __str__(self) -> str:
        return f'{self.__title} : {self.__istate}, {self.__effect}, {self.__actual}'

    """

    effect 10110
    actual 10110
    dual False

    struct.tensor = {0: (0,1,2,3,4), 1: (0,1,2,3,4), 2: (0,1,2,3,4), 3: (0,1,2,3,4), 4: (0,1,2,3,4)}

    idx_effect = [0, 2, 4]
    idx_causes = [0, 2, 4]


    """

    # [ic(k, mat.as_dataframe()) for k, mat in self.__tensor.items()]

    # Al configurar las condiciones de Background, en función al dual si envían 0 implica debemos mantener las posiciones en 0, las de 1 caso primal.
    # Reemplazamos primero el tensor según indique el efecto
    # effect = effect[not dual]
    # Vamos a tomar las condiciones de bg, nos interesa conocer estos estados causales.
    # actual = actual[dual]

    # self.__tensor = OrderedDict((idx, self.__tensor[idx]) for idx in effect)
    # self.__tensor = OrderedDict((idx, self.__tensor[idx].at_states(actual)) for idx in effect)
    # new_tensor = OrderedDict()
    # Seteamos las condiciones de backgroun para tanto el primal como el dual

    # self.__tensor[idx].at_states(self.__istate, actual)
    # new_tensor[idx] = self.__tensor[idx].at_states(self.__istate, actual)
    # self.__tensor = new_tensor
    # Subseleccionamos por cada matriz del tensor así mismo las filas donde se indique debe mantenerse la causa, de forma que si originalmente tenemos las combinaciones d  el [000, 100, 010, 110, ..., 111] pero el dual indica sólo seleccionar los elementos de forma 101 con dual off.
    # La entrada es 1 o 0, 1si dual=False entonces 1 ses primal y por ende vamos a seleccionar en dichos elementos, si está en 0 no lo seleccionamos, el valor estará delimitado por el istate, el estado inicial determina las secciones a tomar e ignorar

    # def drop_matrices(self, mat_idxs: list[int]) -> None:
    #     self.__effect = None
    #     self.__causes = None
    #     for elem in mat_idxs:
    #         self.__tensor.pop(elem)

    # # def subsystem(self, dual: bool = False) -> None:
    # #     # Given the effect and actual, this function takes the primal selection for the tensor and returns the subsystem.
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

    # def set_causes():
    # Hay que pasar si quiere que el indice quede en el primal o el dual
    # Por eso usabamos 101 porque así se sabe que cada elemento es una posición de la cadena de texto pero a cambio no conocemos cuál indice nos estamos refiriendo
    # No podemos usar el tensor per se puesto maneja los indices de las matrices en el futuro y no conocemos el presente, además que cada matriz es distinta y no se sabe a cuál partición estaríamos referenciando; Los índices determinan la partición de la matriz y no al contrario!!!

    # originamos de la cadena 10110, idx []
    # self.__causes = {True: list(), False: list()}
    # for idx in actual:
    #     self.__causes[b == STR_ONE].append(idx)
    # for i, b in enumerate(actual):
    #     self.__causes[b == STR_ONE].append(i)
