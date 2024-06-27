import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.middlewares.exception import ExceptionMiddleware
from api.models.enums.frontend import NextJSPort

from data.motors import Base, engine

from api.routes import analyze, server, network, structure


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[NEXT_LOCALE_URL],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_middleware(ExceptionMiddleware)

""" Routes """

app.include_router(server.router, tags=['Server'], prefix='/server')
app.include_router(network.router, tags=['Networks'], prefix='/network')
app.include_router(structure.router, tags=['Structures'], prefix='/structure')
app.include_router(analyze.router, tags=['Analyze'], prefix='/analyze')

""" Default routes """


@app.get('/')
async def root():
    return {'message': 'Hello algorithms!'}


@app.get('/error')
async def trigger_error():
    raise ValueError('This is a test error!')
