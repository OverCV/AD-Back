from typing import Optional
from fastapi import HTTPException, status, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import numpy as np
from numpy.typing import NDArray

from sqlalchemy.orm import Session
from api.schemas.genetic.control import ControlSchema
from api.shared.validators import analyze as av
from data.motors import get_mongo, get_sqlite

from api.models.props.structure import StructProps
from api.schemas.structure import StructureResponse
from api.services.analyze.compute import Compute
from api.shared.formatter import Format

from constants.structure import N1, N15, N5, N6, N7, SA, SAMPLES
from api.services.structure.base import (
    get_structure,
    get_structure_by_title,
)

from api.services.network import reconstruct_network
from icecream import ic

from utils.consts import DATA, MIP
from utils.funcs import temporizer


router: APIRouter = APIRouter()
fmt: Format = Format()


@temporizer
@router.get(
    '/sia-pyphi/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante PyPhi.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def pyphi_strategy(
    id: Optional[int] = None,
    title: str = SAMPLES[N15][SA][N1][StructProps.TITLE],
    istate: str = SAMPLES[N15][SA][N1][StructProps.ISTATE],
    subsys: str = SAMPLES[N15][SA][N1][StructProps.SUBSYS],
    effect: str = SAMPLES[N15][SA][N1][StructProps.EFFECT],
    actual: str = SAMPLES[N15][SA][N1][StructProps.ACTUAL],
    dual: bool = False,
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    struct_response: StructureResponse = (
        get_structure_by_title(title, db_sql) if id is None else get_structure(id, db_sql)
    )
    subtensor: NDArray[np.float64] = fmt.deserialize_tensor(struct_response.tensor)
    av.has_valid_inputs(istate, effect, actual, subsys, len(subtensor))
    computing: Compute = Compute(struct_response, istate, effect, actual, subsys, subtensor, dual)

    results = computing.use_pyphi()
    # ic(results)
    return JSONResponse(content={DATA: jsonable_encoder(results)}, status_code=status.HTTP_200_OK)


@temporizer
@router.get(
    '/sia-force/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante fuerza bruta.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def force_strategy(
    # ! Add the optional parameter to select struct by id
    id: Optional[int] = None,
    title: str = SAMPLES[N6][SA][N7][StructProps.TITLE],
    istate: str = SAMPLES[N6][SA][N7][StructProps.ISTATE],
    subsys: str = SAMPLES[N6][SA][N7][StructProps.SUBSYS],
    effect: str = SAMPLES[N6][SA][N7][StructProps.EFFECT],
    actual: str = SAMPLES[N6][SA][N7][StructProps.ACTUAL],
    dual: bool = False,
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    struct_response: StructureResponse = (
        get_structure_by_title(title, db_sql) if id is None else get_structure(id, db_sql)
    )
    subtensor: NDArray[np.float64] = fmt.deserialize_tensor(struct_response.tensor)
    av.has_valid_inputs(istate, effect, actual, subsys, len(subtensor))
    computing: Compute = Compute(struct_response, istate, effect, actual, subsys, subtensor, dual)
    # ! Change to init bg conditions
    # if not computing.init_concept():
    if not computing.init_concept():
        raise HTTPException(
            status_code=500,
            detail='One or more of the SIA properties are not calculated',
        )
    results = computing.use_brute_force()

    # reconstruct_network(results[MIP], db_nosql)
    # ic(results)
    return JSONResponse(content={DATA: jsonable_encoder(results)}, status_code=status.HTTP_200_OK)


@temporizer
@router.get(
    '/sia-mst/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante árbol de expansión mínima.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def mst_strategy(
    id: Optional[int] = None,
    title: str = SAMPLES[N5][SA][N1][StructProps.TITLE],
    istate: str = SAMPLES[N5][SA][N1][StructProps.ISTATE],
    subsys: str = SAMPLES[N5][SA][N1][StructProps.SUBSYS],
    effect: str = SAMPLES[N5][SA][N1][StructProps.EFFECT],
    actual: str = SAMPLES[N5][SA][N1][StructProps.ACTUAL],
    dual: bool = False,
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    """
    `codigo de error 508` - No implementado aún
    """
    # raise HTTPException(status_code=508, detail='Not implemented yet')
    struct_response: StructureResponse = (
        get_structure_by_title(title, db_sql) if id is None else get_structure(id, db_sql)
    )
    subtensor: NDArray[np.float64] = fmt.deserialize_tensor(struct_response.tensor)
    av.has_valid_inputs(istate, effect, actual, subsys, len(subtensor))
    computing: Compute = Compute(struct_response, istate, effect, actual, subsys, subtensor, dual)
    if not computing.init_concept():
        raise HTTPException(
            status_code=500,
            detail='One or more of the SIA properties are not calculated',
        )
    results = computing.use_min_span_tree()

    reconstruct_network(results[MIP], db_nosql)
    return JSONResponse(content={DATA: jsonable_encoder(results)}, status_code=status.HTTP_200_OK)


@temporizer
@router.get(
    '/sia-branch/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante ramificación y poda.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def branch_strategy(
    # ! Add the optional parameter to select struct by id
    id: Optional[int] = None,
    title: str = SAMPLES[N6][SA][N7][StructProps.TITLE],
    istate: str = SAMPLES[N6][SA][N7][StructProps.ISTATE],
    subsys: str = SAMPLES[N6][SA][N7][StructProps.SUBSYS],
    effect: str = SAMPLES[N6][SA][N7][StructProps.EFFECT],
    actual: str = SAMPLES[N6][SA][N7][StructProps.ACTUAL],
    dual: bool = False,
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    ic(istate, subsys, effect, actual)
    struct_response: StructureResponse = (
        get_structure_by_title(title, db_sql) if id is None else get_structure(id, db_sql)
    )
    subtensor: NDArray[np.float64] = fmt.deserialize_tensor(struct_response.tensor)
    av.has_valid_inputs(istate, effect, actual, subsys, len(subtensor))
    computing: Compute = Compute(struct_response, istate, effect, actual, subsys, subtensor, dual)
    if not computing.init_concept():
        raise HTTPException(
            status_code=500,
            detail='One or more of the SIA properties are not calculated',
        )
    results = computing.use_branch_and_bound()

    reconstruct_network(results[MIP], db_nosql)
    return JSONResponse(content={DATA: jsonable_encoder(results)}, status_code=status.HTTP_200_OK)


@temporizer
@router.post(
    '/sia-genetic/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante un Algoritmo Genético.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def genetic_strategy(
    ctrl_params: ControlSchema,
    id: Optional[int] = None,
    title: str = SAMPLES[N6][SA][N7][StructProps.TITLE],
    istate: str = SAMPLES[N6][SA][N7][StructProps.ISTATE],
    subsys: str = SAMPLES[N6][SA][N7][StructProps.SUBSYS],
    effect: str = SAMPLES[N6][SA][N7][StructProps.EFFECT],
    actual: str = SAMPLES[N6][SA][N7][StructProps.ACTUAL],
    dual: bool = False,
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    ic(ctrl_params, id, title)
    struct_response: StructureResponse = (
        get_structure_by_title(title, db_sql) if id is None else get_structure(id, db_sql)
    )
    subtensor: NDArray[np.float64] = fmt.deserialize_tensor(struct_response.tensor)
    av.has_valid_inputs(istate, effect, actual, subsys, len(subtensor))
    computing: Compute = Compute(struct_response, istate, effect, actual, subsys, subtensor, dual)
    if not computing.init_concept():
        raise HTTPException(
            status_code=500,
            detail='One or more of the SIA properties are not calculated',
        )
    results = computing.use_genetic_algorithm([ctrl_params.model_dump()])
    ic(results)
    reconstruct_network(results[MIP], db_nosql)
    return JSONResponse(content={DATA: jsonable_encoder(results)}, status_code=status.HTTP_200_OK)


@router.get(
    '/sia-testing/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante un Algoritmo Genético.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def sia_testing():
    raise HTTPException(status_code=508, detail='Not implemented yet')


# struct_res: StructureResponse = get_structure_by_title(title, db)
# subtensor: NDArray[np.float64] = fmt.deserialize_tensor(struct_res.tensor)
# av.has_valid_inputs(istate, effect, actual, len(subtensor))
# # ic(type(subtensor))
# computing: Compute = Compute(struct_res, istate, effect, actual, subtensor, dual)
# results = computing.use_genetic_algorithm()
# return JSONResponse(content=jsonable_encoder(results), status_code=status.HTTP_200_OK)


# @router.get(
#     '/sia-pyphi/',
#     response_description='Hallar la partición con menor pérdida de información, acercamiento mediante PyPhi.',
#     status_code=status.HTTP_200_OK,
#     response_model_by_alias=False,
# )
# async def pyphi_strategy(
#     title:  str = SYSTEMS[R10A][SysProps.TITLE],
#     istate: str = SYSTEMS[R10A][SysProps.ISTATE],
#     effect: str = SYSTEMS[R10A][SysProps.EFFECT],
#     actual: str = SYSTEMS[R10A][SysProps.CAUSES],
#     # ! Should be a GLOBAL configuration
#     store_network: bool = False,
#     db=Depends(get_sqlite)
# ):
#     db_system = get_system_by_title(title, db)
#     form: Format = Format()
#     subtensor = form.deserialize_tensor(db_system.tensor)

#     computing: Compute = Compute(db_system, istate, effect, actual, subtensor)
#     results = computing.use_pyphi()
#     return JSONResponse(content=jsonable_encoder(results), status_code=status.HTTP_200_OK)
