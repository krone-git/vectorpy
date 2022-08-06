from .abc import MatrixSingletonABC, MatrixLinearTransformSingletonABC
from ..vector.vector2d import Vector2D
# from ..line.line2d import Line2D
# from ..line.plane2d import Plane2D
from math import cos, sin


__all__ = (
    "mat2d", "Matrix2D", "mat2dt", "Matrix2DTransform"
    )


class Matrix2DSingleton(MatrixSingletonABC):
    @staticmethod
    def new(a, b, c, d): return [a / 1.0, b / 1.0, c / 1.0, d / 1.0]
    @staticmethod
    def from_row_vectors(vectors):
        row1, row2 = vectors
        a, b = row1
        c, d = row2
        return [a / 1.0, b / 1.0, c / 1.0, d / 1.0]
    @staticmethod
    def from_column_vectors(vectors):
        column1, column2 = vectors
        a, c = column1
        b, d = column2
        return [a / 1.0, b / 1.0, c / 1.0, d / 1.0]
    @staticmethod
    def from_basis(basis):
        a, c = basis
        return [a, 0.0, 0.0, c]

    @staticmethod
    def zero_matrix():
        return [0.0, 0.0, 0.0, 0.0]
    @staticmethod
    def identity_matrix():
        return [1.0, 0.0, 0.0, 1.0]

    @staticmethod
    def to_row_vectors(matrix):
        new_vector = Vector2D.new
        a, b, c, d = matrix
        return new_vector(a, b), new_vector(c, d)
    @staticmethod
    def to_column_vectors(matrix):
        new_vector = Vector2D.new
        a, b, c, d, e, f, g, h, i = matrix
        return new_vector(a, c), new_vector(b, d)
    @staticmethod
    def to_basis(matrix):
        new_vector = Vector2D.new
        a, _, _, d = matrix
        return new_vector(a, d)

    @staticmethod
    def get_component(matrix, column, row):
        return matrix[row * 2 + column]

    @staticmethod
    def columns(matrix):
        a, b, c, d = matrix
        return (a, c), (b, d)
    @staticmethod
    def column(matrix, column): return matrix[column::2]
    @staticmethod
    def rows(matrix):
        a, b, c, d = matrix
        return (a, b), (c, d)
    @staticmethod
    def row(matrix, row): return matrix[row * 2: (row + 1) * 2]

    @staticmethod
    def clear(matrix):
        matrix[0] = matrix[1] = matrix[2] = matrix[3] = 0.0
        return matrix
    @staticmethod
    def reset(matrix):
        matrix[1] = matrix[2] = 0.0
        matrix[0] = matrix[3] = 1.0
        return matrix

    @staticmethod
    def set_component(matrix, column, row, value):
        matrix[row * 2 + column] = value / 1.0
        return matrix
    @staticmethod
    def set_components(matrix, a, b, c, d):
        matrix[0] = a / 1.0
        matrix[1] = b / 1.0
        matrix[2] = c / 1.0
        matrix[3] = d / 1.0
        return matrix
    @staticmethod
    def set_row_vector(matrix, row, vector):
        index = row * 2
        matrix[index], matrix[index + 1] = vector
        return matrix
    @staticmethod
    def set_row_components(matrix, row, a, b):
        index = row * 2
        matrix[index] = a / 1.0
        matrix[index + 1] = b / 1.0
        return matrix
    @staticmethod
    def set_column_vector(matrix, column, vector):
        matrix[column], matrix[2 + column] = vector
        return matrix
    @staticmethod
    def set_column_components(matrix, column, a, b):
        matrix[column] = a / 1.0
        matrix[2 + column] = b / 1.0
        return matrix
    @staticmethod
    def set_matrix(matrix, other):
        matrix[0], matrix[1], matrix[2], matrix[3] = other
        return matrix

    @staticmethod
    def determinant(matrix):
        a, b, c, d = matrix
        return a * d - b * c

    @staticmethod
    def add_scalar(matrix, scalar):
        a, b, c, d = matrix
        return [a + scalar, b + scalar, c + scalar, d + scalar]
    @staticmethod
    def iadd_scalar(matrix, scalar):
        matrix[0] += scalar
        matrix[1] += scalar
        matrix[2] += scalar
        matrix[3] += scalar
        return matrix
    @staticmethod
    def add_matrix(matrix, other):
        a, b, c, d = matrix
        e, f, g, h = other
        return [a + e, b + f, c + g, d + h]
    @staticmethod
    def iadd_matrix(matrix, other):
        e, f, g, h = other
        matrix[0] += e
        matrix[1] += f
        matrix[2] += g
        matrix[3] += h
        return matrix
    @staticmethod
    def subtract_scalar(matrix, scalar):
        a, b, c, d = matrix
        return [a - scalar, b - scalar, c - scalar, d - scalar]
    @staticmethod
    def isubtract_scalar(matrix, scalar):
        matrix[0] -= scalar
        matrix[1] -= scalar
        matrix[2] -= scalar
        matrix[3] -= scalar
        return matrix
    @staticmethod
    def subtract_matrix(matrix, other):
        a, b, c, d = matrix
        e, f, g, h = other
        return [a - e, b - f, c - g, d - h]
    @staticmethod
    def isubtract_matrix(matrix, other):
        e, f, g, h = other
        matrix[0] -= e
        matrix[1] -= f
        matrix[2] -= g
        matrix[3] -= h
        return matrix

    @staticmethod
    def multiply_scalar(matrix, scalar):
        a, b, c, d = matrix
        return [a * scalar, b * scalar, c * scalar, d * scalar]
    @staticmethod
    def imultiply_scalar(matrix, scalar):
        matrix[0] *= scalar
        matrix[1] *= scalar
        matrix[2] *= scalar
        matrix[3] *= scalar
        return matrix
    @staticmethod
    def multiply_vector(matrix, vector):
        new_vector = Vector2D.new
        a, b, c, d = matrix
        p, q = vector
        return new_vector(a * p + b * q, c * p + d * q)
    @staticmethod
    def imultiply_vector(matrix, vector):
        set_components = Vector2D.set_components
        a, b, c, d = matrix
        p, q = vector
        return set_components(
            vector, a * p + b * q, c * p + d * q
            )
    @staticmethod
    def multiply_line(matrix, line):
        line2 = Line2D
        get_direction = line2.direction
        get_point = line2.through_point
        new_line = line2.new
        a, b, c, d = matrix
        p, q = get_direction(line)
        x, y = get_point(line)
        return new_line(
            a * p + b * q, c * p + d * q,
            a * x + b * y, c * x + d * y
            )
    @staticmethod
    def imultiply_line(matrix, line):
        line2 = Line2D
        get_direction = line2.direction
        get_point = line2.through_point
        set_components = line2.set_components
        a, b, c, d = matrix
        p, q = get_direction(line)
        x, y = get_point(line)
        return set_components(
            line,
            a * p + b * q, c * p + d * q,
            a * x + b * y, c * x + d * y,
            )
    @staticmethod
    def multiply_plane(matrix, plane):
        plane2 = Plane2D
        get_direction = plane2.direction
        get_point = plane2.through_point
        new_line = plane2.new
        a, b, c, d = matrix
        p, q = get_direction(plane)
        x, y = get_point(plane)
        return new_plane(
            a * p + b * q, c * p + d * q,
            a * x + b * y, f * x + d * y
            )
    @staticmethod
    def imultiply_plane(matrix, plane):
        plane2 = Plane2D
        get_direction = plane2.direction
        get_point = plane2.through_point
        set_components = plane2.set_components
        a, b, c, d = matrix
        p, q = get_direction(plane)
        x, y = get_point(plane)
        return set_components(
            plane,
            a * p + b * q, c * p + d * q,
            a * x + b * y, c * x + d * y
            )
    @staticmethod
    def multiply_matrix(matrix, other):
        a, b, c, d = matrix
        e, f, g, h = other
        return [
            a * e + b * g, a * f + b * h,
            d * e + e * g, d * f + e * h
            ]
    @staticmethod
    def imultiply_matrix(matrix, other):
        a, b, c, d = matrix
        e, f, g, h = other
        matrix[0] = a * e + b * g
        matrix[1] = a * f + b * h
        matrix[2] = c * e + d * g
        matrix[3] = c * f + d * h
        return matrix

    @staticmethod
    def divide_scalar(matrix, scalar):
        a, b, c, d = matrix
        return [a / scalar, b / scalar, c / scalar, d / scalar]


