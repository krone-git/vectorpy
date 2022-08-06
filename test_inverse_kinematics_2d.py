from lib import vec2d, mat2d, mat2dt
import tkinter as tk, abc


class TkinterCanvasShape(abc.ABC):
    _function = None
    def __init__(self, canvas, width, height, origin=None **kwargs):
        self._origin = origin if origin else [0.0, 0.0]
        self._canvas = canvas
        self._vector = [width / 2, height / 2]
        self._tag = None
        self._config = {**kwargs}

    @property
    def vector(self): return self._vector
    @property
    def origin(self): return self._origin
    @property
    def width(self): return self._vector[0] * 2
    @width.setter
    def width(self, value): self._vector[0] = value / 2
    @property
    def height(self): return self._vector[1] * 2
    @height.setter
    def height(self, value): self._vector[1] = value / 2
    @property
    def bbox(self):
        x, y = self._origin
        w, h = self._vector
        return (x - w, y - h, x + w, y + h)
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
    def __init__(self, canvas, vector, **kwargs):
        super().__init__(canvas, *vector, **kwargs)

    @property
    def length(self): return (self.vector_x**2 + self.vector_y**2)**0.5


class TkinterCanvasOval(TkinterCanvasShape):
    _function = "create_oval"


class TkinterCanvasCircle(TkinterCanvasOval):
    def __init__(self, canvas, radius, **kwargs):
        super().__init__(canvas, radius, radius, **kwargs)

    @property
    def radius(self): return self._vector[0]
    @radius.setter
    def radius(self, value):
        self._vector[0] = self.vector[1] = radius
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

    origin = vec2d.new(CANVAS_WIDTH * 1/2, 100),
    origin_mark = TkinterCanvasCircle(canvas, 12, origin=origin, fill="red")
    origin_mark.draw()

    line = vec2d.new(0, 100)
    line_mark = TkinterCanvasLine.from_vector(
        canvas, line, origin=origin, fill="blue"
        )
    line_end = TkinterCanvasCircle(canvas, 8, origin=line, outline="blue")
    line_mark.draw()
    line_end.draw()
    border = TkinterCanvasCircle(canvas, line.origin, 2 * line.length, fill="", outline="blue")
    border.draw()

    rotate = mat2dt.rotation(0.05)

    def rotate_line():
        mat2dt.itransform_vector(rotate, line)
        line_mark.update()
        line_end.update()
        window.after(2, rotate_line)

    window.after(2, rotate_line)

    window.mainloop()
