from .abc import VectorABC
from functools import reduce


__all__ = (
    "vec", "Vector"
    )

class VectorNDSingleton(VectorABC):
    def new(*args): return [float(i) for i in args]

    def set_vector(vector, other):
        for i, v in enumerate(other): vector[i] = v
        return vectors

    def zero_vector(size): return [0.0] * size

    def axis_vector(axis, size):
        vector = [0.0] * size
        vector[axis] = 1.0
        return vector

    def magnitude(vector): return sum([i ** 2 for i in vector]) ** 0.5

    def add_vector(vector, other): return [a + b for a, b in zip(vector, other)]
    def iadd_vector(vector, other):
        for i, v in enumerate(other): vector[i] += v
        return vector
    def add_scalar(vector, scalar): return [i + scalar for i in vector]
    def iadd_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] += scalar
        return vector

    def subtract_vector(vector, other):
        return [a - b for a, b in zip(vector, other)]
    def isubtract_vector(vector, other):
        for i, v in enumerate(other): vector[i] -= v
        return vector
    def subtract_scalar(vector, scalar): return [i - scalar for i in vector]
    def isubtract_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] -= scalar
        return vector

    def multiply_scalar(vector, scalar): return [i * scalar for i in vector]
    def imultiply_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] *= scalar
        return vector

    def divide_scalar(vector, scalar): return [i / scalar for i in vector]
    def idivide_scalar(vector, scalar):
        for i in range(len(vector)): vector[i] /= scalar
        return vector

    def dot_product(vector, other):
        return sum([a * b for a, b in zip(vector, other)])

    def cross_product(): raise NotImplementedError

vec = Vector = VectorNDSingleton()
