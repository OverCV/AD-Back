"""Database"""

TO_SECONDS: float = 1000

""" General """

INFTY: float = float('inf')
FLOAT_ZERO: float = float(0)
FLOAT_ONE: float = float(1)

DATA: str = 'data'

INT_ZERO: int = int(0)
INT_ONE: int = int(1)

STR_ZERO: str = str(INT_ZERO)
STR_ONE: str = str(INT_ONE)

BASE_2: int = 2

ROWS_IDX = EFFECT = INT_ZERO
COLS_IDX = CAUSES = INT_ONE

EMPTY_STR: str = ''


""" Schemas """

EX_STR: str = 'example'

""" Analyze """

NET_ID: str = 'net_view_id'
SMALL_PHI: str = 'φ'
MIP: str = 'mip'
SUB_DIST: str = 'sub_distribution'
DIST: str = 'distribution'

""" Network """

W_LBL: str = 'weight'

NODE_DATA_OPTIONS: list[str] = ['color', 'label', 'value']
EDGE_DATA_OPTIONS: list[str] = [W_LBL, 'color']
COLORS_NAMES_LIST: list[str] = [
    'red',
    'green',
    'blue',
    'yellow',
    'purple',
    'cyan',
    'magenta',
    'orange',
    'lime',
    'pink',
    'teal',
    'indigo',
    'brown',
    'grey',
    'black',
    'white',
]
