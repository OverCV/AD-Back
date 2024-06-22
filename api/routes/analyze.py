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
from data.base import get_sqlite

from api.services.system.service import *

# from shared.log import Log
# import api.shared.logger as lg

from constants.format import (
    DEFAULT_FORMAT, DEFFAULT_SHEET, S2C, S2P, S2S
)
from utils.consts import DEFAULT_CAUSES, DEFAULT_ISTATE, DEFAULT_EFFECT, FLOAT_ZERO, ISTATE
from utils.funcs import cout, printnl

router: APIRouter = APIRouter()


@router.post(
    '/sia-zero/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante fuerza bruta.',
    response_model=bool,
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def strategy_zero(
    system_id: str,
    effect: str = Form(default=DEFAULT_EFFECT),
    causes: str = Form(default=DEFAULT_CAUSES),
    store_network: bool = False,
    db=Depends(get_sqlite)
):
    print('Hello math! - SIA Zero')
    system = get_system(system_id, db)

    # tensor = np.array(eval(system.tensor))

    tensor_str = system.tensor
    form: Format = Format()
    subtensor = form.deserialize_tensor(tensor_str)
    cout(type(subtensor))
    # cout(tensor.sum(axis=1))
    cout(subtensor)
    [
        cout(mat.sum(axis=1))
        for mat in subtensor
    ]
    # [
    #     cout(type(mat))
    #     for mat in tensor
    # ]
    return system is None
