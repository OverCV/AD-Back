from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import pandas as pd
import json

from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends

from api.models.props.structure import StructProps
from api.schemas.genetic.control import ControlSchema

# from api.schemas.sample import SampleRequest
from api.routes.analyze import (
    branch_strategy,
    force_strategy,
    genetic_strategy,
    pyphi_strategy,
)
from api.schemas.sample import SampleRequest
from data.motors import get_mongo, get_sqlite


from constants.metrics import (
    FORCE_ST,
    STORAGE_URL,
    UTF8_FORMAT,
    PYPHI_ST,
    BRANCH_ST,
    GENETIC_ST,
    SERVER_URL,
)
from constants.structure import IS_DUAL, N1, N3, N4, N5, N6, N7, SA, SAMPLES, SHEET_NAME
from utils.consts import DATA, SMALL_PHI

from server import conf
from icecream import ic


router: APIRouter = APIRouter()
executed_df: list[pd.DataFrame] = []


@router.post(
    '/all-strats/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante las distintas estrategias implementadas.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def all_strats(
    ctrl_parameters: ControlSchema,
    sheet: str = SAMPLES[N4][SA][N4][SHEET_NAME],
    id: int = SAMPLES[N4][SA][N4][StructProps.ID],
    title: str = SAMPLES[N4][SA][N4][StructProps.TITLE],
    istate: str = SAMPLES[N4][SA][N4][StructProps.ISTATE],
    subsys: str = SAMPLES[N4][SA][N4][StructProps.SUBSYS],
    effect: str = SAMPLES[N4][SA][N4][StructProps.EFFECT],
    actual: str = SAMPLES[N4][SA][N4][StructProps.ACTUAL],
    dual: bool = SAMPLES[N4][SA][N4][IS_DUAL],
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
    ic(ctrl_parameters)
    # ic()
    ic(sheet, id, title, istate, subsys, effect, actual, dual)

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

    # ic(loss_report_df, time_report_df)

    # Llamar a los otros endpoints y obtener los resultados
    # common_params = (id, title, istate, subsys, effect, actual, dual)
    common_params = {
        'id': id,
        'title': title,
        'istate': istate,
        'subsys': subsys,
        'effect': effect,
        'actual': actual,
        'dual': dual,
        'db_sql': db_sql,
        'db_nosql': db_nosql,
    }

    try:
        pyphi_response = await pyphi_strategy(**common_params)
        pyphi_results = pyphi_response.body.decode(UTF8_FORMAT)
        pyphi_data = json.loads(pyphi_results)[DATA]

        ic(pyphi_data)

        loss_report_df.at[LOSS_ROW_PYPHI, f'{subsys}=({effect}|{actual})'] = pyphi_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_PYPHI, f'{subsys}=({effect}|{actual})'] = conf.execution_times[
            'pyphi_strategy'
        ]
    except Exception as e:
        print('\nPyPhi failed', e, '\n')

    try:
        force_response = await force_strategy(**common_params)
        force_results = force_response.body.decode(UTF8_FORMAT)
        force_data = json.loads(force_results)[DATA]

        loss_report_df.at[LOSS_ROW_BFORCE, f'{subsys}=({effect}|{actual})'] = force_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_BFORCE, f'{subsys}=({effect}|{actual})'] = conf.execution_times[
            'force_strategy'  #! Obtenible del diccionario #!
        ]
    except Exception as e:
        print('\nForce failed', e, '\n')

    try:
        branch_response = await branch_strategy(**common_params)
        branch_results = branch_response.body.decode(UTF8_FORMAT)
        branch_data = json.loads(branch_results)[DATA]

        # ic(branch_data)
        loss_report_df.at[LOSS_ROW_BRANCH, f'{subsys}=({effect}|{actual})'] = branch_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_BRANCH, f'{subsys}=({effect}|{actual})'] = conf.execution_times[
            'branch_strategy'
        ]
    except Exception as e:
        print('\nBranch failed', e, '\n')

    try:
        # ! Mejorar la forma de pasar parámetros, luego volver función ! #

        genetic_response = await genetic_strategy(
            ctrl_params=ctrl_parameters,
            **common_params,
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

    ic(loss_report_df, time_report_df)

    combined_df = pd.concat(
        [
            loss_report_df,
            separator,
            time_report_df,
            separator,
        ]
    )

    ic(combined_df)
    combined_df.to_excel(STORAGE_URL, sheet_name=sheet)
    executed_df.append(combined_df)

    combined_dict = combined_df.to_json(orient='split')
    return JSONResponse(content={DATA: jsonable_encoder(combined_dict)})
    # return combined_df


# ! Asociar como servicio


@router.post(
    '/multiple-metrics/',
    response_description='Generación de reporte de múltiples subsistemas en una misma red.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def mutlple_metrics(
    samples: list[SampleRequest],
    sql_db: Session = Depends(get_sqlite),
    nosql_db: Session = Depends(get_mongo),
):
    merged_df = pd.DataFrame()
    # Pasamos como lista de objetos las estructuras samples de las redes ya guardadas.
    for sample in samples:
        # ic(sample)
        try:
            await all_strats(
                ctrl_parameters=sample.ctrl_params,
                sheet=sample.sheet,
                id=sample.id,
                title=sample.title,
                istate=sample.istate,
                subsys=sample.subsys,
                effect=sample.effect,
                actual=sample.actual,
                dual=sample.dual,
                db_sql=sql_db,
                db_nosql=nosql_db,
            )
        except Exception as e:
            print('Metric crashed the execution', e)

    # Unimos los resutados de executed_df en un solo DataFrame horizontalmente
    ic(executed_df)
    for df in executed_df:
        merged_df = pd.concat([merged_df, df], axis=1)
    ic(merged_df)
    # Guardamos el DataFrame en un archivo Excel
    merged_df.to_excel(STORAGE_URL, sheet_name='Multiple Metrics')

    # return combined_df


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


"""
2024-07-19 05:56:33,320 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2024-07-19 05:56:33,323 INFO sqlalchemy.engine.Engine SELECT structure.id AS structure_id, structure.title AS structure_title, structure.tensor AS structure_tensor, structure.size AS structure_size, structure.format AS 
structure_format 
FROM structure 
WHERE structure.title = ?
 LIMIT ? OFFSET ?
2024-07-19 05:56:33,323 INFO sqlalchemy.engine.Engine [generated in 0.00031s] ('R5A', 1, 0)
2024-07-19 05:56:33,324 INFO sqlalchemy.engine.Engine SELECT structure.id AS structure_id, structure.title AS structure_title, structure.tensor AS structure_tensor, structure.size AS structure_size, structure.format AS 
structure_format 
FROM structure 
WHERE structure.title = ?
 LIMIT ? OFFSET ?
2024-07-19 05:56:33,325 INFO sqlalchemy.engine.Engine [cached since 0.001756s ago] ('R5A', 1, 0)
ic| self.__str_bgcond: '11100', STR_ONE: '1', self.__dual: False
2024-07-19 05:56:33,759 INFO sqlalchemy.engine.Engine ROLLBACK
"""
