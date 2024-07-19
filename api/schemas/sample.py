# from fastapi import Body
from pydantic import BaseModel, ConfigDict, Field

from api.models.props.structure import StructProps
from api.schemas.genetic.control import ControlSchema
from constants.structure import (
    CONTROL_PARAMETERS,
    IS_DUAL,
    N5,
    N7,
    SA,
    SAMPLES,
    SHEET_NAME,
)
from utils.consts import EX_STR


class SampleRequest(BaseModel):
    ctrl_params: ControlSchema
    sheet: str = Field(SAMPLES[N5][SA][N7][SHEET_NAME], alias=SHEET_NAME)
    id: int | None = None
    title: str = ...
    istate: str = ...
    subsys: str = ...
    effect: str = ...
    actual: str = ...
    dual: bool = Field(False, alias=IS_DUAL)

    class Config:
        schema_extra = {
            EX_STR: {
                CONTROL_PARAMETERS: {
                    SHEET_NAME: SAMPLES[N5][SA][N7][SHEET_NAME],
                    StructProps.ID: SAMPLES[N5][SA][N7][StructProps.ID],
                    StructProps.TITLE: SAMPLES[N5][SA][N7][StructProps.TITLE],
                    StructProps.ISTATE: SAMPLES[N5][SA][N7][StructProps.ISTATE],
                    StructProps.SUBSYS: SAMPLES[N5][SA][N7][StructProps.SUBSYS],
                    StructProps.EFFECT: SAMPLES[N5][SA][N7][StructProps.EFFECT],
                    StructProps.ACTUAL: SAMPLES[N5][SA][N7][StructProps.ACTUAL],
                    IS_DUAL: SAMPLES[N5][SA][N7][IS_DUAL],
                }
            }
        }


# class StructureResponse(SampleRequest):
#     id: int
#     tensor: str
#     size: int
