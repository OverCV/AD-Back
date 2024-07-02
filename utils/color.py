from functools import cache
from random import sample
from typing import Literal
from api.models.props import spectrum
from constants.colors import SPEC_REF, SPEC_TAGS


@cache
def get_color(
    tone: str,
    intensity: str,
    format: str = spectrum.FormatProp.RGB,
) -> (
    str
    | tuple[Literal[0], Literal[0], Literal[0]]
    | tuple[Literal[255], Literal[255], Literal[255]]
):
    if tone == spectrum.ColorProp.BLACK:
        return (0, 0, 0)
    elif tone == spectrum.ColorProp.WHITE:
        return (255, 255, 255)
    color = SPEC_TAGS[0].index(tone)
    intensity = SPEC_TAGS[1].index(intensity)
    spec = SPEC_REF[color][intensity]
    return spec if format == spectrum.FormatProp.RGB else '#' + ''.join(f'{i:02x}' for i in spec)
    # f'#{spec[0]:02x}{spec[1]:02x}{spec[2]:02x}'


def get_rnd_colors(times: int, format: str) -> tuple[int, int, int]:
    # Take a sample of `times` colors from the spectrum
    colors = sample(SPEC_TAGS[0], times)
    intensities = sample(SPEC_TAGS[1], times)
    specs = [get_color(c, i, format) for c, i in zip(colors, intensities)]
    return tuple(specs)
