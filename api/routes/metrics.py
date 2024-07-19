from collections import OrderedDict
from typing import Any
from fastapi import HTTPException, status, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import json

import pandas as pd
from sqlalchemy.orm import Session

from api.models.props.structure import StructProps
from api.routes.analyze import branch_strategy, force_strategy, genetic_strategy, pyphi_strategy
from api.schemas.genetic.control import ControlSchema
from constants.metrics import FORCE_ST, UTF8_FORMAT, PYPHI_ST, BRANCH_ST, GENETIC_ST, SERVER_URL
from constants.structure import R5A, STRUCTURES
from data.motors import get_mongo, get_sqlite


from utils.consts import DATA, SMALL_PHI

from server import conf
from icecream import ic


router: APIRouter = APIRouter()


@router.post(
    '/all-strats/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante PyPhi.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def all_strats(
    ctrl_parameters: ControlSchema,
    sheet: str = 'Red N Nodos',
    id: int = None,
    title: str = STRUCTURES[R5A][StructProps.TITLE],
    istate: str = STRUCTURES[R5A][StructProps.ISTATE],
    subsys: str = STRUCTURES[R5A][StructProps.SUBSYS],
    effect: str = STRUCTURES[R5A][StructProps.EFFECT],
    actual: str = STRUCTURES[R5A][StructProps.ACTUAL],
    dual: bool = False,
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    # ! Permitir seleccionar cuáles quiere ver? ! #
    # strategies = OrderedDict(
    #     (
    #         ('PyPhi', pyphi_strategy),
    #         ('Fuerza Brutal', force_strategy),
    #         ('Ramificación', branch_strategy),
    #         ('Genetico', genetic_strategy),
    #     )
    # )

    # ic(strategies.keys(), strategies.values())

    LOSS_ROW_PYPHI = f'{SMALL_PHI} PyPhi'
    TIME_ROW_PYPHI = '(ms) PyPhi'

    LOSS_ROW_BFORCE = f'{SMALL_PHI} Fuerza Brutal'
    TIME_ROW_BFORCE = '(ms) Fuerza Brutal'

    LOSS_ROW_BRANCH = f'{SMALL_PHI} Ramificación'
    TIME_ROW_BRANCH = '(ms) Ramificación'

    LOSS_ROW_GENETIC = f'{SMALL_PHI} Genético'
    TIME_ROW_GENETIC = '(ms) Genético'

    loss_rows = [LOSS_ROW_PYPHI, LOSS_ROW_BFORCE]
    time_rows = [TIME_ROW_PYPHI, TIME_ROW_BFORCE]

    # ! Formatear mejor ! #
    report_columns = [f'{subsys}=({effect}|{actual})']

    loss_report_df = pd.DataFrame(index=loss_rows, columns=report_columns)
    time_report_df = pd.DataFrame(index=time_rows, columns=report_columns)

    ic(loss_report_df, time_report_df)

    # Llamar a los otros endpoints y obtener los resultados
    common_params = (id, title, istate, subsys, effect, actual, dual)

    try:
        pyphi_response = await pyphi_strategy(*common_params, db_sql=db_sql, db_nosql=db_nosql)
        pyphi_results = pyphi_response.body.decode(UTF8_FORMAT)
        pyphi_data = json.loads(pyphi_results)[DATA]

        # ic(conf.execution_times.keys())

        loss_report_df.at[LOSS_ROW_PYPHI, f'{subsys}=({effect}|{actual})'] = pyphi_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_PYPHI, f'{subsys}=({effect}|{actual})'] = conf.execution_times[
            'pyphi_strategy'
        ]

        # ic(brutal_data[SMALL_PHI], brutal_data)
        # force_response = await force_strategy(*tuple_parameters, db_sql=db_sql, db_nosql=db_nosql)
    except Exception as e:
        print('PyPhi failed', e)

    try:
        force_response = await force_strategy(*common_params, db_sql=db_sql, db_nosql=db_nosql)
        force_results = force_response.body.decode(UTF8_FORMAT)
        force_data = json.loads(force_results)[DATA]

        loss_report_df.at[LOSS_ROW_BFORCE, f'{subsys}=({effect}|{actual})'] = force_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_BFORCE, f'{subsys}=({effect}|{actual})'] = conf.execution_times[
            'force_strategy'  #! Obtenible del diccionario #!
        ]
    except Exception as e:
        print('Force failed', e)

    try:
        branch_response = await branch_strategy(*common_params, db_sql=db_sql, db_nosql=db_nosql)
        branch_results = branch_response.body.decode(UTF8_FORMAT)
        branch_data = json.loads(branch_results)[DATA]

        ic(branch_data)
        loss_report_df.at[LOSS_ROW_BRANCH, f'{subsys}=({effect}|{actual})'] = branch_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_BRANCH, f'{subsys}=({effect}|{actual})'] = conf.execution_times[
            'branch_strategy'
        ]
    except Exception as e:
        print('Branch failed', e)

    try:
        # genetic_params = {
        #     'ctrl_params': ctrl_parameters,
        #     **common_params,
        #     'db_sql': db_sql,
        #     'db_nosql': db_nosql,
        # }
        genetic_response = await genetic_strategy(
            ctrl_params=ctrl_parameters,
            #
            id=id,
            title=title,
            istate=istate,
            subsys=subsys,
            effect=effect,
            actual=actual,
            dual=dual,
            #
            db_sql=db_sql,
            db_nosql=db_nosql,
        )
        genetic_results = genetic_response.body.decode(UTF8_FORMAT)
        genetic_data = json.loads(genetic_results)[DATA]

        loss_report_df.at[LOSS_ROW_GENETIC, f'{subsys}=({effect}|{actual})'] = genetic_data[
            SMALL_PHI
        ]
        time_report_df.at[TIME_ROW_GENETIC, f'{subsys}=({effect}|{actual})'] = conf.execution_times[
            'genetic_strategy'
        ]
    except Exception as e:
        print('\nGenetic failed', e, '\n')

    separator = pd.DataFrame(
        [{col: '═━━━━━═' for col in loss_report_df.columns}],
        index=['═━━━━━═'],
    )

    combined_df = pd.concat(
        [
            loss_report_df,
            separator,
            time_report_df,
        ],
    )

    ic(combined_df)
    combined_df.to_excel(
        'data/reports/reporte_metricas.xlsx',
        sheet_name=sheet,
    )

    return {'message': 'Reporte generado exitosamente'}

    # force_results = await force_strategy(db_sql=db_sql, db_nosql=db_nosql)
    # branch_results = await branch_strategy(db_sql=db_sql, db_nosql=db_nosql)
    # genetic_results = await genetic_strategy(ctrl_params, db_sql=db_sql, db_nosql=db_nosql)
    # strategies = [PYPHI_ST, FORCE_ST]  # BRANCH_ST, GENETIC_ST #
    # metrics_data: dict[str, dict[str, Any]] = dict()
    # for strategy in strategies:
    #     try:
    #         request_url = f'{SERVER_URL}/{strategy}/{query_params(
    #             title=STRUCTURES[R5A][StructProps.TITLE],
    #             istate=STRUCTURES[R5A][StructProps.ISTATE],
    #             subsys=STRUCTURES[R5A][StructProps.SUBSYS],
    #             effect=STRUCTURES[R5A][StructProps.EFFECT],
    #             actual=STRUCTURES[R5A][StructProps.ACTUAL],
    #             dual=False,
    #         )}'
    #         ic(request_url)
    #         response = req.get(request_url)
    #         response.raise_for_status()
    #         metrics_data[strategy] = response.json()
    #     except Exception as e:
    #         raise HTTPException(
    #             status_code=500, detail=f'Error fetching {strategy} metrics: {str(e)}'
    #         )

    # Generar el Excel
    # excel_file = generate_excel(metrics_data)
    # return {'message': 'Comparison completed', 'excel_file': excel_file}


# ! Asociar como servicio


@router.get(
    '/multiple-metrics/',
    response_description='Generación de reporte de múltiples subsistemas en una misma red.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
def mutlple_metric():
    # ! pasar como lista de objetos! Las estructuras de las redes ya guardadas!
    pass


@router.get(
    '/multiple-subsystems/',
    response_description='Generación de reporte para varias rededs con un mismo subsistema.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
def mutlple_subsystems():
    pass


# cond: bool = False

# if cond:
#     raise HTTPException(
#         status_code=500,
#         detail='One or more of the SIA properties are not calculated',
#     )
# results = {}
# return JSONResponse(content=jsonable_encoder(results), status_code=status.HTTP_200_OK)
