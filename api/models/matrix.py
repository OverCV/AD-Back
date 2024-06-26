import math
from typing import Callable
from fastapi import HTTPException
import numpy as np
import pandas as pd
from numpy.typing import NDArray


from utils.consts import COLS_IDX, INT_ONE, INT_ZERO, ROWS_IDX, STR_ONE, STR_ZERO
from utils.funcs import (
    big_endian, lil_endian,
    cout
)
#
from server import conf


class Matrix:
    ''' Class Matrix is used to apply marginalization actions over it's array. '''

    def __init__(self, array: NDArray[np.float64]) -> None:
        self.__array: NDArray[np.float64] = array
        # cout(1)
        self.__effect: list[int] = list(range(
            self.__array.shape[COLS_IDX]
        ))
        self.__causes: list[int] = list(range(
            int(math.log2(self.__array.shape[ROWS_IDX]))
        ))

    @ property
    def shape(self):
        return self.__array.shape

    def margin(
        self, states: list[int], axis: int = ROWS_IDX, dual: bool = False,
        le: bool = conf.little_endian, data: bool = False
    ) -> None | NDArray[np.float64]:
        """#! Propper documentation: Ahora se envían las que se salvan!!!
        Args:
            states (list[int]): Represents the states to marginalize if dual is disabled, these states must be a subset of the causes because are the states to drop or preserve.
            axis (int, optional): _description_. Defaults to ROWS_IDX. This determine if we're marginalizing rows (0) or columns (1).
            dual (bool, optional): The actual matrix has a set of causes, on whichever the incoming state is, is marginalized if dual is disabled, else the given states are the states to preserve. Defaults to False.
            le (bool, optional): _description_. Defaults to conf.little_endian. Indicates if the generated states are in little or big endian notation.
        """
        self.__array = self.__array.transpose() \
            if axis == COLS_IDX else self.__array
        # We init an empty dataframe to fill it with the new values
        margin_df: pd.DataFrame = pd.DataFrame()
        dataframe = self.as_dataframe()
        margined_rows = 2**(
            len(self.__causes if axis == ROWS_IDX else self.__effect)-len(states)
        )
        # If we have a collapsed matrix, we just sum all the values.
        if len(states) == INT_ZERO:
            vector_sum: NDArray[np.float64] = np.sum(dataframe, axis=ROWS_IDX)
            collapsed: pd.DataFrame = pd.DataFrame(
                vector_sum.values.reshape(1, -1),
                columns=dataframe.columns,
                index=[STR_ZERO]
            )
            margin_df = collapsed
        else:
            notation: Callable = lil_endian if le else big_endian
            rows: list[str] = notation(len(states))
            zeros_df = pd.DataFrame(
                np.zeros((len(rows), dataframe.shape[COLS_IDX])),
                columns=dataframe.columns,
                index=rows
            )
            for row in dataframe.index:
                for col in dataframe.columns:
                    # States should be a ordered collection or the row[i] would be a disordered string (and that's a catastrophe).
                    selected_row = ''.join([row[i] for i in states])
                    zeros_df.at[selected_row, col] += dataframe.at[row, col]
            margin_df = zeros_df

        margin_df /= margined_rows if axis == ROWS_IDX else INT_ONE
        if axis == COLS_IDX:
            self.__effect = states
        else:
            self.__causes = states
        self.__array = margin_df.to_numpy().transpose() \
            if axis == COLS_IDX else margin_df.to_numpy()
        cout('keeped', self.__causes, margin_df)
        return self.__array if data else None

    def at_state(
        self, istate: str, axis: int = ROWS_IDX, le: bool = conf.little_endian
    ) -> NDArray[np.float64]:
        ''' Select the serie at the given state. '''
        if axis == COLS_IDX:
            self.__array = self.__array.transpose()

        concat_digits: str = ''.join([istate[i] for i in self.__causes]) if axis == ROWS_IDX else \
            ''.join([istate[i] for i in self.__effect])
        tpm = self.as_dataframe()
        # If the dataframe has only one row(collapsed tpm), return it
        arr = tpm.values \
            if len(tpm.index) == 1 \
            else tpm.loc[[concat_digits]].values

        if axis == COLS_IDX:
            self.__array = self.__array.transpose()
        return arr

    def as_dataframe(self, le: bool = conf.little_endian) -> pd.DataFrame:
        notation: Callable = lil_endian if le else big_endian
        num_row_vars: int = int(math.log2(self.__array.shape[ROWS_IDX]))
        num_col_vars: int = int(math.log2(self.__array.shape[COLS_IDX]))
        col_states: list[str] = notation(num_col_vars)
        row_states: list[str] = notation(num_row_vars)
        return pd.DataFrame(self.__array, columns=col_states, index=row_states)

    def get_arr(self):
        return self.__array.copy()

    def __str__(self):
        return f'[Matrix]: \n{self.as_dataframe()}\n'
