from typing import Any
from fastapi import HTTPException, requests, status, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


import pandas as pd
from sqlalchemy.orm import Session

from constants.metrics import BRANCH_ST, FORCE_ST, GENETIC_ST, PYPHI_ST
from data.motors import get_mongo, get_sqlite

router: APIRouter = APIRouter()


@router.get(
    '/all-strats/',
    response_description='Hallar la partición con menor pérdida de información, acercamiento mediante PyPhi.',
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def pyphi_strategy(
    db_sql: Session = Depends(get_sqlite),
    db_nosql: Session = Depends(get_mongo),
):
    strategies = [PYPHI_ST, FORCE_ST]  # , BRANCH_ST, GENETIC_ST
    metrics_data: dict[str, dict[str, Any]] = dict()
    for strategy in strategies:
        try:
            response = requests.get(f'/{strategy}/')
            response.raise_for_status()
            metrics_data[strategy] = response.json()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f'Error fetching {strategy} metrics: {str(e)}'
            )

    # Generar el Excel
    excel_file = generate_excel(metrics_data)
    return {'message': 'Comparison completed', 'excel_file': excel_file}

    cond: bool = False

    if cond:
        raise HTTPException(
            status_code=500,
            detail='One or more of the SIA properties are not calculated',
        )
    results = {}
    return JSONResponse(content=jsonable_encoder(results), status_code=status.HTTP_200_OK)


def generate_excel(metrics_data: dict[str, dict[str, Any]]) -> str:
    # Aquí generas tu archivo Excel usando pandas u otra librería
    # Por ejemplo, crear un DataFrame con los datos y luego guardar a Excel
    df = pd.DataFrame(metrics_data)
    excel_filename = '/path/to/compare_metrics.xlsx'  # Ruta donde guardar el archivo
    df.to_excel(excel_filename, index=False)
    return excel_filename
