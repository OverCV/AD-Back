from enum import Enum, member


# from numpy import little_endian


class ExecConfig(Enum):
    # Maybe a boolean?
    MAIN_APP_FILE: member = 'main:app'
    LOCALHOST: member = '127.0.0.1'
    APP_PORT: member = 8000
