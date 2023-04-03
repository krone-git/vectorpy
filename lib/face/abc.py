from abc import ABC, abstractmethod
from copy import deepcopy


class BaseFaceSingletonABC(ABC):
    __slots__ = ()

    @classmethod
    def new(cls, center, left, right):
        return [center, left, right]
    @classmethod
    def  __call__(cls, *args, **kwargs): return cls.new(*args, **kwargs)
    @staticmethod
    def copy(face): return deepcopy(face)

    @classmethod
    def vertex(cls, face, index): return face[index]
    @classmethod
    def center_vertex(cls, face): return face[0]
    @classmethod
    def left_vertex(cls, face): return face[1]
    @classmethod
    def right_vertex(cls, face): return face[2]
    @classmethod
    def vertices(cls, face): return face

    @classmethod
    def set_vertex(cls, face, index, vertex):
        face[index] = vertex
        return face
    @classmethod
    def set_center_vertex(cls, face, vertex):
        face[0] = vertex
        return self
    @classmethod
    def set_left_vertex(cls, face, vertex):
        face[1] = vertex
        return self
    @classmethod
    def set_right_vertex(cls, face, vertex):
        face[2] = vertex
        return self
    @classmethod
    def set_vertices(cls, center, left, right):
        face[0] = center
        face[1] = left
        face[2] = right
        return face
    @classmethod
    def set_face(cls, face, other):
        face[0], face[1], face[2] = other
        return face
    @classmethod
    def invert_normal(cls, face):
        _, left, right = face
        cls.set_left_vertex(right)
        cls.set_right_vertex(left)
        return face
    @classmethod
    def inverted_face(cls, face):
        center, left, right = face
        return cls.new(center, right, left)



class DimensionedFaceSingletonABC(BaseFaceSingletonABC):
    @abstractmethod
    def to_plane(cls, face): raise NotImplementedError

    @abstractmethod
    def normal(cls, face): raise NotImplementedError
    @abstractmethod
    def area(cls, face): raise NotImplementedError
    @abstractmethod
    def center_point(cls, face): raise NotImplementedError
