import os
from motor.motor_asyncio import AsyncIOMotorClient


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from api.models.enums.database import NoSQLPort, SQLPort
from server import conf
from utils.consts import TO_SECONDS


""" NoSQL Database """

REMOTE_MONGO_URI: str = os.environ.get(NoSQLPort.REMOTE_MONGO_URI.value)
LOCAL_MONGO_URI: str = os.environ.get(NoSQLPort.LOCAL_MONGO_URI.value)

MONGO_CLIENT: int = os.environ.get(NoSQLPort.MONGO_CLIENT.value)
MONGO_COLLECTION: int = os.environ.get(NoSQLPort.MONGO_COLLECTION.value)


async def get_mongo() -> AsyncIOMotorClient:
    MONGO_URI: str = LOCAL_MONGO_URI if conf.locale_nosql else REMOTE_MONGO_URI
    client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=2.5 * TO_SECONDS)
    db = client[MONGO_CLIENT]
    return db.get_collection(MONGO_COLLECTION)


""" SQL Database """
SQLITE_URL: str = os.environ.get(SQLPort.SQLITE_URL.value)
print(SQLITE_URL)
engine = create_engine(SQLITE_URL, echo=True, future=True)

Base: registry = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_sqlite():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    # try:
    #     # Intento conectarme al MongoDB remoto
    #     client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    #     db = client[MONGO_CLIENT]
    #     return db.get_collection(MONGO_COLLECTION)
    # except ServerSelectionTimeoutError:
    #     # Si falla, me conecto al MongoDB local
    #     print("Conexión remota fallida, conectando a MongoDB local.")
    #     client = AsyncIOMotorClient(
    #         LOCAL_MONGO_URI, serverSelectionTimeoutMS=3000
    #     )
    #     db = client[LOCAL_MONGO_CLIENT]
    #     return db.get_collection(LOCAL_MONGO_COLLECTION)
    # except Exception as e:
    #     # Captura cualquier otro error
    #     print(f"Error inesperado: {e}")
    #     raise e  # O maneja el error de una manera que no detenga tu aplicación


# def get_mongo():
#     # try:
#     #     client = AsyncIOMotorClient(
#     #         MONGO_URI,
#     #         # Tiempo máximo en milisegundos para la selección del servidor
#     #         serverSelectionTimeoutMS=3000
#     #     )
#     #     db = client[MONGO_CLIENT]
#     #     return db.get_collection(MONGO_COLLECTION)
#     # except ServerSelectionTimeoutError as e:
#     # print(f"Error connecting to remote MongoDB: {e}")
#     client = AsyncIOMotorClient(LOCAL_MONGO_URI)
#     db = client[LOCAL_MONGO_CLIENT]
#     return db.get_collection(LOCAL_MONGO_COLLECTION)
#     # except Exception as e:
#     #     print(f"Unhandled error: {e}")
