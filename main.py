import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.middlewares.exception import ExceptionMiddleware
from api.middlewares.profiling import ProfilingMiddleware

from api.models.enums.frontend import NextJSPort
from api.models.enums.backend import ExecConfig

from data.motors import Base, engine

from api.routes import analyze, server, network, structure, metrics
from utils.consts import STR_ONE, STR_ZERO
from icecream import install

install()


""" Relational Database """

Base.metadata.create_all(bind=engine)
# ! Read config table from database and set to app params ! #

""" Main application """

app: FastAPI = FastAPI(
    title='Algorithms Project | Over V.',
    summary='Software development for the minimal information partition problem in the Analisis and Design of Algorithms course.',
    version='2.0.0',
)


NEXT_LOCALE_URL: str = os.environ.get(NextJSPort.NEXT_LOCALE_URL.value)

WITH_PROFILING: str = os.environ.get(ExecConfig.ENABLE_PROFILING.value, STR_ZERO)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[NEXT_LOCALE_URL],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_middleware(ExceptionMiddleware)
app.add_middleware(ProfilingMiddleware)


""" Routes """

app.include_router(server.router, prefix='/server', tags=['Server'])
app.include_router(network.router, prefix='/network', tags=['Networks'])
app.include_router(structure.router, prefix='/structure', tags=['Structures'])
app.include_router(analyze.router, prefix='/analyze', tags=['Analyze'])
app.include_router(metrics.router, prefix='/metrics', tags=['Metrics'])


""" Default routes """


@app.get('/')
async def root():
    return {'message': 'Hello algorithms!'}


@app.get('/error')
async def trigger_error():
    raise ValueError('This is a test error!')
