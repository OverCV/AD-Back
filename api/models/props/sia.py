from typing import NotRequired, TypedDict

import numpy as np
from numpy.typing import NDArray

from utils.consts import BEST_DISTRIBUTION, MIP, NET_ID, SMALL_PHI


class SiaType(TypedDict):
    NET_ID: str | None
    SMALL_PHI: float
    MIP: list
    BEST_DISTRIBUTION: NDArray


# SiaType = TypedDict(
#     'SiaType',
#     {
#         NET_ID: str | None,
#         SMALL_PHI: float,
#         MIP: list,
#         BEST_DISTRIBUTION: NDArray,
#     },
# )
