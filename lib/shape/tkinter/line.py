from .abc import TkinterCanvasShapeABC


__all__ = (
    "TkLine", "TkinterLine", "TkinterCanvasLine"
    )

class TkinterCanvasLine(TkinterCanvasShapeABC):
    __DRAW_FUNCTION__ = "create_line"

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
        return x, y, x + p, y + q

TkLine = TkinterLine = TkinterCanvasLine
