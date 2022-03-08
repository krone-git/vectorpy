from .abc import LineABC
from ..vector.vector3d import Vector3D


__all__ = (
    "line3d", "Line3D"
    )

class Line3DSingleton(LineABC):
    def new(a, b, c, x, y, z):
        return [float(x), float(a), float(y), float(b), float(z), float(c)]
    def from_points(point, other):
        x, y, z = point
        a, b, c = other
        return [float(x), a - x, float(y), b - y, float(z), c - z]
    def from_vector(vector, point):
        a, b, c = vector
        x, y, z = point
        return [float(x), float(a), float(y), float(b), float(z), float(c)]

    def axis(axis):
        line = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        line[axis * 2 + 1] = 1.0
        return line

    def set_line(line, other):
        line[0], line[1], line[2], line[3], line[4], line[5] = other
        return line

    def parametric_point(line, t):
        x, a, y, b, z, c = line
        return [x + t * a, y + t * b, z + t * c]

    def direction(line):
        x, a, y, b, z, c = line
        return Vector3D.new(a, b, c)
    def through_point(line):
        x, a, y, b, z, c = line
        return [x, y, z]

    def set_direction(line, vector):
        a, b, c = vector
        # line[1], line[3], line[5] = vector
        line[1] = a
        line[3] = b
        line[4] = c
        return line
    def set_through_point(line, point):
        x, y, z = point
        # line[0], line[2], line[4] = point
        line[0] = x
        line[2] = y
        line[4] = z
        return line

    def point_distance(line, point):
        vec3 = Vector3D
        x, a, y, b, z, c = line
        direction = vec3.new(a, b, c)
        vector = vec3.from_points([x, y, z], point)
        normal = vec3.cross_product(vector, direction)
        return vec3.magnitude(normal) / vec3.magnitude(direction)

    def line_distance(line, other):
        vec3 = Vector3D
        x, a, y, b, z, c = line
        q, i, r, j, s, k = other
        normal = vec3.cross_product(
            vec3.new(a, b, c), vec3.new(i, j, k)
            )
        unit = vec3.unit_vector(normal)
        vector = vec3d.from_points([x, y, z], [q, r, s])
        return abs(vec3d.dot_product(unit, vector))

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

    def line_cosine(line, other):
        vec3 = Vector3D
        x, a, y, b, z, c = line
        q, i, r, j, s, k = other
        return vec3.vector_cosine(
            vec3.new(a, b, c), vec3.new(i, j, k)
            )


line3d = Line3D = Line3DSingleton()
