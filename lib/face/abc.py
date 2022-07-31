from abc import ABC, abstractmethod
from copy import deepcopy


class FaceSingletonABC():
    VERTICES = "vertices"

    __slots__ = ()

    @classmethod
    def new(cls, center, first, second):
        return {cls.VERTICES: [center, first, second]}

    @abstractmethod
    def from_normal(cls, normal, vertices): raise NotImplementedError
    @abstractmethod
    def to_plane(cls, face): raise NotImplementedError

    @staticmethod
    def copy(face): return deepcopy(face)

    @classmethod
    def vertex(cls, face, index): return face[cls.VERTICES][index]
    @classmethod
    def vertices(cls, face): return face[cls.VERTICES]

    @classmethod
    def set_vertex(cls, face, index, vertex):
        face[cls.VERTICES][index] = vertex
        return face
    @classmethod
    def set_vertices(cls, center, first, second):
        face[cls.VERTICES][0] = center
        face[cls.VERTICES][1] = first
        face[cls.VERTICES][2] = second
        return face
    @classmethod
    def set_face(cls, face, other):
        face[cls.VERTICES][0], face[cls.VERTICES][1], face[cls.VERTICES][2] \
            = other[cls.VERTICES]
        return face

    @abstractmethod
    def normal(cls, face): raise NotImplementedError
