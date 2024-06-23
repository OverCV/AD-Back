from fastapi import HTTPException


def has_valid_effect_causes(effect_len: int, causes_len: int, tensor_len: int) -> bool:
    if effect_len != causes_len:
        raise HTTPException('Effect and Causes should have the same length')

    if effect_len != tensor_len:
        raise HTTPException('Effect and Tensor should have the same length')

    return effect_len == causes_len == tensor_len
