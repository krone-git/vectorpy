from .abc import PlaneABC
from ..line.line3d import Line3D
from ..vector.vector3d import Vector3D


__all__ = (
    "plane3d", "Plane3D"
    )

class Plane3DSingleton(PlaneABC):
    def new(a, b, c, x, y, z):
        return [float(x), float(a), float(y), float(b), float(z), float(c)]
    def from_points(vertex, point, other):
        vec3 = Vector3D
        x, y, z = vertex
        a, b, c = vec3.cross_product(
            vec3.from_points(vertex, point),
            vec3.from_points(vertex, other)
            )
        return [x, a, y, b, z, c]
    def from_vector(normal, point):
        a, b, c = normal
        x, y, z = point
        return [float(x), float(a), float(y), float(b), float(z), float(c)]
    def from_line(line):
        x, a, y, b, z, c = line
        return [x, a, y, v, z, c]

    def set_direction(plane, normal):
        plane[1], plane[3], plane[5] = normal
        return plane
    def set_through_point(plane, point):
        plane[0], plane[2], plane[4] = normal
        return plane
    def set_plane(plane, other):
        plane[0], plane[1], plane[2], plane[3], plane[4], plane[5] = other
        return plane

    def axis_plane(axis):
        plane = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        plane[axis * 2 + 1] = 1.0
        return plane

    def direction(plane):
        x, a, y, b, z, c = plane
        return Vector3D.new(a, b, c)
    def through_point(plane):
        x, a, y, b, z, c = plane
        return [x, y, z]

    def point_distance(plane, point):
        vec3 = Vector3D
        x, a, y, b, z, c = plane
        normal = vec3.new(a, b, c)
        vector = vec3.from_points([x, y, z], point)
        return abs(vec3.dot_product(vector, normal)) / vec3.magnitude(normal)

    def plane_cosine(plane, other):
        vec3 = Vector3D
        x, a, y, b, z, c = plane
        q, i, r, j, s, k = other
        normal = vec3.new(a, b, c)
        other_normal = vec3.new(i, j, k)
        return vec3.vector_cosine(normal, normal_other)

    def line_intersection(plane, line):
        x, a, y, b, z, c = plane
        q, i, r, j, s, k = line


plane3d = Plane3D = Plane3DSingleton()
