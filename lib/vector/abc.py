from abc import ABC, abstractmethod
from math import acos


class VectorABC(ABC):
    __slots__ = ()

    @abstractmethod
    def new(*args): raise NotImplementedError
    @classmethod
    def __call__(cls, *args, **kwargs): return cls.new(*args, **kwargs)
    @classmethod
    def from_points(point, other): return cls.subtract_vector(other, point)
    # @abstractmethod
    # def from_direction(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def zero_vector(): raise NotImplementedError

    @abstractmethod
    def axis_vector(): raise NotImplementedError

    def copy(vector): return vector.copy()
    @abstractmethod
    def set_vector(vector, other): raise NotImplementedError

    ###-------------

    @abstractmethod
    def magnitude(vector): raise NotImplementedError
    @classmethod
    def length(cls, *args, **kwargs): return cls.magnitude(*args, **kwargs)
    len = length

    @abstractmethod
    def add_vector(vector, other): raise NotImplementedError
    @abstractmethod
    def iadd_vector(vector, other): raise NotImplementedError
    @abstractmethod
    def add_scalar(vector, scalar): raise NotImplementedError
    @abstractmethod
    def iadd_scalar(vector, scalar): raise NotImplementedError
    @classmethod
    def sum_vectors(cls, vectors): return reduce(cls.add_vector, vectors)
    @classmethod
    def isum_vectors(cls, vector, others):
        return reduce(cls.iadd_vector, [vector, *others])

    @abstractmethod
    def subtract_vector(vector, other): raise NotImplementedError
    @abstractmethod
    def isubtract_vector(vector, other): raise NotImplementedError
    @abstractmethod
    def subtract_scalar(vector, scalar): raise NotImplementedError
    @abstractmethod
    def isubtract_scalar(vector, scalar): raise NotImplementedError

    @abstractmethod
    def multiply_scalar(vector, scalar): raise NotImplementedError
    @classmethod
    def scale(cls, *args, **kwargs): return cls.multiply_scalar(*args, **kwargs)
    @abstractmethod
    def imultiply_scalar(vector, scalar): raise NotImplementedError
    @classmethod
    def iscale(cls, *args, **kwargs): return cls.imultiply_scalar(*args, **kwargs)

    @abstractmethod
    def divide_scalar(vector, scalar): raise NotImplementedError
    @abstractmethod
    def idivide_scalar(vector, scalar): raise NotImplementedError

    @abstractmethod
    def dot_product(vector, other): raise NotImplementedError
    @classmethod
    def dot(cls, *args, **kwargs): return cls.dot_product()

    @abstractmethod
    def cross_product(vector, other): raise NotImplementedError
    @classmethod
    def cross(cls, *args, **kwargs): return cls.cross_product(*args, **kwargs)

    ###------------

    @classmethod
    def triple_scalar_product(cls, vector, other1, other2):
        return cls.dot_product(vector, cls.cross_product(other1, other2))
    @classmethod
    def triple_scalar(cls, *args, **kwargs): return cls.triple_scalar_product(*args, **kwargs)

    @classmethod
    def unit_vector(cls, vector):
        return cls.divide_scalar(vector, cls.magnitude(vector))
    @classmethod
    def normalize_vector(cls, vector):
        return cls.idivide_scalar(vector, cls.magnitude(vector))

    @classmethod
    def vector_projection(cls, vector, other):
        scalar = cls.dot_product(vector, other) / cls.magnitude(other) ** 2
        return cls.multiply_scalar(other, scalar)
    @classmethod
    def scalar_projection(cls, vector, other):
        return abs(cls.dot_product(vector, other)) / cls.magnitude(other)

    @classmethod
    def vector_cosine(cls, vector, other):
        return cls.dot_product(vector, other) / (cls.magnitude(vector) * cls.magnitude(other))

    @classmethod
    def vector_angle(cls, *args, **kwargs): return acos(cls.vector_cosine(*args, **kwargs))
    @classmethod
    def circle_inverse_vector_angle(cls, *args, **kwargs):
        c = 2 * pi
        return (c - cls.vector_angle(*args, **kwargs)) % c
    @classmethod
    def circle_vector_angles(cls, *args, **kwargs):
        c = 2 * pi
        angle = cls.vector_angle(*args, **kwargs)
        return (angle, (c - angle) % c)
    @classmethod
    def parallel_inverse_vector_angle(cls, *args, **kwargs):
        return (pi - cls.vector_angle(*args, **kwargs)) % pi
    @classmethod
    def parallel_vector_angles(cls, *args, **kwargs):
        angle = cls.vector_angle(*args, **kwargs)
        return (angle, (pi - angle) % pi)
    @classmethod
    def perpendicular_inverse_vector_angle(cls, *args, **kwargs):
        p = pi / 2
        return (p - cls.vector_angle(*args, **kwargs)) % p
    @classmethod
    def perpendicular_vector_angles(cls, *args, **kwargs):
        p = pi / 2
        angle = cls.vector_angle(*args, **kwargs)
        return (angle, (p - angle) % p)
    @classmethod
    def inverse_vector_angle(cls, *args, **kwargs):
        return cls.parallel_inverse_vector_angle(*args, **kwargs)
    @classmethod
    def vector_angles(cls, *args, **kwargs):
        return parallel_vector_angles(*args, **kwargs)

    @classmethod
    def axis_angle(cls, vector, axis):
        return cls.vector_angle(vector, cls.axis_vector(axis))
    @classmethod
    def circle_inverse_axis_angle(cls, *args, **kwargs):
        c = 2 * pi
        return (c - cls.axis_angle(*args, **kwargs)) % c
    @classmethod
    def circle_axis_angles(cls, *args, **kwargs):
        c = 2 * pi
        angle = cls.axis_angle(*args, **kwargs)
        return (angle, (c - angle) % c)
    @classmethod
    def parallel_inverse_axis_angle(cls, *args, **kwargs):
        return (pi - cls.axis_angle(*args, **kwargs)) % pi
    @classmethod
    def parallel_axis_angles(cls, *args, **kwargs):
        angle = cls.axis_angle(*args, **kwargs)
        return (angle, (pi - angle) % pi)
    @classmethod
    def perpendicular_inverse_axis_angle(cls, *args, **kwargs):
        p = pi / 2
        return (p - cls.axis_angle(*args, **kwargs)) % p
    @classmethod
    def perpendicular_axis_angles(cls, *args, **kwargs):
        p = pi / 2
        angle = cls.axis_angle(*args, **kwargs)
        return (angle, (p - angle) % p)
    @classmethod
    def inverse_axis_angle(cls, *args, **kwargs):
        return cls.parallel_inverse_axis_angle(*args, **kwargs)
    @classmethod
    def axis_angles(cls, *args, **kwargs):
        return parallel_axis_angles(*args, **kwargs)

    @classmethod
    def acute_vector_angle(cls, *args, **kwargs):
        return 0 < cls.vector_cosine(*args, **kwargs) < 1
    @classmethod
    def obtuse_vector_angle(cls, *args, **kwargs):
        return -1 < cls.vector_cosine(*args, **kwargs) < 0

    @classmethod
    def perpendicular_vectors(cls, *args, **kwargs):
        return cls.dot_product(*args, **kwargs) == 0
    @classmethod
    def parallel_vectors(cls, *args, **kwargs):
        return abs(cls.vector_cosine(*args, **kwargs)) == 1
    @classmethod
    def scaled_vectors(cls, *args, **kwargs):
        return cls.vector_cosine(*args, **kwargs) == 1
    @classmethod
    def inverted_vectors(cls, *args, **kwargs):
        return cls.vector_cosine(*args, **kwargs) == -1
    @classmethod
    def equivalent_vectors(cls, vector, other):
        vector_magnitude = cls.magnitude(vector)
        other_magnitude = cls.magnitude(other)
        cosine = cls.dot_product(vector, other) / (vector_magnitude * other_magnitude)
        return cosine == 1 and vector_magnitude == other_magnitude


class VectorTransformABC(ABC):
    @abstractmethod
    def truncate(): raise NotImplementedError
    @abstractmethod
    def expand(): raise NotImplementedError
