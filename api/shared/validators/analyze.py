
from httpx import HTTPError
from sqlalchemy import true
from data.tables import SystemTable
from utils.funcs import printnl


def has_valid_effect_causes(effect_len: int, causes_len: int, tensor_len: int) -> bool:
    if effect_len != causes_len:
        raise HTTPError('Effect and Causes should have the same length')

    if effect_len != tensor_len:
        raise HTTPError('Effect and Tensor should have the same length')

    return effect_len == causes_len == tensor_len
