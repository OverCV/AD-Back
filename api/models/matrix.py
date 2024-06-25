import math
from typing import Callable
import numpy as np
import pandas as pd
from numpy.typing import NDArray


from utils.consts import COLS_IDX, INT_ONE, ROWS_IDX, STR_ONE, STR_ZERO
from utils.funcs import big_endian, cout, lil_endian

from server import conf


class Matrix:
    ''' Class Matrix is used to apply marginalization actions over it's array. '''

    def __init__(self, array: NDArray[np.float64]) -> None:
        self.__array: NDArray[np.float64] = array
        self.__effect: set[int] = set(range(
            self.__array.shape[COLS_IDX]
        ))
        self.__causes: set[int] = set(range(int(
            math.log2(self.__array.shape[ROWS_IDX])
        )))
        # cout('shape', self.__array.shape, self.__effect, self.__causes)
        # cout(self.__array)

    def margin(
        self, states: list[int], axis: int = ROWS_IDX, dual: bool = False,
        le: bool = conf.little_endian, data: bool = False
    ) -> None | NDArray[np.float64]:
        """#! Propper documentation
        Args:
            states (list[int]): Represents the states to marginalize if dual is disabled, these states must be a subset of the causes because are the states to drop or preserve.
            axis (int, optional): _description_. Defaults to ROWS_IDX. This determine if we're marginalizing rows (0) or columns (1).
            dual (bool, optional): The actual matrix has a set of causes, on whichever the incoming state is, is marginalized if dual is disabled, else the given states are the states to preserve. Defaults to False.
            le (bool, optional): _description_. Defaults to conf.little_endian. Indicates if the generated states are in little or big endian notation.
        """
        self.__array = self.__array.transpose() \
            if axis == COLS_IDX else self.__array

        if set(states).difference(self.__causes):
            # ! Retornar un arreglo de tamaño según la dimensión de la columna de entrada.
            ...
        dataframe = self.as_dataframe()
        margined_rows = 2**(len(self.__causes) - len(states))

        notation: Callable = lil_endian if le else big_endian
        rows: list[str] = notation(len(states))
        zeros_df = pd.DataFrame(
            np.zeros((len(rows), dataframe.shape[COLS_IDX])),
            columns=dataframe.columns,
            index=rows
        )
        for row in dataframe.index:
            for col in dataframe.columns:
                selected_row = ''.join([row[i] for i in states])
                zeros_df.at[selected_row, col] += dataframe.at[row, col]

        zeros_df /= margined_rows if axis == ROWS_IDX else INT_ONE
        cout('zeros_df', zeros_df)

        # zeros_df.transpose() if axis == COLS_IDX else zeros_df
        if axis == COLS_IDX:
            self.__effect = set(states)
        else:
            self.__causes = set(states)
        self.__array = zeros_df.to_numpy().transpose() \
            if axis == COLS_IDX else zeros_df.to_numpy()
        if data:
            return self.__array

    def as_dataframe(self, le: bool = conf.little_endian) -> pd.DataFrame:
        notation: Callable = lil_endian if le else big_endian
        num_row_vars: int = int(math.log2(self.__array.shape[ROWS_IDX]))
        num_col_vars: int = int(math.log2(self.__array.shape[COLS_IDX]))
        col_states: list[str] = notation(num_col_vars)
        row_states: list[str] = notation(num_row_vars)
        return pd.DataFrame(self.__array, columns=col_states, index=row_states)

    # def margin_col(self, states: str) -> None:
    #     self.transposed()
    #     self.margin_row(states, False)
    #     self.transposed()
    #     return self.__array

    # def margin_row(self, states: str, from_row: bool = True, be: bool = False, dual=False) -> NDArray[np.float64]:
    #     """
    #     Margins the matrix with the given states.
    #     """
    #     dframe: pd.DataFrame = self.as_dataframe()
    #     indices_to_select: list[int] = self.find_indices(states)
    #     margined_rows = 2**states.count(STR_ZERO)

    #     if all(k == STR_ZERO for k in states):
    #         vector_sum: NDArray[np.float64] = np.sum(dframe, axis=0)
    #         collapsed: pd.DataFrame = pd.DataFrame(
    #             vector_sum.values.reshape(1, -1),
    #             columns=dframe.columns,
    #             index=[STR_ZERO]
    #         )
    #         dframe = collapsed
    #         if from_row:
    #             dframe /= margined_rows

    #     elif any(k == STR_ZERO for k in states):
    #         new_states: list[str] = lil_endian(states.count(STR_ONE))
    #         if be:
    #             new_states: list[str] = big_endian(states.count(STR_ONE))
    #         new_data: NDArray[np.float64] = np.zeros((len(new_states), dframe.shape[1]))
    #         matrix_zeros: pd.DataFrame = pd.DataFrame(
    #             new_data, columns=dframe.columns, index=new_states)
    #         for row in dframe.index:
    #             for col in dframe.columns:
    #                 selected_row = self.select_chars_at_indices(
    #                     row, indices_to_select)
    #                 matrix_zeros.at[selected_row, col] += dframe.at[row, col]
    #         if from_row:
    #             matrix_zeros /= margined_rows
    #         dframe = matrix_zeros

    #     self.__array = dframe.to_numpy()
    #     return self.__array

    # def select_chars_at_indices(
    #     self, cadena: list[str], indices: list[int]
    # ) -> str:
    #     ''' Select the chars at the given indices. '''
    #     # print('select_chars_at_indices', [cadena[i] for i in indices])
    #     return ''.join([cadena[i] for i in indices])

    # def find_indices(self, states: str) -> list[int]:
    #     return [i for i in range(len(states)) if states[i] == STR_ONE]

    # def select_series(self, states: list[str]) -> NDArray[np.float64]:
    #     ''' Select the serie at the given state. '''

    #     concat_digits: str = ''.join(states)
    #     matrix_information = self.as_dataframe()

    #     # ! Mirar el estado presente no sea vacío ! #
    #     if concat_digits == '':
    #         return self.__array

    #     return matrix_information.loc[[concat_digits]].values

    # def as_dataframe(self) -> pd.DataFrame:
    #     num_row_vars: int = int(math.log2(self.__array.shape[0]))
    #     num_col_vars: int = int(math.log2(self.__array.shape[1]))
    #     col_states: list[str] = lil_endian(num_col_vars)
    #     row_states: list[str] = lil_endian(num_row_vars)
    #     return pd.DataFrame(self.__array, columns=col_states, index=row_states)

    # def transposed(self):
    #     ''' Transpose the matrix with it's keys. '''
    #     self.__array: NDArray[np.float64] = self.__array.transpose()

    def __str__(self):
        return f'[Matrix]: \n{self.__array}\n'

    def copy(self):
        return Matrix(self.__array.copy())
