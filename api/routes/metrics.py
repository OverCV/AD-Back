from typing import Any
from fastapi import HTTPException, status, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import requests as req


import pandas as pd
from sqlalchemy.orm import Session

from api.models.props.structure import StructProps
from api.routes.analyze import force_strategy, pyphi_strategy
from constants.metrics import FORCE_ST, PYPHI_ST, BRANCH_ST, GENETIC_ST, SERVER_URL
from constants.structure import R5A, STRUCTURES
from data.motors import get_mongo, get_sqlite

from icecream import ic

router: APIRouter = APIRouter()


@router.post(
    '/all-strats/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante PyPhi.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def all_strats(
    title: str = STRUCTURES[R5A][StructProps.TITLE],
    istate: str = STRUCTURES[R5A][StructProps.ISTATE],
    subsys: str = STRUCTURES[R5A][StructProps.SUBSYS],
    effect: str = STRUCTURES[R5A][StructProps.EFFECT],
    actual: str = STRUCTURES[R5A][StructProps.ACTUAL],
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    # Llamar a los otros endpoints y obtener los resultados
    pyphi_results = await pyphi_strategy(
        title=title,
        istate=istate,
        subsys=subsys,
        effect=effect,
        actual=actual,
        db_sql=db_sql,
        db_nosql=db_nosql,
    )
    force_results = await force_strategy(db_sql=db_sql, db_nosql=db_nosql)

    report_data = {
        'Estrategia': ['PyPhi', 'Fuerza Bruta'],
        'Resultado': [pyphi_results, force_results],
    }
    report_df = pd.DataFrame(report_data)
    report_df.to_excel('reporte_metricas.xlsx', index=False)
    ic(report_df)
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


def query_params(
    title: str,
    istate: str,
    subsys: str,
    effect: str,
    actual: str,
    dual: bool,
) -> str:
    # return 'title=R5A&istate=10001&subsys=11100&effect=11111&actual=11111&dual=false'
    return (
        f'title={title}&istate={istate}&subsys={subsys}&effect={effect}&actual={actual}&dual={dual}'
    )


def generate_excel(metrics_data: dict[str, dict[str, Any]]) -> str:
    # Aquí generas tu archivo Excel usando pandas u otra librería
    # Por ejemplo, crear un DataFrame con los datos y luego guardar a Excel
    df = pd.DataFrame(metrics_data).T
    excel_filename = '/path/to/compare_metrics.xlsx'  # Ruta donde guardar el archivo
    df.to_excel(excel_filename, index=False)
    return excel_filename


# cond: bool = False

# if cond:
#     raise HTTPException(
#         status_code=500,
#         detail='One or more of the SIA properties are not calculated',
#     )
# results = {}
# return JSONResponse(content=jsonable_encoder(results), status_code=status.HTTP_200_OK)
