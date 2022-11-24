from .abc import TkinterCanvasPolygonABC


__all__ = (
    "tkTriangle", "TkinterTriangle", "TkinterCanvasTriangle"
    )

class TkinterCanvasTriangle(TkinterCanvasPolygonABC):
    def __init__(self, canvas, origin, left, right, *args, **kwargs):
        super().__init__(canvas, origin, *args, **kwargs)
        self._left = left
        self._right = right

    def coords(self):
        return (*self._origin, *self._left, *self._right)

tkTriangle = TkinterTriangle = TkinterCanvasTriangle
