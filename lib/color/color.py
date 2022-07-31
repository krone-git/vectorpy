

class Color:
    __slots__ = ()

    @staticmethod
    def new(r, g, b):
        return [
            255 if r > 255 else 0 if r < 0 else r,
            255 if g > 255 else 0 if r < 0 else g,
            255 if b > 255 else 0 if r < 0 else b
            ]

    @staticmethod
    def from_hex(hex_string):
        return [
            int(hexstring[-6:-4], 16),
            int(hexstring[-4:-2], 16),
            int(hexstring[-2:], 16)
            ]

    @staticmethod
    def from_ratio(r, g, b):
        return [
            256 * (1 if r > 1 else 0 if r < 0 else r) // 1,
            256 * (1 if g > 1 else 0 if r < 0 else g) // 1,
            256 * (1 if b > 1 else 0 if r < 0 else b) // 1
            ]

    @staticmethod
    def copy(color): return color.copy()

    @staticmethod
    def to_hex(color):
        r, g, b = color
        r_hex = hex(r)[2:].rjust(2, "0")
        g_hex = hex(g)[2:].rjust(2, "0")
        b_hex = hex(b)[2:].rjust(2, "0")
        return "#" + r_hex + g_hex + b_hex

    @staticmethod
    def to_ratio(color):
        r, g, b = color
        return [r / 256, g / 256, b / 256]

    @staticmethod
    def components(color):
        r, g, b = color
        return r, g, b

    @staticmethod
    def set_color(color, other):
        r, g, b = other
        color[0] = 255 if r > 255 else 0 if r < 0 else r
        color[1] = 255 if g > 255 else 0 if r < 0 else g
        color[2] = 255 if b > 255 else 0 if r < 0 else b
        return color

    @staticmethod
    def set_components(color, r, g, b):
        color[0] = 255 if r > 255 else 0 if r < 0 else r
        color[1] = 255 if g > 255 else 0 if r < 0 else g
        color[2] = 255 if b > 255 else 0 if r < 0 else b
        return color

    @staticmethod
    def add_color(color, other):
        r, g, b = color
        R, G, B = other
        r += R
        g += G
        b += B
        return [
            255 if r > 255 else 0 if r < 0 else r
            255 if g > 255 else 0 if r < 0 else g
            255 if b > 255 else 0 if r < 0 else b
            ]

    @staticmethod
    def iadd_color(color, other):
        r, g, b = color
        R, G, B = other
        r += R
        g += G
        b += B
        color[0] = 255 if r > 255 else 0 if r < 0 else r
        color[1] = 255 if g > 255 else 0 if r < 0 else g
        color[2] = 255 if b > 255 else 0 if r < 0 else b
        return color

    @staticmethod
    def add_components(color, r, g, b):
        R, G, B = color
        r += R
        g += G
        b += B
        return [
            255 if r > 255 else 0 if r < 0 else r
            255 if g > 255 else 0 if r < 0 else g
            255 if b > 255 else 0 if r < 0 else b
            ]

    @staticmethod
    def iadd_components(color, r, g, b):
        R, G, B = color
        r += R
        g += G
        b += B
        color[0] = 255 if r > 255 else 0 if r < 0 else r
        color[1] = 255 if g > 255 else 0 if r < 0 else g
        color[2] = 255 if b > 255 else 0 if r < 0 else b
        return color

    @staticmethod
    def subtract_color(color, other):
        r, g, b = color
        R, G, B = other
        r -= R
        g -= G
        b -= B
        return [
            255 if r > 255 else 0 if r < 0 else r
            255 if g > 255 else 0 if r < 0 else g
            255 if b > 255 else 0 if r < 0 else b
            ]

    @staticmethod
    def isubtract_color(color, other):
        r, g, b = color
        R, G, B = other
        r -= R
        g -= G
        b -= B
        color[0] = 255 if r > 255 else 0 if r < 0 else r
        color[1] = 255 if g > 255 else 0 if r < 0 else g
        color[2] = 255 if b > 255 else 0 if r < 0 else b
        return color

    @staticmethod
    def subtract_components(color, r, g, b):
        R, G, B = color
        r -= R
        g -= G
        b -= B
        return [
            255 if r > 255 else 0 if r < 0 else r
            255 if g > 255 else 0 if r < 0 else g
            255 if b > 255 else 0 if r < 0 else b
            ]

    @staticmethod
    def isubtract_components(color, r, g, b):
        R, G, B = color
        r -= R
        g -= G
        b -= B
        color[0] = 255 if r > 255 else 0 if r < 0 else r
        color[1] = 255 if g > 255 else 0 if r < 0 else g
        color[2] = 255 if b > 255 else 0 if r < 0 else b
        return color

    @staticmethod
    def multiply_components(color, r, g, b):
        R, G, B = color
        r *= R
        g *= G
        b *= B
        return [
            255 if r > 255 else 0 if r < 0 else r
            255 if g > 255 else 0 if r < 0 else g
            255 if b > 255 else 0 if r < 0 else b
            ]

    @staticmethod
    def imultiply_components(color, r, g, b):
        R, G, B = color
        r *= R
        g *= G
        b *= B
        color[0] = 255 if r > 255 else 0 if r < 0 else r
        color[1] = 255 if g > 255 else 0 if r < 0 else g
        color[2] = 255 if b > 255 else 0 if r < 0 else b
        return color

    @staticmethod
    def divide_components(color, r, g, b):
        R, G, B = color
        R /= r
        G /= g
        B /= b
        return [
            255 if R > 255 else 0 if R < 0 else R
            255 if G > 255 else 0 if G < 0 else G
            255 if B > 255 else 0 if B < 0 else B
            ]

    @staticmethod
    def idivide_components(color, r, g, b):
        R, G, B = color
        R /= r
        G /= g
        B /= b
        color[0] = 255 if R > 255 else 0 if R < 0 else R
        color[1] = 255 if G > 255 else 0 if G < 0 else G
        color[2] = 255 if B > 255 else 0 if B < 0 else B
        return color
