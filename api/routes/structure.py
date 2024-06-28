from fastapi import (
    APIRouter,
    status,
    UploadFile,
    HTTPException,
    File,
    Form,
    Depends,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from data.motors import get_sqlite

from api.models.props.structure import StructProps
from api.schemas.structure import StructureRequest, StructureResponse

from api.services.structure.base import (
    get_all,
    get_structure,
    delete_structure,
    post_structure,
)
from api.shared.formatter import Format

from constants.format import DEFFAULT_SHEET
from data.tables import StructureTable
from constants.structure import R3A, R4A, STRUCTURES
from utils.consts import DATA


router: APIRouter = APIRouter()


@router.post(
    '/',
    response_description='Crea una etructura.',
    status_code=status.HTTP_201_CREATED,
    response_model=StructureResponse,
)
async def create_structure(
    title: str = Form(default=STRUCTURES[R3A][StructProps.TITLE]),
    format: str = Form(default=STRUCTURES[R3A][StructProps.FORMAT]),
    tensor: UploadFile = File(...),
    sheet: str = Form(default=DEFFAULT_SHEET),
    db: Session = Depends(get_sqlite),
):
    structure_req: StructureRequest = StructureRequest(title=title, format=format)
    form: Format = Format(tensor, sheet, format)
    await form.set_array()
    new_structure: StructureResponse = post_structure(structure_req, form, db)
    return JSONResponse(content={DATA: jsonable_encoder(new_structure)})


@router.get(
    '/all',
    response_description='Obtiene todos las estructuras.',
    response_model=list[StructureResponse],
    status_code=status.HTTP_200_OK,
)
async def all_structures(db: Session = Depends(get_sqlite)):
    structures: list[StructureTable] = get_all(db)
    return JSONResponse(content={DATA: jsonable_encoder(structures)})


@router.get(
    '/{id}',
    response_description='Obtiene una estructura.',
    response_model=StructureResponse,
    status_code=status.HTTP_200_OK,
)
async def get_structure_by_id(id: int, db: Session = Depends(get_sqlite)):
    structure: StructureResponse = get_structure(id, db)
    return JSONResponse(content={DATA: jsonable_encoder(structure)})


@router.delete(
    '/{id}',
    response_description='Elimina una estructura.',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_structure_by_id(id: int, db: Session = Depends(get_sqlite)):
    structure_removed: bool = delete_structure(id, db)
    if structure_removed:
        return JSONResponse(status_code=status.HTTP_200_OK, content={'data': True})
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Structure with id {id} not found.',
    )
