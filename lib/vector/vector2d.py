from .abc import VectorABC, VectorTransformABC
from math import cos, sin, atan


__all__ = (
    "vec2d", "vec2dt", "Vector2D", "Vector2DTransform"
    )

class Vector2DSingleton(VectorABC):
    def new(x, y): return [float(x), float(y)]
    def from_direction(theta_x, magnitude):
        return [magnitude * cos(theta_x), magnitude * sin(theta_x)]

    def set_vector(vector, other):
        vector[0], vector[1] = other
        return vector

    def zero_vector(): return [0.0, 0.0]

    def axis_vector(axis):
        vector = [0.0, 0.0]
        vector[axis] = 1.0
        return vector

    def magnitude(vector):
        x, y = vector
        return (x ** 2 + y ** 2) ** 0.5

    def add_vector(vector, other):
        x, y = vector
        a, b = other
        return [x + a, y + b]
    def iadd_vector(vector, other):
        a, b = other
        vector[0] += a
        vector[1] += b
        return vector
    def add_scalar(vector, scalar):
        x, y = vector
        return [x + scalar, y + scalar]
    def iadd_scalar(vector, scalar):
        vector[0] += scalar
        vector[1] += scalar
        return vector

    def subtract_vector(vector, other):
        x, y = vector
        a, b = other
        return [x - a, y - b]
    def isubtract_vector(vector, other):
        a, b = other
        vector[0] -= a
        vector[1] -= b
        return vector
    def subtract_scalar(vector, scalar):
        x, y = vector
        return [x - scalar, y - scalar]
    def isubtract_scalar(vector, scalar):
        vector[0] -= scalar
        vector[1] -= scalar
        return vector

    def multiply_scalar(vector, scalar):
        x, y = vector
        return [x * scalar, y * scalar]
    def imultiply_scalar(vector, scalar):
        vector[0] *= scalar
        vector[1] *= scalar
        return vector

    def divide_scalar(vector, scalar):
        x, y = vector
        return [x / scalar, y / scalar]
    def idivide_scalar(vector, scalar):
        vector[0] /= scalar
        vector[1] /= scalar
        return vector

    def dot_product(vector, other):
        x, y = vector
        a, b = other
        return x * a + y * b

    def cross_product(vector, other): return [0.0, 0.0]

    def axis_angle(vector, axis):
        return atan(vector[1 - axis] / vector[axis])

vec2d = Vector2D = Vector2DSingleton()


class Vector2DTransformSingleton(Vector2DSingleton, VectorTransformABC):
    def truncate(vector): return vector[:2]
    def expand(vector): return [*vector[:2], 1.0]

    def set_vector(vector, other):
        vector[0], vector[1], vector[2] = other
        return vector

    def new(x, y): return [float(x), float(y), 1.0]
    def from_direction(theta_x, magnitude):
        return [magnitude * cos(theta_x), magnitude * sin(theta_x), 1.0]

    def zero_vector(): return [0.0, 0.0, 1.0]

    def axis_vector(axis):
        vector = [0.0, 0.0, 1.0]
        vector[axis] = 1.0
        return vector

    def magnitude(vector):
        x, y, _ = vector
        return (x ** 2 + y ** 2) ** 0.5

    def add_vector(vector, other):
        x, y, _ = vector
        a, b, _ = other
        return [x + a, y + b, 1.0]

    def iadd_vector(vector, other):
        a, b, _ = other
        vector[0] += a
        vector[1] += b
        return vector

    def add_scalar(vector, scalar):
        x, y, _ = vector
        return [x + scalar, y + scalar, 1.0]

    def subtract_vector(vector, other):
        x, y, _ = vector
        a, b, _ = other
        return [x - a, y - b, 1.0]

    def isubtract_vector(vector, other):
        a, b, _ = other
        vector[0] -= a
        vector[1] -= b
        return vector

    def subtract_scalar(vector, scalar):
        x, y, _ = vector
        return [x - scalar, y - scalar, 1.0]

    def multiply_scalar(vector, scalar):
        x, y, _ = vector
        return [x * scalar, y * scalar]

    def divide_scalar(vector, scalar):
        x, y, _ = vector
        return [x / scalar, y / scalar, 1.0]

    def dot_product(vector, other):
        x, y, _ = vector
        a, b, _ = other
        return x * a + y * b

    def cross_product(vector, other): return [0.0, 0.0, 1.0]

vec2dt = Vector2DTransform = Vector2DTransformSingleton()
