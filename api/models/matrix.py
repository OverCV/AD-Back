import math
from typing import Callable
from fastapi import HTTPException
import numpy as np
from numpy.typing import NDArray
import pandas as pd


from constants.structure import BIN_RANGE, BOOL_RANGE
from utils.consts import COLS_IDX, INT_ONE, INT_ZERO, ROWS_IDX, STR_ZERO
from utils.funcs import big_endian, lil_endian
# from numba import njit

from server import conf
from icecream import ic


class Matrix:
    """Class Matrix is used to apply marginalization actions over it's array."""

    def __init__(self, array: NDArray[np.float64]) -> None:
        self.__array: NDArray[np.float64] = array
        # cout(1)
        self.__effect: list[int] = list(range(self.__array.shape[COLS_IDX]))
        # self.__causes: dict[int:int] = OrderedDict(
        #     (c, j) for j, c in enumerate(range(int(math.log2(self.__array.shape[ROWS_IDX]))))
        # )
        # self.__effect: list[int] = list(range(self.__array.shape[COLS_IDX]))
        self.__causes: list[int] = list(range(int(math.log2(self.__array.shape[ROWS_IDX]))))

    @property
    def shape(self):
        return self.__array.shape

    def margin(
        self,
        states: list[int],
        axis: int = ROWS_IDX,
        dual: bool = False,
        le: bool = conf.little_endian,
        data: bool = False,
    ) -> None | NDArray[np.float64]:
        """
        Marginalize the matrix over the given states. The states to marginalize are the states to drop if dual is disabled, else the given states are the states to preserve.

        Args:
            states (list[int]): Represents the states to marginalize if dual is disabled, these states must be a subset of the causes because are the states to drop or preserve.
            axis (int, optional): _description_. Defaults to ROWS_IDX. This determine if we're marginalizing rows (0) or columns (1).
            dual (bool, optional): The actual matrix has a set of causes, on whichever the incoming state is, is marginalized if dual is disabled, else the given states are the states to preserve. Defaults to False.
            le (bool, optional): _description_. Defaults to conf.little_endian. Indicates if the generated states are in little or big endian notation.
        """
        self.__array = self.__array.transpose() if axis == COLS_IDX else self.__array
        # We init an empty dataframe to fill it with the new values
        margin_df: pd.DataFrame = pd.DataFrame()
        dataframe = self.as_dataframe()
        margined_rows = 2 ** (
            len(self.__causes if axis == ROWS_IDX else self.__effect) - len(states)
        )
        # If we have a collapsed matrix, we just sum all the values.
        if len(states) == INT_ZERO:
            vector_sum: NDArray[np.float64] = np.sum(dataframe, axis=ROWS_IDX)
            collapsed: pd.DataFrame = pd.DataFrame(
                vector_sum.values.reshape(1, -1), columns=dataframe.columns, index=[STR_ZERO]
            )
            margin_df = collapsed
        else:
            notation: Callable = lil_endian if le else big_endian
            rows: list[str] = notation(len(states))
            zeros_df = pd.DataFrame(
                np.zeros((len(rows), dataframe.shape[COLS_IDX])),
                columns=dataframe.columns,
                index=rows,
            )
            for row in dataframe.index:
                for col in dataframe.columns:
                    # States should be a ordered collection or the row[i] would be a disordered string (and that's a catastrophe).
                    # element is the key, value is the position or index
                    selected_row = ''.join(
                        [row[self.__causes.index(k)] for k in states],
                    )
                    """ 
                    STATES: abcde [0->0, 2->1, 3->2] [0:a,1:b,2:c]
                    
                    Necesitamos usar el tamaño actual de la matriz usada, como se manja una única matriz, independiente del tamaño del arreglo, 


                    (b)b(bb)b
                    [0->0, 1->1, 2->2, 3->3, 4->4]
                    [0->0, 2->1, 3->2]                     

                    """
                    zeros_df.at[selected_row, col] += dataframe.at[row, col]
            margin_df = zeros_df

        margin_df /= margined_rows if axis == ROWS_IDX else INT_ONE
        if axis == COLS_IDX:
            self.__effect = states  #! Check case !#
        else:
            self.__causes = states
        self.__array = (
            margin_df.to_numpy().transpose() if axis == COLS_IDX else margin_df.to_numpy()
        )
        return self.__array if data else None

    def on_state(
        self, istate: str, axis: int = ROWS_IDX, le: bool = conf.little_endian
    ) -> NDArray[np.float64]:
        """Select the serie at the given state."""
        if axis == COLS_IDX:
            self.__array = self.__array.transpose()

        row_istates = ''.join([istate[e] for e in self.__causes])
        col_istates = ''.join([istate[i] for i in self.__effect])
        # ic('ERROR?', self.__causes, sub_istates)
        concat_digits: str = row_istates if axis == ROWS_IDX else col_istates
        tpm = self.as_dataframe()
        # If the dataframe has only one row(collapsed tpm), return it
        # ic(concat_digits)
        arr = tpm.values if len(tpm.index) == 1 else tpm.loc[[concat_digits]].values

        self.__array = self.__array.transpose() if axis == COLS_IDX else self.__array
        return arr

    def at_states(
        self,
        istate: str,
        in_states: list[int],
        out_states: list[int],
        data: bool = False,
        axis: int = ROWS_IDX,
        le: bool = conf.little_endian,
    ):
        # ic(in_states)
        m: int = len(in_states)
        if axis == COLS_IDX:
            self.__array = self.__array.transpose()
        # Generamos la sub-cadena de estados específicos selectores
        row_istate = ''.join([istate[e] for e in out_states])
        # col_istates = ''.join([istate[i] for i in self.__effect])
        rows_notation: Callable = lil_endian if le else big_endian
        # Generamos los indices de las nuevas filas
        new_rows = rows_notation(m)
        zeros_df = pd.DataFrame(
            np.zeros((2**m, self.__array.shape[COLS_IDX])),  # (2**m, 2)
            index=new_rows,
            columns=list(BIN_RANGE),  # range(2)
        )
        tpm = self.as_dataframe()
        for row in tpm.index:
            row: int
            in_row: str = ''
            out_row: str = ''
            for i, s in enumerate(row):
                if i in in_states:
                    out_row += s
                else:
                    in_row += s
            if in_row == row_istate:
                # ic(row_istate, row, in_row, out_row)
                zeros_df.loc[out_row] = tpm.loc[row].values
        # ic(zeros_df)
        if axis == COLS_IDX:
            self.__array = zeros_df.to_numpy().transpose()
            self.__effect = in_states
        else:
            self.__array = zeros_df.to_numpy()
            self.__causes = in_states
        return self.__array if data else None

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
        return f'{self.as_dataframe()}'

    # def at_states(
    #     self,
    #     istate: str,
    #     states: list[int],
    #     data: bool = False,
    #     axis: int = ROWS_IDX,
    #     le: bool = conf.little_endian,
    # ):
    #     out_states = [s for s in self.__causes if s not in states]
    #     m: int = len(self.__causes) - len(states)
    #     if axis == COLS_IDX:
    #         self.__array = self.__array.transpose()
    #     # Generamos la sub-cadena de estados específicos selectores
    #     row_istate = ''.join([istate[e] for e in self.__causes if e in states])
    #     rows_notation: Callable = lil_endian if le else big_endian
    #     # Generamos los indices de las nuevas filas
    #     new_rows = rows_notation(m)
    #     zeros_df = pd.DataFrame(
    #         np.zeros((2**m, self.__array.shape[COLS_IDX])),  # (2**m, 2)
    #         index=new_rows,
    #         columns=list(BIN_RANGE),  # range(2)
    #     )
    #     tpm = self.as_dataframe()
    #     # Utilizamos el vectorizado de pandas para realizar la operación de forma eficiente
    #     mask = (
    #         tpm.index.to_series().apply(lambda row: ''.join([row[i] for i in states])) == row_istate
    #     )
    #     filtered_tpm: pd.DataFrame = tpm[mask]
    #     for row in filtered_tpm.index:
    #         in_row = ''.join(
    #             [row[i] for i in range(len(row)) if i in out_states],
    #         )
    #         zeros_df.loc[in_row] = filtered_tpm.loc[row].values
    #     if axis == COLS_IDX:
    #         self.__array = self.__array.transpose()
    #         self.__effect = out_states
    #     else:
    #         self.__array = zeros_df.to_numpy()
    #         self.__causes = out_states
    #     ic(zeros_df)
    #     return zeros_df.to_numpy() if data else None

    # def filter_rows(
    #     self,
    #     tpm_values: NDArray[np.float64],
    #     states,
    #     istate,
    #     causes,
    # ):
    #     mask = np.ones(tpm_values.shape[0], dtype=np.bool_)
    #     for i, state in enumerate(states):
    #         mask &= tpm_values[:, state] == int(istate[i])
    #     return mask

    # def at_states(self, istate: str, states: list[int]):
    #     causes = self.__causes
    #     tpm = self.as_dataframe()

    #     # Convert states and causes to numpy arrays for faster indexing
    #     states = np.array(states)
    #     causes = np.array(causes)

    #     # Find indices not in states
    #     excluded_indices = np.setdiff1d(causes, states)

    #     # Create the key for filtering
    #     key = ''.join(istate[i] for i in states)

    #     # Convert TPM to numpy array for faster operations
    #     tpm_values = tpm.index.to_frame().values

    #     # Use numba-accelerated function to filter rows
    #     mask = self.filter_rows(tpm_values, states, key, causes)
    #     filtered_tpm = tpm[mask]

    #     # Create the result DataFrame
    #     result_index = lil_endian(len(excluded_indices))
    #     result = pd.DataFrame(index=result_index, columns=tpm.columns, dtype=float)

    #     # Fill the result DataFrame
    #     for idx, row in filtered_tpm.iterrows():
    #         new_idx = ''.join(str(idx)[i] for i in excluded_indices)
    #         result.loc[new_idx] = row.values

    #     return result


