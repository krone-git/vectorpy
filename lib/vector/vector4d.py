from .abc import VectorSingletonABC


__all__ = (
    "vec4d", "Vector4D"
    )

class Vector4DSingleton(VectorSingletonABC):
    @staticmethod
    def new(x, y, z, w): return [x / 1.0, y / 1.0, z / 1.0, w / 1.0]
    @staticmethod
    def from_iterable(values): return [v / 1.0 for v in values][:4]
    @staticmethod
    def zero_vector(): return [0.0, 0.0, 0.0, 0.0]

    @staticmethod
    def axis_vector(axis):
        vector = [0.0, 0.0, 0.0, 0.0]
        vector[axis] = 1.0
        return vector

    @staticmethod
    def set_vector(vector, other):
        vector[0], vector[1], vector[2], vector[3] = other
        return vector
    @staticmethod
    def set_components(vector, x, y, z, w):
        vector[0], vector[1], vector[2], vector[3] = x / 1.0, y / 1.0, z / 1.0, w / 1.0
        return vector

    @staticmethod
    def clear(vector):
        vector[0] = vector[1] = vector[2] = vector[3] = 0.0

    @staticmethod
    def magnitude(vector):
        x, y, z, w = vector
        return (x ** 2 + y ** 2 + z ** 2 + w ** 2) ** 0.5

    @staticmethod
    def add_vector(vector, other):
        x, y, z, w = vector
        a, b, c, d = other
        return [x + a, y + b, z + c, w + d]
    @staticmethod
    def iadd_vector(vector, other):
        a, b, c, d = other
        vector[0] += a
        vector[1] += b
        vector[2] += c
        vector[3] += d
        return vector
    @staticmethod
    def add_scalar(vector, scalar):
        x, y, z, w = vector
        return [x + scalar, y + scalar, z + scalar, w + scalar]
    @staticmethod
    def iadd_scalar(vector, scalar):
        vector[0] += scalar
        vector[1] += scalar
        vector[2] += scalar
        vector[3] += scalar
        return vector

    @staticmethod
    def subtract_vector(vector, other):
        x, y, z, w = vector
        a, b, c, d = other
        return [x - a, y - b, z - c, w - d]
    @staticmethod
    def isubtract_vector(vector, other):
        a, b, c, d = other
        vector[0] -= a
        vector[1] -= b
        vector[2] -= c
        vector[3] -= d
        return vector
    @staticmethod
    def subtract_scalar(vector, scalar):
        x, y, z, w = vector
        return [x - scalar, y - scalar, z - scalar, w - scalar]
    @staticmethod
    def isubtract_scalar(vector, scalar):
        vector[0] -= scalar
        vector[1] -= scalar
        vector[2] -= scalar
        vector[3] -= scalar
        return vector

    @staticmethod
    def multiply_scalar(vector, scalar):
        x, y, z, w = vector
        return [x * scalar, y * scalar, z * scalar, w * scalar]
    @staticmethod
    def imultiply_scalar(vector, scalar):
        vector[0] *= scalar
        vector[1] *= scalar
        vector[2] *= scalar
        vector[3] *= scalar
        return vector

    @staticmethod
    def divide_scalar(vector, scalar):
        x, y, z, w = vector
        return [x / scalar, y / scalar, z / scalar, w / scalar]
    @staticmethod
    def idivide_scalar(vector, scalar):
        vector[0] /= scalar
        vector[1] /= scalar
        vector[2] /= scalar
        vector[3] /= scalar
        return vector

    @staticmethod
    def dot_product(vector, other):
        x, y, z, w = vector
        a, b, c, d = other
        return x * a + y * b + z * c + w * d

    @staticmethod
    def cross_product(vector, other):
        raise NotImplementedError

vec4d = Vector4D = Vector4DSingleton()
