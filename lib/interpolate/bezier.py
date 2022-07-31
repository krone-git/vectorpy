from abc import ABC, abstractmethod
from .abc import InterpolationSingletonABC, ParametricFunctionType


__all__ = (
    "c_bez", "cube_bez", "cubic_bezier", "CubicBezier", "CubicBezierCurve"
    )

class CubicBezierCurveSingleton(InterpolationSingletonABC,
                                ParametricFunctionType):
    @staticmethod
    def new(a, b, c, d):
        return [
            1.0 if a > 1.0 else 0.0 if a < 0.0 else a / 1.0, b / 1.0,
            1.0 if c > 1.0 else 0.0 if c < 0.0 else c / 1.0, d / 1.0
            ]
    @staticmethod
    def zero_curve(): return [0.0, 0.0, 0.0, 0.0] 

    @staticmethod
    def set_curve(curve, other):
        curve[0], curve[1], curve[2], curve[3] = other
        return curve

    @staticmethod
    def set_component(curve, index, value):
        value = value / 1.0 if index % 2 \
            else (1.0 if a > 1.0 else 0.0 if a < 0.0 else a / 1.0)
        curve[index] = value
        return curve
    @staticmethod
    def set_components(curve, a, b, c, d):
        curve[0] = 1.0 if a > 1.0 else 0.0 if a < 0.0 else a / 1.0
        curve[1] = b / 1.0
        curve[2] = 1.0 if c > 1.0 else 0.0 if c < 0.0 else c / 1.0
        curve[3] = d / 1.0
        return curve

    @staticmethod
    def set_point(curve, point, a, b):
        index = point * 2
        curve[index] = 1.0 if a > 1.0 else 0.0 if a < 0.0 else a / 1.0
        curve[index + 1] = b / 1.0
        return curve

    @staticmethod
    def parametric(curve, t):
        a, b, c, d = curve
        a3 = 3 * a
        b3 = 3 * b
        c3 = 3 * c
        d3 = 3 * d
        tt = t**2
        ttt = t**3
        return (
            (a3 - c3 + 1) * ttt + (c3 - 2 * a3) * tt + a3 * t,
            (b3 - d3 + 1) * ttt + (d3 - 2 * b3) * tt + b3 * t
            )
    @staticmethod
    def parametric_generator(curve, steps):
        a, b, c, d = curve
        a3 = 3 * a
        b3 = 3 * b
        c3 = 3 * c
        d3 = 3 * d
        for i in range(steps):
            t = i / steps
            tt = t**2
            ttt = t**3
            yield (
                (a3 - c3 + 1) * ttt + (c3 - 2 * a3) * tt + a3 * t,
                (b3 - d3 + 1) * ttt + (d3 - 2 * b3) * tt + b3 * t
                )


c_bez = cube_bez = cubic_bezier = CubicBezier = CubicBezierCurve = CubicBezierCurveSingleton()
