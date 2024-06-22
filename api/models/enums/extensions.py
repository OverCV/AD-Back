from enum import Enum, member


class FileExt(Enum):
    EXCEL: member = '.xlsx'
    CSV: member = '.csv'
    TXT: member = '.txt'
    JSON: member = '.json'
