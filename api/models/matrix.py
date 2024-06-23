import math
import numpy as np
import pandas as pd

from utils.consts import COLS_IDX, ROWS_IDX, STR_ONE, STR_ZERO
from utils.funcs import big_endian, cout, lil_endian


class Matrix:
    ''' Class Matrix is used to apply marginalization actions over it's array. '''

    def __init__(self, ndarray: np.ndarray) -> None:
        self.__array: np.ndarray = ndarray
        self.__causes: set[int] = set(range(int(
            math.log2(self.__array.shape[ROWS_IDX])
        )))
        self.__effect: set[int] = set(range(
            self.__array.shape[COLS_IDX]
        ))
        cout('shape', self.__array.shape, self.__effect, self.__causes)
        # cout(self.__array)

    def margin_col(self, states: str) -> None:
        self.transposed()
        self.margin_row(states, False)
        self.transposed()
        return self.__array

    def margin_row(self, states: str, from_row: bool = True, be: bool = False, dual=False) -> np.ndarray:
        """
        Margins the matrix with the given states.
        """
        dframe: pd.DataFrame = self.as_dataframe()
        indices_to_select: list[int] = self.find_indices(states)
        margined_rows = 2**states.count(STR_ZERO)

        if all(k == STR_ZERO for k in states):
            vector_sum: np.ndarray = np.sum(dframe, axis=0)
            collapsed: pd.DataFrame = pd.DataFrame(
                vector_sum.values.reshape(1, -1),
                columns=dframe.columns,
                index=[STR_ZERO]
            )
            dframe = collapsed
            if from_row:
                dframe /= margined_rows

        elif any(k == STR_ZERO for k in states):
            new_states: list[str] = lil_endian(states.count(STR_ONE))
            if be:
                new_states: list[str] = big_endian(states.count(STR_ONE))
            new_data: np.ndarray = np.zeros((len(new_states), dframe.shape[1]))
            matrix_zeros: pd.DataFrame = pd.DataFrame(
                new_data, columns=dframe.columns, index=new_states)
            for row in dframe.index:
                for col in dframe.columns:
                    selected_row = self.select_chars_at_indices(
                        row, indices_to_select)
                    matrix_zeros.at[selected_row, col] += dframe.at[row, col]
            if from_row:
                matrix_zeros /= margined_rows
            dframe = matrix_zeros

        self.__array = dframe.to_numpy()
        return self.__array

    def select_chars_at_indices(
        self, cadena: list[str], indices: list[int]
    ) -> str:
        ''' Select the chars at the given indices. '''
        # print('select_chars_at_indices', [cadena[i] for i in indices])
        return ''.join([cadena[i] for i in indices])

    def find_indices(self, states: str) -> list[int]:
        return [i for i in range(len(states)) if states[i] == STR_ONE]

    def select_series(self, states: list[str]) -> np.ndarray:
        ''' Select the serie at the given state. '''

        concat_digits: str = ''.join(states)
        matrix_information = self.as_dataframe()

        # ! Mirar el estado presente no sea vacío ! #
        if concat_digits == '':
            return self.__array

        return matrix_information.loc[[concat_digits]].values

    def as_dataframe(self) -> pd.DataFrame:
        num_row_vars: int = int(math.log2(self.__array.shape[0]))
        num_col_vars: int = int(math.log2(self.__array.shape[1]))
        col_states: list[str] = lil_endian(num_col_vars)
        row_states: list[str] = lil_endian(num_row_vars)
        return pd.DataFrame(self.__array, columns=col_states, index=row_states)

    def transposed(self):
        ''' Transpose the matrix with it's keys. '''
        self.__array: np.ndarray = self.__array.transpose()

    def __str__(self):
        return f'[Matrix]: \n{self.__array}\n'

    def copy(self):
        return Matrix(self.__array.copy())
