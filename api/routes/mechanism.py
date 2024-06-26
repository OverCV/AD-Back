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
from api.models.props.mechanism import SysProps
from api.schemas.mechanism import MechanismRequest, MechanismResponse
from constants.mechanism import R4A, MECHANISMS
from data.motors import get_sqlite

from api.services.mechanism.service import (
    get_all,
    get_mechanism,
    delete_mechanism,
    post_mechanism,
)
from api.shared.formatter import Format

from constants.format import DEFFAULT_SHEET
from data.tables import MechanismTable
from utils.consts import DATA


router: APIRouter = APIRouter()


@router.post(
    '/',
    response_description='Crea un sistema.',
    status_code=status.HTTP_201_CREATED,
    response_model=MechanismResponse,
)
async def create_system(
    title: str = Form(default=MECHANISMS[R4A][SysProps.TITLE]),
    # istate: str = Form(default=SYSTEMS[R4A][SysProps.ISTATE]),
    format: str = Form(default=MECHANISMS[R4A][SysProps.FORMAT]),
    tensor: UploadFile = File(...),
    sheet: str = Form(default=DEFFAULT_SHEET),
    db: Session = Depends(get_sqlite),
):
    system_req: MechanismRequest = MechanismRequest(
        title=title, format=format
    )
    form: Format = Format(tensor, sheet, format)
    await form.set_array()
    new_system: MechanismResponse = post_mechanism(system_req, form, db)
    return JSONResponse(content={DATA: jsonable_encoder(new_system)})


@router.get(
    '/all',
    response_description='Obtiene todos los sistemas.',
    response_model=list[MechanismResponse],
    status_code=status.HTTP_200_OK,
)
async def all_systems(db: Session = Depends(get_sqlite)):
    systems: list[MechanismTable] = get_all(db)
    return JSONResponse(content={DATA: jsonable_encoder(systems)})


@router.get(
    '/{id}',
    response_description='Obtiene un sistema.',
    response_model=MechanismResponse,
    status_code=status.HTTP_200_OK,
)
async def get_system_by_id(id: int, db: Session = Depends(get_sqlite)):
    system: MechanismResponse = get_mechanism(id, db)
    return JSONResponse(content={DATA: jsonable_encoder(system)})


@router.delete(
    '/{id}',
    response_description='Elimina un sistema.',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_system_by_id(id: int, db: Session = Depends(get_sqlite)):
    system_removed: bool = delete_mechanism(id, db)
    if system_removed:
        return JSONResponse(
            status_code=status.HTTP_200_OK, content={'data': True}
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'System with id {id} not found.',
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
#     #     # arr: list[NDArray] = []
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
