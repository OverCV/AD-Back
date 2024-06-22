from enum import Enum, member


class SQLPort(Enum):
    SQLITE_URL: member = 'SQLITE_URL'


class NoSQLPort(Enum):
    REMOTE_MONGO_URI: member = 'REMOTE_MONGO_URI'
    LOCAL_MONGO_URI: member = 'LOCAL_MONGO_URI'
    MONGO_CLIENT: member = 'MONGO_CLIENT'
    MONGO_COLLECTION: member = 'MONGO_COLLECTION'
