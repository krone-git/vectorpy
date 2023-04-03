from .abc import DimensionedFaceSingletonABC
from ..vector.vector2d import Vector2D
# from ..plane.plane2d import Plane2D


__all__ = ("face2d", "Face2D")

class Face2DSingleton(DimensionedFaceSingletonABC):
    @classmethod
    def to_plane(cls, face):
        return Plane2D.from_vector(
            cls.normal(face), cls.center_point(face)
            )
    @classmethod
    def center_point(cls, face):
        return Vector2D.center_vector(
            cls.vertices(face)
            )
    @classmethod
    def area(cls, face):
        return cls.normal(face) / 2
    @classmethod
    def normal(cls, face):
        vec2 = Vector2D
        sub_vec = vec2.subtract_vector
        cross = vec2.cross_product
        center, left, right = cls.vertices(face)
        return cross(
            sub_vec(left, center),
            sub_vec(right, center)
            )


face2d = Face2D = Face2DSingleton()
