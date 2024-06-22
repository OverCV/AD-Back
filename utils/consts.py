from click import INT
from api.models.enums.backend import SysProps
from constants.format import S2C


INFTY: float = float('inf')
FLOAT_ZERO: float = float(0)

DATA: str = 'data'

INT_ZERO: int = int(0)
INT_ONE: int = int(1)

STR_ZERO: str = str(INT_ZERO)
STR_ONE: str = str(INT_ONE)

ROWS_IDX = EFFECT = INT_ZERO
COLS_IDX = CAUSES = INT_ONE

EMPTY_STR: str = ''

""" System """

VOID: str = '∅'
PARTITION: str = 'partition'
DIST: str = 'distribution'
TIME: str = 'time'
LOSS: str = 'loss'

ISTATE: str = 'istate'
SUBSYS: str = 'subsystem'
TENSOR: str = 'tensor'


DEFAULT_TITLE: str = 'System_Title'
DEFAULT_ISTATE: str = '1000000000'
DEFAULT_EFFECT: str = '1111111111'
DEFAULT_CAUSES: str = '1111111111'


R2A: str = 'F2A'
F3A: str = 'F3A'
F4A: str = 'F4A'  # 1010
F4B: str = 'F4B'  # 1000
F5A: str = 'F5A'
F6A: str = 'F6A'
F8A: str = 'F8A'
F8B: str = 'F8B'

SYSTEMS: dict[str, dict[str, str]] = {
    R2A: {
        SysProps.TITLE.value: 'R2A System',
        SysProps.ISTATE.value: '1000000000',
        SysProps.EFFECT.value: '1111111111',
        SysProps.CAUSES.value: '1111111111',
        SysProps.FORMAT.value: S2C,
    },
}


DUAL_LBL: str = 'dual'
PRIM_LBL: str = 'prim'

# ZERO_CHANNELS: int = 0
# ONE_CHANNEL: int = 1

""" Schemas """

EXAMPLE: str = 'example'

""" Analyze """

BEST_NETWORK: str = 'netx'
MIN_INFO_LOSS: str = 'loss'
BEST_PARTITION: str = 'part'
BEST_DISTRIBUTION: str = 'dist'

""" Netowork """

W_LBL: str = 'weight'

NODE_DATA_OPTIONS: list[str] = [
    'color', 'label', 'value'
]
EDGE_DATA_OPTIONS: list[str] = [
    W_LBL, 'color'
]
COLORS_NAMES_LIST: list[str] = [
    'red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'orange', 'lime', 'pink', 'teal', 'indigo', 'brown', 'grey', 'black', 'white'
]

""" Analyze - Genetic """

INIT_POP_SIZE: str = 'r'
CROSS_RATE: str = 'xi'
MUTATE_RATE: str = 'mu'
MAX_GENS_STR: str = 'G'
BAD_STREAKS: str = 'unimprovement'

PARENTS_NUM: int = 2
CROSSED_IND: int = 2
MAX_STREAK: int = 3

DEFAULT_PARAMS: dict[str, float | int] = {
    INIT_POP_SIZE: 60,
    CROSS_RATE: 0.6,
    MUTATE_RATE: 0.1,
    MAX_GENS_STR: 100,
    BAD_STREAKS: 10,
}
