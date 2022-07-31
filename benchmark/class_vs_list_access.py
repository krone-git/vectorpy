import timeit


class VariableAccess:
    def __init__(self, x, y, z):
        self.x = x / 1.0
        self.y = y / 1.0
        self.z = z / 1.0


class IndexAccess:
    def __init__(self, x, y, z):
        self.x = x / 1.0
        self.y = y / 1.0
        self.z = z / 1.0

    def __getitem__(self, index):
        return self.x if index == 0 else self.y if index == 1 else self.z if index == 2 else None

    def __setitem__(self, index, value):
        self.x = value if index == 0 else self.x
        self.y = value if index == 1 else self.y
        self.z = value if index == 2 else self.z


class FunctionAccess:
    def __init__(self, x, y, z):
        self._x = x / 1.0
        self._y = y / 1.0
        self._z = z / 1.0

    def get(self, index):
        return (self._x if index == 0 else self._y if index == 1 else self._z if index == 2 else None)

    def x(self): return self._x
    def y(self): return self._y
    def z(self): return self._z


class PropertyAccess:
    def __init__(self, x, y, z):
        self._x = x / 1.0
        self._y = y / 1.0
        self._z = z / 1.0

    @property
    def x(self): return self._x
    @property
    def y(self): return self._y
    @property
    def z(self): return self._z


class HandlerAccess:
    @staticmethod
    def x(ls): return ls[0]
    @staticmethod
    def y(ls): return ls[1]
    @staticmethod
    def z(ls): return ls[2]

def get_x(ls): return ls[0]


if __name__ == "__main__":
    text_width = 20

    X, Y, Z = 1.0, 2.0, 3.0
    variable = VariableAccess(X, Y, Z)
    index = IndexAccess(X, Y, Z)
    function = FunctionAccess(X, Y, Z)
    _property = PropertyAccess(X, Y, Z)
    ls = [X, Y, Z]
    get_x = HandlerAccess.x

    variable_time = timeit.timeit(lambda: variable.x)
    index_time = timeit.timeit(lambda: index[0])
    function_time = timeit.timeit(lambda: function.x())
    _property_time = timeit.timeit(lambda: _property.x)
    ls_time = timeit.timeit(lambda: ls[0])
    handler_class_time = timeit.timeit(lambda: HandlerAccess.x(ls))
    handler_function_time = timeit.timeit(lambda: get_x(ls))


print(
    "variable_time: ".ljust(text_width) + str(variable_time),
    "index_time: ".ljust(text_width) + str(index_time),
    "function_time: ".ljust(text_width) + str(function_time),
    "_property_time: ".ljust(text_width) + str(_property_time),
    "ls_time: ".ljust(text_width) + str(ls_time),
    "handler_class_time: ".ljust(text_width) + str(handler_class_time),
    "handler_function_time: ".ljust(text_width) + str(handler_function_time),
    sep="\n", end="\n\n"
    )
