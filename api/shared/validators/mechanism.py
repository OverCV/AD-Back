from sqlalchemy.orm import Session
from data.tables import MechanismTable


def exist_mecha_id(system_id: int, db: Session) -> bool:
    db_system: MechanismTable = db.query(MechanismTable).filter(
        MechanismTable.id == system_id
    ).first()
    return False if db_system is None else True


def exist_mechanism_title(system_title: str, db: Session) -> bool:
    db_system: MechanismTable = db.query(MechanismTable).filter(
        MechanismTable.title == system_title
    ).first()
    return db_system is not None


def has_valid_istate(istate: str, tensor_len) -> bool:
    return len(istate) == tensor_len
