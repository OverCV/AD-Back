from typing import TypedDict


class MipType(TypedDict):
    min_info_part: tuple[tuple[tuple[str], tuple[str]], tuple[tuple[str], tuple[str]]]
    integrated_info: float
    network: str | None
    distribution: list[float]
