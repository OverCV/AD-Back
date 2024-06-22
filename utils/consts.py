INFTY: float = float('inf')
FLOAT_ZERO: float = float(0)

DATA: str = 'data'

"""  """


EXAMPLE: str = 'example'
EMPTY_STR: str = ''

ZERO_CHANNELS: int = 0
ONE_CHANNEL: int = 1

INITIAL: str = 'initial'
FUTURE: int = 0
CURRENT: int = 1

STR_ZERO: str = '0'
STR_ONE: str = '1'

ONE_LBL: str = 'one'
TWO_LBL: str = 'two'


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


F2A: str = 'F2A'
F3A: str = 'F3A'
F4A: str = 'F4A'  # 1010
F4B: str = 'F4B'  # 1000
F5A: str = 'F5A'
F6A: str = 'F6A'
F8A: str = 'F8A'
F8B: str = 'F8B'


INIT_POP_SIZE: str = 'r'
CROSS_RATE: str = 'xi'
MUTATE_RATE: str = 'mu'
MAX_GENS_STR: str = 'max_gens'
STREAK_IMPROVE: str = 'streak_improve'

PARENTS_NUM: int = 2
CROSSED_IND: int = 2
MAX_STREAK: int = 3

DEFAULT_PARAMS: dict[str, float | int] = {
    INIT_POP_SIZE: 60,
    CROSS_RATE: 0.6,
    MUTATE_RATE: 0.1,
    MAX_GENS_STR: 100,
    STREAK_IMPROVE: 10,
}
