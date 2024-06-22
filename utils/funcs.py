import networkx as nx
from functools import reduce
import itertools
import random
import math

import numpy as np

''' If needed, this class could partitionate into several modules associated with the business logic. '''


def emd(u: np.ndarray, v: np.ndarray, be: bool = False) -> float:
    ''' Returns the Earth Mover's Distance between two distributions.'''
    u = np.asarray(u, dtype=float).flatten()
    v = np.asarray(v, dtype=float).flatten()

    if len(u) != len(v):
        raise ValueError('Both distributions must have the same size')

    max_len = int(math.log2(len(u)))
    end_keys = big_endian(max_len) if be \
        else lil_endian(max_len)
    earth_moved = 0.0

    while not np.allclose(u, 0):
        u_sorter = np.argsort(-u)
        v_sorter = np.argsort(-v)

        u_idx = u_sorter[0]
        v_idx = v_sorter[0]

        end_u_key = int(end_keys[u_idx], 2)
        end_v_key = int(end_keys[v_idx], 2)

        restar = min(u[u_idx], v[v_idx])
        u[u_idx] -= restar
        v[v_idx] -= restar

        distance = hamming_distance(end_u_key, end_v_key)
        earth_moved += restar * distance
    return earth_moved


def be_product(arrays: list[np.ndarray]) -> np.ndarray:
    ''' Returns the tensor product of a list of arrays.'''
    return reduce(
        lambda x, y: np.kron(x, y),
        arrays
    )


def le_product(arrays: list[np.ndarray]) -> np.ndarray:
    ''' Returns the tensor product of a list of arrays.'''
    return reduce(
        lambda x, y: np.kron(y, x),
        arrays
    )


def hamming_distance(a: int, b: int) -> int:
    return bin(a ^ b).count('1')


def lil_endian(n: int) -> list[str]:
    """Generate a list of strings representing the numbers in
    little-endian for indices in ``range(2**n)``.
    """
    return [bin(i)[2:].zfill(n)[::-1] for i in range(2**n)]


def big_endian(n: int) -> list[str]:
    """Generate a list of strings representing the numbers in
    big-endian for indices in ``range(2**n)``.
    """
    return [bin(i)[2:].zfill(n) for i in range(2**n)]


def get_labels(n: int) -> tuple[str]:
    def get_excel_column(n: int) -> str:
        if n <= 0:
            return ''
        return get_excel_column((n-1) // 26) + chr((n-1) % 26 + ord('A'))
    # return tuple([get_excel_column(i) for i in range(1, n+1)] + ['∅'])
    return tuple([get_excel_column(i) for i in range(1, n+1)])


async def logger(func):
    def wrapper(*args, **kwargs):
        print('\n')
        result = func(*args, **kwargs)
        print('\n')
        return result
    return wrapper


def printnl(*args):
    print()
    for arg in args:
        print(arg)
    # '\n'
    print()


def cout(*args):
    print()
    for arg in args:
        print(arg, end=' ')
    print()
