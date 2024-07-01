import numpy as np
from icecream import ic

from utils.funcs import emd


# def main():
"""Application initializer."""
d0 = np.array([0, 0, 0, 0, 0.5, 0.5, 0, 0], dtype=np.float64)
d1 = np.array([0, 0, 0, 0, 0.375, 0.125, 0.375, 0.125], dtype=np.float64)
d2 = np.array([0, 0, 0.375, 0.375, 0, 0, 0.125, 0.125], dtype=np.float64)

ic(emd(d0, d2))
ic(emd(d2, d1))
ic(emd(d1, d0))


# if __name__ == '__main__':
#     main()
