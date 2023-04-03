from .abc import MutableVertexBodyType
from ..element.abc import BaseElementABC


__all__ = ("VertexBody",)

class VertexBody(BaseElementABC, MutableVertexBodyType):
    __slots__ = ()

    def __init__(self, origin, basis, vertices):
        ElementTypeABC.__init__(self, origin, basis)
        MutableVertexBodyType.__init__(self, vertices)
