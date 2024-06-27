from pydantic import BaseModel


class StructureRequest(BaseModel):
    title: str
    format: str


class StructureResponse(StructureRequest):
    id: int
    tensor: str
    size: int

    # @field_validator('tensor', mode='before')
    # def convert_tensor_to_string(cls, v):
    #     if isinstance(v, np.matrix):
    #         return np.array_str(v)
    #     return v
