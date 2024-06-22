from sqlalchemy import Boolean, Column, Integer, String, CLOB, DateTime
from data.base import Base


# Se almacenan las matrices ya marginalizadas y a su vez se tiene la distribución objetivo #


class SystemTable(Base):
    __tablename__ = 'system'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(31))
    istate = Column(CLOB)
    effect = Column(CLOB)
    causes = Column(CLOB)
    tensor = Column(CLOB)
    # jstate: Column[str] = Column(String(255))
    # format: Column[str] = Column(String(31))


class ConfigTable(Base):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(31))
    using_le = Column(Boolean)
    using_local_nosql = Column(Boolean)
    storing_nets = Column(Boolean)
    time = Column(DateTime)
