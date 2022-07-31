from abc import ABC, abstractmethod


class ExplicitFunctionType(ABC):
    @abstractmethod
    def explicit(curve, x): raise NotImplementedError
    @abstractmethod
    def explicit_generator(curve, steps): raise NotImplementedError

    @abstractmethod
    def explicit_derivative(curve, x): raise NotImplementedError
    @abstractmethod
    def explicit_derivative_generator(curve, steps): raise NotImplementedError

    @abstractmethod
    def explicit_integral(curve, x): raise NotImplementedError
    @abstractmethod
    def explicit_integral_generator(curve, steps): raise NotImplementedError


class ParametricFunctionType(ABC):
    @abstractmethod
    def parametric(curve, t): raise NotImplementedError
    @abstractmethod
    def parametric_generator(curve, steps): raise NotImplementedError


class InterpolationSingletonABC(ABC):
    __slots__ = ()

    @abstractmethod
    def new(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def zero_curve(): raise NotImplementedError

    @staticmethod
    def copy(bezier): return bezier.copy()

    @abstractmethod
    def set_component(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_components(*args, **kwargs): raise NotImplementedError
    @abstractmethod
    def set_curve(curve, other): raise NotImplementedError
