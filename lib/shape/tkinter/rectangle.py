from .abc import TkinterCanvasShapeABC


__all__ = (
    "TkinterCanvasRectangle", "TkinterRectangle", "TkRectangle",
    "TkinterCanvasSquare", "TkinterSquare", "TkSquare"
    )

class TkinterCanvasRectangle(TkinterCanvasShapeABC):
    __DRAW_FUNCTION__ = "create_rectangle"

TkRectangle = TkinterRectangle = TkinterCanvasRectangle


class TkinterCanvasSquare(TkinterCanvasRectangle):
    def __init__(self, canvas, origin, dimension, *args, **kwargs):
        super().__init__(
            canvas, origin, [dimension / 2, dimension / 2], *args, **kwargs
            )

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)
        return self
    def set_height(self, height):
        self.set_width(height)
        return self

TkSquare = TkinterSquare = TkinterCanvasSquare
