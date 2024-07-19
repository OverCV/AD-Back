import re
from fastapi import HTTPException

from icecream import ic


def has_valid_inputs(istate: str, effect: str, actual: str, bgconds: str, tensor_len: int) -> bool:
    # Check with a reg exp if is a binary string
    # ic(istate, effect, actual, tensor_len)
    binary_pattern = r'^[01]+$'
    if not all(
        [
            re.match(binary_pattern, istate),
            re.match(binary_pattern, effect),
            re.match(binary_pattern, actual),
        ]
    ):
        raise HTTPException('Initial state should be a binary string')

    # ! Validate the bg-condition ! #

    # ! Validate the non-sense of giving an empty future or the actual [#10] ! #

    if len(effect) != len(actual):
        raise HTTPException('Effect and Actual should have the same length')

    if len(istate) != tensor_len:
        raise HTTPException('Initial state and Tensor should have the same length')

    if len(effect) != tensor_len:
        raise HTTPException('Effect and Tensor should have the same length')

    return len(effect) == len(actual) == tensor_len
