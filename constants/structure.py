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


FUTURE = INT_ZERO
CURRENT = INT_ONE

# class MechaInt(TypedDict):
#     title: str
#     istate: str
#     effect: str
#     actual: str
#     format: str

DUAL_LBL: str = 'dual'
PRIM_LBL: str = 'prim'


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
STR_NUMBERS: list[str] = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15]

# S -> String
SA: str = 'A'
SB: str = 'B'
SC: str = 'C'
SD: str = 'D'
SE: str = 'E'
SF: str = 'F'
SG: str = 'G'
STR_LETTERS: list[str] = [SA, SB, SC, SD, SE, SF, SG]


SHEET_NAME: str = 'sheet'
CONTROL_PARAMETERS: str = 'ctrl_params'
IS_DUAL: str = 'dual'

SAMPLES = {
    # Nivel de redes (R3..R15)
    N3: {
        # Nivel de red (A..Z)
        SA: {
            # Nivel de parámetros (subsistemas/mecanismos/alcances)
            N1: {
                SHEET_NAME: 'Red de 03 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R3A',
                StructProps.ISTATE: '100',
                StructProps.SUBSYS: '111',
                StructProps.EFFECT: '111',
                StructProps.ACTUAL: '111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
    },
    N4: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 04 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R4A',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABCD | ABCD
                StructProps.EFFECT: '1111',
                StructProps.ACTUAL: '1111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N2: {
                SHEET_NAME: 'Red de 04 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R4A',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABC | ABCD
                StructProps.EFFECT: '1110',
                StructProps.ACTUAL: '1111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N3: {
                SHEET_NAME: 'Red de 04 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R4A',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABCD | AC
                StructProps.EFFECT: '1111',
                StructProps.ACTUAL: '1010',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N4: {
                SHEET_NAME: 'Red de 04 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R4A',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # AC | ABC
                StructProps.EFFECT: '1010',
                StructProps.ACTUAL: '1110',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N5: {
                SHEET_NAME: 'Red de 04 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R4A',
                StructProps.ISTATE: '1000',
                StructProps.SUBSYS: '1111',  # ABC | ABC
                StructProps.EFFECT: '1110',
                StructProps.ACTUAL: '1110',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
    },
    N5: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDt+1|ABCDt
                StructProps.EFFECT: '11110',
                StructProps.ACTUAL: '11110',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N2: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDt+1|ABCDEt
                StructProps.EFFECT: '11110',
                StructProps.ACTUAL: '11111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N3: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDEt+1|ABCDt
                StructProps.EFFECT: '11111',
                StructProps.ACTUAL: '11110',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N4: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCt+1|ABCDEt
                StructProps.EFFECT: '11100',
                StructProps.ACTUAL: '11111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N5: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCDEt+1|ABt
                StructProps.EFFECT: '11111',
                StructProps.ACTUAL: '11000',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N6: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ACDt+1|ACDt
                StructProps.EFFECT: '10110',
                StructProps.ACTUAL: '10110',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N7: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCt+1|ABCt
                StructProps.EFFECT: '11100',
                StructProps.ACTUAL: '11100',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N8: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCEt+1|ABEt
                StructProps.EFFECT: '11101',
                StructProps.ACTUAL: '11001',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N9: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # BCt+1|ABCt
                StructProps.EFFECT: '01100',
                StructProps.ACTUAL: '11100',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N10: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A1',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # BCt+1|Ct
                StructProps.EFFECT: '01100',
                StructProps.ACTUAL: '00100',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N11: {
                SHEET_NAME: 'Red de 05 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R5A1',
                StructProps.ISTATE: '10001',
                StructProps.SUBSYS: '11111',  # ABCt+1|ACt
                StructProps.EFFECT: '11100',
                StructProps.ACTUAL: '10100',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
    },
    N6: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 06 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R6A',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '101000',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N2: {
                SHEET_NAME: 'Red de 06 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R6A',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '111000',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N3: {
                SHEET_NAME: 'Red de 06 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R6A',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '111110',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N4: {
                SHEET_NAME: 'Red de 06 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R6A',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '111010',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N5: {
                SHEET_NAME: 'Red de 06 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R6A',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '101110',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N6: {
                SHEET_NAME: 'Red de 06 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R6A',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '111000',
                StructProps.ACTUAL: '101111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N7: {
                SHEET_NAME: 'Red de 06 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R6A',
                StructProps.ISTATE: '100000',
                StructProps.SUBSYS: '111111',
                StructProps.EFFECT: '011111',
                StructProps.ACTUAL: '110011',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
    },
    N8: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8A',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '11111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N2: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8A',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11100011',
                StructProps.ACTUAL: '11111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N3: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8A',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '01111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N4: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8A',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '00011111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N5: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8A',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11110000',
                StructProps.ACTUAL: '00011111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
        SB: {
            N1: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8B',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '11111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N2: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8B',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11111111',
                StructProps.ACTUAL: '10111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N3: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8B',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '00111111',
                StructProps.ACTUAL: '00001111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N4: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8B',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '00111111',
                StructProps.ACTUAL: '11100000',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N5: {
                SHEET_NAME: 'Red de 08 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R8B',
                StructProps.ISTATE: '10000000',
                StructProps.SUBSYS: '11111111',
                StructProps.EFFECT: '11100000',
                StructProps.ACTUAL: '11100000',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
    },
    N10: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 10 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R10A',
                StructProps.ISTATE: '1000000000',
                StructProps.SUBSYS: '1111111111',
                StructProps.EFFECT: '1111111111',
                StructProps.ACTUAL: '1111111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N2: {
                SHEET_NAME: 'Red de 10 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R10A',
                StructProps.ISTATE: '1000000000',
                StructProps.SUBSYS: '1111111111',
                StructProps.EFFECT: '1111110001',
                StructProps.ACTUAL: '1111111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N3: {
                SHEET_NAME: 'Red de 10 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R10A',
                StructProps.ISTATE: '1000000000',
                StructProps.SUBSYS: '1111111111',
                StructProps.EFFECT: '1111110001',
                StructProps.ACTUAL: '1001111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
            N4: {
                SHEET_NAME: 'Red de 10 Nodos',
                StructProps.ID: None,
                StructProps.TITLE: 'R10A',
                StructProps.ISTATE: '1000000000',
                StructProps.SUBSYS: '1111111111',
                StructProps.EFFECT: '1111111001',
                StructProps.ACTUAL: '1101111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
    },
    N15: {
        SA: {
            N1: {
                SHEET_NAME: 'Red de 15 Nodos (Awake)',
                StructProps.ID: None,
                StructProps.TITLE: 'R15A',
                StructProps.ISTATE: '100000000000000',
                StructProps.SUBSYS: '111000000000000',
                StructProps.EFFECT: '111111111111111',
                StructProps.ACTUAL: '111111111111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
        SB: {
            N1: {
                SHEET_NAME: 'Red de 15 Nodos (Asleep)',
                StructProps.ID: None,
                StructProps.TITLE: 'R15B',
                StructProps.ISTATE: '100000000000000',
                StructProps.SUBSYS: '111000000000000',
                StructProps.EFFECT: '111111111111111',
                StructProps.ACTUAL: '111111111111111',
                CONTROL_PARAMETERS: ControlSchema,
                StructProps.FORMAT: S2C,
                IS_DUAL: False,
            },
        },
    },
}
