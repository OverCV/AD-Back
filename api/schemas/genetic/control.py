from pydantic import BaseModel, ConfigDict, Field

from constants.genetic import (
    DECAY,
    CROSSED_IND,
    DEFAULT_PARAMS,
    CROSS_RATE,
    INIT_POP_SIZE,
    MAX_GENS,
    MAX_STREAK,
    MUTATE_RATE,
    PARENTS_NUM,
)
from utils.consts import EX_STR


class ControlSchema(BaseModel):
    xi: float = Field(...)
    r: float = Field(...)
    mu: float = Field(...)
    G: int = Field(...)

    decay: int = Field(...)
    parents_num: int = Field(...)
    crossed_ind: int = Field(...)
    max_streak: int = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            EX_STR: {
                CROSS_RATE: DEFAULT_PARAMS[CROSS_RATE],
                INIT_POP_SIZE: DEFAULT_PARAMS[INIT_POP_SIZE],
                MUTATE_RATE: DEFAULT_PARAMS[MUTATE_RATE],
                MAX_GENS: DEFAULT_PARAMS[MAX_GENS],
                DECAY: DEFAULT_PARAMS[DECAY],
                #
                PARENTS_NUM: DEFAULT_PARAMS[PARENTS_NUM],
                CROSSED_IND: DEFAULT_PARAMS[CROSSED_IND],
                MAX_STREAK: DEFAULT_PARAMS[MAX_STREAK],
            },
        },
    )
