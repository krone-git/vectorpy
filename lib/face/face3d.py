from .abc import DimensionedFaceSingletonABC
from ..vector.vector3d import Vector3D
from ..plane.plane3d import Plane3D


__all__ = ("face3d", "Face3D")

class Face3DSingleton(DimensionedFaceSingletonABC):
    pass

face3d = Face3D = Face3DSingleton()