# @njit

# def select_rows_from_tpm(self,istate, indices, states):
#     """
#     Selecciona y procesa filas de la matriz TPM basada en el istate y states.

#     Args:
#     - tpm (np.ndarray): Matriz de transición de probabilidades de 2^m x 2.
#     - istate (str): String binario de tamaño m que indica el estado inicial.
#     - indices (list): Lista de índices que indican las posiciones de las filas a seleccionar.
#     - states (list): Lista de estados que indican las filas que no queremos mantener directamente.

#     Returns:
#     - np.ndarray: Nuevo arreglo procesado basado en la lógica dada.
#     """
#     m = len(istate)
#     non_states_positions = [i for i in range(m) if i not in states]
#     selected_rows = []

#     # Crear el patrón basado en las posiciones de non_states en el istate
#     pattern = ''.join([istate[i] for i in non_states_positions])

#     # Recorrer las filas de la TPM y seleccionar aquellas que cumplan el patrón
#     for row in tpm:
#         tpm_state = ''.join([row[i] for i in non_states_positions])
#         if tpm_state == pattern:
#             selected_rows.append(row)

#     # Crear el nuevo arreglo basado en los índices y las filas seleccionadas
#     new_array = np.zeros((2 ** len(states), 2))
#     for row in selected_rows:
#         new_index = int(''.join([row[i] for i in states]), 2)
#         new_array[new_index] = row

