import io
from logging import *

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


from server import conf
from utils.consts import DATA

router: APIRouter = APIRouter()


@router.post(
    '/',
    response_description='Cambiar las configuraciones del servidor.',
    response_model=bool,
    status_code=status.HTTP_202_ACCEPTED,
    response_model_by_alias=False,
)
async def configure_server(
    little_endian: bool = Form(default=conf.little_endian),
    store_networks: bool = Form(default=conf.store_nets),
    locale_nosql: bool = Form(default=conf.locale_nosql),
):
    # ! Read from table config to set the actual config ! #
    conf.use_le() if little_endian else conf.use_be()
    conf.do_store_nets() if store_networks else conf.dont_store_nets()
    conf.use_locale_nosql() if locale_nosql else conf.use_remote_nosql()

    using_le = 'Server notation has been set to little endian.' if little_endian \
        else 'The server notation has been set to big endian.'
    storing_nets = 'The server is storing networks.' if store_networks \
        else 'The server is not storing networks.'
    using_locale_nosql = 'The server is using a local NoSQL database.' if locale_nosql \
        else 'The server is using a remote NoSQL database.'

    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content=jsonable_encoder({
            DATA: [using_le, storing_nets, using_locale_nosql]
        })
    )


@router.get('/load-config')
async def load_config():
    await conf.load_config()
    return {'message': 'Config loaded successfully!'}
