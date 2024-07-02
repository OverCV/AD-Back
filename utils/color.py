from functools import cache
from typing import Literal
from api.models.props import spectrum
from constants.colors import SPEC_REF, SPEC_TAGS


@cache
def get_color(
    tone: spectrum.ColorProp,
    intensity: spectrum.IntensityProp,
    format: spectrum.FormatProp = spectrum.FormatProp.RGB,
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
    return (
        SPEC_REF[color][intensity]
        if format == spectrum.FormatProp.RGB
        else f'#{SPEC_REF[color][intensity]:02x}'
    )
