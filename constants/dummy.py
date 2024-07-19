import numpy as np
from numpy.typing import NDArray

from constants.structure import VOID

DUMMY_NET_INT_ID: int = -1
DUMMY_SUBDIST: NDArray[np.float64] = np.array([[-1]], dtype=np.float64)
MIN_INFO_PARTITION: tuple[tuple[tuple[str], tuple[str]]] = (((VOID,), (VOID,)), ((VOID,), (VOID,)))
