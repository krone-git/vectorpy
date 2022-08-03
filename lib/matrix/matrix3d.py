from .abc import MatrixSingletonABC, MatrixLinearTransformSingletonABC, \
                    MatrixPerspectiveTransformSingletonABC
from ..vector.vector3d import Vector3D
from ..line.line3d import Line3D
from ..plane.plane3d import Plane3D
from math import cos, sin


__all__ = (
    "mat3d", "Matrix3D", "mat3dlt", "Matrix3DLinearTransform",
    "mat3dpt", "Matrix3DPerspectiveTransform"
    )

class Matrix3DSingleton(MatrixSingletonABC):
    @staticmethod
    def new(a, b, c, d, e, f, g, h, i):
        return [
            a / 1.0, b / 1.0, c / 1.0,
            d / 1.0, e / 1.0, f / 1.0,
            g / 1.0, h / 1.0, i / 1.0
            ]
    @staticmethod
    def from_row_vectors(vectors):
        row1, row2, row3 = vectors
        a, b, c = row1
        d, e, f = row2
        g, h, i = row3
        return [
            a / 1.0, b / 1.0, c / 1.0,
            d / 1.0, e / 1.0, f / 1.0,
            g / 1.0, h / 1.0, i / 1.0
            ]
    @staticmethod
    def from_column_vectors(vectors):
        column1, column2, column3 = vectors
        a, d, g = column1
        b, e, h = column2
        c, f, i = column3
        return [
            a / 1.0, b / 1.0, c / 1.0,
            d / 1.0, e / 1.0, f / 1.0,
            g / 1.0, h / 1.0, i / 1.0
            ]
    @staticmethod
    def from_basis(basis):
        a, e, i = basis
        return [a / 1.0, 0.0, 0.0, 0.0, e / 1.0, 0.0, 0.0, 0.0, i / 1.0]

    @staticmethod
    def zero_matrix():
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    @staticmethod
    def identity_matrix():
        return [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]

    @staticmethod
    def to_row_vectors(matrix):
        new_vector = Vector3D.new
        a, b, c, d, e, f, g, h, i = matrix
        return new_vector(a, b, c), new_vector(d, e, f), new_vector(g, h, i)
    @staticmethod
    def to_column_vectors(matrix):
        new_vector = Vector3D.new
        a, b, c, d, e, f, g, h, i = matrix
        return new_vector(a, d, g), new_vector(b, e, h), new_vector(c, f, i)
    @staticmethod
    def to_basis(matrix):
        new_vector = Vector3D.new
        a, _, _, _, e, _, _, _, i = matrix
        return new_vector(a, e, i)

    @staticmethod
    def get_component(matrix, column, row):
        return matrix[row * 3 + column]

    @staticmethod
    def columns(matrix):
        a, b, c, d, e, f, g, h, i = matrix
        return (a, d, f), (b, e, h), (c, f, i)
    @staticmethod
    def column(matrix, column): return matrix[column::3]
    @staticmethod
    def rows(matrix):
        a, b, c, d, e, f, g, h, i = matrix
        return (a, b, c), (c, d, e), (g, h, i)
    @staticmethod
    def row(matrix, row): return matrix[row * 3: (row + 1) * 3]

    @staticmethod
    def clear(matrix):
        matrix[0] = matrix[1] = matrix[2] = \
        matrix[3] = matrix[4] = matrix[5] = \
        matrix[6] = matrix[7] = matrix[8] = 0.0
        return matrix
    @staticmethod
    def reset(matrix):
        matrix[1] = matrix[2] = matrix[3] = \
        matrix[5] = matrix[6] = matrix[7] = 0.0
        matrix[0] = matrix[4] = matrix[8] = 1.0
        return matrix

    @staticmethod
    def set_component(matrix, column, row, value):
        matrix[row * 3 + column] = value / 1.0
        return matrix
    @staticmethod
    def set_components(matrix, a, b, c, d, e, f, g, h, i):
        matrix[0] = a / 1.0
        matrix[1] = b / 1.0
        matrix[2] = c / 1.0
        matrix[3] = d / 1.0
        matrix[4] = e / 1.0
        matrix[5] = f / 1.0
        matrix[6] = g / 1.0
        matrix[7] = h / 1.0
        matrix[8] = i / 1.0
        return matrix
    @staticmethod
    def set_row_vector(matrix, row, vector):
        index = row * 3
        matrix[index], matrix[index + 1], matrix[index + 2] = vector
        return matrix
    @staticmethod
    def set_row_components(matrix, row, a, b, c):
        index = row * 3
        matrix[index] = a / 1.0
        matrix[index + 1] = b / 1.0
        matrix[index + 2] = c / 1.0
        return matrix
    @staticmethod
    def set_column_vector(matrix, column, vector):
        matrix[column], matrix[3 + column], matrix[6 + column] = vector
        return matrix
    @staticmethod
    def set_column_components(matrix, column, a, b, c):
        matrix[column] = a / 1.0
        matrix[3 + column] = b / 1.0
        matrix[6 + column] = c / 1.0
        return matrix
    @staticmethod
    def set_matrix(matrix, other):
        matrix[0], matrix[1], matrix[2], \
        matrix[3], matrix[4], matrix[5], \
        matrix[6], matrix[7], matrix[8] = other
        return matrix

    @staticmethod
    def determinant(matrix):
        a, b, c, d, e, f, g, h, i = matrix
        return a * (e * i - f * h) - b * (d * i - g * f) + c (d * h - e * g)

    @staticmethod
    def add_scalar(matrix, scalar):
        a, b, c, d, e, f, g, h, i = matrix
        return [
            a + scalar, b + scalar, c + scalar,
            d + scalar, e + scalar, f + scalar,
            g + scalar, h + scalar, i + scalar,
            ]
    @staticmethod
    def iadd_scalar(matrix, scalar):
        matrix[0] += scalar
        matrix[1] += scalar
        matrix[2] += scalar
        matrix[3] += scalar
        matrix[4] += scalar
        matrix[5] += scalar
        matrix[6] += scalar
        matrix[7] += scalar
        matrix[8] += scalar
        return matrix
    @staticmethod
    def add_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i = matrix
        j, k, l, m, n, o, p, q, r = other
        return [a + j, b + k, c + l, d + m, e + n, f + o, g + p, h + q, i + r]
    @staticmethod
    def iadd_matrix(matrix, other):
        j, k, l, m, n, o, p, q, r = other
        matrix[0] += j
        matrix[1] += k
        matrix[2] += l
        matrix[3] += m
        matrix[4] += n
        matrix[5] += o
        matrix[6] += p
        matrix[7] += q
        matrix[8] += r
        return matrix

    @staticmethod
    def subtract_scalar(matrix, scalar):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        return [
            a - scalar, b - scalar, c - scalar,
            d - scalar, e - scalar, f - scalar,
            g - scalar, h - scalar, i - scalar
            ]
    @staticmethod
    def isubtract_scalar(matrix, scalar):
        matrix[0] -= scalar
        matrix[1] -= scalar
        matrix[2] -= scalar
        matrix[3] -= scalar
        matrix[4] -= scalar
        matrix[5] -= scalar
        matrix[6] -= scalar
        matrix[7] -= scalar
        matrix[8] -= scalar
        return matrix
    @staticmethod
    def subtract_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i = matrix
        j, k, l, m, n, o, p, q, r = other
        return [a - j, b - k, c - l, d - m, e - n, f - o, g - p, h - q, i - r]
    @staticmethod
    def isubtract_matrix(matrix, other):
        j, k, l, m, n, o, p, q, r = other
        matrix[0] -= j
        matrix[1] -= k
        matrix[2] -= l
        matrix[3] -= m
        matrix[4] -= n
        matrix[5] -= o
        matrix[6] -= p
        matrix[7] -= q
        matrix[8] -= r
        return matrix

    @staticmethod
    def multiply_scalar(matrix, scalar):
        a, b, c, d, e, f, g, h, i = matrix
        return [
            a * scalar, b * scalar, c * scalar,
            d * scalar, e * scalar, f * scalar,
            g * scalar, h * scalar, i * scalar
            ]
    @staticmethod
    def imultiply_scalar(matrix, scalar):
        matrix[0] *= scalar
        matrix[1] *= scalar
        matrix[2] *= scalar
        matrix[3] *= scalar
        matrix[4] *= scalar
        matrix[5] *= scalar
        matrix[6] *= scalar
        matrix[7] *= scalar
        matrix[8] *= scalar
        return matrix
    @staticmethod
    def multiply_vector(matrix, vector):
        new_vector = Vector3D.new
        a, b, c, d, e, f, g, h, i = matrix
        p, q, r = vector
        return new_vector(
            a * p + b * q + c * r,
            d * p + e * q + f * r,
            g * p + h * q + i * r
            )
    @staticmethod
    def imultiply_vector(matrix, vector):
        set_components = Vector3D.set_components
        a, b, c, d, e, f, g, h, i = matrix
        p, q, r = vector
        return set_components(
            vector,
            a * p + b * q + c * r,
            d * p + e * q + f * r,
            g * p + h * q + i * r
            )
    @staticmethod
    def multiply_line(matrix, line):
        line3 = Line3D
        get_direction = line3.direction
        get_point = line3.through_point
        new_line = line3.new
        a, b, c, d, e, f, g, h, i = matrix
        p, q, r = get_direction(line)
        x, y, z = get_point(line)
        return new_line(
            a * p + b * q + c * r,
            d * p + e * q + f * r,
            g * p + h * q + i * r,
            a * x + b * y + c * z,
            d * x + e * y + f * z,
            g * x + h * y + i * z
            )
    @staticmethod
    def imultiply_line(matrix, line):
        line3 = Line3D
        get_direction = line3.direction
        get_point = line3.through_point
        set_components = line3.set_components
        a, b, c, d, e, f, g, h, i = matrix
        p, q, r = get_direction(line)
        x, y, z = get_point(line)
        return set_components(
            line,
            a * p + b * q + c * r,
            d * p + e * q + f * r,
            g * p + h * q + i * r,
            a * x + b * y + c * z,
            d * x + e * y + f * z,
            g * x + h * y + i * z
            )
    @staticmethod
    def multiply_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        new_line = plane3.new
        a, b, c, d, e, f, g, h, i = matrix
        p, q, r = get_direction(plane)
        x, y, z = get_point(plane)
        return new_plane(
            a * p + b * q + c * r,
            d * p + e * q + f * r,
            g * p + h * q + i * r,
            a * x + b * y + c * z,
            d * x + e * y + f * z,
            g * x + h * y + i * z
            )
    @staticmethod
    def imultiply_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        set_components = plane3.set_components
        a, b, c, d, e, f, g, h, i = matrix
        p, q, r = get_direction(plane)
        x, y, z = get_point(plane)
        return set_components(
            plane,
            a * p + b * q + c * r,
            d * p + e * q + f * r,
            g * p + h * q + i * r,
            a * x + b * y + c * z,
            d * x + e * y + f * z,
            g * x + h * y + i * z
            )
    @staticmethod
    def multiply_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i = matrix
        j, k, l, m, n, o, p, q, r = other
        return [
            a * j + b * m + c * p, a * k + b * n + c * q, a * l + b * o + c * r,
            d * j + e * m + f * p, d * k + e * n + f * q, d * l + e * o + f * r,
            g * j + h * m + i * p, g * k + h * n + i * q, g * l + h * o + i * r,
            ]
    @staticmethod
    def imultiply_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i = matrix
        j, k, l, m, n, o, p, q, r = other
        matrix[0] = a * j + b * m + c * p
        matrix[1] = a * k + b * n + c * q
        matrix[2] = a * l + b * o + c * r
        matrix[3] = d * j + e * m + f * p
        matrix[4] = d * k + e * n + f * q
        matrix[5] = d * l + e * o + f * r
        matrix[6] = g * j + h * m + i * p
        matrix[7] = g * k + h * n + i * q
        matrix[8] = g * l + h * o + i * r
        return matrix

    @staticmethod
    def divide_scalar(matrix, scalar):
        a, b, c, d, e, f, g, h, i = matrix
        return [
            a / scalar, b / scalar, c / scalar,
            d / scalar, e / scalar, f / scalar,
            g / scalar, h / scalar, i / scalar
            ]
    @staticmethod
    def idivide_scalar(matrix, scalar):
        matrix[0] /= scalar
        matrix[1] /= scalar
        matrix[2] /= scalar
        matrix[3] /= scalar
        matrix[4] /= scalar
        matrix[5] /= scalar
        matrix[6] /= scalar
        matrix[7] /= scalar
        matrix[8] /= scalar
        return matrix

