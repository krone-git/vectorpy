from .abc import MatrixSingletonABC, SquareMatrixSingletonABC
from ..vector.vector import VectorND
from ..line.line import LineND
from ..plane.plane import PlaneND
from collections.abc import Sized


__all__ = (
    "mat", "matrix", "Matrix",
    "matmnd", "matrixmnd", "MatrixMND",
    "matnd", "matrixnd", "MatrixND",
)

class _MatrixMND(list):
    def __init__(self, args, m, n):
        m = int(m)
        n = int(n)
        self._m = m
        self._n = n
        super().__init__((*args,)[:m * n])


class MatrixMNDSingleton(MatrixSingletonABC):
    @staticmethod
    def new(args, m, n):
        return _MatrixMND((i / 1.0 for i in args), m, n)
    @classmethod
    def from_row_vectors(cls, vectors):
        m = max((len(v) for v in vectors))
        n = len(vectors)
        matrix = cls.zero_matrix(m, n)
        for i, vector in enumerate(vectors):
            for j, v in enumerate(vector):
                matrix[i * m + j] = v
        return matrix
    @classmethod
    def from_column_vectors(cls, vectors):
        m = len(vectors)
        n = max((len(v) for v in vectors))
        matrix = cls.zero_matrix(m, n)
        for i, vector in enumerate(vectors):
            for j, v in enumerate(vector):
                matrix[j * m + i] = v
        return matrix
    @classmethod
    def from_basis(cls, basis):
        n = len(basis)
        matrix = cls.zero_matrix(n, n)
        for i, v in enumerate(basis):
            matrix[n * i + i] = v
        return matrix

    @staticmethod
    def zero_matrix(m, n):
        return _MatrixMND([0.0] * (m * n), m, n)
    @classmethod
    def left_identity_matrix(cls, m, n):
        matrix = cls.zero_matrix(m, n)
        rows = min(m, n)
        for i in range(rows):
            matrix[m * i + i] = 1.0
        return matrix
    @classmethod
    def right_identity_matrix(cls, m, n):
        matrix = cls.zero_matrix(m, n)
        rows = min(m, n)
        for i in range(rows):
            matrix[m * i + i + m - rows] = 1.0
        return matrix
    @classmethod
    def identity_matrix(cls, *args):
        return cls.left_identity_matrix(*args)

    @classmethod
    def to_row_vectors(cls, matrix):
        return tuple(
            *(VectorND.from_iterable(row) for row in cls.rows(matrix))
            )
    @classmethod
    def to_column_vectors(cls, matrix):
        return tuple(
            *(VectorND.from_iterable(column) for column in cls.columns(matrix))
            )
    @classmethod
    def to_left_basis(cls, matrix):
        m, n = cls.shape(matrix)
        rows = min(m, n)
        return VectorND.from_iterable(matrix[n * i + i] for i in range(rows))
    @classmethod
    def to_right_basis(cls, matrix):
        m, n = cls.shape(matrix)
        rows = min(m, n)
        return VectorND.from_iterable(
            matrix[m * i + i + m - rows] for i in range(rows)
            )
    @classmethod
    def to_basis(cls, *args): return cls.to_left_basis(*args)

    @classmethod
    def get_component(cls, matrix, column, row):
        width = cls.width(matrix)
        return matrix[row * width + column]

    @staticmethod
    def width(matrix): return getattr(matrix, "_m", int(len(matrix))**0.5)
    @staticmethod
    def height(matrix): return getattr(matrix, "_n", int(len(matrix))**0.5)
    @classmethod
    def columns(cls, matrix):
        m = cls.width(matrix)
        return (matrix[i::m] for i in range(m))
    @classmethod
    def column(cls, matrix, column): return matrix[column::cls.matrix(width)]
    @classmethod
    def column_vector(cls, matrix, column):
        return VectorND.from_iterable(cls.column(matrix, column))
    @classmethod
    def rows(cls, matrix):
        n = cls.height(matrix)
        return (matrix[n * i: n * (i + 1)] for i in range(n))
    @classmethod
    def row(cls, matrix, row):
        n = cls.height(matrix)
        return matrix[n * row: n * (row + 1)]
    @classmethod
    def row_vector(cls, matrix, row):
        return VectorND.from_iterable(cls.row(matrix, row))
    @classmethod
    def sub_matrix(cls, matrix, row, column, m, n):
        new_matrix = cls.zero_matrix(m, n)
        w = cls.width(matrix)
        for i in range(m):
            for j in range(n):
                new_matrix[i * m + j] = matrix[(row + i) * w + (column + j)]
        return new_matrix

    @staticmethod
    def copy(matrix):
        new = matrix.copy()
        new._m = matrix._m
        new._n = matrix._n
        return new
    @staticmethod
    def clear(matrix):
        for i in range(len(matrix)):
            matrix[i] = 0.0
        return matrix
    @classmethod
    def reset(cls, matrix):
        m, n = cls.shape(matrix)
        return cls.set_matrix(matrix, cls.left_identity_matrix(m, n))

    @classmethod
    def set_component(cls, matrix, column, row, value):
        matrix[row * cls.width(matrix) + column] = value / 1.0
        return matrix
    @classmethod
    def set_components(matrix, *components):
        for i, v in enumerate(components):
            matrix[i] = v
        return matrix
    @classmethod
    def set_row_vector(cls, matrix, row, vector):
        m = cls.width(matrix)
        for i in range(len(vector)):
            matrix[m * row + i] = vector[i]
        return matrix
    @classmethod
    def set_row_components(cls, matrix, row, *components):
        m = cls.width(matrix)
        for i, v in enumerate(components):
            matrix[m * row + i] = v
        return matrix
    @classmethod
    def set_column_vector(cls, matrix, column, vector):
        m = cls.width(matrix)
        for i in range(len(vector)):
            matrix[m * i + column] = vector[i]
        return matrix
    @classmethod
    def set_column_components(cls, matrix, column, *components):
        m = cls.width(matrix)
        for i, v in enumerate(components):
            matrix[m * i + column] = v
        return matrix
    @classmethod
    def set_matrix(cls, matrix, other):
        for i in range(len(other)):
            matrix[i] = other[i]
        return matrix
    @classmethod
    def set_sub_matrix(cls, matrix, other, row, column, m, n):
        w = cls.width(matrix)
        for i in range(m):
            for j in range(n):
                matrix[w * (row + i) + (column + j)] = other[i * m + j]
        return matrix

    @classmethod
    def add_scalar(cls, matrix, scalar):
        m, n = cls.shape(matrix)
        return _MatrixMND((v + scalar for v in matrix), m, n)
    @staticmethod
    def iadd_scalar(matrix, scalar):
        for i in range(len(matrix)):
            matrix[i] += scalar
        return matrix
    @classmethod
    def add_matrix(cls, matrix, other):
        m, n = cls.shape(matrix)
        return _MatrixMND((a + b for a, b in zip(matrix, other)), m, n)
    @staticmethod
    def iadd_matrix(matrix, other):
        for i in range(len(other)):
            matrix[i] += other[i]
        return matrix
    @classmethod
    def subtract_scalar(cls, matrix, scalar):
        m, n = cls.shape(matrix)
        return _MatrixMND((v + scalar for v in matrix), m, n)
    @staticmethod
    def isubtract_scalar(matrix, scalar):
        for i in range(len(matrix)):
            matrix[i] -= scalar
        return matrix
    @classmethod
    def subtract_matrix(cls, matrix, other):
        m, n = cls.shape(matrix)
        return _MatrixMND((a - b for a, b in zip(matrix, other)), m, n)
    @staticmethod
    def isubtract_matrix(matrix, other):
        for i in range(len(other)):
            matrix[i] -= other[i]
        return matrix
    @staticmethod
    def multiply_scalar(matrix, scalar):
        m, n = cls.shape(matrix)
        return _MatrixMND((i * scalar for i in matrix), m, n)
    @staticmethod
    def imultiply_scalar(matrix, scalar):
        for i in range(len(matrix)):
            matrix[i] *= scalar
        return matrix
    @classmethod
    def multiply_vector(cls, matrix, vector):
        vecnd = VectorND
        new_vector = vecnd.new
        dot = vecnd.dot_product
        return new_vector(
            [dot(vector, row) for row in cls.rows(matrix)]
            )
    @classmethod
    def imultiply_vector(cls, matrix, vector):
        new_vector = cls.multiply_vector(matrix, vector)
        return VectorND.set_components(vector, new_vector)
    @staticmethod
    def multiply_line(matrix, line):
        linend = LineND
        new_line = linend.new
        get_direction = linend.direction
        get_point = linend.through_point
        transform = cls.multiply_vector
        direction = transform(matrix, get_direction(line))
        point = transform(matrix, get_point(line))
        return new_line(direction, point)
    @classmethod
    def imultiply_line(matrix, line):
        new_line = cls.multiply_line(matrix, line)
        return LineND.set_line(line, new_line)
    @staticmethod
    def multiply_plane(matrix, plane):
        planend = PlaneND
        new_line = planend.new
        get_direction = planend.direction
        get_point = planend.through_point
        set_components = planend.set_components
        transform = cls.multiply_vector
        direction = transform(matrix, get_direction(plane))
        point = transform(matrix, get_point(plane))
        return new_plane(direction, point)
    @classmethod
    def imultiply_plane(cls,matrix, plane):
        new_plane = cls.multiply_plane(matrix, plane)
        return PlaneND.set_plane(plane, new_plane)
    @classmethod
    def multiply_matrix(cls, matrix, other):
        dot = VectorND.dot_product
        m, n = cls.width(other), cls.height(matrix)
        new_matrix = cls.zero_matrix(m, n)
        for i in range(n):
            row = cls.row_vector(matrix, i)
            for j in range(m):
                column = cls.column_vector(other, j)
                new_matrix[m * i + j] = dot(row, column)
        return new_matrix
    @classmethod
    def imultiply_matrix(cls, matrix, other):
        new_matrix = cls.multiply_matrix(matrix, other)
        return cls.set_matrix(matrix, new_matrix)

    @classmethod
    def divide_scalar(cls, matrix, scalar):
        m, n = cls.shape(matrix)
        return _MatrixMND((v / scalar for v in matrix), m, n)

