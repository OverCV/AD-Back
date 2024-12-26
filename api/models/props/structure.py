from typing import TypedDict


class StructProps:
    ID: str = 'id'
    TITLE: str = 'title'
    ISTATE: str = 'istate'
    EFFECT: str = 'effect'
    ACTUAL: str = 'actual'
    SUBSYS: str = 'subsys'
    FORMAT: str = 'format'
    TENSOR: str = 'tensor'
    SIZE: str = 'size'

    DIST_INDICES: int = 0
    DIST_ARRAY: int = 1


class ConceptType(TypedDict):
    bool: list[int]
