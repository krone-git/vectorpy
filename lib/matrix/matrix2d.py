from .abc import MatrixSingletonABC, MatrixLinearTransformSingletonABC
from math import cos, sin


__all__ = (
    "mat2d", "Matrix2D", "mat2dt", "Matrix2DTransform"
    )


class Matrix2DSingleton(MatrixSingletonABC):
    @staticmethod
    def new(a, b, c, d): return [a / 1.0, b / 1.0, c / 1.0, d / 1.0]

mat2d = Matrix2D = Matrix2DSingleton()


class Matrix2DTransformSingleton(MatrixLinearTransformSingletonABC):
    pass

mat2dt = Matrix2DTransform = Matrix2DTransformSingleton()
