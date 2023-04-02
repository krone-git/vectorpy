from .abc import VectorSingletonABC
from math import cos, sin, atan


__all__ = (
    "vec2d", "Vector2D"
    )

class Vector2DSingleton(VectorSingletonABC):
    @staticmethod
    def new(x, y): return [x / 1.0, y / 1.0]
    @staticmethod
    def from_iterable(values): return [v / 1.0 for v in values][:2]
    @staticmethod
    def from_direction(theta_x, magnitude):
        return [magnitude * cos(theta_x), magnitude * sin(theta_x)]

    @staticmethod
    def zero_vector(): return [0.0, 0.0]

    @staticmethod
    def axis_vector(axis):
        vector = [0.0, 0.0]
        vector[axis] = 1.0
        return vector
    @staticmethod
    def x_axis(): return [1.0, 0.0]
    @staticmethod
    def y_axis(): return [0.0, 1.0]

    @staticmethod
    def set_vector(vector, other):
        vector[0], vector[1] = other
        return vector
    @staticmethod
    def set_components(vector, x, y):
        vector[0], vector[1] = x / 1.0, y / 1.0
        return vector

    @staticmethod
    def clear(vector):
        vector[0] = vector[1] = 0.0
        return vector

    @staticmethod
    def magnitude(vector):
        x, y = vector
        return (x ** 2 + y ** 2) ** 0.5

    @staticmethod
    def add_vector(vector, other):
        x, y = vector
        a, b = other
        return [x + a, y + b]
    @staticmethod
    def iadd_vector(vector, other):
        a, b = other
        vector[0] += a
        vector[1] += b
        return vector
    @staticmethod
    def add_scalar(vector, scalar):
        x, y = vector
        return [x + scalar, y + scalar]
    @staticmethod
    def iadd_scalar(vector, scalar):
        vector[0] += scalar
        vector[1] += scalar
        return vector

    @staticmethod
    def subtract_vector(vector, other):
        x, y = vector
        a, b = other
        return [x - a, y - b]
    @staticmethod
    def isubtract_vector(vector, other):
        a, b = other
        vector[0] -= a
        vector[1] -= b
        return vector
    @staticmethod
    def subtract_scalar(vector, scalar):
        x, y = vector
        return [x - scalar, y - scalar]
    @staticmethod
    def isubtract_scalar(vector, scalar):
        vector[0] -= scalar
        vector[1] -= scalar
        return vector

    @staticmethod
    def multiply_scalar(vector, scalar):
        x, y = vector
        return [x * scalar, y * scalar]
    @staticmethod
    def imultiply_scalar(vector, scalar):
        vector[0] *= scalar
        vector[1] *= scalar
        return vector

    @staticmethod
    def divide_scalar(vector, scalar):
        x, y = vector
        return [x / scalar, y / scalar]
    @staticmethod
    def idivide_scalar(vector, scalar):
        vector[0] /= scalar
        vector[1] /= scalar
        return vector

    @staticmethod
    def dot_product(vector, other):
        x, y = vector
        a, b = other
        return x * a + y * b

    @staticmethod
    def cross_product(vector, other): return [0.0, 0.0]

    @staticmethod
    def axis_angle(vector, axis):
        return atan(vector[1 - axis] / vector[axis])

vec2d = Vector2D = Vector2DSingleton()
