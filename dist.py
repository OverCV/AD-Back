import numpy as np
from pyemd import emd
from decimal import Decimal, getcontext  # Esto es para lograr mayor precision en los calculos

from numpy.typing import NDArray

from utils.consts import STR_ONE


# Set the precision to 50 decimal places
# getcontext().prec = 50


# def emd_hamming(p, q):
#     """
#     Calculate the Earth Mover's Distance (EMD) between two probability distributions p and q
#     using the Hamming distance as the ground metric.
#     """
#     n = len(p)
#     cost_matrix = np.zeros((n, n))

#     # Fill the cost matrix with Hamming distances
#     for i in range(n):
#         for j in range(n):
#             binary_i = np.binary_repr(i, width=int(np.log2(n)))
#             binary_j = np.binary_repr(j, width=int(np.log2(n)))
#             cost_matrix[i, j] = hamming_distance(binary_i, binary_j)

#     # Convert p and q to numpy arrays
#     p = np.array([Decimal(x) for x in p], dtype=object)
#     q = np.array([Decimal(x) for x in q], dtype=object)

#     # Normalize the distributions to sum to 1
#     p /= sum(p)
#     q /= sum(q)

#     # Convert p, q, and cost_matrix to float64
#     p = np.array(p, dtype=np.float64)
#     q = np.array(q, dtype=np.float64)
#     cost_matrix = np.array(cost_matrix, dtype=np.float64)


#     # Calculate EMD using the cost matrix
#     emd_value = emd(p, q, cost_matrix)
#     return emd_value


# def hamming_distance(x: str, y: str) -> int:
#     """Calculate the Hamming distance between two binary vectors."""
#     return sum(x_i != y_i for x_i, y_i in zip(x, y))


def hamming_distance(a: int, b: int) -> int:
    return (a ^ b).bit_count()


def emd_hamming(u: NDArray[np.float64], v: NDArray[np.float64]) -> float:
    """
    Calculate the Earth Mover's Distance (EMD) between two probability distributions u and v.
    The Hamming distance was used as the ground metric.
    """
    # Validate (u, v) are NDArrays of type np.float64
    if not all(isinstance(arr, np.ndarray) for arr in [u, v]):
        raise TypeError('u and v must be numpy arrays.')

    n: int = len(u)
    costs: NDArray[np.float64] = np.empty((n, n))

    # Fill the cost matrix with Hamming distances
    # for i in range(n):
    #     costs[i, i] = 0
    #     for j in range(i):
    #         costs[i, j] = hamming_distance(i, j)
    #         costs[j, i] = costs[i, j]
    # costs = np.array(
    #     [[0 if i == j else hamming_distance(i, j) for j in range(n)] for i in range(n)]
    # )
    for i in range(n):
        # Utiliza comprensión de listas para calcular los costos
        costs[i, :i] = [hamming_distance(i, j) for j in range(i)]
        costs[:i, i] = costs[i, :i]  # Reflejar los valores

    cost_mat = np.array(costs, dtype=np.float64)
    emd_value: float = emd(u, v, cost_mat)
    return emd_value


# Ejemplo
# # Distribución de probabilidades 1
# # Distribución de probabilidades 2
u = [
    0.7433188140668004,
    0.0446111846555956,
    0.028838031261284997,
    0.0017307495967476057,
    0.029893838854202492,
    0.0017941151763576889,
    0.0011597708050476365,
    6.960505850656328e-05,
    0.022253234910773672,
    0.001335555017580458,
    0.0008633435235017987,
    5.1814613890144376e-05,
    0.0008949519450043116,
    5.3711631834040764e-05,
    3.472083805625669e-05,
    2.0838134170857923e-06,
    0.04295748310461209,
    0.0025781457092881504,
    0.0016665920695579173,
    0.00010002255445927393,
    0.0017276087369369275,
    0.00010368454412508304,
    6.702485369700183e-05,
    4.022578291046078e-06,
    0.0012860470428192545,
    7.718368083420598e-05,
    4.989388687930056e-05,
    2.994442436590668e-06,
    5.1720583859064665e-05,
    3.1040738823874265e-06,
    2.0065680915828124e-06,
    1.204266298169904e-07,
    0.058031220725719895,
    0.0034828144459586666,
    0.0022513975507532976,
    0.00013512036823110053,
    0.0023338249053540382,
    0.00014006734638795295,
    9.054380745556764e-05,
    5.434096968058205e-06,
    0.0017373196568280984,
    0.00010426735681896674,
    6.740160160933471e-05,
    4.045189276221791e-06,
    6.986928472227564e-05,
    4.193290286097493e-06,
    2.71067081700899e-06,
    1.626842131124302e-07,
    0.003353709251924166,
    0.00020127694858174672,
    0.00013011156238480238,
    7.808804009170194e-06,
    0.00013487515994968385,
    8.094697123363285e-06,
    5.232659264629151e-06,
    3.140444238415386e-07,
    0.000100402247855382,
    6.025763285080525e-06,
    3.895237289253636e-06,
    2.337774138091965e-07,
    4.037848311100003e-06,
    2.4233638811351127e-07,
    1.566536372014448e-07,
    9.401758981357211e-09,
]
v = [
    0.7417451663058411,
    0.04451674026710644,
    0.02877697952619368,
    0.0017270855024502988,
    0.02983055191501953,
    0.0017903169335623372,
    0.001157315504985199,
    6.945770068055719e-05,
    0.02382688267173332,
    0.0014299994060696297,
    0.0009243952585931253,
    5.547870818745206e-05,
    0.0009582388841872832,
    5.750987462939301e-05,
    3.7176138118694715e-05,
    2.231171243091895e-06,
    0.042866539695371346,
    0.002572687629731881,
    0.0016630638003562487,
    9.981080108253763e-05,
    0.0017239512920165971,
    0.00010346503811013926,
    6.688295830978317e-05,
    4.014062266426232e-06,
    0.0013769904520600162,
    8.264176039047618e-05,
    5.342215608096942e-05,
    3.2061958133270134e-06,
    5.5378028779395714e-05,
    3.3235798973312314e-06,
    2.148463478801487e-06,
    1.28942654436839e-07,
    0.05790836536563404,
    0.003475441131775034,
    0.0022466312154369767,
    0.00013483431080741777,
    0.002328884066689283,
    0.0001397708159331122,
    9.035212111967143e-05,
    5.422592678963415e-06,
    0.0018601750169139756,
    0.00011164067100260077,
    7.21679369256564e-05,
    4.331246699904605e-06,
    7.48101233870322e-05,
    4.489820740938306e-06,
    2.902357152905246e-06,
    1.7418850220722213e-07,
    0.0033466092607019274,
    0.00020085083395438315,
    0.00012983610888497562,
    7.792272331628535e-06,
    0.00013458962164573235,
    8.077560194009738e-06,
    5.221581430488783e-06,
    3.133795741228612e-07,
    0.00010750223907762199,
    6.451877912444162e-06,
    4.170690789080434e-06,
    2.5030909135085905e-07,
    4.3233866150515295e-06,
    2.59473317467061e-07,
    1.6773147134181456e-07,
    1.0066608700034839e-08,
]
u = [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
v = [0.0, 0.0, 0.0, 0.0, 0.75, 0.0, 0.25, 0.0]

u = np.array(u, dtype=np.float64)
v = np.array(v, dtype=np.float64)

emd_value = emd_hamming(u, v)
print(f'EMD using Hamming distance: {round(emd_value, 17)}')
