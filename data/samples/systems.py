import numpy as np

from utils.consts import (
    ISTATE, TENSOR,
    R2A, F3A, F4A, F5A, F6A, F8A,
)

SYSTEMS: dict[str, dict[str, str | list[list[list[float]]]]] = {
    R2A: {
        ISTATE: '10',
        TENSOR: np.random.rand(2, 2, 2).tolist()
    },
    F3A: {
        ISTATE: '100',
        TENSOR: np.random.rand(3, 3, 3).tolist()
    },
    F4A: {
        ISTATE: '1001',
        TENSOR: np.random.rand(4, 4, 4).tolist()
    },
    F5A: {
        ISTATE: '01010',
        TENSOR: np.random.rand(5, 5, 5).tolist()
    },
    F6A: {
        ISTATE: '100001',
        TENSOR: np.random.rand(6, 6, 6).tolist()
    },
    F8A: {
        ISTATE: '01000001',
        TENSOR: np.random.rand(8, 8, 8).tolist()
    }
}
