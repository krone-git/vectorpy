from copy import deepcopy
from ..face import Face


__all__ = (
    "Body",
    )

class BodySingleton:
    VERTICES = "vertices",
    FACES = "faces"

    __slots__ = ()

    @classmethod
    def new(cls, faces):
        body = {
            cls.FACES: faces,
            cls.VERTICES: []
            }
        cls.refresh(body)
        return body

    @classmethod
    def copy(cls, body):
        new_body = deepcopy(body)
        cls.refresh(new_body)
        return new_body

    @classmethod
    def vertices(cls, body): return body[cls.VERTICES]
    @classmethod
    def faces(cls, body): return body[cls.FACES]
    @classmethod
    def contents(cls, body): return body[cls.FACES], body[cls.VERTICES]

    @classmethod
    def refresh(cls, body):
        get_vertices = Face.vertices
        set_vertex = Face.set_vertex
        vertices = body[cls.VERTICES]
        faces = body[cls.FACES]

        vertices.clear()
        for face in faces:
            face_vertices = get_vertices(face)
            for i, vertex in enumerate(face_vertices):
                if vertex not in vertices:
                    vertices.append(vertex)
                else:
                    set_vertext(face, i, vertices[vertices.index(vertex)])
        return body

    @classmethod
    def add_face(cls, body, face):
        body[cls.FACES].append(face)
        cls.refresh(body)
        return body

    @classmethod
    def add_faces(cls, body, faces):
        body[cls.FACES].extend(faces)
        cls.refresh(body)
        return body

    @classmethod
    def remove_face(cls, body, index):
        body[cls.FACES].pop(index)
        cls.refresh(body)
        return body

    @classmethod
    def remove_faces(cls, body, indices):
        faces = body[cls.FACES]
        [faces.pop(index) for index in sorted(indices)[::-1]]
        cls.refresh(body)
        return body

Body = BodySingleton
