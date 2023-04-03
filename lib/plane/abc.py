from abc import ABC, abstractmethod
from math import acos, pi


class PlaneSingletonABC(ABC):
    __slots__ = ()

    @abstractmethod
    def new(*args): raise NotImplementedError
    @classmethod
    def  __call__(cls, *args, **kwargs): return cls.new(*args, **kwargs)
    @abstractmethod
    def from_points(vertex, point, other): raise  NotImplementedError
    @abstractmethod
    def from_vector(vector, point): raise NotImplementedError
    @abstractmethod
    def from_line(line, point): raise NotImplementedError

    @staticmethod
    def copy(plane): return plane.copy()

    @abstractmethod
    def axis_plane(axis): raise NotImplementedError

    @abstractmethod
    def direction(plane): raise NotImplementedError
    @classmethod
    def normal(cls, *args, **kwargs): return cls.direction(*args, **kwargs)
    @abstractmethod
    def through_point(plane): raise NotImplementedError

    @abstractmethod
    def set_plane(plane, other): raise NotImplementedError
    @abstractmethod
    def set_direction(plane, normal): raise NotImplementedError
    @classmethod
    def set_normal(cls, *args, **kwargs): return cls.set_direction(*args, **kwargs)
    @abstractmethod
    def set_through_point(plane, point): raise NotImplementedError
    @abstractmethod
    def set_components(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def point_distance(plane, point): raise NotImplementedError

    @abstractmethod
    def plane_cosine(plane, other): raise NotImplementedError

    @classmethod
    def plane_angle(cls, *args, **kwargs):
        return acos(cls.plane_cosine(*args, **kwargs))
    @classmethod
    def inverse_plane_angle(cls, *args, **kwargs):
        return pi - cls.line_angle(*args, **kwargs)
    @classmethod
    def plane_angles(cls, *args, **kwargs):
        angle = cls.plane_angle(*args, **kwargs)
        return (angle, pi - angle)
    @classmethod
    def small_plane_angle(cls, *args, **kwargs):
        return min(cls.plane_angles(*args, **kwargs))
    @classmethod
    def large_plane_angles(cls, *args, **kwargs):
        return max(cls.plane_angles(*args, **kwargs))

    # @abstractmethod
    # def line_intersection(plane, line): raise NotImplementedError
    # @abstractmethod
    # def plane_intersection(plane, other): raise NotImplementedError

    # @abstractmethod
    # def intersects_point(plane, point): raise NotImplementedError
    # @abstractmethod
    # def intersects_line(plane, line): raise NotImplementedError
    # @abstractmethod
    # def intersects_plane(plane, other): raise NotImplementedError
    #
    # @abstractmethod
    # def perpendicular_planes(plane, other): raise NotImplementedError
    # @abstractmethod
    # def parallel_planes(cls, plane, other):
    #     raise NotImplementedError
