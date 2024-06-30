from functools import cache, reduce
import itertools as it
import math

from numpy.typing import NDArray
import numpy as np
from scipy.stats import wasserstein_distance

from utils.consts import INT_ONE, INT_ZERO, STR_ONE

from server import conf
from icecream import ic

""" If needed, this class could partitionate into several modules associated with the business logic. """

up_sep_ln: str = '\n' + '︵' * 16 + '\n'
dn_sep_ln: str = '\n' + '︶' * 16 + '\n'
up_sep: str = '︵' * 16
dn_sep: str = '︶' * 16


def emd(u: NDArray[np.float64], v: NDArray[np.float64], be: bool = False) -> float:
    """Returns the Earth Mover's Distance between two distributions."""
    # return wasserstein_distance(u, v)
    u = np.asarray(u, dtype=np.float64).flatten()
    v = np.asarray(v, dtype=np.float64).flatten()

    if len(u) != len(v):
        raise ValueError('Both distributions must have the same size')

    max_len = int(math.log2(len(u)))
    end_keys = big_endian(max_len) if be else lil_endian(max_len)
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


def be_product(arrays: list[NDArray[np.float64]]) -> NDArray[np.float64]:
    """Returns the tensor product of a list of arrays."""
    return reduce(lambda x, y: np.kron(x, y), arrays)


def le_product(arrays: list[NDArray[np.float64]]) -> NDArray:
    """Returns the tensor product of a list of arrays."""
    return reduce(lambda x, y: np.kron(y, x), arrays)


def hamming_distance(a: int, b: int) -> int:
    return bin(a ^ b).count(STR_ONE)


@cache
def all_states(n, lil_endian=conf.little_endian):
    """Return all binary states until N.

    Args:
        n (int): The number of elements in the system.
        big_endian (bool): Whether to return the states in big-endian order
            instead of little-endian order.

    Yields:
        tuple[int]: The next state of an ``n``-element system, in little-endian
        order unless ``big_endian`` is ``True``.
    """
    if n == 0:
        return

    for state in it.product((INT_ZERO, INT_ONE), repeat=n):
        yield state if lil_endian else state[::-1]


@cache
def lil_endian(n: int) -> list[str]:
    """Generate a list of strings representing the numbers in
    little-endian for indices in ``range(2**n)``.
    """
    return [bin(i)[2:].zfill(n)[::-1] for i in range(2**n)]


@cache
def big_endian(n: int) -> list[str]:
    """Generate a list of strings representing the numbers in
    big-endian for indices in ``range(2**n)``.
    """
    return [bin(i)[2:].zfill(n) for i in range(2**n)]


@cache
def get_labels(n: int) -> tuple[str]:
    def get_excel_column(n: int) -> str:
        if n <= 0:
            return ''
        return get_excel_column((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))

    # return tuple([get_excel_column(i) for i in range(1, n+1)] + ['∅'])
    return tuple([get_excel_column(i) for i in range(1, n + 1)])


async def logger(func):
    def wrapper(*args, **kwargs):
        print('\n')
        result = func(*args, **kwargs)
        print('\n')
        return result

    return wrapper


# def printnl(*args):
#     print()
#     for arg in args:
#         print(arg)
#     # '\n'
#     print()


def cout(*args):
    print(up_sep_ln)
    for arg in args:
        print(arg)
    print(dn_sep_ln)


def coute(*args):
    print(up_sep)
    for arg in args:
        print(arg)
    print(dn_sep)


def combs(a, r):
    """NumPy implementation of ``itertools.combinations``.

    Return successive ``r``-length combinations of elements in the array ``a``.

    Args:
        a (np.ndarray): The array from which to get combinations.
        r (int): The length of the combinations.

    Returns:
        np.ndarray: An array of combinations.
    """
    # Special-case for 0-length combinations
    if r == 0:
        return np.asarray([])

    a = np.asarray(a)
    data_type = a.dtype if r == 0 else np.dtype([('', a.dtype)] * r)
    b = np.fromiter(it.combinations(a, r), data_type)
    return b.view(a.dtype).reshape(-1, r)
