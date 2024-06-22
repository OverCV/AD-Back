from typing import List
from pydantic import BaseModel

from api.schemas.network.schema import NetworkSchema


class NetworkCollection(BaseModel):
    """
    A container holding a list of `NetworkSchema` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    networks: List[NetworkSchema]
