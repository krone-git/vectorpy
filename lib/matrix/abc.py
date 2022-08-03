from abc import ABC, abstractmethod
from functools import reduce


class MatrixFactoryType(ABC):
    @abstractmethod
    def new(*args): raise NotImplementedError
    @classmethod
    def __call__(cls, *args, **kwargs): return cls.new(*args, **kwargs)

    @abstractmethod
    def zero_matrix(): raise NotImplementedError
    @abstractmethod
    def identity_matrix(): raise NotImplementedError

    @staticmethod
    def copy(matrix): return matrix.copy()


class MatrixFactoryVectorType(ABC):
    @abstractmethod
    def from_row_vectors(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def from_column_vectors(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def to_column_vectors(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def to_row_vectors(*args, **kwargs): raise NotImplementedError


class MatrixFactoryBasisType(ABC):
    @abstractmethod
    def from_basis(*args, **kwargs): raise NotImplementedError
    @classmethod
    def from_basis_vectors(cls, *args, **kwargs):
        return cls.from_column_vectors(*args, **kwargs)

    @abstractmethod
    def to_basis(*args, **kwargs): raise NotImplementedError
    @classmethod
    def to_basis_vectors(cls, *args, **kwargs):
        return cls.to_column_vectors(*args, **kwargs)


class MatrixAccessibleType(ABC):
    @abstractmethod
    def get_component(*args, **kwargs): raise NotImplementedError
    @classmethod
    def component(cls, *args, **kwargs): return cls.get_component(*args, **kwargs)
    get = component

    def get_components(matrix): return tuple(matrix)
    @classmethod
    def components(cls, *args, **kwargs): return cls.get_components(*args, **kwargs)

    @abstractmethod
    def column(matrix, column): raise NotImplementedError
    @abstractmethod
    def columns(matrix): raise NotImplementedError

    @abstractmethod
    def row(matrix, row): raise NotImplementedError
    @abstractmethod
    def rows(matrix): raise NotImplementedError


class MatrixMutableType(ABC):
    @abstractmethod
    def clear(matrix): raise NotImplementedError

    @abstractmethod
    def reset(matrix): raise NotImplementedError

    @abstractmethod
    def set_matrix(matrix, other): raise NotImplementedError

    @abstractmethod
    def set_component(matrix, row, column, value): raise NotImplementedError
    @classmethod
    def set(cls, *args, **kwargs): raise NotImplementedError

    @abstractmethod
    def set_components(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def set_row_vector(*args, **kwargs): raise NotImplementedError
    @classmethod
    def set_row(cls, *args, **kwargs): return cls.set_row_vector(*args, **kwargs)
    @abstractmethod
    def set_row_components(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def set_column_vector(*args, **kwargs): raise NotImplementedError
    @classmethod
    def set_column(cls, *args, **kwargs):
        return cls.set_column_vector(*args, **kwargs)
    @abstractmethod
    def set_column_components(*args, **kwargs): raise NotImplementedError


class MatrixPropertiesType(ABC):
    @abstractmethod
    def determinant(matrix): raise NotImplementedError


class MatrixScalarArithmeticType(ABC):
    @abstractmethod
    def add_scalar(matrix, other): raise NotImplementedError
    @classmethod
    def sum_matrices(cls, matrices): return reduce(cls.add_matrix, matrices)

    @abstractmethod
    def subtract_scalar(matrix, other): raise NotImplementedError

    @abstractmethod
    def multiply_scalar(matrix, scalar): raise NotImplementedError

    @abstractmethod
    def divide_scalar(matrix, scalar): raise NotImplementedError


class MatrixMutableScalarArithmeticType(ABC):
    @abstractmethod
    def iadd_scalar(matrix, other): raise NotImplementedError
    @classmethod
    def isum_matrices(cls, matrix, others):
        return reduce(cls.iadd_matrix, [matrix, *others])

    @abstractmethod
    def isubtract_scalar(matrix, other): raise NotImplementedError

    @abstractmethod
    def imultiply_scalar(matrix, scalar): raise NotImplementedError


class MatrixVectorArithmeticType(ABC):
    @abstractmethod
    def multiply_vector(matrix, vector): raise NotImplementedError
    @abstractmethod
    def imultiply_vector(matrix, vector): raise NotImplementedError

    @classmethod
    def apply_matrices_to_vector(cls, vector, matrices):
        return map(lambda matrix: cls.multiply_vector(matrix, vector), matrices)
    @classmethod
    def iapply_matrices_to_vector(cls, vector, matrices):
        return map(lambda matrix: cls.imultiply_vector(matrix, vector), matrices)

    @classmethod
    def product_vectors(cls, matrix, vectors):
        return map(lambda vector: cls.multiply_vector(matrix, vector), vectors)
    @classmethod
    def iproduct_vectors(cls, matrix, vectors):
        return map(lambda vector: cls.imultiply_vector(matrix, vector), vectors)


class MatrixLineArithmeticType(ABC):
    @abstractmethod
    def multiply_line(matrix, line): raise NotImplementedError
    @abstractmethod
    def imultiply_line(matrix, line): raise NotImplementedError

    @classmethod
    def product_lines(cls, matrix, lines):
        return map(lambda line: cls.multiply_line(matrix, line), lines)
    @classmethod
    def iproduct_lines(cls, matrix, lines):
        return map(lambda line: cls.imultiply_line(matrix, line), lines)


class MatrixPlaneArithmeticType(ABC):
    @abstractmethod
    def multiply_plane(matrix, plane): raise NotImplementedError
    @abstractmethod
    def imultiply_plane(matrix, plane): raise NotImplementedError

    @classmethod
    def product_planes(cls, matrix, planes):
        return map(lambda plane: cls.multiply_plane(matrix, plane), planes)
    @classmethod
    def iproduct_planes(cls, matrix, planes):
        return map(lambda plane: cls.imultiply_plane(matrix, plane), planes)


class MatrixArithmeticType(ABC):
    @abstractmethod
    def add_matrix(matrix, other): raise NotImplementedError

    @abstractmethod
    def subtract_matrix(matrix, other): raise NotImplementedError

    @abstractmethod
    def multiply_matrix(matrix, other): raise NotImplementedError

    @classmethod
    def product_matrices(cls, matrices):
        return reduce(cls.multiply_matrix, matrices)

    @classmethod
    def power_matrix(cls, matrix, power):
        return reduce(cls.multiply_matrix, [matrix] * (1 if power < 1 else power))


class MatrixMutableArithmeticType(ABC):
    @abstractmethod
    def iadd_matrix(matrix, other): raise NotImplementedError

    @abstractmethod
    def isubtract_matrix(matrix, other): raise NotImplementedError

    @abstractmethod
    def imultiply_matrix(matrix, other): raise NotImplementedError

    @classmethod
    def iproduct_matrices(cls, matrix, others):
        return reduce(cls.imultiply_matrix, [matrix, *others])

    @classmethod
    def ipower_matrix(cls, matrix, power):
        copy = cls.copy(matrix)
        return reduce(
            cls.imultiply_matrix,
            [matrix, *([copy] * (1 if power < 1 else power))]
            )


class MatrixSingletonABC(MatrixFactoryType,
                            MatrixFactoryVectorType,
                            MatrixFactoryBasisType,
                            MatrixAccessibleType,
                            MatrixMutableType,
                            MatrixPropertiesType,
                            MatrixScalarArithmeticType,
                            MatrixMutableScalarArithmeticType,
                            MatrixVectorArithmeticType,
                            MatrixLineArithmeticType,
                            MatrixPlaneArithmeticType,
                            MatrixArithmeticType,
                            MatrixMutableArithmeticType):
    __slots__=()

    @classmethod
    def apply_matrices_to_vectors(cls, matrices, vectors):
        matrix = cls.multiply_matrices(matrices)
        return map(lambda vector: cls.multiply_vector(matrix, vector), vectors)
    @classmethod
    def iapply_matrices_to_vectors(cls, matrices, vector):
        matrix = cls.multiply_matrices(matrices)
        return map(lambda vector: cls.imultiply_vector(matrix, vector), vectors)


class MatrixTransformArithmeticType(MatrixArithmeticType):
    @abstractmethod
    def compile(matrix, other): raise NotImplementedError

    @classmethod
    def multiply_matrix(cls, *args, **kwargs):
        return cls.compile(*args, **kwargs)

    @classmethod
    def compile_matrices(cls, matrics):
        return reduce(cls.compile, matrices)

    @classmethod
    def product_matrices(cls, matrics):
        return reduce(cls.compile, matrices)

    @classmethod
    def power_matrix(cls, matrix, power):
        return reduce(cls.compile_matrix, [matrix] * (1 if power < 1 else power))


class MatrixTransformMutableArithmeticType(MatrixMutableArithmeticType):
    @abstractmethod
    def icompile(matrix, other): raise NotImplementedError

    @classmethod
    def imultiply_matrix(cls, *args, **kwargs):
        return cls.icompile(*args, **kwargs)

    @classmethod
    def icompile_matrices(cls, matrix, others):
        return reduce(cls.icompile, [matrix, *others])

    @classmethod
    def iproduct_matrices(cls, matrix, others):
        return reduce(cls.icompile, [matrix, *others])

    @classmethod
    def ipower_matrix(cls, matrix, power):
        copy = cls.copy(matrix)
        return reduce(
            cls.icompile_matrix,
            [matrix, *([copy] * (1 if power < 1 else power))]
            )


class MatrixTransformVectorType(MatrixVectorArithmeticType):
    @abstractmethod
    def transform_vector(matrix, vector): raise NotImplementedError
    @abstractmethod
    def itransform_vector(matrix, vector): raise NotImplementedError

    @classmethod
    def multiply_vector(cls, *args, **kwargs):
        return cls.transform_vector(*args, **kwargs)
    @classmethod
    def imultiply_vector(cls, *args, **kwargs):
        return cls.itransform_vector(*args, **kwargs)

    @classmethod
    def transform_vectors(cls, matrix, vectors):
        return map(lambda vector: cls.transform_vector(matrix, vector), vectors)
    @classmethod
    def itransform_vectors(cls, matrix, vectors):
        return map(lambda vector: cls.itransform_vector(matrix, vector), vectors)

    @classmethod
    def product_vectors(cls, matrix, vectors):
        return map(lambda vector: cls.transform_vector(matrix, vector), vectors)
    @classmethod
    def iproduct_vectors(cls, matrix, vectors):
        return map(lambda vector: cls.itransform_vector(matrix, vector), vectors)


class MatrixTransformLineType(MatrixLineArithmeticType):
    @abstractmethod
    def transform_line(matrix, line): raise NotImplementedError
    @abstractmethod
    def itransform_line(matrix, line): raise NotImplementedError

    @classmethod
    def multiply_line(cls, *args, **kwargs):
        return cls.transform_line(*args, **kwargs)
    @classmethod
    def imultiply_line(cls, *args, **kwargs):
        return cls.itransform_line(*args, **kwargs)

    @classmethod
    def transform_lines(cls, matrix, lines):
        return map(lambda line: cls.transform_line(matrix, line), lines)
    @classmethod
    def itransform_lines(cls, matrix, lines):
        return map(lambda line: cls.itransform_line(matrix, line), lines)

    @classmethod
    def product_lines(cls, matrix, lines):
        return map(lambda line: cls.transform_line(matrix, line), lines)
    @classmethod
    def iproduct_lines(cls, matrix, lines):
        return map(lambda line: cls.itransform_line(matrix, line), lines)


class MatrixTransformPlaneType(MatrixPlaneArithmeticType):
    @abstractmethod
    def transform_plane(matrix, plane): raise NotImplementedError
    @abstractmethod
    def itransform_plane(matrix, plane): raise NotImplementedError

    @classmethod
    def multiply_plane(cls, *args, **kwargs):
        return cls.transform_plane(*args, **kwargs)
    @classmethod
    def imultiply_plane(cls, *args, **kwargs):
        return cls.itransform_plane(*args, **kwargs)

    @classmethod
    def transform_planes(cls, matrix, planes):
        return map(lambda plane: cls.transform_plane(matrix, plane), planes)
    @classmethod
    def itransform_planes(cls, matrix, planes):
        return map(lambda plane: cls.itransform_plane(matrix, plane), planes)

    @classmethod
    def product_planes(cls, matrix, planes):
        return map(lambda line: cls.transform_plane(matrix, plane), planes)
    @classmethod
    def iproduct_planes(cls, matrix, planes):
        return map(lambda line: cls.itransform_plane(matrix, plane), planes)


class MatrixTransformType(MatrixFactoryType,
                            MatrixAccessibleType,
                            MatrixMutableType,
                            MatrixPropertiesType,
                            MatrixTransformVectorType,
                            MatrixTransformArithmeticType,
                            MatrixTransformMutableArithmeticType,
                            MatrixTransformLineType,
                            MatrixTransformPlaneType):
    @abstractmethod
    def from_base_matrix(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def to_base_matrix(matrix): raise NotImplementedError

    # @abstractmethod
    # def change_basis(*args, **kwargs): raise NotImplementedError

    @classmethod
    def apply_matrices_to_vectors(cls, matrices, vectors):
        matrix = cls.compile_matrices(matrices)
        return map(lambda vector: cls.transform_vector(matrix, vector), vectors)
    @classmethod
    def iapply_matrices_to_vectors(cls, matrices, vector):
        matrix = cls.compile_matrices(matrices)
        return map(lambda vector: cls.itransform_vector(matrix, vector), vectors)


class MatrixLinearTransformSingletonABC(MatrixTransformType):
    __slots__ = ()

    @abstractmethod
    def base_matrix_to_linear_transform(matrix): raise NotImplementedError
    @classmethod
    def base_to_linear(cls, *args, **kwargs):
        return cls.base_matrix_to_linear_transform(*args, **kwargs)

    @abstractmethod
    def rotation(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_rotation(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def shear(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_shear(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def reflection(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_reflection(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def scale(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_scale(*args, **kwargs): raise NotImplementedError

    @abstractmethod
    def translation(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_translation(*args, **kwargs): raise NotImplementedError


class MatrixPerspectiveTransformSingletonABC(MatrixLinearTransformSingletonABC):
    __slots__ = ()

    @abstractmethod
    def perspective(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_perspective(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def orthogonal_perspective(): raise NotImplementedError
    @classmethod
    def indentity_matrix(cls, *args, **kwargs):
        return cls.orthogonal_perspective(*args, **kwargs)

    @abstractmethod
    def from_linear_transform(*args, **kwargs): raise NotImplementedError
    @classmethod
    def from_linear(cls, *args, **kwargs):
        return cls.from_linear_transform(*args, **kwargs)
    @abstractmethod
    def linear_transform_to_perspective_transform(matrix): raise NotImplementedError
    @classmethod
    def linear_to_perspective(cls, args, **kwargs):
        return cls.linear_transform_to_perspective_transform(*args, **kwargs)
    @abstractmethod
    def base_matrix_to_perspective_transform(matrix): raise NotImplementedError
    @classmethod
    def base_to_perspective(cls, *args, **kwargs):
        return cls.base_matrix_to_perspective_transform(*args, **kwargs)

    @abstractmethod
    def compile_linear(matrix, other): raise NotImplementedError
    @classmethod
    def compile_linear_matrices(cls, matrices):
        return reduce(cls.compile_linear, matrices)
    @classmethod
    def product_linear(cls, matrices):
        return reduce(cls.compile_linear, matrices)
    @abstractmethod
    def icompile_linear(matrix, other): raise NotImplementedError
    @classmethod
    def icompile_linear_matrices(cls, matrix, others):
        return reduce(cls.icompile_linear, [matrix, *others])
    @classmethod
    def iproduct_linear(cls, matrix, others):
        return reduce(cls.icompile_linear, [matrix, *others])

    @abstractmethod
    def compile_perspective(matrix, other): raise NotImplementedError
    @classmethod
    def compile(cls, *args, **kwargs):
        return cls.compile_perspective(*args, **kwargs)
    @classmethod
    def multiply_matrix(cls, *args, **kwargs):
        return cls.compile_perspective(*args, **kwargs)
    @classmethod
    def compile_perspective_matrices(cls, matrices):
        return reduce(cls.compile_perspective, matrices)
    @classmethod
    def product_perspective(cls, matrices):
        return reduce(cls.compile_perspective, matrices)
    @classmethod
    def compile_matrices(cls, matrics):
        return reduce(cls.compile_perspective, matrices)
    @classmethod
    def product_matrices(cls, matrics):
        return reduce(cls.compile_perspective, matrices)

    @abstractmethod
    def icompile_perspective(matrix, other): raise NotImplementedError
    @classmethod
    def icompile(cls, *args, **kwargs):
        return cls.icompile_perspective(*args, **kwargs)
    @classmethod
    def imultiply_matrix(cls, *args, **kwargs):
        return cls.icompile_perspective(*args, **kwargs)
    @classmethod
    def icompile_perspective_matrices(cls, matrix, others):
        return reduce(cls.icompile_perspective, [matrix, *others])
    @classmethod
    def iproduct_perspective(cls, matrix, others):
        return reduce(cls.icompile_perspective, [matrix, *others])
    @classmethod
    def icompile_matrices(cls, matrix, others):
        return reduce(cls.icompile_perspective, [matrix, *others])
    @classmethod
    def iproduct_matrices(cls, matrix, others):
        return reduce(cls.icompile_perspective, [matrix, *others])

    @classmethod
    def power_matrix(cls, matrix, power):
        return reduce(cls.compile_perspective, [matrix] * (1 if power < 1 else power))