#     return new_array

# def at_states(
#     self,
#     istate: str,
#     states: list[int],
#     data: bool = False,
#     axis: int = ROWS_IDX,
#     le: bool = True,
# ):
#     """Select the serie at the given state."""
#     ic(istate, states, self.__causes)
#     if axis == COLS_IDX:
#         self.__array = self.__array.transpose()

#     # Generamos la sub-cadena de estados específicos a seleccionar
#     row_istates = ''.join([istate[e] for e in self.__causes if e not in states])
#     rows_notation = lil_endian if le else big_endian
#     new_rows = rows_notation(len(states))
#     zeros_df = pd.DataFrame(
#         np.zeros((2 ** len(states), self.__array.shape[COLS_IDX])),
#         index=new_rows,
#         columns=list(range(self.__array.shape[COLS_IDX])),
#     )
#     tpm = self.as_dataframe()
#     ic(tpm)
#     # Crear un mapeo para las filas de tpm
#     row_istates_mapping = {
#         row: ''.join(
#             [row[i] for i in states],
#         )
#         for row in tpm.index
#     }
#     out_row_mapping = {
#         row: ''.join([row[i] for i in range(len(row)) if i not in states]) for row in tpm.index
#     }

#     ic(row_istates, row_istates_mapping, out_row_mapping)

#     for row in tpm.index:
#         ic(row, row_istates_mapping[row], out_row_mapping[row])
#         if row_istates_mapping[row] == row_istates:
#             ic('Updating zeros_df at', out_row_mapping[row], 'with tpm at', row)
#             zeros_df.loc[out_row_mapping[row]] = tpm.loc[row]
#             ic(zeros_df)

#     self.__array = zeros_df.to_numpy()
#     if axis == COLS_IDX:
#         self.__array = self.__array.transpose()

#     return self.__array
