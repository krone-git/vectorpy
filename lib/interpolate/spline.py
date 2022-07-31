from abc import ABC, abstractmethod
from .abc import InterpolationSingletonABC, ExplicitFunctionType


__all__ = (
    "ch_spline", "cubic_hermite_spline", "CubicHermiteSpline"
    )

class CubicHermiteSplineSingleton(InterpolationSingletonABC,
                                    ExplicitFunctionType):
    @staticmethod
    def new(a, b): return [a / 1.0, b / 1.0]

    @staticmethod
    def zero_curve(): return [0.0, 0.0]

    @staticmethod
    def set_curve(curve, other):
        curve[0], curve[1] = other
        return spline

    @staticmethod
    def set_component(curve, index, value):
        curve[index] = value / 1.0
        return spline
    @staticmethod
    def set_components(curve, a, b):
        curve[0] = a / 1.0
        curve[1] = b / 1.0
        return curve

    @staticmethod
    def explicit(curve, x):
        a, b = curve
        return x**3 * (a - 2 + b) + x**2 * (3 - b - 2 * a) + x * a
    @staticmethod
    def explicit_derivative(curve, x):
        a, b = curve
        return 3 * x**2 * (a - 2 + b) + 2 * x * (2 - b - 2 * a) + a
    @staticmethod
    def explicit_second_derivative(curve, x):
        a, b = curve
        return 6 * x * (a - 2 + b) + 2 * (2 - b - 2 * a) + a
    @staticmethod
    def explicit_third_derivative(curve, x):
        a, b = curve
        return 6 * (a - 2 + b)
    @staticmethod
    def explicit_integral(curve, x):
        a, b = curve
        return x**4 * (a - 2 + b) / 4 + x**3 * (2 - b - 2 * a) / 3 + x**2 * a / 2

    @staticmethod
    def explicit_generator(curve, steps):
        a, b = curve
        p = a - 2 + b
        q = 3 - b - 2 * a
        for i in range(steps):
            x = i / steps
            yield x**3 * p + x**2 * q + x * a
    @staticmethod
    def explicit_derivative_generator(curve, steps):
        a, b = curve
        p = 3 * (a - 2 + b)
        q = 2 * (3 - b - 2 * a)
        for i in range(steps):
            x = i / steps
            yield x**2 * p + x * q + a
    @staticmethod
    def explicit_second_derivative_generator(curve, steps):
        a, b = curve
        p = 6 * (a - 2 + b)
        q = 2 * (3 - b - 2 * a)
        for i in range(steps):
            x = i / steps
            yield x * p + q
    @staticmethod
    def explicit_third_derivative_generator(curve, steps):
        a, b = curve
        p = 6 * (a - 2 + b)
        for i in range(steps):
            yield p
    @staticmethod
    def explicit_integral_generator(curve, steps):
        a, b = curve
        p = (a - 2 + b) / 4
        q = (2 - b - 2 * a) / 3
        r = a / 2
        for i in range(steps):
            x = i / steps
            yield x**4 * p + x**3 * q + x**2 * r

ch_spline = cubic_hermite_spline = CubicHermiteSpline = CubicHermiteSplineSingleton()
