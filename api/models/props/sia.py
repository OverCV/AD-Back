from typing import NotRequired, TypedDict


class SiaType(TypedDict):
    NET_ID: NotRequired[str]
    SMALL_PHI: float
    MIP: list
    SUB_DISTRIBUTION: list[list[float | int]]
    DISTRIBUTION: list[list[float | int]]


# Object instance:
# SiaType = TypedDict(
#     'SiaType',
#     {
#         NET_ID: str | None,
#         SMALL_PHI: float,
#         MIP: list,
#         BEST_DISTRIBUTION: NDArray,
#     },
# )
