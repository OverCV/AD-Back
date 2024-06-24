import io
from logging import *

from fastapi import status, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from api.models.props.system import SysProps
from api.services.analyze.compute import Compute
from constants.system import R2A, R4A, R5A, SYSTEMS
from data.base import get_sqlite

from api.services.system.service import *

from utils.funcs import cout

router: APIRouter = APIRouter()


@router.get(
    '/sia-genetic/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante fuerza bruta.',
    response_model=bool,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def genetic_strategy(
    title:  str = SYSTEMS[R5A][SysProps.TITLE],
    istate: str = SYSTEMS[R5A][SysProps.ISTATE],
    effect: str = SYSTEMS[R5A][SysProps.EFFECT],
    causes: str = SYSTEMS[R5A][SysProps.CAUSES],
    # ! Should be a GLOBAL configuration
    store_network: bool = False,
    db=Depends(get_sqlite)
):
    db_system = get_system_by_title(title, db)
    form: Format = Format()
    subtensor = form.deserialize_tensor(db_system.tensor)

    computing: Compute = Compute(db_system, istate, effect, causes, subtensor)
    response = computing.use_genetic_algorithm()
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
