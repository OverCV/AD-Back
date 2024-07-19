from typing import TypedDict

import numpy as np
from numpy.typing import NDArray

from api.models.props.structure import StructProps
from api.schemas.genetic.control import ControlSchema
from constants.format import S2C
from utils.consts import INT_ONE, INT_ZERO


VOID: str = '∅'
PARTITION: str = 'partition'
DIST: str = 'distribution'
TIME: str = 'time'
LOSS: str = 'loss'

# T0_SYM: str = '(t=0)'
# T1_SYM: str = '(t=1)'
T0_SYM: str = '(0)'
T1_SYM: str = '(1)'

ISTATE: str = 'istate'
SUBSYS: str = 'subsystem'
TENSOR: str = 'tensor'

BIN_RANGE = range(2)
BOOL_RANGE: list[bool] = [False, True]
UNIT_MAT: NDArray[np.float64] = np.array([INT_ONE], dtype=np.float64)
UNIT_MUL: tuple[tuple[int, ...], NDArray[np.float64]] = ((), UNIT_MAT)


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
    actual: str
    format: str


STRUCTURES: dict[str, MechaInt] = {
    R2A: {
        StructProps.TITLE: R2A,
        StructProps.ISTATE: '10',
        StructProps.EFFECT: '11',
        StructProps.ACTUAL: '11',
        StructProps.SUBSYS: '11',
        StructProps.FORMAT: S2C,
    },
    R3A: {
        StructProps.TITLE: R3A,
        StructProps.ISTATE: '100',
        StructProps.EFFECT: '111',
        StructProps.ACTUAL: '111',
        StructProps.SUBSYS: '111',
        StructProps.FORMAT: S2C,
    },
    R4A: {
        StructProps.TITLE: R4A,
        StructProps.ISTATE: '1000',
        StructProps.EFFECT: '1111',
        StructProps.ACTUAL: '1111',
        StructProps.SUBSYS: '1110',
        StructProps.FORMAT: S2C,
    },
    R5A: {
        StructProps.TITLE: R5A,
        StructProps.ISTATE: '10001',
        StructProps.EFFECT: '11111',
        StructProps.ACTUAL: '11111',
        StructProps.SUBSYS: '11100',  # ! Implement for all ! #
        StructProps.FORMAT: S2C,
    },
    R6A: {
        StructProps.TITLE: R6A,
        StructProps.ISTATE: '100000',
        StructProps.EFFECT: '111111',
        StructProps.ACTUAL: '111111',
        StructProps.SUBSYS: '111000',
        StructProps.FORMAT: S2C,
    },
    R8A: {
        StructProps.TITLE: R8A,
        StructProps.ISTATE: '10000000',
        StructProps.EFFECT: '11111111',
        StructProps.ACTUAL: '11111111',
        StructProps.SUBSYS: '11100000',
        StructProps.FORMAT: S2C,
    },
    R10A: {
        StructProps.TITLE: R10A,
        StructProps.ISTATE: '1000000000',
        StructProps.EFFECT: '1111111111',
        StructProps.ACTUAL: '1111111111',
        StructProps.SUBSYS: '1110000000',
        StructProps.FORMAT: S2C,
    },
}

DUAL_LBL: str = 'dual'
PRIM_LBL: str = 'prim'

# ZERO_CHANNELS: int = 0
# ONE_CHANNEL: int = 1


"""

colección de redes: R3, R4, R5, R6, R8, R10
Coleccion de una red -> R3: A, B, C, D


"""


# N -> Number
N1: str = '1'
N2: str = '2'
N3: str = '3'
N4: str = '4'
N5: str = '5'
N6: str = '6'
N7: str = '7'
N8: str = '8'
N9: str = '9'
N10: str = '10'
N11: str = '11'
N12: str = '12'
N13: str = '13'
N14: str = '14'
N15: str = '15'

# S -> String
SA: str = 'A'
SB: str = 'B'
SC: str = 'C'
SD: str = 'D'
SE: str = 'E'
SF: str = 'F'
SG: str = 'G'


CTRL_PARAMS: str = 'control_parameters'
SHEET_NAME: str = 'sheet_name'
IS_DUAL: str = 'is_dual'
STRUCT_ID: str = 'struct_id'

