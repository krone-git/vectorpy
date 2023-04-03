from .abc import DimensionedFaceSingletonABC
from ..vector.vector3d import Vector3D
from ..plane.plane3d import Plane3D


__all__ = ("face3d", "Face3D")

class Face3DSingleton(DimensionedFaceSingletonABC):
    @classmethod
    def to_plane(cls, face):
        return Plane3D.from_vector(
            cls.normal(face), cls.center_point(face)
            )
    @classmethod
    def center_point(cls, face):
        return Vector3D.center_vector(
            cls.vertices(face)
            )
    @classmethod
    def area(cls, face):
        return Vector3D.divide_scalar(
            cls.normal(face), 2
            )
    @classmethod
    def normal(cls, face):
        vec2 = Vector3D
        sub_vec = vec3.subtract_vector
        cross = vec3.cross_product
        center, left, right = cls.vertices(face)
        return cross(
            sub_vec(left, center),
            sub_vec(right, center)
            )


face3d = Face3D = Face3DSingleton()
