from .abc import PlaneSingletonABC
from ..line.line3d import Line3D
from ..vector.vector3d import Vector3D


__all__ = (
    "plane3d", "Plane3D"
    )

class Plane3DSingleton(PlaneSingletonABC):
    @staticmethod
    def new(a, b, c, x, y, z):
        return [x / 1.0, a / 1.0, y / 1.0, b / 1.0, z / 1.0, c / 1.0]
    @staticmethod
    def from_points(vertex, point, other):
        vec3 = Vector3D
        from_points = vec3.from_points
        cross = vec3.cross_product
        x, y, z = vertex
        a, b, c = cross(
            from_points(vertex, point),
            from_points(vertex, other)
            )
        return [x, a, y, b, z, c]
    @staticmethod
    def from_vector(normal, point):
        a, b, c = normal
        x, y, z = point
        return [x / 1.0, a / 1.0, y / 1.0, b / 1.0, z / 1.0, c / 1.0]
    @staticmethod
    def from_line(line):
        x, a, y, b, z, c = line
        return [x, a, y, b, z, c]

    @staticmethod
    def set_direction(plane, normal):
        plane[1], plane[3], plane[5] = normal
        return plane
    @staticmethod
    def set_through_point(plane, point):
        plane[0], plane[2], plane[4] = point
        return plane
    @staticmethod
    def set_plane(plane, other):
        plane[0], plane[1], plane[2], plane[3], plane[4], plane[5] = other
        return plane
    @staticmethod
    def set_components(plane, a, b, c, x, y, z):
        plane[0] = x / 1.0
        plane[1] = a / 1.0
        plane[2] = y / 1.0
        plane[3] = b / 1.0
        plane[4] = z / 1.0
        plane[5] = c / 1.0
        return plane

    @staticmethod
    def axis_plane(axis):
        plane = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        plane[axis * 2 + 1] = 1.0
        return plane

    @staticmethod
    def direction(plane):
        new_vector = Vector3D.new
        x, a, y, b, z, c = plane
        return new_vector(a, b, c)
    @staticmethod
    def through_point(plane):
        x, a, y, b, z, c = plane
        return [x, y, z]

    @staticmethod
    def point_distance(plane, point):
        vec3 = Vector3D
        new_vector = vec3.new
        from_points = vec3.from_points
        dot = vec3.dot_product
        magnitude = vec3.magnitude
        x, a, y, b, z, c = plane
        normal = new_vector(a, b, c)
        vector = from_points([x, y, z], point)
        return abs(dot(vector, normal)) / magnitude(normal)

    @staticmethod
    def plane_cosine(plane, other):
        vec3 = Vector3D
        new_vector = vec3.new
        vector_cosine = vec3.vector_cosine
        x, a, y, b, z, c = plane
        q, i, r, j, s, k = other
        normal = new_vector(a, b, c)
        other_normal = new_vector(i, j, k)
        return vector_cosine(normal, normal_other)

    @staticmethod
    def line_intersection(plane, line):
        vec3 = Vector3D
        line3 = Line3D
        new_vector = vec3.new
        from_points = vec3.from_points
        dot = vec3.dot_product
        parametric_point = line3.parametric_point
        x, a, y, b, z, c = plane
        q, i, r, j, s, k = line
        normal = new_vector(a, b, c)
        direction = new_vector(i, j, k)
        vector = from_points([x, y, z], [q, r, s])
        t = -dot(normal, vector) / dot(normal, direction)
        return parametric_point(line, t)


plane3d = Plane3D = Plane3DSingleton()
