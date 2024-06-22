import io
from logging import info, warn
import random
from typing import Annotated, Callable
import numpy as np

from fastapi import HTTPException, UploadFile, status
import pandas as pd
from sqlalchemy.orm import Session

from api.models.enums.extensions import FileExt
from api.shared.formatter import Format
from api.shared.validators import system as sv
from api.schemas.system import SystemRequest, SystemResponse
from data.tables import SystemTable
from utils.funcs import printnl


def post_system(
    system: SystemRequest, formater: Format, db: Session
) -> SystemResponse:
    if sv.exist_system_title(system.title, db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'System was not created.《{system.title}》already exists'
        )
    formater.set_matrices()
    subtensor = np.array(formater.get_matrices(), dtype=float)
    subtensor_str = formater.serialize_tensor(subtensor)
    db_system = SystemTable(
        **system.model_dump(),
        tensor=subtensor_str
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
    db_rol: SystemTable = db.query(SystemTable).filter(
        SystemTable.id == id
    ).first()
    if db_rol is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'System with id {id} has no structure.'
        )
    return SystemResponse(**db_rol.__dict__)


def delete_system(id: int, db: Session) -> bool:
    db_rol: SystemTable = db.query(SystemTable).filter(
        SystemTable.id == id
    ).first()
    if db_rol is None:
        return False
    db.delete(db_rol)
    db.commit()
    return True
