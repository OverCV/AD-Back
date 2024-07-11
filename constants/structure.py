from typing import TypedDict

import numpy as np
from numpy.typing import NDArray

from api.models.props.structure import StructProps
from constants.format import S2C
from utils.consts import INT_ONE, INT_ZERO


VOID: str = '∅'
PARTITION: str = 'partition'
DIST: str = 'distribution'
TIME: str = 'time'
LOSS: str = 'loss'

# T0_SYM: str = '(t=0)'
# T1_SYM: str = '(t=1)'
T0_SYM: str = '.0'
T1_SYM: str = '.1'

ISTATE: str = 'istate'
SUBSYS: str = 'subsystem'
TENSOR: str = 'tensor'

BIN_RANGE = range(2)
BOOL_RANGE: list[bool] = [False, True]
UNIT_MATRIX: NDArray[np.float64] = np.array([INT_ONE], dtype=np.float64)
UNIT_PROD: tuple[tuple[int, ...], NDArray[np.float64]] = ((), UNIT_MATRIX)


# DEFAULT_TITLE: str = 'System_Title'
# DEFAULT_ISTATE: str = '1000000000'
# DEFAULT_EFFECT: str = '1111111111'
# DEFAULT_CAUSES: str = '1111111111'

FUTURE = INT_ZERO
CURRENT = INT_ONE

R2A: str = 'R2A'
R3A: str = 'R3A'

R4A: str = 'R4A'
R4B: str = 'R4B'
R4C: str = 'R4C'
R4D: str = 'R4D'
R4E: str = 'R4E'

R5A: str = 'R5A'

R6A: str = 'R6A'

R8A: str = 'R8A'
R8B: str = 'R8B'

R10A: str = 'R10A'


class MechaInt(TypedDict):
    title: str
    istate: str
    effect: str
    causes: str
    format: str


STRUCTURES: dict[str, MechaInt] = {
    R2A: {
        StructProps.TITLE: R2A,
        StructProps.ISTATE: '10',
        StructProps.EFFECT: '11',
        StructProps.CAUSES: '11',
        StructProps.FORMAT: S2C,
    },
    R3A: {
        StructProps.TITLE: R3A,
        StructProps.ISTATE: '100',
        StructProps.EFFECT: '111',
        StructProps.CAUSES: '111',
        StructProps.FORMAT: S2C,
    },
    R4A: {
        StructProps.TITLE: R4A,
        StructProps.ISTATE: '1000',
        StructProps.EFFECT: '1111',
        StructProps.CAUSES: '1111',
        StructProps.FORMAT: S2C,
    },
    R5A: {
        StructProps.TITLE: R5A,
        StructProps.ISTATE: '10001',
        StructProps.EFFECT: '11111',
        StructProps.CAUSES: '11111',
        StructProps.BGCOND: '11100',  # ! Implement for all ! #
        StructProps.FORMAT: S2C,
    },
    R6A: {
        StructProps.TITLE: R6A,
        StructProps.ISTATE: '100000',
        StructProps.EFFECT: '111111',
        StructProps.CAUSES: '111111',
        StructProps.FORMAT: S2C,
    },
    R8A: {
        StructProps.TITLE: R8A,
        StructProps.ISTATE: '10000000',
        StructProps.EFFECT: '11111111',
        StructProps.CAUSES: '11111111',
        StructProps.FORMAT: S2C,
    },
    R10A: {
        StructProps.TITLE: R10A,
        StructProps.ISTATE: '1000000000',
        StructProps.EFFECT: '1111111111',
        StructProps.CAUSES: '1111111111',
        StructProps.FORMAT: S2C,
    },
}

DUAL_LBL: str = 'dual'
PRIM_LBL: str = 'prim'

# ZERO_CHANNELS: int = 0
# ONE_CHANNEL: int = 1
