from .abc import DimensionedFaceSingletonABC
from ..vector.vector2d import Vector2D
# from ..plane.plane2d import Plane2D


__all__ = ("face2d", "Face2D")

class Face2DSingleton(DimensionedFaceSingletonABC):
    pass

face2d = Face2D = Face2DSingleton()
