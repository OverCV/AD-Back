import re
from fastapi import HTTPException

from icecream import ic

from utils.consts import INT_ZERO


def has_valid_inputs(istate: str, effect: str, causes: str, tensor_len: int) -> bool:
    # Check with a reg exp if is a binary string
    ic(istate, effect, causes, tensor_len)
    binary_pattern = r'^[01]+$'
    if not all(
        [
            re.match(binary_pattern, istate),
            re.match(binary_pattern, effect),
            re.match(binary_pattern, causes),
        ]
    ):
        raise HTTPException('Initial state should be a binary string')

    # ! Validate the no-sense of giving empty the future or the causes [#10] ! #
    
    if len(effect) != len(causes):
        raise HTTPException('Effect and Causes should have the same length')

    if len(istate) != tensor_len:
        raise HTTPException('Initial state and Tensor should have the same length')

    if len(effect) != tensor_len:
        raise HTTPException('Effect and Tensor should have the same length')

    return len(effect) == len(causes) == tensor_len
