from logging import *
from os import system


from fastapi import Body, File, Form, HTTPException, Response, UploadFile, status, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from matplotlib.pylab import f
import numpy as np
import pandas as pd
from sqlalchemy.orm import Session
from api.schemas.system import SystemRequest
from data.base import get_sqlite


from api.services.system.service import *

from api.shared.formatter import Format


from constants.format import (
    DEFAULT_FORMAT, DEFFAULT_SHEET, S2C, S2P, S2S
)
from utils.funcs import printnl
from utils.consts import (
    DEFAULT_CAUSES, DATA, DEFAULT_ISTATE, DEFAULT_EFFECT, DEFAULT_TITLE, FLOAT_ZERO, ISTATE
)

router: APIRouter = APIRouter()


@router.post(
    '/',
    response_description='Crea un sistema.',
    status_code=status.HTTP_201_CREATED,
    response_model=SystemResponse,
)
async def create_system(
    title: str = Form(default=DEFAULT_TITLE),
    istate: str = Form(default=DEFAULT_ISTATE),
    format: str = Form(default=DEFAULT_FORMAT),
    tensor: UploadFile = File(...),
    db: Session = Depends(get_sqlite),
):
    system_req: SystemRequest = SystemRequest(
        title=title, istate=istate
    )
    form: Format = Format(tensor, format)
    await form.set_array()
    new_system: SystemResponse = post_system(system_req, form, db)
    return JSONResponse(
        content={DATA: jsonable_encoder(new_system)}
    )


@router.get(
    '/all',
    response_description='Obtiene todos los sistemas.',
    response_model=list[SystemResponse],
    status_code=status.HTTP_200_OK,
)
async def all_systems(db: Session = Depends(get_sqlite)):
    systems: list[SystemTable] = get_all(db)
    return JSONResponse(
        content={DATA: jsonable_encoder(systems)}
    )


@router.get(
    '/{id}',
    response_description='Obtiene un sistema.',
    response_model=SystemResponse,
    status_code=status.HTTP_200_OK,
)
async def get_system_by_id(id: int, db: Session = Depends(get_sqlite)):
    system: SystemResponse = get_system(id, db)
    return JSONResponse(
        content={DATA: jsonable_encoder(system)}
    )


@router.delete(
    '/{id}',
    response_description='Elimina un sistema.',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_system_by_id(id: int, db: Session = Depends(get_sqlite)):
    system_removed: bool = delete_system(id, db)
    if system_removed:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'data': True}
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'System with id {id} not found.'
    )

# async def strategy_zero(system_schema: SystemSchema):
# res: dict = await compute_zero(system_schema)
# return JSONResponse(
#     status_code=status.HTTP_200_OK,
#     content={DATA: jsonable_encoder(res)}
# )
# @router.post(
#     '/',
#     response_description='Crea un sistema.',
#     response_model=bool,
#     status_code=status.HTTP_201_CREATED,
#     response_model_by_alias=False,
# )
# async def create_system(
#     initial_state: str = Form(...),
#     system_id: int = Form(...),
#     system_initial_state: str = Form(...),
#     system_subsystem: list[str] = Form(...),
#     tensor: UploadFile = File(...),
#     sheet: str = Form(...),
#     format: str = Form(...),
#     db: Session = Depends(get_sqlite),
# ):
#     print(initial_state)
#     system = SystemSchema(
#         id=system_id,
#         initial_state=system_initial_state,
#         subsystem=system_subsystem,
#     )
#     if tensor.filename.endswith('.xlsx'):
#         bit_chunk: bytes = await tensor.read()
#         xlsx: io.BytesIO = io.BytesIO(bit_chunk)
#         wb: op.Workbook = op.load_workbook(xlsx)
#         ws = wb[sheet]
#         format_options: dict[str, Callable] = {
#             "state-to-state": lambda: print('S2S'),
#             "state-to-correlation": lambda: print('S2C'),
#             "state-to-pair": lambda: print('S2P'),
#         }
#         format_options[format]()
#         arr: list[list[float]] = []
#         for cells in ws.iter_rows():
#             row = [cell.value for cell in cells if cell.value is not None]
#             arr.append(row)
#         mat = np.array(arr)
#         mat = np.delete(mat, np.where(mat.sum(axis=1) == 0), axis=0)
#         return True
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
#         )
# @router.post(
#     '/',
#     response_description='Crea un sistema.',
#     response_model=bool,
#     status_code=status.HTTP_201_CREATED,
#     response_model_by_alias=False,
# )
# async def create_system(
#     system: SystemSchema = Body(...),
#     # initial_state: str = '10000000000',
#     # tensor: UploadFile = File(...),
#     # sheet: str = Body(default=DEFFAULT_SHEET),
#     # sheet: str = DEFFAULT_SHEET,
#     # format: str = Body(default=DEFFAULT_FORMAT),
#     # format: str = DEFFAULT_FORMAT,
#     db: Session = Depends(get_sqlite),
# ):
#     return True
#     # if tensor.filename.endswith('.xlsx'):
#     #     # Read it, 'f' type is bytes
#     #     bit_chunk: bytes = await tensor.read()
#     #     xlsx: io.BytesIO = io.BytesIO(bit_chunk)
#     #     wb: op.Workbook = op.load_workbook(xlsx)
#     #     ws = wb[sheet]
#     #     format_options: dict[str, Callable] = {
#     #         S2S: lambda: print('S2S'),
#     #         S2C: lambda: print('S2C'),
#     #         S2P: lambda: print('S2P'),
#     #     }
#     #     format_options[format]()
#     #     # Call to format service
#     #     # Call to strategy
#     #     # arr: list[np.ndarray] = []
#     #     arr: list[float] = list()
#     #     for cells in ws.iter_rows():
#     #         arr.append([
#     #             cell.value
#     #             for cell in cells
#     #             if cell.value is not None
#     #         ])
#     #     mat = np.np.matrix(arr)
#     #     # Delete a row if it's sum is zero:
#     #     mat = np.delete(mat, np.where(mat.sum(axis=1) == 0), axis=0)
#     #     return True
#     # else:
#     #     raise HTTPException(
#     #         status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
#     #     )
#     return True
# @router.post('/system/', response_model=SystemSchema)
# def create_system(system: SystemSchema, db: Session = Depends(get_sqlite)):
#     sys_created: SystemSchema = post_sys(system, db)
#     if sys_created is None:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail=f'System {system.name} already exists'
#         )
#     return JSONResponse(
#         status_code=status.HTTP_201_CREATED,
#         content={'data': jsonable_encoder(sys_created)}
#     )