mat = matrix = Matrix = matmnd = matrixmnd = MatrixMND = MatrixMNDSingleton()


class MatrixNDSingleton(SquareMatrixSingletonABC):
    @staticmethod
    def new(args, n): return [i / 1.0 for i in (*args,)[:int(n)**2]]
    @classmethod
    def from_row_vectors(cls, vectors):
        n = max(len(v) for v in vectors)
        matrix = cls.zero_matrix(n)
        for i, vector in enumerate(vectors):
            for j, v in enumerate(vector):
                matrix[n * i + j] = v
        return matrix
    @classmethod
    def from_column_vectors(cls, vectors):
        n = max(len(v) for v in vectors)
        matrix = cls.zero_matrix(n)
        for i, vector in enumerate(vectors):
            for j, v in enumerate(vector):
                matrix[n * j + i] = v
        return matrix
    @classmethod
    def from_basis(cls, basis):
        n = len(basis)
        matrix = cls.zero_matrix(n)
        for i in range(len(basis)):
            matrix[n * i + i] = basis[i]
        return matrix

    @staticmethod
    def zero_matrix(n): return [0.0] * (n**2)
    @staticmethod
    def identity_matrix(n):
        matrix = [0.0] * (n**2)
        for i in range(n):
            matrix[n * i + i] = 1.0
        return matrix

    @classmethod
    def to_row_vectors(cls, matrix):
        return tuple(
            *(VectorND.from_iterable(row) for row in cls.rows(matrix))
            )
    @classmethod
    def to_column_vectors(cls, matrix):
        return tuple(
            *(VectorND.from_iterable(column) for column in cls.columns(matrix))
            )
    @classmethod
    def to_basis(cls, matrix):
        n = cls.width(matrix)
        return VectorND.from_iterable(matrix[n * i + i] for i in range(n))

    @staticmethod
    def get_component(matrix, column, row):
        return matrix[cls.width(matrix) * row + column]

    @classmethod
    def columns(cls, matrix):
        n = cls.width(matrix)
        return (matrix[i::n] for i in range(n))
    @classmethod
    def column(cls, matrix, column):
        n = cls.width(matrix)
        return matrix[column::n]
    @classmethod
    def column_vector(cls, matrix, column):
        return VectorND.from_iterable(cls.column(matrix, column))
    @classmethod
    def rows(cls, matrix):
        n = cls.width(matrix)
        return (matrix[n * i: n * (i + 1)] for i in range(n))
    @classmethod
    def row(cls, matrix, row):
        n = cls.width(matrix)
        return matrix[n * row: n * (row + 1)]
    @classmethod
    def row_vector(cls, matrix, row):
        return VectorND.from_iterable(cls.row(matrix, row))
    @classmethod
    def sub_matrix(cls, matrix, row, column, m, n):
        new_matrix = MatrixMNDSingleton.zero_matrix(m, n)
        w = cls.width(matrix)
        for i in range(m):
            for j in range(n):
                new_matrix[i * m + j] = matrix[(row + i) * w + (column + j)]
        return new_matrix

    @staticmethod
    def clear(matrix):
        for i in range(len(matrix)):
            matrix[i] = 0.0
        return matrix
    @classmethod
    def reset(cls, matrix):
        n = cls.width(matrix)
        for i in range(len(matrix)):
            matrix[i] = 0.0
        for i in range(n):
            matrix[n * i + i] = 1.0
        return matrix

    @classmethod
    def set_component(cls, matrix, column, row, value):
        matrix[row * cls.width(matrix) + column] = value / 1.0
        return matrix
    @classmethod
    def set_components(matrix, *components):
        for i, v in enumerate(components):
            matrix[i] = v
        return matrix
    @classmethod
    def set_row_vector(cls, matrix, row, vector):
        n = cls.width(matrix)
        for i in range(len(vector)):
            matrix[n * row + i] = vector[i]
        return matrix
    @classmethod
    def set_row_components(cls, matrix, row, *components):
        n = cls.width(matrix)
        for i, v in enumerate(components):
            matrix[n * row + i] = v
        return matrix
    @classmethod
    def set_column_vector(cls, matrix, column, vector):
        n = cls.width(matrix)
        for i in range(len(vector)):
            matrix[n * i + column] = vector[i]
        return matrix
    @classmethod
    def set_column_components(cls, matrix, column, *components):
        n = cls.width(matrix)
        for i, v in enumerate(components):
            matrix[n * i + column] = v
        return matrix
    @classmethod
    def set_matrix(cls, matrix, other):
        for i in range(len(other)):
            matrix[i] = other[i]
        return matrix
    @classmethod
    def set_sub_matrix(cls, matrix, other, row, column, m, n):
        w = cls.width(matrix)
        for i in range(m):
            for j in range(n):
                matrix[w * (row + i) + (column + j)] = other[i * m + j]
        return matrix

    @classmethod
    def determinant_sub_matrix(cls, matrix, column):
        n = cls.width(matrix)
        sub_matrix = cls.zero_matrix(n - 1)
        cls.set_sub_matrix(
            sub_matrix, cls.sub_matrix(matrix, 1, 0, n - 1, i),
            0, 0, n - 1, i
            )
        cls.set_sub_matrix(
            sub_matrix, cls.sub_matrix(matrix, 1, i + 1, n - 1, n - 1 - i),
            0, i, n - 1, n - 1 - i
            )
        return sub_matrix
    @classmethod
    def determinant(cls, matrix):
        n = cls.width(matrix)
        if n > 2:
            result = 0
            for i in range(n):
                sub_matrix = cls.determinant_sub_matrix(matrix, i)
                result += matrix[i] * cls.determinant(sub_matrix)
        else:
            a, b, c, d = matrix
            result = a * c - b * d
        return result

    @staticmethod
    def add_scalar(matrix, scalar):
        return [i + scalar for i in matrix]
    @staticmethod
    def iadd_scalar(matrix, scalar):
        for i in range(len(matrix)):
            matrix[i] += scalar
        return matrix
    @staticmethod
    def add_matrix(matrix, other):
        return [a + b for a, b in zip(matrix, other)]
    @staticmethod
    def iadd_matrix(matrix, other):
        for i in range(len(other)):
            matrix[i] += other[i]
        return matrix
    @staticmethod
    def subtract_scalar(matrix, scalar):
        return [i - scalar for i in matrix]
    @staticmethod
    def isubtract_scalar(matrix, scalar):
        for i in range(len(matrix)):
            matrix[i] -= scalar
        return matrix
    @staticmethod
    def subtract_matrix(matrix, other):
        return [a - b for a, b in zip(matrix, other)]
    @staticmethod
    def isubtract_matrix(matrix, other):
        for i in range(len(other)):
            matrix[i] -= other[i]
        return matrix
    @staticmethod
    def multiply_scalar(matrix, scalar):
        return [i * scalar for i in matrix]
    @staticmethod
    def imultiply_scalar(matrix, scalar):
        for i in range(len(matrix)):
            matrix[i] *= scalar
        return matrix
    @classmethod
    def multiply_vector(cls, matrix, vector):
        vecnd = VectorND
        new_vector = vecnd.new
        dot = vecnd.dot_product
        return new_vector(
            [dot(vector, row) for row in cls.rows(matrix)]
            )
    @classmethod
    def imultiply_vector(cls, matrix, vector):
        new_vector = cls.multiply_vector(matrix, vector)
        return VectorND.set_components(vector, new_vector)
    @staticmethod
    def multiply_line(matrix, line):
        linend = LineND
        new_line = linend.new
        get_direction = linend.direction
        get_point = linend.through_point
        transform = cls.multiply_vector
        direction = transform(matrix, get_direction(line))
        point = transform(matrix, get_point(line))
        return new_line(direction, point)
    @classmethod
    def imultiply_line(matrix, line):
        new_line = cls.multiply_line(matrix, line)
        return LineND.set_line(line, new_line)
    @staticmethod
    def multiply_plane(matrix, plane):
        planend = PlaneND
        new_line = planend.new
        get_direction = planend.direction
        get_point = planend.through_point
        set_components = planend.set_components
        transform = cls.multiply_vector
        direction = transform(matrix, get_direction(plane))
        point = transform(matrix, get_point(plane))
        return new_plane(direction, point)
    @classmethod
    def imultiply_plane(cls,matrix, plane):
        new_plane = cls.multiply_plane(matrix, plane)
        return PlaneND.set_plane(plane, new_plane)
    @classmethod
    def multiply_matrix(cls, matrix, other):
        dot = VectorND.dot_product
        n = cls.width(other)
        new_matrix = cls.zero_matrix(n)
        for i in range(n):
            row = cls.row_vector(matrix, i)
            for j in range(n):
                column = cls.column_vector(other, j)
                new_matrix[n * i + j] = dot(row, column)
        return new_matrix
    @classmethod
    def imultiply_matrix(cls, matrix, other):
        new_matrix = cls.multiply_matrix(matrix, other)
        return cls.set_matrix(matrix, new_matrix)

    @staticmethod
    def divide_scalar(matrix, scalar):
        return [i / scalar for i in matrix]

matnd = matrixnd = MatrixND = MatrixNDSingleton()
