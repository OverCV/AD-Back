# from fastapi import Body
from pydantic import BaseModel, ConfigDict, Field

from api.schemas.genetic.control import ControlSchema
from utils.consts import EX_STR


class SampleRequest(BaseModel):
    ctrl_params: ControlSchema = Field(...)
    sheet: str = Field(...)
    id: int = Field(None)
    title: str = Field(...)
    istate: str = Field(...)
    subsys: str = Field(...)
    effect: str = Field(...)
    actual: str = Field(...)
    dual: bool = Field(False)
    # db_sql: Session = Depends(get_sqlite),
    # db_nosql: Session = Depends(get_mongo),

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            EX_STR: {
                ctrl_params: ControlSchema,
                sheet: 'Red 5 Nodos',
                id: None,
                title: 'System_Title',
                istate: '10001',
                subsys: '11100',
                effect: '11111',
                actual: '11111',
                dual: False,
            },
        },
    )


# class StructureResponse(SampleRequest):
#     id: int
#     tensor: str
#     size: int
