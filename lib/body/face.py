from .abc import MutableFaceBodyType
from ..element.abc import BaseElementABC


__all__ = ("FaceBody",)

class FaceBody(BaseElementABC, MutableFaceBodyType):
    __slots__ = ()

    def __init__(self, origin, basis, faces):
        ElementTypeABC.__init__(self, origin, basis)
        MutableFaceBodyType.__init__(self, faces)
        self.update_vertices()

    def refresh(self):
        self.update_vertices()
        return self

    def update_vertices(self):
        self._vertices.clear()
        for face in self._faces:
            for i, vertex in enumerate(face.vertices()):
                if vertex not in self._vertices:
                    vertices.append(vertex)
                else:
                    index = self._vertices.index(vertex)
                    face.set_vertex(i, self._vertices[index])
        return self
