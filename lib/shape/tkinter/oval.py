from .abc import TkinterCanvasShapeABC


__all__ = (
    "TkOval", "TkinterOval", "TkinterCanvasOval",
    "TkCircle", "TkinterCircle", "TkinterCanvasCircle"
    )

class TkinterCanvasOval(TkinterCanvasShapeABC):
    __DRAW_FUNCTION__ = "create_oval"

TkOval = TkinterOval = TkinterCanvasOval


class TkinterCanvasCircle(TkinterCanvasOval):
    def __init__(self, canvas, origin, radius, *args, **kwargs):
        super().__init__(
            canvas, origin, [radius / 2, radius / 2], *args, **kwargs
            )

    def radius(self): return self._dimension[0]
    def set_radius(self, width):
        super().set_width(width)
        super().set_height(width)
        return self
    def set_width(self, width):
        self.set_radius(width)
        return self
    def set_height(self, height):
        self.set_radius(height)
        return self

TkCircle = TkinterCircle = TkinterCanvasCircle
