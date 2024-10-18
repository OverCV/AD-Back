from enum import Enum


class ExecConfig(Enum):
    MAIN_APP_FILE = 'main:app'
    LOCALHOST = '127.0.0.1'
    APP_PORT = 8000

    __MAIN__ = '__main__'
    LOGGER_DIR = 'app.log'
    LOGGER_ENCODING = 'utf-8'
    DOTENV_PATH = '.venv/.dev.env'
    YES = True
    NO = False
