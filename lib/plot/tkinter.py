

class TkinterPlotter:
    def __init__(self, canvas, origin=(0, 0), x_config={}, y_config={}):
        self._canvas = canvas
        self._visible = True
        self._origin = list(origin)
        self._axes = (
            TkinterPlotAxis(0, **x_config), TkinterPlotAxis(1, **y_config)
            )
        self._functions = []

    @property
    def canvas(self): return self._canvas
    @property
    def origin(self): return self._origin
    @property
    def axes(self): return self._axes
    @property
    def visible(self): return self._visible
    @property
    def functions(self): return self._functions

    def draw(self):
        [axis.draw(self._canvas, origin=self._origin) for axis in self._axes]
        [function.draw(self._canvas, origin=self._origin) for function in self._functions]
        return self

    def hide(self):
        self._visible = False

        return self

    def show(self):
        self._visible = True

        return self


class TkinterPlotAxis:
    def __init__(self, axis, scale=1, indices=10, index_len=10, color="black"):
        self._direction = 1 if axis else 0
        self._scale = scale
        self._color = color
        self._axis = None
        self._indices = indices
        self._index_len = index_len
        self._tags = []

    @property
    def scale(self): return self._scale
    @property
    def color(self): return self._color
    @property
    def indices(self): return self._indices
    @property
    def index_length(self): return self._index_len

    def draw(self, canvas, origin=(0, 0)):
        direction = self._direction
        color = self._color
        index = (direction + 1) % 2
        canvas_dimensions = (canvas.winfo_width(), canvas.winfo_height())
        axis_coords = [0] * 4
        axis_coords[index] = origin[index]
        axis_coords[index + 2] = origin[index]
        axis_coords[direction + 2] = canvas_dimensions[direction]
        if self._axis is None:
            self._axis = canvas.create_line(*axis_coords, fill=color)
        else:
            canvas.itemconfig(self._axis, fill=color)

        tag_count = len(self._tags)
        index_spacing = (canvas_dimensions[index] - origin[direction]) / self._indices
        for i in range(self._indices):
            tag = self._tags[i]
            coords = [0] * 4
            coords[index] = origin[index] - self._index_len
            coords[index + 2] = origin[index] + self._index_len
            coords[direction] = coords[direction + 2] = origin[direction] + index_spacing * (i + 1)
            if i < tag_count:
                canvas.coords(tag, *coords)
                canvas.itemconfig(tag, fill=color)
            else:
                indice = canvas.create_line(*coords, fill=color)
                self._tags.append(indice)
        return self


class TkinterPlotFunction:
    def __init__(self, function, resolution=50, color="red"):
        self._function = function
        self._resolution = resolution
        self._color = color
        self._tags = []

    def draw(canvas, origin=(0, 0)):
        pass

    def hide(self):
        pass

    def show(self):
        pass
