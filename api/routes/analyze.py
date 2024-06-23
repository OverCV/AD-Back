import io
from logging import *

from os import system
from typing import Annotated, Callable
import numpy as np
import openpyxl as op
from fastapi import Body, File, Form, HTTPException, Response, UploadFile, status, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import pandas as pd
from pydantic import Field
from sqlalchemy.orm import Session
from api.schemas.system import SystemRequest
from api.services.analyze.compute import Compute
from data.base import get_sqlite

from api.services.system.service import *

# from shared.log import Log
# import api.shared.logger as lg

from constants.format import (
    DEFAULT_FORMAT, DEFFAULT_SHEET, S2C, S2P, S2S
)
from utils.consts import DEFAULT_CAUSES, DEFAULT_ISTATE, DEFAULT_EFFECT, FLOAT_ZERO, ISTATE, TENSOR
from utils.funcs import cout, printnl

router: APIRouter = APIRouter()


@router.get(
    '/sia-genetic/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante fuerza bruta.',
    response_model=bool,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def genetic_strategy(
    system_id: str,
    effect: str = DEFAULT_EFFECT,
    causes: str = DEFAULT_CAUSES,
    # ! Should be a GLOBAL configuration
    store_network: bool = False,
    db=Depends(get_sqlite)
):
    print('Hello math! - SIA Zero')
    db_system = get_system(system_id, db)
    form: Format = Format()
    subtensor = form.deserialize_tensor(db_system.tensor)

    computing: Compute = Compute(db_system, effect, causes, subtensor)
    response = computing.use_genetic_algorithm()
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)