SAMPLES = {
    # Nivel de redes (R3..R15)
    N3: {
        # Nivel de red (A..Z)
        SA: {
            # Nivel de parámetros (subsistemas/mecanismos/alcances)
            N1: {
                SHEET_NAME: 'Red de 03 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R3A1',
                StructProps.ISTATE: '100',
                StructProps.SUBSYS: '111',
                StructProps.EFFECT: '111',
                StructProps.ACTUAL: '111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
    },
    N4: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 04 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R4A1',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABCD | ABCD
                StructProps.EFFECT: '1111',
                StructProps.ACTUAL: '1111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N2: {
                SHEET_NAME: 'Red de 04 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R4A2',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABC | ABCD
                StructProps.EFFECT: '1110',
                StructProps.ACTUAL: '1111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N3: {
                SHEET_NAME: 'Red de 04 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R4A3',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABCD | AC
                StructProps.EFFECT: '1111',
                StructProps.ACTUAL: '1010',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N4: {
                SHEET_NAME: 'Red de 04 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R4A4',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # AC | ABC
                StructProps.EFFECT: '1010',
                StructProps.ACTUAL: '1110',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N5: {
                SHEET_NAME: 'Red de 04 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R4A5',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABC | ABC
                StructProps.EFFECT: '1110',
                StructProps.ACTUAL: '1110',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
    },
    N5: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A1',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDt+1|ABCDt
                StructProps.EFFECT: '11110',
                StructProps.ACTUAL: '11110',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N2: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A2',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDt+1|ABCDEt
                StructProps.EFFECT: '11110',
                StructProps.ACTUAL: '11111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N3: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A3',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDEt+1|ABCDt
                StructProps.EFFECT: '11111',
                StructProps.ACTUAL: '11110',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N4: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A4',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCt+1|ABCDEt
                StructProps.EFFECT: '11100',
                StructProps.ACTUAL: '11111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N5: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A5',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDEt+1|ABt
                StructProps.EFFECT: '11111',
                StructProps.ACTUAL: '11000',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N6: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A6',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ACDt+1|ACDt
                StructProps.EFFECT: '10110',
                StructProps.ACTUAL: '10110',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N7: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A7',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCt+1|ABCt
                StructProps.EFFECT: '11100',
                StructProps.ACTUAL: '11100',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N8: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A8',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCEt+1|ABEt
                StructProps.EFFECT: '11101',
                StructProps.ACTUAL: '11001',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N9: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A9',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # BCt+1|ABCt
                StructProps.EFFECT: '01100',
                StructProps.ACTUAL: '11100',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N10: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A10',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # BCt+1|Ct
                StructProps.EFFECT: '01100',
                StructProps.ACTUAL: '00100',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N11: {
                SHEET_NAME: 'Red de 05 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R5A11',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCt+1|ACt
                StructProps.EFFECT: '11100',
                StructProps.ACTUAL: '10100',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
    },
    N6: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 06 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R6A1',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '101000',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N2: {
                SHEET_NAME: 'Red de 06 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R6A1',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '111000',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N3: {
                SHEET_NAME: 'Red de 06 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R6A1',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '111110',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N4: {
                SHEET_NAME: 'Red de 06 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R6A1',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '111010',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N5: {
                SHEET_NAME: 'Red de 06 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R6A1',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '101110',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N6: {
                SHEET_NAME: 'Red de 06 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R6A1',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '101111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N7: {
                SHEET_NAME: 'Red de 06 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R6A1',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '011111',
                StructProps.ACTUAL: '110011',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
    },
    N8: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8A1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '11111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N2: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8A1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11100011',
                StructProps.ACTUAL: '11111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N3: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8A1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '01111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N4: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8A1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '00011111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N5: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8A1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11110000',
                StructProps.ACTUAL: '00011111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
        SB: {
            N1: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8B1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '11111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N2: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8B1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '10111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N3: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8B1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '00111111',
                StructProps.ACTUAL: '00001111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N4: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8B1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '00111111',
                StructProps.ACTUAL: '11100000',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
            N5: {
                SHEET_NAME: 'Red de 08 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R8B1',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11100000',
                StructProps.ACTUAL: '11100000',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
    },
    N10: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 10 Nodos',
                STRUCT_ID: None,
                StructProps.TITLE: 'R10A1',
                StructProps.ISTATE: '1000000000',
                StructProps.SUBSYS: '1110000000',
                StructProps.EFFECT: '1111111111',
                StructProps.ACTUAL: '1111111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
    },
    N15: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 15 Nodos (Awake)',
                STRUCT_ID: None,
                StructProps.TITLE: 'R15A1',
                StructProps.ISTATE: '100000000000000',
                StructProps.SUBSYS: '111000000000000',
                StructProps.EFFECT: '111111111111111',
                StructProps.ACTUAL: '111111111111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
        SB: {
            N1: {
                SHEET_NAME: 'Red de 15 Nodos (Asleep)',
                STRUCT_ID: None,
                StructProps.TITLE: 'R15B1',
                StructProps.ISTATE: '100000000000000',
                StructProps.SUBSYS: '111000000000000',
                StructProps.EFFECT: '111111111111111',
                StructProps.ACTUAL: '111111111111111',
                IS_DUAL: False,
                CTRL_PARAMS: ControlSchema,
            },
        },
    },
}
