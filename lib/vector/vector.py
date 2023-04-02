from .abc import VectorSingletonABC
from functools import reduce


__all__ = (
    "vec", "Vector", "vecnd", "VectorND"
    )

class VectorNDSingleton(VectorSingletonABC):
    @staticmethod
    def new(*args): return [i / 1.0 for i in args]
    @staticmethod
    def from_iterable(values): return [v / 1.0 for v in values]

    @staticmethod
    def zero_vector(size): return [0.0] * size

    @staticmethod
    def axis_vector(axis, size):
        vector = [0.0] * size
        vector[axis] = 1.0
        return vector

    @staticmethod
    def set_vector(vector, other):
        for i, v in enumerate(other): vector[i] = v / 1.0
        return vectors
    @staticmethod
    def set_components(vector, *components):
        for i, v in enumerate(components): vector[i] = v / 1.0
        return vectors

    @staticmethod
    def clear(vector):
        for i, v in enumerate(vector): vector[i] = 0.0
        return vector

    @staticmethod
    def magnitude(vector): return sum([i ** 2 for i in vector]) ** 0.5

    @staticmethod
    def add_vector(vector, other): return [a + b for a, b in zip(vector, other)]
    @staticmethod
    def iadd_vector(vector, other):
        for i, v in enumerate(other): vector[i] += v
        return vector
    @staticmethod
    def add_scalar(vector, scalar): return [i + scalar for i in vector]
    @staticmethod
    def iadd_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] += scalar
        return vector

    @staticmethod
    def subtract_vector(vector, other):
        return [a - b for a, b in zip(vector, other)]
    @staticmethod
    def isubtract_vector(vector, other):
        for i, v in enumerate(other): vector[i] -= v
        return vector
    @staticmethod
    def subtract_scalar(vector, scalar): return [i - scalar for i in vector]
    @staticmethod
    def isubtract_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] -= scalar
        return vector

    @staticmethod
    def multiply_scalar(vector, scalar): return [i * scalar for i in vector]
    @staticmethod
    def imultiply_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] *= scalar
        return vector

    @staticmethod
    def divide_scalar(vector, scalar): return [i / scalar for i in vector]
    @staticmethod
    def idivide_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] /= scalar
        return vector

    @staticmethod
    def dot_product(vector, other):
        return sum([a * b for a, b in zip(vector, other)])

    @staticmethod
    def cross_product(): raise NotImplementedError

vec = Vector = vecnd = VectorND = VectorNDSingleton()
