"""Database"""

TO_SECONDS: float = 1000

""" General """

INFTY_POS: float = float('inf')
INFTY_NEG: float = float('-inf')
FLOAT_ZERO: float = float(0)
FLOAT_ONE: float = float(1)

DATA: str = 'data'

INT_ZERO: int = int(0)
INT_ONE: int = int(1)

STR_ZERO: str = str(INT_ZERO)
STR_ONE: str = str(INT_ONE)

BASE_2: int = 2

ROWS_IDX = EFFECT = INT_ZERO
COLS_IDX = ACTUAL = INT_ONE

EMPTY_STR: str = ''


""" Schemas """

EX_STR: str = 'example'
SAMPLES_STR: str = 'samples'

""" Analyze """

NET_ID: str = 'net_view_id'
SMALL_PHI: str = 'φ'
MIP: str = 'mip'
SUB_DIST: str = 'sub_distribution'
DIST: str = 'distribution'

""" Network """
FIRST: int = INT_ZERO
LAST_IDX: int = -INT_ONE
U_IDX: int = 0
V_IDX: int = 1
DATA_IDX: int = 2
WT_LBL: str = 'weight'

# NODE_DATA_OPTIONS: list[str] = ['color', 'label', 'value']
# EDGE_DATA_OPTIONS: list[str] = [W_LBL, 'color']
# COLORS_NAMES_LIST: list[str] = [
#     'red',
#     'green',
#     'blue',
#     'yellow',
#     'purple',
#     'cyan',
#     'magenta',
#     'orange',
#     'lime',
#     'pink',
#     'teal',
#     'indigo',
#     'brown',
#     'grey',
#     'black',
#     'white',
# ]
