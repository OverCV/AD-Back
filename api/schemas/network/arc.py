from typing import List
from pydantic import BaseModel, Field


class Arc(BaseModel):
    id: str = Field(...)
    source: str = Field(...)
    target: str = Field(...)
    data: dict = Field(...)
    animated: bool = Field(...)
    type: str = Field(...)


class arc_collection(BaseModel):
    """
    A container holding a list of `CreateEdge` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    arcs: List[Arc]
