from .abc import VectorABC


__all__ = (
    "vec4d", "Vector4D"
    )

class Vector4DSingleton(VectorABC):
    def new(x, y, z, w): return [float(x), float(y), float(z), float(w)]

    def set_vector(vector, other):
        vector[0], vector[1], vector[2], vector[3] = other
        return vector

    def zero_vector(): return [0.0, 0.0, 0.0, 0.0]

    def axis_vector(axis):
        vector = [0.0, 0.0, 0.0, 0.0]
        vector[axis] = 1.0
        return vector

    def magnitude(vector):
        x, y, z, w = vector
        return (x ** 2 + y ** 2 + z ** 2 + w ** 2) ** 0.5

    def add_vector(vector, other):
        x, y, z, w = vector
        a, b, c, d = other
        return [x + a, y + b, z + c, w + d]
    def iadd_vector(vector, other):
        a, b, c, d = other
        vector[0] += a
        vector[1] += b
        vector[2] += c
        vector[3] += d
        return vector
    def add_scalar(vector, scalar):
        x, y, z, w = vector
        return [x + scalar, y + scalar, z + scalar, w + scalar]
    def iadd_scalar(vector, scalar):
        vector[0] += scalar
        vector[1] += scalar
        vector[2] += scalar
        vector[3] += scalar
        return vector

    def subtract_vector(vector, other):
        x, y, z, w = vector
        a, b, c, d = other
        return [x - a, y - b, z - c, w - d]
    def isubtract_vector(vector, other):
        a, b, c, d = other
        vector[0] -= a
        vector[1] -= b
        vector[2] -= c
        vector[3] -= d
        return vector
    def subtract_scalar(vector, scalar):
        x, y, z, w = vector
        return [x - scalar, y - scalar, z - scalar, w - scalar]
    def isubtract_scalar(vector, scalar):
        vector[0] -= scalar
        vector[1] -= scalar
        vector[2] -= scalar
        vector[3] -= scalar
        return vector

    def multiply_scalar(vector, scalar):
        x, y, z, w = vector
        return [x * scalar, y * scalar, z * scalar, w * scalar]
    def imultiply_scalar(vector, scalar):
        vector[0] *= scalar
        vector[1] *= scalar
        vector[2] *= scalar
        vector[3] *= scalar
        return vector

    def divide_scalar(vector, scalar):
        x, y, z, w = vector
        return [x / scalar, y / scalar, z / scalar, w / scalar]
    def idivide_scalar(vector, scalar):
        vector[0] /= scalar
        vector[1] /= scalar
        vector[2] /= scalar
        vector[3] /= scalar
        return vector

    def dot_product(vector, other):
        x, y, z, w = vector
        a, b, c, d = other
        return x * a + y * b + z * c + w * d

    def cross_product(vector, other):
        raise NotImplementedError

vec4d = Vector4D = Vector4DSingleton()
