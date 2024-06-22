from enum import Enum, member


class ExecConfig(Enum):
    MAIN_APP_FILE: member = 'main:app'
    LOCALHOST: member = '127.0.0.1'
    APP_PORT: member = 8000


class SysProps(Enum):
    TITLE: member = 'title'
    ISTATE: member = 'istate'
    EFFECT: member = 'effect'
    CAUSES: member = 'causes'
    FORMAT: member = 'format'
