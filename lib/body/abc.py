from abc import ABC, abstractmethod
# from ..element.abc import ElementTypeABC


class VertexBodyType(ABC):
    def __init__(self, vertices):
        self._vertices = vertices

    def vertices(self): return self._vertices


class MutableVertexBodyType(VertexBodyType):
    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        return self
    def add_vertices(cls, body, vertices):
        self._vertices.extend(vertices)
        return self

    def remove_vertex(self, vertex):
        self._vertices.remove(vertex)
        return self
    def remove_vertices(self, vertices):
        [self._bodies.remove(vertex) for vertex in vertices]
        return self


class FaceBodyType(VertexBodyType):
    def __init__(self, faces):
        super().__init__([])
        self._faces = faces

    @abstractmethod
    def update_vertices(self): raise NotImplementedError

    def faces(self): return self._faces


class MutableFaceBodyType(FaceBodyType):
    def add_face(self, face):
        self._faces.append(face)
        self.update_vertices()
        return self
    def add_faces(self, faces):
        self._faces.extend(faces)
        self.update_vertices()
        return self

    def remove_face(self, face):
        self._faces.remove(face)
        self.update_vertices()
        return self
    def remove_faces(self, faces):
        [self._faces.remove(face) for face in faces]
        self.update_vertices()
        return self
