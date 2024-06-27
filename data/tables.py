from sqlalchemy import Boolean, Column, Integer, String, CLOB, DateTime
from data.motors import Base


# Se almacenan las matrices ya marginalizadas y a su vez se tiene la distribución objetivo #


class StructureTable(Base):
    __tablename__ = 'structure'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(31))
    tensor = Column(CLOB)
    size = Column(Integer)
    format = Column(String(31))
    # jstate: Column[str] = Column(String(255))


class ConfigTable(Base):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(31))
    using_le = Column(Boolean)
    using_local_nosql = Column(Boolean)
    storing_nets = Column(Boolean)
    config_time = Column(DateTime)
