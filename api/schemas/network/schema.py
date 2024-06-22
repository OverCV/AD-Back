from typing import Optional, List

from pydantic import ConfigDict, BaseModel, Field

from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

from api.schemas.network.vertex import Vertex
from api.schemas.network.arc import Arc
from api.schemas.network.info import Info
from api.schemas.network.samples import DEFFAULT_NETWORK_EXAMPLE


PyObjectId = Annotated[str, BeforeValidator(str)]


class NetworkSchema(BaseModel):
    '''
    Container for a single System record.
    '''

    # The primary key for the NetworkSchema, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    vertices: List[Vertex] = Field(...)
    arcs: List[Arc] = Field(...)
    info: Info = Field(...)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra=DEFFAULT_NETWORK_EXAMPLE
    )


class network_collection(BaseModel):
    """
    A container holding a list of `NetworkSchema` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    networks: List[NetworkSchema]
