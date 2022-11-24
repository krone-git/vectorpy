from .abc import VertexBodySingletonABC


__all__ = ("VertexBody",)

class VertexBody(ElementTypeABC, MutableVertexBodyType):
    __slots__ = ()

    def __init__(self, origin, basis, vertices):
        ElementTypeABC.__init__(self, origin, basis)
        MutableVertexBodyType.__init__(self, vertices)
