from typing import List
from pydantic import BaseModel, Field


class Info(BaseModel):
    label: str = Field(...)
    is_complete: bool = Field(...)
    is_connected: bool = Field(...)
    is_weighted: bool = Field(...)
    is_directed: bool = Field(...)
    is_k_bipartite: bool = Field(...)
    k_degree: int = Field(...)


class info_collection(BaseModel):
    """
    A container holding a list of `SystemModel` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    knowledge: List[Info]
