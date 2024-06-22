import os
import server
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.middlewares.exception import ExceptionMiddleware
from api.models.enums.frontend import NextJSPort

from data.base import Base, engine

from api.routes import (
    analyze, server, system, network
)


''' Relational Database '''

Base.metadata.create_all(bind=engine)

''' Main application '''

app: FastAPI = FastAPI(
    title='Algorithms Project | Over V.',
    summary='The development of the partitioning problem for the Analisis and Design of Algorithms course.',
    version='1.0.4',
)


NEXT_LOCALE_URL: str = os.environ.get(NextJSPort.NEXT_LOCALE_URL.value)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[NEXT_LOCALE_URL], allow_credentials=True,
    allow_methods=['*'], allow_headers=['*']
)
app.add_middleware(ExceptionMiddleware)

''' Routes '''

app.include_router(server.router, tags=['Server'], prefix='/server')
app.include_router(network.router, tags=['Networks'], prefix='/network')
app.include_router(system.router, tags=['Systems'], prefix='/system')
app.include_router(analyze.router, tags=['Analyze'], prefix='/analyze')

''' Default routes '''


@app.get('/')
async def root():
    return {'message': 'Hello algorithms!'}


@app.get('/error')
async def trigger_error():
    raise ValueError('This is a test error!')
