from sqlalchemy.orm import Session
from data.tables import StructureTable


def exist_structure_id(system_id: int, db: Session) -> bool:
    db_system: StructureTable = (
        db.query(StructureTable).filter(StructureTable.id == system_id).first()
    )
    return False if db_system is None else True


def exist_structure_title(system_title: str, db: Session) -> bool:
    db_system: StructureTable = (
        db.query(StructureTable).filter(StructureTable.title == system_title).first()
    )
    return db_system is not None


def has_valid_istate(istate: str, tensor_len) -> bool:
    return len(istate) == tensor_len
