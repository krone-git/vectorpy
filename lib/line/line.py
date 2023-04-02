from .abc import LineSingletonABC


__all__ = (
    "line", "linend", "Line", "LineND"
    )

class LineNDSingleton():
    pass

line = linend = Line = LineND = LineNDSingleton()
