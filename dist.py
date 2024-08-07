import numpy as np
from pyemd import emd
from decimal import Decimal, getcontext  # Esto es para lograr mayor precision en los calculos

# Set the precision to 50 decimal places
# getcontext().prec = 50


def hamming_distance(x: str, y: str):
    """Calculate the Hamming distance between two binary vectors."""
    print(x, y, type(x), type(y), int(x, 2), int(y, 2))
    res = sum(x_i != y_i for x_i, y_i in zip(x, y))
    # return res
    return int(x, 2) ^ int(y, 2)


def emd_hamming(p, q):
    """
    Calculate the Earth Mover's Distance (EMD) between two probability distributions p and q
    using the Hamming distance as the ground metric.
    """
    n = len(p)
    lg_n = int(np.log2(n))
    cost_matrix = np.zeros((n, n))

    # Fill the cost matrix with Hamming distances
    for i in range(n):
        for j in range(n):
            binary_i = np.binary_repr(i, width=lg_n)
            binary_j = np.binary_repr(j, width=lg_n)
            cost_matrix[i, j] = hamming_distance(binary_i, binary_j)

    print(cost_matrix)

    # Convert p and q to numpy arrays
    p = np.array([Decimal(x) for x in p], dtype=object)
    q = np.array([Decimal(x) for x in q], dtype=object)

    # Normalize the distributions to sum to 1
    p /= sum(p)
    q /= sum(q)

    # Convert p, q, and cost_matrix to float64
    p = np.array(p, dtype=np.float64)
    q = np.array(q, dtype=np.float64)
    cost_matrix = np.array(cost_matrix, dtype=np.float64)

    # Calculate EMD using the cost matrix
    emd_value = emd(p, q, cost_matrix)
    return emd_value


# Ejemplo
p = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]  # Distribución de probabilidades 1
q = [0.0, 0.0, 0.0, 0.0, 0.38, 0.38, 0.13, 0.13]  # Distribución de probabilidades 2

emd_value = emd_hamming(p, q)
print(f'EMD using Hamming distance: {emd_value}')
