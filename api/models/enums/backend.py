from enum import Enum


class ExecConfig(Enum):
    MAIN_APP_FILE = 'main:app'
    LOCALHOST = '127.0.0.1'
    APP_PORT = 8000