mat2d = Matrix2D = Matrix2DSingleton()


class Matrix2DTransformSingleton(MatrixLinearTransformSingletonABC):
    @staticmethod
    def new(a, b, c, d, e, f):
        return [a / 1.0, b / 1.0, c / 1.0, d / 1.0, e / 1.0, f / 1.0]
    @staticmethod
    def from_basis(basis):
        a, e = basis
        return [a, 0.0, 0.0, 0.0, e, 0.0]

    @staticmethod
    def zero_matrix():
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    @staticmethod
    def identity_matrix():
        return [1.0, 0.0, 0.0, 0.0, 1.0, 0.0]

    @staticmethod
    def from_base_matrix(matrix):
        a, b, c, d = matrix
        return [a, b, 0.0, c, d, 0.0]
    @staticmethod
    def to_base_matrix(matrix):
        a, b, _, d, e, _ = matrix
        return [a, b, d, e]

    @staticmethod
    def base_matrix_to_linear_transform(matrix):
        a, b, c, d = matrix
        matrix.clear()
        matrix.extend([a, b, 0.0, c, d, 0.0])
        return matrix

    @staticmethod
    def get_component(matrix, column, row):
        return matrix[row * 2 + column]

    @staticmethod
    def columns(matrix):
        a, b, c, d, e, f = matrix
        return (a, c), (b, d), (e, f)
    @staticmethod
    def column(matrix, column): return matrix[column::3]
    @staticmethod
    def rows(matrix):
        a, b, c, d, e, f = matrix
        return (a, b, c), (d, e, f)
    @staticmethod
    def row(matrix, row): return matrix[row * 3: (row + 1) * 3]

    @staticmethod
    def clear(matrix):
        matrix[0] = matrix[1] = matrix[2] = \
        matrix[3] = matrix[4] = matrix[5] = 0.0
        return matrix
    @staticmethod
    def reset(matrix):
        matrix[1] = matrix[2] = matrix[3] = matrix[5] = 0.0
        matrix[0] = matrix[4] = 1.0
        return matrix

    @staticmethod
    def set_component(matrix, column, row, value):
        matrix[row * 3 + column] = value / 1.0
        return matrix
    @staticmethod
    def set_components(matrix, a, b, c, d, e, f):
        matrix[0] = a / 1.0
        matrix[1] = b / 1.0
        matrix[2] = c / 1.0
        matrix[3] = d / 1.0
        matrix[4] = e / 1.0
        matrix[5] = f / 1.0
        return matrix
    @staticmethod
    def set_row_vector(matrix, row, vector):
        index = row * 3
        matrix[index], matrix[index + 1] = vector
        return matrix
    @staticmethod
    def set_row_components(matrix, row, a, b):
        index = row * 3
        matrix[index] = a / 1.0
        matrix[index + 1] = b / 1.0
        return matrix
    @staticmethod
    def set_column_vector(matrix, column, vector):
        matrix[column], matrix[3 + column] = vector
        return matrix
    @staticmethod
    def set_column_components(matrix, column, a, b):
        matrix[column] = a / 1.0
        matrix[3 + column] = b / 1.0
        return matrix
    @staticmethod
    def set_matrix(matrix, other):
        matrix[0], matrix[1], matrix[2], \
        matrix[3], matrix[4], matrix[5] = other
        return matrix

    @staticmethod
    def determinant(matrix):
        a, b, c, d, e, f = matrix
        return a * e - b * d

    @staticmethod
    def rotation(theta):
        s, c = sin(theta), cos(theta)
        return [c, -s, 0.0, s, c, 0.0]
    @staticmethod
    def set_rotation(matrix, theta):
        s, c = sin(theta), cos(theta)
        matrix[0] = c
        matrix[1] = -s
        matrix[3] = s
        matrix[4] = c
        return matrix
    @staticmethod
    def reflection(x, y):
        return [-1.0 if x else 1.0, 0.0, 0.0, -1.0 if y else 1.0]
    @staticmethod
    def set_reflection(matrix, x, y):
        matrix[0] = -1.0 if x else 1.0
        matrix[4] = -1.0 if y else 1.0
        return matrix
    @staticmethod
    def scale(x_scale, y_scale):
        return [x_scale, 0.0, 0.0, 0.0, y_scale, 0.0]
    @staticmethod
    def set_scale(matrix, x_scale, y_scale):
        matrix[0] = x_scale / 1.0
        matrix[4] = y_scale / 1.0
        return matrix
    @staticmethod
    def shear(matrix, x_shear, y_shear):
        return [1.0, x_shear, 0.0, y_shear, 1.0, 0.0]
    @staticmethod
    def set_shear(matrix, x_shear, y_shear):
        matrix[1] = x_shear / 1.0
        matrix[3] = y_shear / 1.0
        return matrix
    @staticmethod
    def translation(x, y):
        return [1.0, 0.0, x, 0.0, 1.0, y]
    @staticmethod
    def set_translation(matrix, x, y):
        matrix[2] = x / 1.0
        matrix[5] = y / 1.0
        return matrix

    @staticmethod
    def add_matrix(matrix, other):
        a, b, c, d, e, f = matrix
        g, h, i, j, k, l = other
        return [a + g, b + h, c + i, d + j, e + k, f + l]
    @staticmethod
    def iadd_matrix(matrix, other):
        g, h, i, j, k, l = other
        matrix[0] += g
        matrix[1] += h
        matrix[2] += i
        matrix[3] += j
        matrix[4] += k
        matrix[5] += l
        return matrix

    @staticmethod
    def subtract_matrix(matrix, other):
        a, b, c, d, e, f = matrix
        g, h, i, j, k, l = other
        return [a - g, b - h, c - i, d - j, e - k, f - l]
    @staticmethod
    def isubtract_matrix(matrix, other):
        g, h, i, j, k, l = other
        matrix[0] -= g
        matrix[1] -= h
        matrix[2] -= i
        matrix[3] -= j
        matrix[2] -= k
        matrix[3] -= l
        return matrix

    @staticmethod
    def transform_vector(matrix, vector):
        a, b, c, d, e, f = matrix
        x, y = vector
        return Vector2D.new(a * x + b * y + c, d * x + e * y + f)
    @staticmethod
    def itransform_vector(matrix, vector):
        a, b, c, d, e, f = matrix
        x, y = vector
        return Vector2D.set_components(
            vector, a * x + b * y + c, d * x + e * y + f
            )
    @staticmethod
    def transform_line(matrix, line):
        line3 = Line2D
        get_direction = line2.direction
        get_point = line2.through_point
        new_line = line2.new
        a, b, c, d, e, f = matrix
        p, q = get_direction(line)
        x, y = get_point(line)
        return new_line(
            a * p + b * q + c, d * p + e * q + f,
            a * x + b * y + c, d * x + e * y + f,
            )
    @staticmethod
    def itransform_line(matrix, line):
        line3 = Line3D
        get_direction = line3.direction
        get_point = line3.through_point
        set_components = line3.set_components
        a, b, c, d, e, f = matrix
        p, q = get_direction(line)
        x, y = get_point(line)
        return set_components(
            line,
            a * p + b * q + c, d * p + e * q + f,
            a * x + b * y + c, d * x + e * y + f,
            )
    @staticmethod
    def transform_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        new_line = plane3.new
        a, b, c, d, e, f = matrix
        p, q = get_direction(plane)
        x, y = get_point(plane)
        return new_plane(
            a * p + b * q + c, d * p + e * q + f,
            a * x + b * y + c, d * x + e * y + f
            )
    @staticmethod
    def itransform_plane(matrix, plane):
        plane3 = Plane3D
        get_direction = plane3.direction
        get_point = plane3.through_point
        set_components = plane3.set_components
        a, b, c, d, e, f = matrix
        p, q = get_direction(plane)
        x, y = get_point(plane)
        return set_components(
            plane,
            a * p + b * q + c, d * p + e * q + f,
            a * x + b * y + c, d * x + e * y + f
            )
    @staticmethod
    def compile(matrix, other):
        a, b, c, d, e, f = matrix
        A, B, C, D, E, F = other
        return [
            a * A + b * D, a * B + b * E, a * C + b * F + c,
            d * A + e * D, d * B + e * E, d * C + e * F + f,
            ]
    @staticmethod
    def icompile(matrix, other):
        a, b, c, d, e, f = matrix
        A, B, C, D, E, F = other
        matrix[0] = a * A + b * D
        matrix[1] = a * B + b * E
        matrix[2] = a * C + b * F + c
        matrix[3] = d * A + e * D
        matrix[4] = d * B + e * E
        matrix[5] = d * C + e * F + f
        return matrix

mat2dt = Matrix2DTransform = Matrix2DTransformSingleton()
