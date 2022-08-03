from lib import vec2d, mat2d
import tkinter as tk, abc


class TkinterCanvasShape(abc.ABC):
    _function = None
    def __init__(self, canvas, origin, width, height, **kwargs):
        self._canvas = canvas
        self._origin = origin
        self._width = int(width)
        self._height = int(height)
        self._tag = None
        self._config = {**kwargs}

    @property
    def width(self): return self._width
    @width.setter
    def width(self, value): self._width = int(value)
    @property
    def height(self): return self._height
    @height.setter
    def height(self, value): self._height = int(value)
    @property
    def x(self): return self._origin[0]
    @x.setter
    def x(self, value): self._origin[0] = int(value)
    @property
    def y(self): return self._origin[1]
    @y.setter
    def y(self, value): self._origin[1] = int(value)
    @property
    def origin(self): return self._origin
    @origin.setter
    def origin(self, origin):
        self.x = origin[0]
        self.y = origin[1]
    @property
    def bbox(self):
        w, h = self.width / 2, self.height / 2
        return (self.x - w, self.y - h, self.x + w, self.y + h)
    @property
    def config(self): return self._config

    def draw(self):
        if self._function and not self._tag:
            function = getattr(self._canvas, self._function)
            self._tag = function(*self.bbox, **self._config)
        else:
            self.update()
        return self

    def update(self):
        if self._tag:
            self._canvas.coords(self._tag, *self.bbox)
            self._canvas.itemconfig(self._tag, **self._config)
        return self

    @property
    def visible(self): return
    @visible.setter
    def visible(self, value): self.show() if value else self.hide()

    def show(self):
        self._config["state"] = tk.NORMAL
        self.update()
        return self

    def hide(self):
        self._config["state"] = tk.HIDDEN
        self.update()
        return self


class TkinterCanvasRectangle(TkinterCanvasShape):
    _function = "create_rectangle"

class TkinterCanvasLine(TkinterCanvasShape):
    _function = "create_line"
    def __init__(self, canvas, origin, point, **kwargs):
        self._point = point
        super().__init__(canvas, origin, 0, 0, **kwargs)

    @classmethod
    def from_vector(cls, canvas, origin, vector, **kwargs):
        self = cls(canvas, origin, [0, 0], **kwargs)
        self.vector = vector
        return self

    @property
    def point(self): return self._point
    @point.setter
    def point(self, point): self.point_x, self.point_y = point
    @property
    def point_x(self): return self._point[0]
    @point_x.setter
    def point_x(self, value): self._point[0] = int(value)
    @property
    def point_y(self): return self._point[1]
    @point_y.setter
    def point_y(self, value): self._point[1] = int(value)
    @property
    def vector(self): return (self.vector_x, self.vector_y)
    @vector.setter
    def vector(self, vector): self.vector_x, self.vector_y = vector
    @property
    def vector_x(self): return self.point_x - self.origin_x
    @vector_x.setter
    def vector_x(self, value): self.point_x = self.origin_x + value
    @property
    def vector_y(self): return self.point_y - self.origin_x
    @vector_y.setter
    def vector_y(self, value): self.point_y = self.origin_y + value
    @property
    def origin_x(self): return self._origin[0]
    @origin_x.setter
    def origin_x(self, value): self._origin[0] = int(value)
    @property
    def origin_y(self): return self._origin[1]
    @origin_y.setter
    def origin_y(self, value): self._origin[1] = int(value)
    @property
    def width(self): return self.point_x
    @width.setter
    def width(self, value): self.point_x = value
    @property
    def height(self): return self.point_y
    @height.setter
    def height(self, value): self.point_y = value
    @property
    def bbox(self): return (*self.origin, *self.point)


class TkinterCanvasOval(TkinterCanvasShape):
    _function = "create_oval"


class TkinterCanvasCircle(TkinterCanvasOval):
    def __init__(self, canvas, origin, radius, **kwargs):
        super().__init__(canvas, origin, radius, radius, **kwargs)
        self._radius = int(radius)

    @property
    def radius(self): return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = int(value)
    @property
    def width(self): return self.radius
    @width.setter
    def width(self, value): self.radius = value
    @property
    def height(self): return self.radius
    @height.setter
    def height(self, value): self.radius = value


def rotate_line(line, theta):
    pass


if __name__ == "__main__":
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 400

    window = tk.Tk()
    canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()


    origin = TkinterCanvasCircle(
        canvas,
        vec2d.new(CANVAS_WIDTH * 1/2, CANVAS_HEIGHT * 7/8),
        12,
        fill="red"
        )
    origin.draw()

    line = TkinterCanvasLine.from_vector(
        canvas, origin.origin, [0, -150], fill="blue"
        )
    line_end = TkinterCanvasCircle(
        canvas, line.point, 8, outline="blue", fill=""
        )
    line.draw()
    line_end.draw()

    window.mainloop()
