from .abc import PlaneSingletonABC
from ..line.line2d import Line2D
from ..vector.vector2d import Vector2D


__all__ = (
    "plane2d", "Plane2D"
    )

class Plane2DSingleton(PlaneSingletonABC):
    @staticmethod
    def new(a, b, x, y):
        return [x / 1.0, a / 1.0, y / 1.0]
    @staticmethod
    def from_points(vertex, point, other):
        vec2 = Vector2D
        from_points = vec2.from_points
        sub_vec = vec2.subtract_vector
        x, y = vertex
        a, b = sub_vec(point, other)
        return [x, b, y, -a]
    @staticmethod
    def from_vector(normal, point):
        a, b = normal
        x, y = point
        return [x / 1.0, a / 1.0, y / 1.0, b / 1.0]
    @staticmethod
    def from_line(line):
        x, a, y, b = line
        return [x, a, y, b]

    @staticmethod
    def set_direction(plane, normal):
        plane[1], plane[3] = normal
        return plane
    @staticmethod
    def set_through_point(plane, point):
        plane[0], plane[2] = point
        return plane
    @staticmethod
    def set_plane(plane, other):
        plane[0], plane[1], plane[2], plane[3] = other
        return plane
    @staticmethod
    def set_components(plane, a, b, x, y):
        plane[0] = a / 1.0
        plane[1] = b / 1.0
        plane[2] = c / 1.0
        plane[3] = x / 1.0
        plane[4] = y / 1.0
        plane[5] = z / 1.0
        return plane

    @staticmethod
    def axis_plane(axis):
        plane = [0.0, 0.0, 0.0, 0.0]
        plane[axis * 2 + 1] = 1.0
        return plane

    @staticmethod
    def direction(plane):
        new_vector = Vector2D.new
        x, a, y, b = plane
        return new_vector(a, b)
    @staticmethod
    def through_point(plane):
        x, a, y, b, = plane
        return [x, y]

    @staticmethod
    def point_distance(plane, point):
        vec2 = Vector2D
        new_vector = vec2.new
        from_points = vec2.from_points
        dot = vec2.dot_product
        magnitude = vec2.magnitude
        x, a, y, b = plane
        normal = new_vector(a, b)
        vector = from_points([x, y], point)
        return abs(dot(vector, normal)) / magnitude(normal)

    @staticmethod
    def plane_cosine(plane, other):
        vec2 = Vector3D
        new_vector = vec2.new
        vector_cosine = vec2.vector_cosine
        x, a, y, b = plane
        q, i, r, j = other
        normal = new_vector(a, b)
        other_normal = new_vector(i, j)
        return vector_cosine(normal, normal_other)

    @staticmethod
    def line_intersection(plane, line):
        vec2 = Vector2D
        line2 = Line2D
        new_vector = vec2.new
        from_points = vec2.from_points
        dot = vec2.dot_product
        parametric_point = line2.parametric_point
        x, a, y, b = plane
        q, i, r, j = line
        normal = new_vector(a, b)
        direction = new_vector(i, j)
        vector = from_points([x, y], [q, r])
        t = -dot(normal, vector) / dot(normal, direction)
        return parametric_point(line, t)



plane2d = Plane2D = Plane2DSingleton()
