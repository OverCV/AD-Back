# from fastapi import Body
from pydantic import BaseModel, ConfigDict, Field

from api.models.props.structure import StructProps
from api.schemas.genetic.control import ControlSchema
from constants.structure import (
    CONTROL_PARAMETERS,
    IS_DUAL,
    N1,
    N10,
    N15,
    N2,
    N3,
    N4,
    N5,
    N6,
    N7,
    N8,
    N9,
    SA,
    SAMPLES,
    SB,
    SHEET_NAME,
)
from utils.consts import EX_STR, SAMPLES_STR

indexed_samples = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10]

example_ctrl_schema = ControlSchema.model_config['json_schema_extra']['example']


class SampleRequest(BaseModel):
    ctrl_params: ControlSchema
    sheet: str = Field(SAMPLES[N15][SA][N1][SHEET_NAME], alias=SHEET_NAME)
    id: int | None = Field(None)
    title: str = Field(...)
    istate: str = Field(...)
    subsys: str = Field(...)
    effect: str = Field(...)
    actual: str = Field(...)
    dual: bool = Field(False, alias=IS_DUAL)

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            EX_STR: {
                CONTROL_PARAMETERS: example_ctrl_schema,
                SHEET_NAME: SAMPLES[N15][SA][N1][SHEET_NAME],
                StructProps.ID: SAMPLES[N15][SA][N1][StructProps.ID],
                StructProps.TITLE: SAMPLES[N15][SA][N1][StructProps.TITLE],
                StructProps.ISTATE: SAMPLES[N15][SA][N1][StructProps.ISTATE],
                StructProps.SUBSYS: SAMPLES[N15][SA][N1][StructProps.SUBSYS],
                StructProps.EFFECT: SAMPLES[N15][SA][N1][StructProps.EFFECT],
                StructProps.ACTUAL: SAMPLES[N15][SA][N1][StructProps.ACTUAL],
                IS_DUAL: SAMPLES[N15][SA][N1][IS_DUAL],
            }
        },
    )


class SampleCollection(BaseModel):
    samples: list[SampleRequest]

    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            EX_STR: {
                SAMPLES_STR: [
                    {
                        CONTROL_PARAMETERS: example_ctrl_schema,
                        SHEET_NAME: SAMPLES[N15][SB][N_i][SHEET_NAME],
                        StructProps.ID: SAMPLES[N15][SB][N_i][StructProps.ID],
                        StructProps.TITLE: SAMPLES[N15][SB][N_i][StructProps.TITLE],
                        StructProps.ISTATE: SAMPLES[N15][SB][N_i][StructProps.ISTATE],
                        StructProps.SUBSYS: SAMPLES[N15][SB][N_i][StructProps.SUBSYS],
                        StructProps.EFFECT: SAMPLES[N15][SB][N_i][StructProps.EFFECT],
                        StructProps.ACTUAL: SAMPLES[N15][SB][N_i][StructProps.ACTUAL],
                        IS_DUAL: SAMPLES[N15][SB][N_i][IS_DUAL],
                    }
                    for N_i in SAMPLES[N15][SB].keys()
                ],
            }
        },
    )


# class StructureResponse(SampleRequest):
#     id: int
#     tensor: str
#     size: int
