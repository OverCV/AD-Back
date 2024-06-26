from numpy.typing import NDArray
import numpy as np

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from api.shared.formatter import Format
from api.shared.validators import mechanism as sv
from api.schemas.mechanism import MechanismRequest, MechanismResponse
from data.tables import MechanismTable
from utils.funcs import cout


def post_mechanism(
    mechanism: MechanismRequest, formatter: Format, db: Session
) -> MechanismResponse:
    if sv.exist_mechanism_title(mechanism.title, db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Mechanism was not created.《{mechanism.title}》already exists',
        )
    formatter.set_matrices()
    subtensor: NDArray[np.float64] = np.array(
        formatter.get_matrices(), dtype=float
    )
    subtensor_size: int = len(subtensor)
    cout(subtensor_size)

    subtensor_str = formatter.serialize_tensor(subtensor)

    db_mecha = MechanismTable(
        **mechanism.model_dump(),
        tensor=subtensor_str,
        size=subtensor_size,
    )
    db.add(db_mecha)
    db.commit()
    db.refresh(db_mecha)
    return MechanismResponse(**db_mecha.__dict__)


def get_all(db: Session) -> list[MechanismResponse]:
    mechas = db.query(MechanismTable).all()
    return [MechanismResponse(**mecha.__dict__) for mecha in mechas]


def get_mechanism(id: int, db: Session) -> MechanismResponse:
    if not sv.exist_mecha_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Mechanism with id {id} not found.',
        )
    db_mecha: MechanismTable = (
        db.query(MechanismTable).filter(MechanismTable.id == id).first()
    )
    if db_mecha is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'Mechanism with id {id} has no structure.',
        )
    return MechanismResponse(**db_mecha.__dict__)


def get_mechanism_by_title(title: str, db: Session) -> MechanismResponse:
    if not sv.exist_mechanism_title(title, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Mechanism with title {title} not found.',
        )
    db_Mechanism: MechanismTable = (
        db.query(MechanismTable)
        .filter(MechanismTable.title == title)
        .first()
    )
    if db_Mechanism is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'Mechanism with title {title} has no structure.',
        )
    return MechanismResponse(**db_Mechanism.__dict__)


def get_db_mechanism(id: int, db: Session) -> MechanismTable:
    if not sv.exist_mecha_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Mechanism with id {id} not found.',
        )
    db_mechanism: MechanismTable = (
        db.query(MechanismTable).filter(MechanismTable.id == id).first()
    )
    if db_mechanism is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'Mechanism with id {id} has no structure.',
        )
    return db_mechanism


def delete_mechanism(id: int, db: Session) -> bool:
    db_mechanism: MechanismTable = (
        db.query(MechanismTable).filter(MechanismTable.id == id).first()
    )
    if db_mechanism is None:
        return False
    db.delete(db_mechanism)
    db.commit()
    return True
