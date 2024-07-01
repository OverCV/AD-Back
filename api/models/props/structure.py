from typing import TypedDict


class StructProps:
    TITLE: str = 'title'
    ISTATE: str = 'istate'
    EFFECT: str = 'effect'
    CAUSES: str = 'causes'
    FORMAT: str = 'format'
    TENSOR: str = 'tensor'
    SIZE: str = 'size'


class ConceptType(TypedDict):
    bool: list[int]
    # bool: list[int]
