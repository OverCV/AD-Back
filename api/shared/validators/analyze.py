from fastapi import HTTPException


def has_valid_inputs(
    istate: int, effect_len: int, causes_len: int, tensor_len: int
) -> bool:
    if effect_len != causes_len:
        raise HTTPException('Effect and Causes should have the same length')

    if istate != tensor_len:
        raise HTTPException(
            'Initial state and Tensor should have the same length'
        )

    if effect_len != tensor_len:
        raise HTTPException('Effect and Tensor should have the same length')

    return effect_len == causes_len == tensor_len