mat3d = Matrix3D = Matrix3DSingleton()


class Matrix3DLinearTransformSingleton(MatrixLinearTransformSingletonABC):
    @staticmethod
    def new(a, b, c, d, e, f, g, h, i, j, k, l):
        return [
            a / 1.0, b / 1.0, c / 1.0, d / 1.0,
            e / 1.0, f / 1.0, g / 1.0, h / 1.0,
            i / 1.0, j / 1.0, k / 1.0, l / 1.0
            ]

    @staticmethod
    def zero_matrix():
        return [
            0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0
            ]
    @staticmethod
    def identity_matrix():
        return [
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0
            ]

    @staticmethod
    def from_base_matrix(matrix):
        a, b, c, d, e, f, g, h, i = matrix
        return [a, b, c, 0.0, d, e, f, 0.0, g, h, i, 0.0]
    @staticmethod
    def to_base_matrix(matrix):
        a, b, c, _, d, e, f, _, g, h, i, _ = matrix
        return [a, b, c, d, e, f, g, h, i]
    @staticmethod
    def base_matrix_to_linear_transform(matrix):
        a, b, c, d, e, f, g, h, i = matrix
        matrix.clear()
        matrix.extend(
            [a, b, c, 0.0, d, e, f, 0.0, g, h, i, 0.0]
            )
        return matrix

    @staticmethod
    def get_component(matrix, column, row):
        return matrix[row * 4 + column]

    @staticmethod
    def column(matrix, column): return matrix[column::4]
    @staticmethod
    def columns(matrix):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        return (a, e, i), (b, f, j), (c, g, k), (d, h, l)

    @staticmethod
    def rows(matrix):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        return (a, b, c, d), (e, f, g, h), (i, j, k, l)
    @staticmethod
    def row(matrix, row): return matrix[row * 4: (row + 1) * 4]

    @staticmethod
    def clear(matrix):
        matrix[0] = matrix[1] = matrix[2] = matrix[3] = \
        matrix[4] = matrix[5] = matrix[6] = matrix[7] = \
        matrix[8] = matrix[9] = matrix[10] = matrix[11] = 0.0
        return matrix

    @staticmethod
    def reset(matrix):
        matrix[1] = matrix[2] = matrix[3] = \
        matrix[4] = matrix[6] = matrix[7] = \
        matrix[8] = matrix[9] = matrix[11] = 0.0
        matrix[0] = matrix[5] = matrix[10] = 1.0
        return matrix

    @staticmethod
    def set_component(matrix, column, row, value):
        matrix[row * 4 + column] = value / 1.0
        return matrix
    @staticmethod
    def set_components(matrix, a, b, c, d, e, f, g, h, i, j, k, l):
        matrix[0] = a / 1.0
        matrix[1] = b / 1.0
        matrix[2] = c / 1.0
        matrix[3] = d / 1.0
        matrix[4] = e / 1.0
        matrix[5] = f / 1.0
        matrix[6] = g / 1.0
        matrix[7] = h / 1.0
        matrix[8] = i / 1.0
        matrix[9] = j / 1.0
        matrix[10] = k / 1.0
        matrix[11] = l / 1.0
        return matrix
    @staticmethod
    def set_column_vector(matrix, column, vector):
        matrix[column], matrix[4 + column], matrix[8 + column] = vector
        return matrix
    @staticmethod
    def set_column_components(matrix, column, a, b, c):
        matrix[column] = a / 1.0
        matrix[4 + column] = b / 1.0
        matrix[8 + column] = c / 1.0
        return matrix
    @staticmethod
    def set_row_vector(matrix, row, vector):
        index = row * 4
        matrix[index], matrix[index + 1], matrix[index + 2], matrix[index + 3] = vector
        return matrix
    @staticmethod
    def set_row_components(matrix, row, a, b, c, d):
        index = row * 4
        matrix[index] = a / 1.0
        matrix[index + 1] = b / 1.0
        matrix[index + 2] = c / 1.0
        matrix[index + 3] = d / 1.0
        return matrix
    @staticmethod
    def set_matrix(matrix, other):
        matrix[0], matrix[1], matrix[2], matrix[3], \
        matrix[4], matrix[5], matrix[6], matrix[7], \
        matrix[8], matrix[9], matrix[10], matrix[11] = other
        return matrix

    @staticmethod
    def determinant(matrix): raise NotImplementedError

    @staticmethod
    def rotation_xz(theta):
        sint, cost = sin(theta), cos(theta)
        return [
            cost, 0.0, sint, 0.0,
            0.0, 1.0, 0.0, 0.0,
            -sint, 0.0, cost, 0.0
            ]
    @staticmethod
    def set_rotation_xz(matrix, theta):
        sint, cost = sin(theta), cos(theta)
        matrix[0] = matrix[10] = cost
        matrix[2] = sint
        matrix[8] = -sint
        return matrix

    @staticmethod
    def rotation_xy(theta):
        sint, cost = sin(theta), cos(theta)
        return [
            cost, -sint, 0.0, 0.0,
            sint, cost, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0
            ]
    @staticmethod
    def set_rotation_xy(matrix, theta):
        sint, cost = sin(theta), cos(theta)
        matrix[0] = matrix[5] = cost
        matrix[1] = -sint
        matrix[4] = sint
        return matrix

    @staticmethod
    def rotation_yz(theta):
        sint, cost = sin(theta), cos(theta)
        return [
            1.0, 0.0, 0.0, 0.0,
            0.0, cost, -sint, 0.0,
            0.0, sint, cost, 0.0
            ]
    @staticmethod
    def set_rotation_yz(matrix, theta):
        sint, cost = sin(theta), cos(theta)
        matrix[5] = matrix[10] = cost
        matrix[6] = -sint
        matrix[9] = sint
        return matrix

    @staticmethod
    def rotation_xzy(yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        return [
            c2 * c3, -s2, c2 * s3, 0.0,
            s1 * s3 + c1 * c3 * s2, c1 * c2, c1 * s2 * s3 - c3 * s1, 0.0,
            c3 * s1 * s2 - c1 * s3, c2 * s1, c1 * c3 + s1 * s2 * s3, 0.0
            ]
    @staticmethod
    def set_rotation_xzy(matrix, yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c2 * c3
        matrix[1] = -s2
        matrix[2] = c2 * s3
        matrix[4] = s1 * s3 + c1 * c3 * s2
        matrix[5] = c1 * c2
        matrix[6] = c1 * s2 * s3 - c3 * s1
        matrix[8] = c3 * s1 * s2 - c1 * s3
        matrix[9] = c2 * s1
        matrix[10] = c1 * c3 + s1 * s2 * s3
        return matrix

    @staticmethod
    def rotation_xyz(yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        return [
            c2 * c3, -c2 * s3, s2, 0.0,
            c1 * s3 + c3 * s1 * s2, c1 * c3 - s1 * s2 * s3, - c2 * s1, 0.0,
            s1 * s3 - c1 * c3 * s2, c3 * s1 + c1 * s2 * s3, c1 * c2, 0.0
            ]
    @staticmethod
    def set_rotation_xyz(matrix, yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c2 * c3
        matrix[1] = -c2 * s3
        matrix[2] = s2
        matrix[4] = c1 * s3 + c3 * s1 * s2
        matrix[5] = c1 * c3 - s1 * s2 * s3
        matrix[6] = - c2 * s1
        matrix[8] = s1 * s3 - c1 * c3 * s2
        matrix[9] = c3 * s1 + c1 * s2 * s3
        matrix[10] = c1 * c2
        return matrix

    @staticmethod
    def rotation_yxz(yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c3 + s1 * s2 * s3, c3 * s1 * s2 - c1 * s3, c2 * s1, 0.0,
            c2 * s3, c2 * c3, -s2, 0.0,
            c1 * s2 * s3 - c3 * s1, c1 * c3 * s2 + s1 * s3, c1 * c2, 0.0
            ]
    @staticmethod
    def set_rotation_yxz(matrix, yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c3 + s1 * s2 * s3
        matrix[1] = c3 * s1 * s2 - c1 * s3
        matrix[2] = c2 * s1
        matrix[4] = c2 * s3
        matrix[5] = c2 * c3
        matrix[6] = -s2
        matrix[8] = c1 * s2 * s3 - c3 * s1
        matrix[9] = c1 * c3 * s2 + s1 * s3
        matrix[10] = c1 * c2
        return matrix

    @staticmethod
    def rotation_yzx(yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c2, s1 * s3 - c1 * c3 * s2, c3 * s1 + c1 * s2 * s3, 0.0,
            s2, c2 * c3, -c2 * s3, 0.0,
            -c2 * s1, c1 * s3 + c3 * s1 * s2, c1 * c3 - s1 * s2 * s3, 0.0
            ]
    @staticmethod
    def set_rotation_yzx(matrix, yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c2
        matrix[1] = s1 * s3 - c1 * c3 * s2
        matrix[2] = c3 * s1 + c1 * s2 * s3
        matrix[4] = s2
        matrix[5] = c2 * c3
        matrix[6] = -c2 * s3
        matrix[8] = -c2 * s1
        matrix[9] = c1 * s3 + c3 * s1 * s2
        matrix[10] = c1 * c3 - s1 * s2 * s3
        return matrix

    @staticmethod
    def rotation_zxy(yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c2, c1 * s2 * s3 - c3 * s1, s1 * s3 + c1 * c3 * s2, 0.0,
            c2 * s1, c1 * c3 + s1 * s2 * s3, c3 * s1 * s2 - c1 * s3, 0.0,
            -s2, c2 * s3, c2 * c3, 0.0
            ]
    @staticmethod
    def set_rotation_zxy(matrix, yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c2
        matrix[1] = c1 * s2 * s3 - c3 * s1
        matrix[2] = s1 * s3 + c1 * c3 * s2
        matrix[4] = c2 * s1
        matrix[5] = c1 * c3 + s1 * s2 * s3
        matrix[6] = c3 * s1 * s2 - c1 * s3
        matrix[8] = -s2
        matrix[9] = c2 * s3
        matrix[10] = c2 * c3
        return matrix

    @staticmethod
    def rotation_zyx(yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c3 - s1 * s2 * s3, -c2 * s1, c1 * s3 + c3 * s1 * s2, 0.0,
            c3 * s1 + c1 * s2 * s3, c1 * c2, s1 * s3 - c1 * c3 * s2, 0.0,
            -c2 * s3, s2, c2 * c3, 0.0
            ]
    @staticmethod
    def set_rotation_zyx(matrix, yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c3 - s1 * s2 * s3
        matrix[1] = -c2 * s1
        matrix[2] = c1 * s3 + c3 * s1 * s2
        matrix[4] = c3 * s1 + c1 * s2 * s3
        matrix[5] = c1 * c2
        matrix[6] = s1 * s3 - c1 * c3 * s2
        matrix[8] = -c2 * s3
        matrix[9] = s2
        matrix[10] = c2 * c3
        return matrix

    @classmethod
    def rotation(cls, *args, **kwargs): return cls.rotation_xyz(*args, **kwargs)
    @classmethod
    def set_rotation(cls, *args, **kwargs):
        return cls.set_rotation_xyz(*args, **kwargs)

    @staticmethod
    def reflection(xz, xy, yz):
        return [
            -1.0 if yz else 1.0, 0.0, 0.0, 0.0,
            0.0, -1.0 if xz else 1.0, 0.0, 0.0,
            0.0, 0.0, -1.0 if xy else 1.0, 0.0
            ]
    @staticmethod
    def set_reflection(matrix, xz, xy, yz):
        matrix[0] = -1.0 if yz else 1.0
        matrix[5] = -1.0 if xz else 1.0
        matrix[10] = -1.0 if xy else 1.0
        return matrix

    @staticmethod
    def scale(x_scale, y_scale, z_scale):
        return [
            x_scale / 1.0, 0.0, 0.0, 0.0,
            0.0, y_scale / 1.0, 0.0, 0.0,
            0.0, 0.0, z_scale / 1.0, 0.0
            ]
    @staticmethod
    def set_scale(matrix, x_scale, y_scale, z_scale):
        matrix[0] = x_scale / 1.0
        matrix[5] = y_scale / 1.0
        matrix[10] = z_scale / 1.0
        return matrix

    @staticmethod
    def shear_x(yx, zx):
        return [
            1.0, 0.0, 0.0, 0.0,
            yx / 1.0, 1.0, 0.0, 0.0,
            zx / 1.0, 0.0, 1.0, 0.0
            ]
    @staticmethod
    def set_shear_x(matrix, yx, zx):
        matrix[4] = yx / 1.0
        matrix[8] = zx / 1.0
        return matrix

    @staticmethod
    def shear_y(xy, zy):
        return [
            1.0, xy / 1.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, zy / 1.0, 1.0, 0.0
            ]
    @staticmethod
    def set_shear_y(matrix, xy, zy):
        matrix[1] = xy / 1.0
        matrix[9] = zy / 1.0
        return matrix

    @staticmethod
    def shear_z(xz, yz):
        return [
            1.0, 0.0, xz / 1.0, 0.0,
            0.0, 1.0, yz / 1.0, 0.0,
            0.0, 0.0, 1.0, 0.0
            ]
    @staticmethod
    def set_shear_z(matrix, xz, yz):
        matrix[2] = xz / 1.0
        matrix[6] = yz / 1.0
        return matrix

    @staticmethod
    def shear(yx, zx, xy, zy, xz, yz):
        return [
            1.0, xy / 1.0, xz / 1.0, 0.0,
            yx / 1.0, 1.0, yz / 1.0, 0.0,
            zx / 1.0, zy / 1.0, 1.0, 0.0
            ]
    @staticmethod
    def set_shear(matrix, yx, zx, xy, zy, xz, yz):
        matrix[4] = yx / 1.0
        matrix[8] = zx / 1.0
        matrix[1] = xy / 1.0
        matrix[9] = zy / 1.0
        matrix[2] = xz / 1.0
        matrix[6] = yz / 1.0
        return matrix

    @staticmethod
    def translation(x, y, z):
        return [
            1.0, 0.0, 0.0, x / 1.0,
            0.0, 1.0, 0.0, y / 1.0,
            0.0, 0.0, 1.0, z / 1.0
            ]
    @staticmethod
    def set_translation(matrix, x, y, z):
        matrix[3] = x / 1.0
        matrix[7] = y / 1.0
        matrix[11] = z / 1.0
        return matrix

    @staticmethod
    def add_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        A, B, C, D, E, F, G, H, I, J, K, L = other
        return [
            a + A, b + B, c + C, d + D,
            e + E, f + F, g + G, h + H,
            i + I, j + J, k + K, l + L
            ]
    @staticmethod
    def iadd_matrix(matrix, other):
        A, B, C, D, E, F, G, H, I, J, K, L = other
        matrix[0] += A
        matrix[1] += B
        matrix[2] += C
        matrix[3] += D
        matrix[4] += E
        matrix[5] += F
        matrix[6] += G
        matrix[7] += H
        matrix[8] += I
        matrix[9] += J
        matrix[10] += K
        matrix[11] += L
        return matrix

    @staticmethod
    def subtract_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        A, B, C, D, E, F, G, H, I, J, K, L = other
        return [
            a - A, b - B, c - C, d - D,
            e - E, f - F, g - G, h - H,
            i - I, j - J, k - K, l - L
            ]
    @staticmethod
    def isubtract_matrix(matrix, other):
        A, B, C, D, E, F, G, H, I, J, K, L = other
        matrix[0] -= A
        matrix[1] -= B
        matrix[2] -= C
        matrix[3] -= D
        matrix[4] -= E
        matrix[5] -= F
        matrix[6] -= G
        matrix[7] -= H
        matrix[8] -= I
        matrix[9] -= J
        matrix[10] -= K
        matrix[11] -= L
        return matrix

    @staticmethod
    def transform_vector(matrix, vector):
        new_vector = Vector3D.new
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        x, y, z = vector
        return new_vector(
            a * x + b * y + c * z + d,
            e * x + f * y + g * z + h,
            i * x + j * y + k * z + l
            )
    @staticmethod
    def itransform_vector(matrix, vector):
        new_vector = Vector3D.new
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        x, y, z = vector
        other = new_vector(
            a * x + b * y + c * z + d,
            e * x + f * y + g * z + h,
            i * x + j * y + k * z + l
            )
        return vec3.set_vector(vector, other)

    @staticmethod
    def transform_line(matrix, line):
        line3 = Line3D
        get_direction = line3.direction
        get_point = line3.through_point
        new_line = line3.new
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(line)
        x, y, z = get_point(line)
        return new_line(
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )
    @staticmethod
    def itransform_line(matrix, line):
        line3 = Line3D
        get_direction = line3.direction
        get_point = line3.through_point
        set_components = line3.set_components
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(line)
        x, y, z = get_point(line)
        return set_components(
            line,
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )

    @staticmethod
    def transform_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        new_line = plane3.new
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(plane)
        x, y, z = get_point(plane)
        return new_plane(
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )
    @staticmethod
    def itransform_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        set_components = plane3.set_components
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(plane)
        x, y, z = get_point(plane)
        return set_components(
            plane,
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )

    @staticmethod
    def compile(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        A, B, C, D, E, F, G, H, I, J, K, L = other
        return [
            a * A + b * E + c * I, a * B + b * F + c * J,
            a * C + b * G + c * K, a * D + b * H + c * L + d,
            e * A + f * E + g * I, e * B + f * F + g * J,
            e * C + f * G + g * K, e * D + f * H + g * L + h,
            i * A + j * E + k * I, i * B + j * F + k * J,
            i * C + j * G + k * K, i * D + j * H + k * L + l
            ]
    @staticmethod
    def icompile(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        A, B, C, D, E, F, G, H, I, J, K, L = other
        matrix[0] = a * A + b * E + c * I
        matrix[1] = a * B + b * F + c * J
        matrix[2] = a * C + b * G + c * K
        matrix[3] = a * D + b * H + c * L + d
        matrix[4] = e * A + f * E + g * I
        matrix[5] = e * B + f * F + g * J
        matrix[6] = e * C + f * G + g * K
        matrix[7] = e * D + f * H + g * L + h
        matrix[8] = i * A + j * E + k * I
        matrix[9] = i * B + j * F + k * J
        matrix[10] = i * C + j * G + k * K
        matrix[11] = i * D + j * H + k * L + l
        return matrix

mat3dlt = Matrix3DLinearTransform = Matrix3DLinearTransformSingleton()


class Matrix3DPerspectiveTransformSingleton(MatrixPerspectiveTransformSingletonABC):
    @staticmethod
    def new(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        return [
            a / 1.0, b / 1.0, c / 1.0, d / 1.0,
            e / 1.0, f / 1.0, g / 1.0, h / 1.0,
            i / 1.0, j / 1.0, k / 1.0, l / 1.0,
            m / 1.0, n / 1.0, o / 1.0, p / 1.0
            ]

    @staticmethod
    def zero_matrix():
        return [
            0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def identity_matrix():
        return [
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def orthogonal_perspective():
        return [
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]

    @staticmethod
    def from_base_matrix(matrix):
        a, b, c, d, e, f, g, h, i = matrix
        return [a, b, c, 0.0, d, e, f, 0.0, g, h, i, 0.0, 0.0, 0.0, 0.0, 1.0]
    @staticmethod
    def from_linear_transform(matrix):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        return [a, b, c, d, e, f, g, h, i, j, k, l, 0.0, 0.0, 0.0, 1.0]

    @staticmethod
    def to_base_matrix(matrix):
        a, b, c, _, d, e, f, _, g, h, i, _, _, _, _, _ = matrix
        return [a, b, c, d, e, f, g, h, i]

    @staticmethod
    def base_matrix_to_linear_transform(*args, **kwargs):
        return Matrix3DLinearTransformSingleton.base_matrix_to_linear_transform(*args, **kwargs)
    @staticmethod
    def base_matrix_to_perspective_transform(matrix):
        a, b, c, d, e, f, g, h, i = matrix
        matrix.clear()
        matrix.extend(
            [a, b, c, 0.0, d, e, f, 0.0, g, h, i, 0.0, 0.0, 0.0, 0.0, 1.0]
            )
        return matrix
    @staticmethod
    def linear_transform_to_perspective_transform(matrix):
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        matrix.clear()
        matrix.extend(
            [a, b, c, d, e, f, g, h, i, j, k, l, 0.0, 0.0, 0.0, 1.0]
            )
        return matrix

    @staticmethod
    def get_component(matrix, column, row):
        return matrix[row * 4 + column]

    @staticmethod
    def column(matrix, column): return matrix[column::4]
    @staticmethod
    def columns(matrix):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        return (a, e, i, m), (b, f, j, n), (c, g, k, o), (d, h, l, p)

    @staticmethod
    def rows(matrix):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        return (a, b, c, d), (e, f, g, h), (i, j, k, l), (m, n, o, p)
    @staticmethod
    def row(matrix, row): return matrix[row * 4: (row + 1) * 4]

    @staticmethod
    def set_component(matrix, column, row, value):
        matrix[row * 4 + column] = value / 1.0
        return matrix
    @staticmethod
    def set_components(matrix, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        matrix[0] = a / 1.0
        matrix[1] = b / 1.0
        matrix[2] = c / 1.0
        matrix[3] = d / 1.0
        matrix[4] = e / 1.0
        matrix[5] = f / 1.0
        matrix[6] = g / 1.0
        matrix[7] = h / 1.0
        matrix[8] = i / 1.0
        matrix[9] = j / 1.0
        matrix[10] = k / 1.0
        matrix[11] = l / 1.0
        matrix[12] = m / 1.0
        matrix[13] = n / 1.0
        matrix[14] = o / 1.0
        matrix[15] = p / 1.0
        return matrix
    @staticmethod
    def set_column_vector(matrix, column, vector):
        matrix[column], matrix[4 + column], \
        matrix[8 + column], matrix[12 + column] = vector
        return matrix
    @staticmethod
    def set_column_components(matrix, column, a, b, c, d):
        matrix[column] = a / 1.0
        matrix[4 + column] = b / 1.0
        matrix[8 + column] = c / 1.0
        matrix[12 + column] = d / 1.0
        return matrix
    @staticmethod
    def set_row_vector(matrix, row, vector):
        index = row * 4
        matrix[index], matrix[index + 1], \
        matrix[index + 2], matrix[index + 3] = vector
        return matrix
    @staticmethod
    def set_row_components(matrix, row, a, b, c, d):
        index = row * 4
        matrix[index] = a / 1.0
        matrix[index + 1] = b / 1.0
        matrix[index + 2] = c / 1.0
        matrix[index + 3] = d / 1.0
        return matrix
    @staticmethod
    def set_matrix(matrix, other):
        matrix[0], matrix[1], matrix[2], matrix[3], \
        matrix[4], matrix[5], matrix[6], matrix[7], \
        matrix[8], matrix[9], matrix[10], matrix[11], \
        matrix[12], matrix[13], matrix[14], matrix[15] = other
        return matrix

    @staticmethod
    def clear(matrix):
        matrix[0] = matrix[1] = matrix[2] = matrix[3] = \
        matrix[4] = matrix[5] = matrix[6] = matrix[7] = \
        matrix[8] = matrix[9] = matrix[10] = matrix[11] = \
        matrix[12] = matrix[13] = matrix[14] = 0.0
        matrix[15] = 1.0
        return matrix

    @staticmethod
    def reset(matrix):
        matrix[1] = matrix[2] = matrix[3] = \
        matrix[4] = matrix[6] = matrix[7] = \
        matrix[8] = matrix[9] = matrix[11] = \
        matrix[12] = matrix[13] = matrix[14] = 0.0
        matrix[0] = matrix[5] = matrix[10] = matrix[15] = 1.0
        return matrix

    @staticmethod
    def determinant(matrix): raise NotImplementedError

    @staticmethod
    def perspective(): raise NotImplementedError
    @staticmethod
    def set_perspective(): raise NotImplementedError

    @staticmethod
    def rotation_xz(theta):
        sint, cost = sin(theta), cos(theta)
        return [
            cost, 0.0, sint, 0.0,
            0.0, 1.0, 0.0, 0.0,
            -sint, 0.0, cost, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_xz(matrix, theta):
        sint, cost = sin(theta), cos(theta)
        matrix[0] = matrix[10] = cost
        matrix[2] = sint
        matrix[8] = -sint
        return matrix

    @staticmethod
    def rotation_xy(theta):
        sint, cost = sin(theta), cos(theta)
        return [
            cost, -sint, 0.0, 0.0,
            sint, cost, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_xy(matrix, theta):
        sint, cost = sin(theta), cos(theta)
        matrix[0] = matrix[5] = cost
        matrix[1] = -sint
        matrix[4] = sint
        return matrix

    @staticmethod
    def rotation_yz(theta):
        sint, cost = sin(theta), cos(theta)
        return [
            1.0, 0.0, 0.0, 0.0,
            0.0, cost, -sint, 0.0,
            0.0, sint, cost, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_yz(matrix, theta):
        sint, cost = sin(theta), cos(theta)
        matrix[5] = matrix[10] = cost
        matrix[6] = -sint
        matrix[9] = sint
        return matrix

    @staticmethod
    def rotation_xzy(yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        return [
            c2 * c3, -s2, c2 * s3, 0.0,
            s1 * s3 + c1 * c3 * s2, c1 * c2, c1 * s2 * s3 - c3 * s1, 0.0,
            c3 * s1 * s2 - c1 * s3, c2 * s1, c1 * c3 + s1 * s2 * s3, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_xzy(matrix, yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c2 * c3
        matrix[1] = -s2
        matrix[2] = c2 * s3
        matrix[4] = s1 * s3 + c1 * c3 * s2
        matrix[5] = c1 * c2
        matrix[6] = c1 * s2 * s3 - c3 * s1
        matrix[8] = c3 * s1 * s2 - c1 * s3
        matrix[9] = c2 * s1
        matrix[10] = c1 * c3 + s1 * s2 * s3
        return matrix

    @staticmethod
    def rotation_xyz(yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        return [
            c2 * c3, -c2 * s3, s2, 0.0,
            c1 * s3 + c3 * s1 * s2, c1 * c3 - s1 * s2 * s3, - c2 * s1, 0.0,
            s1 * s3 - c1 * c3 * s2, c3 * s1 + c1 * s2 * s3, c1 * c2, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_xyz(matrix, yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s1, c1 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c2 * c3
        matrix[1] = -c2 * s3
        matrix[2] = s2
        matrix[4] = c1 * s3 + c3 * s1 * s2
        matrix[5] = c1 * c3 - s1 * s2 * s3
        matrix[6] = - c2 * s1
        matrix[8] = s1 * s3 - c1 * c3 * s2
        matrix[9] = c3 * s1 + c1 * s2 * s3
        matrix[10] = c1 * c2
        return matrix

    @staticmethod
    def rotation_yxz(yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c3 + s1 * s2 * s3, c3 * s1 * s2 - c1 * s3, c2 * s1, 0.0,
            c2 * s3, c2 * c3, -s2, 0.0,
            c1 * s2 * s3 - c3 * s1, c1 * c3 * s2 + s1 * s3, c1 * c2, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_yxz(matrix, yz_theta, xz_theta, xy_theta):
        s3, c3 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c3 + s1 * s2 * s3
        matrix[1] = c3 * s1 * s2 - c1 * s3
        matrix[2] = c2 * s1
        matrix[4] = c2 * s3
        matrix[5] = c2 * c3
        matrix[6] = -s2
        matrix[8] = c1 * s2 * s3 - c3 * s1
        matrix[9] = c1 * c3 * s2 + s1 * s3
        matrix[10] = c1 * c2
        return matrix

    @staticmethod
    def rotation_yzx(yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c2, s1 * s3 - c1 * c3 * s2, c3 * s1 + c1 * s2 * s3, 0.0,
            s2, c2 * c3, -c2 * s3, 0.0,
            -c2 * s1, c1 * s3 + c3 * s1 * s2, c1 * c3 - s1 * s2 * s3, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_yzx(matrix, yz_theta, xz_theta, xy_theta):
        s2, c2 = sin(xy_theta), cos(xy_theta)
        s1, c1 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c2
        matrix[1] = s1 * s3 - c1 * c3 * s2
        matrix[2] = c3 * s1 + c1 * s2 * s3
        matrix[4] = s2
        matrix[5] = c2 * c3
        matrix[6] = -c2 * s3
        matrix[8] = -c2 * s1
        matrix[9] = c1 * s3 + c3 * s1 * s2
        matrix[10] = c1 * c3 - s1 * s2 * s3
        return matrix

    @staticmethod
    def rotation_zxy(yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c2, c1 * s2 * s3 - c3 * s1, s1 * s3 + c1 * c3 * s2, 0.0,
            c2 * s1, c1 * c3 + s1 * s2 * s3, c3 * s1 * s2 - c1 * s3, 0.0,
            -s2, c2 * s3, c2 * c3, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_zxy(matrix, yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s2, c2 = sin(xz_theta), cos(xz_theta)
        s3, c3 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c2
        matrix[1] = c1 * s2 * s3 - c3 * s1
        matrix[2] = s1 * s3 + c1 * c3 * s2
        matrix[4] = c2 * s1
        matrix[5] = c1 * c3 + s1 * s2 * s3
        matrix[6] = c3 * s1 * s2 - c1 * s3
        matrix[8] = -s2
        matrix[9] = c2 * s3
        matrix[10] = c2 * c3
        return matrix

    @staticmethod
    def rotation_zyx(yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        return [
            c1 * c3 - s1 * s2 * s3, -c2 * s1, c1 * s3 + c3 * s1 * s2, 0.0,
            c3 * s1 + c1 * s2 * s3, c1 * c2, s1 * s3 - c1 * c3 * s2, 0.0,
            -c2 * s3, s2, c2 * c3, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_rotation_zyx(matrix, yz_theta, xz_theta, xy_theta):
        s1, c1 = sin(xy_theta), cos(xy_theta)
        s3, c3 = sin(xz_theta), cos(xz_theta)
        s2, c2 = sin(yz_theta), cos(yz_theta)
        matrix[0] = c1 * c3 - s1 * s2 * s3
        matrix[1] = -c2 * s1
        matrix[2] = c1 * s3 + c3 * s1 * s2
        matrix[4] = c3 * s1 + c1 * s2 * s3
        matrix[5] = c1 * c2
        matrix[6] = s1 * s3 - c1 * c3 * s2
        matrix[8] = -c2 * s3
        matrix[9] = s2
        matrix[10] = c2 * c3
        return matrix

    @classmethod
    def rotation(cls, *args, **kwargs): return cls.rotation_xyz(*args, **kwargs)
    @classmethod
    def set_rotation(cls, *args, **kwargs):
        return cls.set_rotation_xyz(*args, **kwargs)


    @staticmethod
    def reflection(xz, xy, yz):
        xz = -1.0 if xz else 1.0
        xy = -1.0 if xy else 1.0
        yz = -1.0 if yz else 1.0
        return [
            yz, 0.0, 0.0, 0.0,
            0.0, xz, 0.0, 0.0,
            0.0, 0.0, xy, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_reflection(matrix, xz, xy, yz):
        matrix[0] = -1.0 if yz else 1.0
        matrix[5] = -1.0 if xz else 1.0
        matrix[10] = -1.0 if xy else 1.0
        return matrix

    @staticmethod
    def scale(x_scale, y_scale, z_scale):
        return [
            x_scale / 1.0, 0.0, 0.0, 0.0,
            0.0, y_scale / 1.0, 0.0, 0.0,
            0.0, 0.0, z_scale / 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_scale(matrix, x_scale, y_scale, z_scale):
        matrix[0] = x_scale / 1.0
        matrix[5] = y_scale / 1.0
        matrix[10] = z_scale / 1.0
        return matrix

    @staticmethod
    def shear_x(yx, zx):
        return [
            1.0, 0.0, 0.0, 0.0,
            yx / 1.0, 1.0, 0.0, 0.0,
            zx / 1.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_shear_x(matrix, yx, zx):
        matrix[4] = yx / 1.0
        matrix[8] = zx / 1.0
        return matrix

    @staticmethod
    def shear_y(xy, zy):
        return [
            1.0, xy / 1.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, zy / 1.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_shear_y(matrix, xy, zy):
        matrix[1] = xy / 1.0
        matrix[9] = zy / 1.0
        return matrix

    @staticmethod
    def shear_z(xz, yz):
        return [
            1.0, 0.0, xz / 1.0, 0.0,
            0.0, 1.0, yz / 1.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_shear_z(matrix, xz, yz):
        matrix[2] = xz / 1.0
        matrix[6] = yz / 1.0
        return matrix

    @staticmethod
    def shear(yx, zx, xy, zy, xz, yz):
        return [
            1.0, xy / 1.0, xz / 1.0, 0.0,
            yx / 1.0, 1.0, yz / 1.0, 0.0,
            zx / 1.0, zy / 1.0, 1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_shear(matrix, yx, zx, xy, zy, xz, yz):
        matrix[4] = yx / 1.0
        matrix[8] = zx / 1.0
        matrix[1] = xy / 1.0
        matrix[9] = zy / 1.0
        matrix[2] = xz / 1.0
        matrix[6] = yz / 1.0
        return matrix

    @staticmethod
    def translation(x, y, z):
        return [
            1.0, 0.0, 0.0, x / 1.0,
            0.0, 1.0, 0.0, y / 1.0,
            0.0, 0.0, 1.0, z / 1.0,
            0.0, 0.0, 0.0, 1.0
            ]
    @staticmethod
    def set_translation(matrix, x, y, z):
        matrix[3] = x / 1.0
        matrix[7] = y / 1.0
        matrix[11] = z / 1.0
        return matrix

    @staticmethod
    def add_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = other
        return [
            a + A, b + B, c + C, d + D,
            e + E, f + F, g + G, h + H,
            i + I, j + J, k + K, l + L,
            m + M, n + N, o + O, p + P
            ]
    @staticmethod
    def iadd_matrix(matrix, other):
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = other
        matrix[0] += A
        matrix[1] += B
        matrix[2] += C
        matrix[3] += D
        matrix[4] += E
        matrix[5] += F
        matrix[6] += G
        matrix[7] += H
        matrix[8] += I
        matrix[9] += J
        matrix[10] += K
        matrix[11] += L
        matrix[12] += M
        matrix[13] += N
        matrix[14] += O
        matrix[15] += P
        return matrix

    @staticmethod
    def subtract_matrix(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = other
        return [
            a - A, b - B, c - C, d - D,
            e - E, f - F, g - G, h - H,
            i - I, j - J, k - K, l - L,
            m - M, n - N, o - O, p - P
            ]
    @staticmethod
    def isubtract_matrix(matrix, other):
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = other
        matrix[0] -= A
        matrix[1] -= B
        matrix[2] -= C
        matrix[3] -= D
        matrix[4] -= E
        matrix[5] -= F
        matrix[6] -= G
        matrix[7] -= H
        matrix[8] -= I
        matrix[9] -= J
        matrix[10] -= K
        matrix[11] -= L
        matrix[12] -= M
        matrix[13] -= N
        matrix[14] -= O
        matrix[15] -= P
        return matrix

    @staticmethod
    def transform_vector(matrix, vector):
        vec3 = Vector3D.new
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        x, y, z = vector
        return new_vector(
            a * x + b * y + c * z + d,
            e * x + f * y + g * z + h,
            i * x + j * y + k * z + l,
            m * x + n * y + o * z + p
            )
    @staticmethod
    def itransform_vector(matrix, vector):
        set_components = Vector3D.set_components
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        x, y, z = vector
        set_components(
            vector,
            a * x + b * y + c * z + d,
            e * x + f * y + g * z + h,
            i * x + j * y + k * z + l,
            m * x + n * y + o * z + p
            )
        return vector

    @staticmethod
    def transform_line(matrix, line):
        line3 = Line3D
        get_direction = line3.direction
        get_point = line3.through_point
        new_line = line3.new
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(line)
        x, y, z = get_point(line)
        return new_line(
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )
    @staticmethod
    def itransform_line(matrix, line):
        line3 = Line3D
        get_direction = line3.direction
        get_point = line3.through_point
        set_components = line3.set_components
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(line)
        x, y, z = get_point(line)
        return set_components(
            line,
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )

    @staticmethod
    def transform_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        new_line = plane3.new
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(plane)
        x, y, z = get_point(plane)
        return new_plane(
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )
    @staticmethod
    def itransform_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        set_components = plane3.set_components
        a, b, c, d, e, f, g, h, i, j, k, l = matrix
        p, q, r = get_direction(plane)
        x, y, z = get_point(plane)
        return set_components(
            plane,
            a * p + b * q + c * r + d,
            d * p + e * q + f * r + h,
            g * p + h * q + i * r + l,
            a * x + b * y + c * z + d,
            d * x + e * y + f * z + h,
            g * x + h * y + i * z + l
            )

    @staticmethod
    def compile_linear(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        A, B, C, D, E, F, G, H, I, J, K, L = other
        return [
            a * A + b * E + c * I, a * B + b * F + c * J,
            a * C + b * G + c * K, a * D + b * H + c * L + d,
            e * A + f * E + g * I, e * B + f * F + g * J,
            e * C + f * G + g * K, e * D + f * H + g * L + h,
            i * A + j * E + k * I, i * B + j * F + k * J,
            i * C + j * G + k * K, i * D + j * H + k * L + l,
            m * A + n * E + o * I, m * B + n * F + o * J,
            m * C + n * G + o * K, m * D + n * H + o * L + p
            ]
    @staticmethod
    def icompile_linear(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        A, B, C, D, E, F, G, H, I, J, K, L = other
        matrix[0] = a * A + b * E + c * I
        matrix[1] = a * B + b * F + c * J
        matrix[2] = a * C + b * G + c * K
        matrix[3] = a * D + b * H + c * L + d
        matrix[4] = e * A + f * E + g * I
        matrix[5] = e * B + f * F + g * J
        matrix[6] = e * C + f * G + g * K
        matrix[7] = e * D + f * H + g * L + h
        matrix[8] = i * A + j * E + k * I
        matrix[9] = i * B + j * F + k * J
        matrix[10] = i * C + j * G + k * K
        matrix[11] = i * D + j * H + k * L + l
        matrix[12] = m * A + n * E + o * I
        matrix[13] = m * B + n * F + o * J
        matrix[14] = m * C + n * G + o * K
        matrix[15] = m * D + n * H + o * L + p
        return matrix

    @staticmethod
    def compile_perspective(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = other
        return [
            a * A + b * E + c * I + d * M, a * B + b * F + c * J + d * N,
            a * C + b * G + c * K + d * O, a * D + b * H + c * L + d * P,
            e * A + f * E + g * I + h * M, e * B + f * F + g * J + h * N,
            e * C + f * G + g * K + h * O, e * D + f * H + g * L + h * P,
            i * A + j * E + k * I + l * M, i * B + j * F + k * J + l * N,
            i * C + j * G + k * K + l * O, i * D + j * H + k * L + l * P,
            m * A + n * E + o * I + p * M, m * B + n * F + o * J + p * N,
            m * C + n * G + o * K + p * O, m * D + n * H + o * L + p * P
            ]
    @staticmethod
    def icompile_perspective(matrix, other):
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = matrix
        A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P = other
        matrix[0] = a * A + b * E + c * I + d * M
        matrix[1] = a * B + b * F + c * J + d * N
        matrix[2] = a * C + b * G + c * K + d * O
        matrix[3] = a * D + b * H + c * L + d * P
        matrix[4] = e * A + f * E + g * I + h * M
        matrix[5] = e * B + f * F + g * J + h * N
        matrix[6] = e * C + f * G + g * K + h * O
        matrix[7] = e * D + f * H + g * L + h * P
        matrix[8] = i * A + j * E + k * I + l * M
        matrix[9] = i * B + j * F + k * J + l * N
        matrix[10] = i * C + j * G + k * K + l * O
        matrix[11] = i * D + j * H + k * L + l * P
        matrix[12] = m * A + n * E + o * I + p * M
        matrix[13] = m * B + n * F + o * J + p * N
        matrix[14] = m * C + n * G + o * K + p * O
        matrix[15] = m * D + n * H + o * L + p * P
        return matrix

mat3dpt = Matrix3DPerspectiveTransform = Matrix3DPerspectiveTransformSingleton()
