from .abc import FaceSingletonABC
from ..vector.vector3d import Vector3D
from ..plane.plane3d import Plane3D


__all__ = (
    "face3d", "Face3D"
    )

class Face3DSingleton(FaceSingletonABC):
    # @classmethod
    # def from_normal(cls, normal, vertices): raise NotImplementedError
    # @classmethod
    # def to_plane(cls, face): raise NotImplementedError
    #
    # @classmethod
    # def normal(cls, face): raise NotImplementedError
    pass

face3d = Face3D = Face3DSingleton()
