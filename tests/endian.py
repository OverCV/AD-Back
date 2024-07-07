from functools import cache
import timeit

import numpy as np

n = 14  # Ajusta este valor según tus necesidades


@cache
def lil_endian(n: int) -> list[str]:
    """Generate a list of strings representing the numbers in
    little-endian for indices in ``range(2**n)``.
    """
    return [bin(i)[2:].zfill(n)[::-1] for i in range(2**n)]


print('Forma Actual:')
print('Tiempo para lil_endian:')
print(timeit.timeit('lil_endian(n)', globals=globals(), number=1000))


def lil_endian_int(n: int) -> np.ndarray:
    return np.arange(2**n, dtype=np.uint32)


def lil_endian_str(n: int) -> list[str]:
    return [f'{i:0{n}b}'[::-1] for i in range(2**n)]


print('Usando NumPy (la más rápida para listas largas):')
print('Tiempo para lil_endian_int:')
print(timeit.timeit('lil_endian_int(n)', globals=globals(), number=1000))

print('Tiempo para lil_endian_str:\n')
print(timeit.timeit('lil_endian_str(n)', globals=globals(), number=1000))


def lil_endian_int(n: int) -> list[int]:
    return list(range(2**n))


def lil_endian_str(n: int) -> list[str]:
    def gen():
        for i in range(2**n):
            s = ['0'] * n
            for j in range(n):
                if i & (1 << j):
                    s[j] = '1'
            yield ''.join(s)

    return list(gen())


print('Usando un generador con bit shifting (muy rápido y eficiente en memoria):')
print('Tiempo para lil_endian_int:')
print(timeit.timeit('lil_endian_int(n)', globals=globals(), number=1000))

print('Tiempo para lil_endian_str:\n')
print(timeit.timeit('lil_endian_str(n)', globals=globals(), number=1000))


def lil_endian_int(n: int) -> list[int]:
    return list(range(2**n))


def lil_endian_str(n: int) -> list[str]:
    return [f'{i:0{n}b}'[::-1] for i in range(2**n)]


print('Usando comprensión de listas (simple y bastante rápida):')
print('Tiempo para lil_endian_int:')
print(timeit.timeit('lil_endian_int(n)', globals=globals(), number=1000))

print('Tiempo para lil_endian_str:\n')
print(timeit.timeit('lil_endian_str(n)', globals=globals(), number=1000))


def lil_endian_str(n: int) -> list[str]:
    if n == 0:
        return ['']
    prev = lil_endian_str(n - 1)
    return [s + '0' for s in prev] + [s + '1' for s in prev]


def lil_endian_int(n: int) -> list[int]:
    return list(range(2**n))


print('Usando recursión (simple y eficiente en memoria):')
print('Tiempo para lil_endian_int:')
print(timeit.timeit('lil_endian_int(n)', globals=globals(), number=1000))

print('Tiempo para lil_endian_str:\n')
print(timeit.timeit('lil_endian_str(n)', globals=globals(), number=1000))
