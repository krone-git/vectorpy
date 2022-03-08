from abc import ABC, abstractmethod
from math import acos, pi


class LineABC(ABC):
    __slots__ = ()

    @abstractmethod
    def new(*args): raise NotImplementedError
    @classmethod
    def __call__(cls, *args, **kwargs): return cls.new(*args, **kwargs)
    @abstractmethod
    def from_points(point, other): raise NotImplementedError
    @abstractmethod
    def from_vector(vector, point): raise NotImplementedError

    @abstractmethod
    def axis(axis): raise NotImplementedError

    @abstractmethod
    def set_line(line, other): raise NotImplementedError
    def copy(line): return line.copy()

    @abstractmethod
    def parametric_point(line, t): raise NotImplementedError

    @abstractmethod
    def direction(line): raise NotImplementedError
    @abstractmethod
    def through_point(line): raise NotImplementedError

    @abstractmethod
    def set_direction(line, vector): raise NotImplementedError
    @abstractmethod
    def set_through_point(line, point): raise NotImplementedError

    @abstractmethod
    def point_distance(line, point): raise NotImplementedError
    @abstractmethod
    def line_distance(line,other): raise NotImplementedError

    @abstractmethod
    def line_intersection(line, other): raise NotImplementedError

    @classmethod
    def intersects_point(cls, *args, **kwargs):
        return cls.point_distance(*args, **kwargs) == 0
    @classmethod
    def intersects_line(cls, *args, **kwargs):
        return cls.line_distance(*args, **kwargs) == 0

    @abstractmethod
    def line_cosine(line, other): raise NotImplementedError

    @classmethod
    def line_angle(cls, *args, **kwargs):
        return acos(cls.line_cosine(*args, **kwargs))
    @classmethod
    def inverse_line_angle(cls, *args, **kwargs):
        return pi - cls.line_angle(*args, **kwargs)
    @classmethod
    def line_angles(cls, *args, **kwargs):
        angle = cls.line_angle(*args, **kwargs)
        return (angle, pi - angle)
    @classmethod
    def small_line_angle(cls, *args, **kwargs):
        return min(cls.line_angles(*args, **kwargs))
    @classmethod
    def large_line_angles(cls, *args, **kwargs):
        return max(cls.line_angles(*args, **kwargs))

    @classmethod
    def perpendicular_lines(cls, *args, **kwargs):
        return cls.line_cosine(*args, **kwargs) == 0
    @classmethod
    def parallel_lines(cls, *args, **kwargs):
        return abs(cls.line_cosine(*args, **kwargs)) == 1
