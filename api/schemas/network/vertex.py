from typing import List
from pydantic import BaseModel, Field


class Vertex(BaseModel):
    id: str = Field(...)
    data: dict = Field(...)
    position: dict = Field(...)
    type: str = Field(...)


class vertex_collection(BaseModel):
    """
    A container holding a list of `CreateNode` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    vertices: List[Vertex]
