import numpy as np
import pandas as pd
from utils.funcs import big_endian, lil_endian


def binary_product(
    idx_dist_u: tuple[tuple[int, ...], np.ndarray],
    idx_dist_v: tuple[tuple[int, ...], np.ndarray],
    le: bool = True,
) -> tuple[tuple[int, ...], np.ndarray]:
    """Returns the binary product of two arrays."""
    u_idx, u = idx_dist_u
    v_idx, v = idx_dist_v

    # Flatten arrays if they're 2D with only one row
    u = u.flatten()
    v = v.flatten()

    d_len = len(u_idx) + len(v_idx)

    result = np.zeros(2**d_len, dtype=np.float64)
    endian_keys = lil_endian(d_len) if le else big_endian(d_len)
    df_result = pd.DataFrame([result], columns=endian_keys)

    for key in endian_keys:
        u_key = ''.join(key[i] for i in u_idx)
        v_key = ''.join(key[i] for i in v_idx)
        u_val = u[int(u_key, 2)]
        v_val = v[int(v_key, 2)]
        df_result.at[0, key] = u_val * v_val

    # Create the union of indices and sort
    combined_idx = tuple(sorted(set(u_idx) | set(v_idx)))

    return combined_idx, df_result.values
