from .abc import VectorABC, VectorTransformABC
from math import cos, sin


__all__ = (
    "vec3d", "vec3dt", "Vector3D", "Vector3DTransform"
    )

class Vector3DSingleton(VectorABC):
    def new(x, y, z): return [float(x), float(y), float(z)]

    def set_vector(vector, other):
        vector[0], vector[1], vector[2] = other
        return vector

    def zero_vector(): return [0.0, 0.0, 0.0]

    def axis_vector(axis):
        vector = [0.0, 0.0, 0.0]
        vector[axis] = 1.0
        return vector

    def magnitude(vector):
        x, y, z = vector
        return (x ** 2 + y ** 2 + z ** 2) ** 0.5

    def add_vector(vector, other):
        x, y, z = vector
        a, b, c = other
        return [x + a, y + b, z + c]
    def iadd_vector(vector, other):
        a, b, c = other
        vector[0] += a
        vector[1] += b
        vector[2] += c
        return vector
    def add_scalar(vector, scalar):
        x, y, z = vector
        return [x + scalar, y + scalar, z + scalar]
    def iadd_scalar(vector, scalar):
        vector[0] += scalar
        vector[1] += scalar
        vector[2] += scalar
        return vector

    def subtract_vector(vector, other):
        x, y, z = vector
        a, b, c = other
        return [x - a, y - b, z - c]
    def isubtract_vector(vector, other):
        a, b, c = other
        vector[0] -= a
        vector[1] -= b
        vector[2] -= c
        return vector
    def subtract_scalar(vector, scalar):
        x, y, z = vector
        return [x - scalar, y - scalar, z - scalar]
    def isubtract_scalar(vector, scalar):
        vector[0] -= scalar
        vector[1] -= scalar
        vector[2] -= scalar
        return vector

    def multiply_scalar(vector, scalar):
        x, y, z = vector
        return [x * scalar, y * scalar, z * scalar]
    def imultiply_scalar(vector, scalar):
        vector[0] *= scalar
        vector[1] *= scalar
        vector[2] *= scalar
        return vector

    def divide_scalar(vector, scalar):
        x, y, z = vector
        return [x / scalar, y / scalar, z / scalar]
    def idivide_scalar(vector, scalar):
        vector[0] /= scalar
        vector[1] /= scalar
        vector[2] /= scalar
        return vector

    def dot_product(vector, other):
        x, y, z = vector
        a, b, c = other
        return x * a + y * b + z * c

    def cross_product(vector, other):
        x, y, z = vector
        a, b, c = other
        return [y * c - z * b, -(x * c - z * a), x * b - y * a]

vec3d = Vector3D = Vector3DSingleton()


class Vector3DTransformSingleton(Vector3DSingleton, VectorTransformABC):
    def truncate(vector): return vector[:3]
    def expand(vector): return [*vector[:3], 1.0]

    def new(x, y, z): return [float(x), float(y), float(z), 1.0]

    def set_vector(vector, other):
        vector[0], vector[1], vector[2], vector[3] = other
        return vector

    def zero_vector(): return [0.0, 0.0, 0.0, 1.0]

    def axis_vector(axis):
        vector = [0.0, 0.0, 0.0, 1.0]
        vector[axis] = 1.0
        return vector

    def magnitude(vector):
        x, y, z, _ = vector
        return (x ** 2 + y ** 2 + z ** 2) ** 0.5

    def add_vector(vector, other):
        x, y, z, _ = vector
        a, b, c, _ = other
        return [x + a, y + b, z + c, 1.0]
    def iadd_vector(vector, other):
        a, b, c, _ = other
        vector[0] += a
        vector[1] += b
        vector[2] += c
        return vector
    def add_scalar(vector, scalar):
        x, y, z, _ = vector
        return [x + scalar, y + scalar, z + scalar, 1.0]

    def subtract_vector(vector, other):
        x, y, z, _ = vector
        a, b, c, _ = other
        return [x - a, y - b, z - c, 1.0]
    def isubtract_vector(vector, other):
        a, b, c, _ = other
        vector[0] -= a
        vector[1] -= b
        vector[2] -= c
        return vector
    def subtract_scalar(vector, scalar):
        x, y, z, _ = vector
        return [x - scalar, y - scalar, z - scalar, 1.0]

    def multiply_scalar(vector, scalar):
        x, y, z, _ = vector
        return [x * scalar, y * scalar, z * scalar, 1.0]

    def divide_scalar(vector, scalar):
        x, y, z, _ = vector
        return [x / scalar, y / scalar, z / scalar, 1.0]

    def dot_product(vector, other):
        x, y, z, _ = vector
        a, b, c, _ = other
        return x * a + y * b + z * c

    def cross_product(vector, other):
        x, y, z, _ = vector
        a, b, c, _ = other
        return [y * c - z * b, -(x * c - z * a), x * b - y * a, 1.0]

vec3dt = Vector3DTransform = Vector3DTransformSingleton()
