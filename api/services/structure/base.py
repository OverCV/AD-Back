from numpy.typing import NDArray
import numpy as np

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from api.shared.formatter import Format
from api.shared.validators import mechanism as sv
from api.schemas.structure import StructureRequest, StructureResponse
from data.tables import StructureTable
from utils.funcs import cout


def post_structure(
    structure: StructureRequest, formatter: Format, db: Session
) -> StructureResponse:
    if sv.exist_structure_title(structure.title, db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Structure was not created.《{structure.title}》already exists',
        )
    formatter.set_matrices()
    subtensor: NDArray[np.float64] = np.array(formatter.get_matrices(), dtype=float)
    subtensor_size: int = len(subtensor)
    cout(subtensor_size)

    subtensor_str = formatter.serialize_tensor(subtensor)

    db_struct = StructureTable(
        **structure.model_dump(),
        tensor=subtensor_str,
        size=subtensor_size,
    )
    db.add(db_struct)
    db.commit()
    db.refresh(db_struct)
    return StructureResponse(**db_struct.__dict__)


def get_all(db: Session) -> list[StructureResponse]:
    structures = db.query(StructureTable).all()
    return [StructureResponse(**struct.__dict__) for struct in structures]


def get_structure(id: int, db: Session) -> StructureResponse:
    if not sv.exist_structure_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Structure with id {id} not found.',
        )
    db_struct: StructureTable = db.query(StructureTable).filter(StructureTable.id == id).first()
    if db_struct is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'Structure with id {id} has no structure.',
        )
    return StructureResponse(**db_struct.__dict__)


def get_structure_by_title(title: str, db: Session) -> StructureResponse:
    if not sv.exist_structure_title(title, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Structure with title {title} not found.',
        )
    db_structure: StructureTable = (
        db.query(StructureTable).filter(StructureTable.title == title).first()
    )
    if db_structure is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'Structure with title {title} has no structure.',
        )
    return StructureResponse(**db_structure.__dict__)


def get_db_structure(id: int, db: Session) -> StructureTable:
    if not sv.exist_structure_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Structure with id {id} not found.',
        )
    db_structure: StructureTable = db.query(StructureTable).filter(StructureTable.id == id).first()
    if db_structure is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'Structure with id {id} do not exists.',
        )
    return db_structure


def delete_structure(id: int, db: Session) -> bool:
    db_structure: StructureTable = db.query(StructureTable).filter(StructureTable.id == id).first()
    if db_structure is None:
        return False
    db.delete(db_structure)
    db.commit()
    return True
