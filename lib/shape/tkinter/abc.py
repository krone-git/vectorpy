from tkinter import NORMAL as TK_NORMAL, HIDDEN as TK_HIDDEN
from abc import ABC, abstractmethod


TK_STATE=  "state"


class TkinterCanvasType(ABC):
    def __init__(self, canvas):
        self._canvas = canvas

    def canvas_reference(self): return self._canvas


class TkinterOriginType(ABC):
    def __init__(self, origin):
        self._origin = origin

    def origin_reference(self): return self._origin
    def set_origin_reference(self, origin):
        self._origin = origin
        return self

    def origin(self): return self.origin_x(), self.origin_y()
    def set_origin(self, x, y):
        self.set_origin_x(x)
        self.set_origin_y(y)
        return self

    def origin_x(self): return self._origin[0]
    def set_origin_x(self, value):
        self._origin[0] = value
        return self
    def origin_y(self): return self._origin[1]
    def set_origin_y(self, value):
        self._origin[1] = value
        return self


class TkinterOrthogonalType(TkinterOriginType):
    def  __init__(self, origin, dimension, **kwargs):
        super().__init__(origin, **kwargs)
        self._dimension = dimension

    def reference_dimension(self): return self._dimension
    def set_reference_dimension(self, dimension):
        self._dimension = dimension
        return self

    def dimensions(self): return self.width(), self.height()
    def set_dimensions(self, width, height):
        self.set_width(width)
        self.set_height(height)
        return self
    def width(self): return self._dimension[0] * 2
    def set_width(self, width):
        self._dimension[0] = width / 2
        return self
    def height(self): return self._dimension[1] * 2
    def set_height(self, height):
        self._dimension[1] = height / 2
        return self
    def coords(self):
        x, y = self._origin
        p, q = self._dimension
        return x - p, y - q, x + p, y + q


class TkinterDrawableType(TkinterCanvasType):
    __DRAW_FUNCTION__ = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self._tag = None
        self._config = kwargs

    def tag(self): return self._tag
    def config(self): return self._config

    def visible(self): return self._config[TK_STATE] == TK_NORMAL
    def hide(self):
        self._config[TK_STATE] = TK_HIDDEN
        self.update_config()
        return self
    def show(self):
        self._config[TK_STATE] = TK_NORMAL
        self.update_config()
        return self

    def draw(self):
        if not self._tag and self.__DRAW_FUNCTION__:
            func = getattr(self._canvas, self.__DRAW_FUNCTION__)
            self._tag = func(*self.coords(), **self._config)
        return self

    @abstractmethod
    def coords(self): raise NotImplementedError
    def update_coords(self):
        self._canvas.coords(self._tag, *self.coords()) if self._tag else None
        return self
    def update_config(self):
        self._canvas.itemconfig(self._tag, **self._config) if self._tag else None
        return self
    def update(self):
        self.update_coords()
        self.update_config()
        return self


class TkinterCanvasShapeABC(TkinterOrthogonalType, TkinterDrawableType):
    __slots__ = ()

    def __init__(self, canvas, *args, **kwargs):
        TkinterOrthogonalType.__init__(self, *args)
        TkinterDrawableType.__init__(self, canvas, **kwargs)


class TkinterCanvasPolygonABC(TkinterOriginType, TkinterDrawableType):
    __slots__ = ()

    def __init__(self, canvas, *args, **kwargs):
        TkinterOriginType.__init__(self, *args)
        TkinterDrawableType.__init__(self, canvas, **kwargs)
