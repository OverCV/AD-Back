class VertexType:
    CUSTOM: str = 'custom'


class VertexPosProps:
    X: str = 'x'
    Y: str = 'y'
    Z: str = 'z'


class VertexDataProps:
    LBL: str = 'label'
    VALUE: str = 'value'
    COLOR: str = 'color'


class ArcDataProps:
    WEIGHT: str = 'weight'
    COLOR: str = 'color'


class ArcProps:
    ID: str = 'id'
    SRC: str = 'source'
    TGT: str = 'target'
    DATA: ArcDataProps = 'data'
    ANIMATED: str = 'animated'


class VertexProps:
    ID: str = 'id'
    POS: str = 'position'
    DATA: VertexDataProps = 'data'
    TYPE: str = 'type'
