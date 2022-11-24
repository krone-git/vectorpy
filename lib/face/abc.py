from abc import ABC, abstractmethod
from copy import deepcopy


class BaseFaceSingletonABC(ABC):
    __slots__ = ()

    @classmethod
    def new(cls, center, left, right):
        return [center, left, right]

    @staticmethod
    def copy(face): return deepcopy(face)

    @classmethod
    def vertex(cls, face, index): return face[cls.VERTICES][index]
    @classmethod
    def center_vertex(cls, face): return face[cls.VERTICES][0]
    @classmethod
    def left_vertex(cls, face): return face[cls.VERTICES][1]
    @classmethod
    def right_vertex(cls, face): return face[cls.VERTICES][2]
    @classmethod
    def vertices(cls, face): return face[cls.VERTICES]

    @classmethod
    def set_vertex(cls, face, index, vertex):
        face[cls.VERTICES][index] = vertex
        return face
    @classmethod
    def set_center_vertex(cls, face, vertex):
        face[cls.VERTICES][0] = vertex
        return self
    @classmethod
    def set_left_vertex(cls, face, vertex):
        face[cls.VERTICES][1] = vertex
        return self
    @classmethod
    def set_right_vertex(cls, face, vertex):
        face[cls.VERTICES][2] = vertex
        return self
    @classmethod
    def set_vertices(cls, center, left, right):
        face[cls.VERTICES][0] = center
        face[cls.VERTICES][1] = left
        face[cls.VERTICES][2] = right
        return face
    @classmethod
    def set_face(cls, face, other):
        face[cls.VERTICES][0], face[cls.VERTICES][1], face[cls.VERTICES][2] \
            = other[cls.VERTICES]
        return face


class DimensionedFaceSingletonABC(BaseFaceSingletonABC):
    @abstractmethod
    def from_normal(cls, normal, vertices): raise NotImplementedError
    @abstractmethod
    def to_plane(cls, face): raise NotImplementedError

    @abstractmethod
    def normal(cls, face): raise NotImplementedError
