from .abc import LineSingletonABC
from ..vector.vector3d import Vector3D


__all__ = (
    "line3d", "Line3D"
    )

class Line3DSingleton(LineSingletonABC):
    @staticmethod
    def new(a, b, c, x, y, z):
        return [x / 1.0, a / 1.0, y / 1.0, b / 1.0, z / 1.0, c / 1.0]
    @staticmethod
    def from_points(point, other):
        x, y, z = point
        a, b, c = other
        return [x / 1.0, a / 1.0 - x, y / 1.0, b / 1.0 - y, z / 1.0, c / 1.0 - z]
    @staticmethod
    def from_vector(vector, point):
        a, b, c = vector
        x, y, z = point
        return [x / 1.0, a / 1.0, y / 1.0, b / 1.0, z / 1.0, c / 1.0]

    @staticmethod
    def axis(axis):
        line = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        line[axis * 2 + 1] = 1.0
        return line

    @staticmethod
    def set_line(line, other):
        line[0], line[1], line[2], line[3], line[4], line[5] = other
        return line
    @staticmethod
    def set_components(line, a, b, c, x, y, z):
        line[0] = x / 1.0
        line[1] = a / 1.0
        line[2] = y / 1.0
        line[3] = b / 1.0
        line[4] = z / 1.0
        line[5] = c / 1.0
        return line

    @staticmethod
    def parametric_point(line, t):
        x, a, y, b, z, c = line
        return [x + t * a, y + t * b, z + t * c]

    @staticmethod
    def direction(line):
        x, a, y, b, z, c = line
        return Vector3D.new(a, b, c)
    @staticmethod
    def through_point(line):
        x, a, y, b, z, c = line
        return [x, y, z]

    @staticmethod
    def set_direction(line, vector):
        line[1], line[3], line[5] = vector
        return line
    @staticmethod
    def set_through_point(line, point):
        line[0], line[2], line[4] = point
        return line

    @staticmethod
    def point_distance(line, point):
        vec3 = Vector3D
        new_vector = vec3.new
        from_points = vec3.from_points
        cross = vec3.cross_product
        magnitude = vec3.magnitude
        x, a, y, b, z, c = line
        direction = new_vector(a, b, c)
        vector = from_points([x, y, z], point)
        normal = cross(vector, direction)
        return magnitude(normal) / magnitude(direction)

    @staticmethod
    def line_distance(line, other):
        vec3 = Vector3D
        cross = vec3.cross_product
        new_vector = vec3.new
        unit_vector = vec3.unit_vector
        from_points = vec3d.from_points
        dot = vec3d.dot_product
        x, a, y, b, z, c = line
        q, i, r, j, s, k = other
        normal = cross(new_vector(a, b, c), new_vector(i, j, k))
        unit = unit_vector(normal)
        vector = from_points([x, y, z], [q, r, s])
        return abs(dot_product(unit, vector))

    @classmethod
    def line_intersection(cls, line, other):
        x, a, y, b, z, c = line
        q, i, r, j, s, k = other
        if a == i:
            return None
        t = (q - x) / (a - i)
        line_tx , line_ty, line_tz = cls.parametric_point(line, t)
        other_tx, other_ty, other_tz = cls.parametric_point(other, t)
        if line_tx == other_tx and line_ty == other_ty and line_tz == other_tz:
            return [line_tx, line_ty, line_tz]
        else:
            return None

    @staticmethod
    def line_cosine(line, other):
        vec3 = Vector3D
        vector_cosine = vec3.vector_cosine
        new_vector = vec3.new
        x, a, y, b, z, c = line
        q, i, r, j, s, k = other
        return vector_cosine(
            new_vector(a, b, c), new_vector(i, j, k)
            )


line3d = Line3D = Line3DSingleton()
