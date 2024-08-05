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
from api.schemas.sample import SampleCollection, SampleRequest
from data.motors import get_mongo, get_sqlite


from constants.metrics import (
    STORAGE_URL,
    UTF8_FORMAT,
    FORCE_ST,
    PYPHI_ST,
    BRANCH_ST,
    GENETIC_ST,
    SERVER_URL,
)
from constants.structure import IS_DUAL, N1, N15, N3, N4, N5, N6, N7, SA, SAMPLES, SHEET_NAME
from utils.consts import DATA, EMPTY_STR, MIP, SMALL_PHI, STR_ONE, STR_ZERO

from server import conf
from icecream import ic

from utils.funcs import get_labels


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
    sheet: str = SAMPLES[N15][SA][N1][SHEET_NAME],
    id: int = SAMPLES[N15][SA][N1][StructProps.ID],
    title: str = SAMPLES[N15][SA][N1][StructProps.TITLE],
    istate: str = SAMPLES[N15][SA][N1][StructProps.ISTATE],
    subsys: str = SAMPLES[N15][SA][N1][StructProps.SUBSYS],
    effect: str = SAMPLES[N15][SA][N1][StructProps.EFFECT],
    actual: str = SAMPLES[N15][SA][N1][StructProps.ACTUAL],
    dual: bool = SAMPLES[N15][SA][N1][IS_DUAL],
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

    print(subsys)
    all_labels = EMPTY_STR.join(get_labels(len(subsys)))

    effect_labels = EMPTY_STR.join(
        [
            s
            for bg, b, s in zip(
                subsys,
                effect,
                all_labels,
            )
            if (b == STR_ONE and bg == STR_ONE)
        ]
    )
    actual_labels = EMPTY_STR.join(
        [
            s
            for bg, b, s in zip(
                subsys,
                actual,
                all_labels,
            )
            if (b == STR_ONE and bg == STR_ONE)
        ]
    )

    # ic(effect, effect_labels)
    # ic(actual, actual_labels)

    subsys_labels = EMPTY_STR
    for b, s in zip(subsys, all_labels):
        subsys_labels += s.lower() if b == STR_ZERO else s

    # ic(subsys_labels)
    # ic(f'{subsys_labels}=({effect_labels}|{actual_labels})')

    # return

    col_str = f'{subsys_labels}=({effect_labels}|{actual_labels})'
    report_columns = [col_str]

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

        # ic(pyphi_data)

        loss_report_df.at[LOSS_ROW_PYPHI, col_str] = pyphi_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_PYPHI, col_str] = conf.execution_times['pyphi_strategy']
    except Exception as e:
        print('\nPyPhi failed', e, '\n')
        # ! Improve the error handling ! #
        return JSONResponse(content={DATA: jsonable_encoder({f'error {e}'})})

    try:
        force_response = await force_strategy(**common_params)
        force_results = force_response.body.decode(UTF8_FORMAT)
        force_data = json.loads(force_results)[DATA]

        loss_report_df.at[LOSS_ROW_BFORCE, col_str] = force_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_BFORCE, col_str] = conf.execution_times[
            'force_strategy'  #! Obtenible del diccionario #!
        ]
    except Exception as e:
        print('\nForce failed', e, '\n')

    try:
        branch_response = await branch_strategy(**common_params)
        branch_results = branch_response.body.decode(UTF8_FORMAT)
        branch_data = json.loads(branch_results)[DATA]

        # ic(branch_data)
        loss_report_df.at[LOSS_ROW_BRANCH, col_str] = branch_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_BRANCH, col_str] = conf.execution_times['branch_strategy']
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

        loss_report_df.at[LOSS_ROW_GENETIC, col_str] = genetic_data[SMALL_PHI]
        time_report_df.at[TIME_ROW_GENETIC, col_str] = conf.execution_times['genetic_strategy']
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
async def multiple_metrics(
    cluster: SampleCollection,
    sql_db: Session = Depends(get_sqlite),
    nosql_db: Session = Depends(get_mongo),
):
    # Pasamos como lista de objetos las estructuras samples de las redes ya guardadas.
    merged_df = pd.DataFrame()
    net_samples = cluster.samples

    for sample in net_samples:
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


@router.get(
    '/all-istates-pyphi/',
    response_description='Generación de reporte para todas las redes con todos los estados iniciales.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def test_all_istates_pyphi(
    id: int = SAMPLES[N6][SA][N7][StructProps.ID],
    title: str = SAMPLES[N6][SA][N7][StructProps.TITLE],
    # istate: str = SAMPLES[N6][SA][N7][StructProps.ISTATE],
    subsys: str = SAMPLES[N6][SA][N7][StructProps.SUBSYS],
    effect: str = SAMPLES[N6][SA][N7][StructProps.EFFECT],
    actual: str = SAMPLES[N6][SA][N7][StructProps.ACTUAL],
    dual: bool = SAMPLES[N6][SA][N7][IS_DUAL],
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    # Generar las combinaciones del estado incial, pero es una perdida pasar todos los estados si al final se seleccionan sólo ciertos indices del estado... La función por defecto recibe el estado complete, but si is selected om a sécofoc dp,aom. tjem ot doesn't matter to iterate all the other states, case:

    """
    R5A

    subsys: 11100
    subsys: 10011

    effect: 11111
    actual: 11111

        istate0: 00000
        istate1: 00001
        istate2: 00010
        istate3: 00011
        ...
        istate31: 11111

    As we can see here until it reaches the third significant bit, istate 0 to 3 are the same and all the iterations over the bits index -1 and -2.
    Then we only iterate len of subsys as dual times, those values then are selectivly assigned in the string and passed for testing.

    But actually it matters, because those unused values are the BG-Conds...

    """

    # letters = get_labels(26)

    # for let_a, let_f in zip(letters[:-1], letters[1:]):
    #     print(let_a, let_f)

    # # for i in letters:
    # #     print(f'{i}XR-79E')
    # return

    num_nodes = len(subsys)

    common_params = {
        'id': id,
        'title': title,
        # 'istate': istate,
        'subsys': subsys,
        'effect': effect,
        'actual': actual,
        'dual': dual,
        'db_sql': db_sql,
        'db_nosql': db_nosql,
    }

    results = []

    for idx in range(2**num_nodes):
        istate = format(idx, f'0{num_nodes}b')
        ic(istate)
        common_params['istate'] = istate

        try:
            pyphi_response = await pyphi_strategy(**common_params)
            pyphi_results = pyphi_response.body.decode(UTF8_FORMAT)
            pyphi_data = json.loads(pyphi_results)[DATA]

            results.append(
                {
                    SMALL_PHI: pyphi_data[SMALL_PHI],
                    MIP: pyphi_data[MIP],
                }
            )

            ic(pyphi_data)

        except Exception as e:
            print('\nPyPhi failed', e, '\n')
            return

    ic(results)


# cond: bool = False

# if cond:
#     raise HTTPException(
#         status_code=500,
#         detail='One or more of the SIA properties are not calculated',
#     )
# results = {}
# return JSONResponse(content=jsonable_encoder(results), status_code=status.HTTP_200_OK)
