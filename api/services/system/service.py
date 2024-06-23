import io
from logging import info, warn
import random
from typing import Annotated, Callable

from numpy.typing import NDArray
import numpy as np

from fastapi import HTTPException, UploadFile, status
import pandas as pd
from sqlalchemy.orm import Session

from api.models.enums.extensions import FileExt
from api.shared.formatter import Format
from api.shared.validators import system as sv
from api.schemas.system import SystemRequest, SystemResponse
from data.tables import SystemTable
from utils.funcs import cout


def post_system(
    system: SystemRequest, formatter: Format, db: Session
) -> SystemResponse:
    if sv.exist_system_title(system.title, db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'System was not created.《{system.title}》already exists'
        )
    formatter.set_matrices()
    subtensor: NDArray[np.float64] = np.array(
        formatter.get_matrices(), dtype=float
    )
    subtensor_size: int = len(subtensor)
    cout(subtensor_size)

    subtensor_str = formatter.serialize_tensor(subtensor)

    db_system = SystemTable(
        **system.model_dump(),
        tensor=subtensor_str,
        size=subtensor_size,
    )
    db.add(db_system)
    db.commit()
    db.refresh(db_system)
    return SystemResponse(**db_system.__dict__)


def get_all(db: Session) -> list[SystemResponse]:
    systems = db.query(SystemTable).all()
    return [SystemResponse(**system.__dict__) for system in systems]


def get_system(id: int, db: Session) -> SystemResponse:
    if not sv.exist_system_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'System with id {id} not found.'
        )
    db_system: SystemTable = db.query(SystemTable).filter(
        SystemTable.id == id
    ).first()
    if db_system is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'System with id {id} has no structure.'
        )
    return SystemResponse(**db_system.__dict__)


def get_system_by_title(title: str, db: Session) -> SystemResponse:
    if not sv.exist_system_title(title, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'System with title {title} not found.'
        )
    db_system: SystemTable = db.query(SystemTable).filter(
        SystemTable.title == title
    ).first()
    if db_system is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'System with title {title} has no structure.'
        )
    return SystemResponse(**db_system.__dict__)


def get_db_system(id: int, db: Session) -> SystemTable:
    if not sv.exist_system_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'System with id {id} not found.'
        )
    db_system: SystemTable = db.query(SystemTable).filter(
        SystemTable.id == id
    ).first()
    if db_system is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'System with id {id} has no structure.'
        )
    return db_system


def delete_system(id: int, db: Session) -> bool:
    db_system: SystemTable = db.query(SystemTable).filter(
        SystemTable.id == id
    ).first()
    if db_system is None:
        return False
    db.delete(db_system)
    db.commit()
    return True
