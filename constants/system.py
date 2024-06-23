from api.models.props.system import SysProps
from constants.format import S2C


VOID: str = '∅'
PARTITION: str = 'partition'
DIST: str = 'distribution'
TIME: str = 'time'
LOSS: str = 'loss'

ISTATE: str = 'istate'
SUBSYS: str = 'subsystem'
TENSOR: str = 'tensor'


# DEFAULT_TITLE: str = 'System_Title'
# DEFAULT_ISTATE: str = '1000000000'
# DEFAULT_EFFECT: str = '1111111111'
# DEFAULT_CAUSES: str = '1111111111'


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

SYSTEMS: dict[str, dict[str, str]] = {
    R2A: {
        SysProps.TITLE: R2A,
        SysProps.ISTATE: '10',
        SysProps.EFFECT: '11',
        SysProps.CAUSES: '11',
        SysProps.FORMAT: S2C,
    },
    R4A: {
        SysProps.TITLE: R4A,
        SysProps.ISTATE: '1000',
        SysProps.EFFECT: '1111',
        SysProps.CAUSES: '1111',
        SysProps.FORMAT: S2C,
    },
    R6A: {
        SysProps.TITLE: R6A,
        SysProps.ISTATE: '100000',
        SysProps.EFFECT: '111111',
        SysProps.CAUSES: '111111',
        SysProps.FORMAT: S2C,
    },
    R8A: {
        SysProps.TITLE: R8A,
        SysProps.ISTATE: '10000000',
        SysProps.EFFECT: '11111111',
        SysProps.CAUSES: '11111111',
        SysProps.FORMAT: S2C,
    },
    R10A: {
        SysProps.TITLE: R10A,
        SysProps.ISTATE: '1000000000',
        SysProps.EFFECT: '1111111111',
        SysProps.CAUSES: '1111111111',
        SysProps.FORMAT: S2C,
    },
}

DUAL_LBL: str = 'dual'
PRIM_LBL: str = 'prim'

# ZERO_CHANNELS: int = 0
# ONE_CHANNEL: int = 1
