from functools import reduce

import numpy as np
from numpy.typing import NDArray
import pandas as pd
from constants.structure import UNIT_MATRIX
from utils.consts import ROWS_IDX
from utils.funcs import big_endian, lil_endian


# def combine_arrays(
#     arrays: list[NDArray[np.float64]], le: bool = True
# ) -> tuple[tuple[int, ...], NDArray[np.float64]]:
#     return reduce(lambda x, y: bin_prod(x, y, le), arrays)


# def product(arrays: list[NDArray[np.float64]], le: bool=conf.little_endian):
#     return (
#         (tuple(), UNIT_MATRIX)
#         if len(arrays) == 0
#         else reduce(lambda x, y: bin_prod(x, y, le), arrays)
#     )


def bin_prod(
    idx_dist_u: tuple[tuple[int, ...], np.ndarray],
    idx_dist_v: tuple[tuple[int, ...], np.ndarray],
    le: bool,
) -> tuple[tuple[int, ...], NDArray[np.float64]]:
    """Returns the binary product of two arrays."""
    u_idx, u = idx_dist_u
    v_idx, v = idx_dist_v

    # Flatten arrays if they're 2D with only one row
    u = u.flatten()
    v = v.flatten()
    print(u_idx, v_idx)
    print(u, v)

    d_len = len(u_idx) + len(v_idx)

    result = np.zeros(2**d_len, dtype=np.float64)
    endian_keys = lil_endian(d_len) if le else big_endian(d_len)
    df_result = pd.DataFrame([result], columns=endian_keys)

    # Create the union of indices and sort
    combined_idx = tuple(sorted(set(u_idx) | set(v_idx)))
    print(combined_idx)

    for key in endian_keys:
        u_key = ''.join(key[combined_idx.index(i)] for i in u_idx)
        v_key = ''.join(key[combined_idx.index(i)] for i in v_idx)
        # print(f'u_key = {u_key}, v_key = {v_key}')
        u_val = u[int(u_key[::-1], 2)]
        v_val = v[int(v_key[::-1], 2)]
        # print(f'u_val <- (u[{u_key}] = {u_val})')
        # print(f'v_val <- (v[{v_key}] = {v_val})')
        # print(f'{key} <- ({u_val} * {v_val} = {u_val * v_val})')
        df_result.at[ROWS_IDX, key] = u_val * v_val

    print(df_result)
    print()
    return combined_idx, df_result.values


A = (0,), np.array([1, 0], dtype=np.float64)
B = (1,), np.array([0.75, 0.25], dtype=np.float64)
C = (2,), np.array([0, 1], dtype=np.float64)

# AC = product([], True)
# print('prod one elem', AC)
# AC = product([A, C], True)
# ABC = product([AC, B], True)
