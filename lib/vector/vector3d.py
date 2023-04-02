from .abc import VectorSingletonABC
from math import cos, sin


__all__ = (
    "vec3d", "Vector3D"
    )

class Vector3DSingleton(VectorSingletonABC):
    @staticmethod
    def new(x, y, z): return [x / 1.0, y / 1.0, z / 1.0]
    @staticmethod
    def from_iterable(values): return [v / 1.0 for v in values][:3]

    @staticmethod
    def zero_vector(): return [0.0, 0.0, 0.0]

    @staticmethod
    def axis_vector(axis):
        vector = [0.0, 0.0, 0.0]
        vector[axis] = 1.0
        return vector
    @staticmethod
    def x_axis(): return [1.0, 0.0, 0.0]
    @staticmethod
    def y_axis(): return [0.0, 1.0, 0.0]
    @staticmethod
    def z_axis(): return [0.0, 0.0, 1.0]

    @staticmethod
    def set_vector(vector, other):
        vector[0], vector[1], vector[2] = other
        return vector
    @staticmethod
    def set_components(vector, x, y, z):
        vector[0], vector[1], vector[2] = x / 1.0, y / 1.0, z / 1.0

    @staticmethod
    def clear(vector):
        vector[0] = vector[1] = vector[2] = 0.0
        return vector

    @staticmethod
    def magnitude(vector):
        x, y, z = vector
        return (x ** 2 + y ** 2 + z ** 2) ** 0.5

    @staticmethod
    def add_scalar(vector, scalar):
        x, y, z = vector
        return [x + scalar, y + scalar, z + scalar]
    @staticmethod
    def iadd_scalar(vector, scalar):
        vector[0] += scalar
        vector[1] += scalar
        vector[2] += scalar
        return vector
    @staticmethod
    def add_vector(vector, other):
        x, y, z = vector
        a, b, c = other
        return [x + a, y + b, z + c]
    @staticmethod
    def iadd_vector(vector, other):
        a, b, c = other
        vector[0] += a
        vector[1] += b
        vector[2] += c
        return vector

    @staticmethod
    def subtract_scalar(vector, scalar):
        x, y, z = vector
        return [x - scalar, y - scalar, z - scalar]
    @staticmethod
    def isubtract_scalar(vector, scalar):
        vector[0] -= scalar
        vector[1] -= scalar
        vector[2] -= scalar
        return vector
    @staticmethod
    def subtract_vector(vector, other):
        x, y, z = vector
        a, b, c = other
        return [x - a, y - b, z - c]
    @staticmethod
    def isubtract_vector(vector, other):
        a, b, c = other
        vector[0] -= a
        vector[1] -= b
        vector[2] -= c
        return vector

    @staticmethod
    def multiply_scalar(vector, scalar):
        x, y, z = vector
        return [x * scalar, y * scalar, z * scalar]
    @staticmethod
    def imultiply_scalar(vector, scalar):
        vector[0] *= scalar
        vector[1] *= scalar
        vector[2] *= scalar
        return vector

    @staticmethod
    def divide_scalar(vector, scalar):
        x, y, z = vector
        return [x / scalar, y / scalar, z / scalar]
    @staticmethod
    def idivide_scalar(vector, scalar):
        vector[0] /= scalar
        vector[1] /= scalar
        vector[2] /= scalar
        return vector

    @staticmethod
    def dot_product(vector, other):
        x, y, z = vector
        a, b, c = other
        return x * a + y * b + z * c

    @staticmethod
    def cross_product(vector, other):
        x, y, z = vector
        a, b, c = other
        return [y * c - z * b, -(x * c - z * a), x * b - y * a]

vec3d = Vector3D = Vector3DSingleton()
