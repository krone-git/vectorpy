import timeit


class T:
    A = 0
    a_key = "a"
    def __init__(self):
        self._a = 0

    def a(self):
        return self.a

    def set_a(self, a):
        self._a = a
        return self

    def _set_a(self, a):
        self._a = a

def get_class_var(cls):
    return cls.A

def get_instance_var(inst):
    return inst._a

def get_instance_func(inst):
    return inst.a()

def get_primitive_key_dict_var(d):
    return d["a"]

def get_reference_key_dict_var(cls, d):
    return d[cls.a_key]

def set_instance_var(inst, a):
    inst._a = a

def set_instance_func(inst, a):
    return inst.set_a(a)

def _set_instance_func(inst, a):
    return inst._set_a(a)

def set_primitive_key_dict_var(d, a):
    d["a"] = a

def set_reference_key_dict_var(cls, d, a):
    d[cls.a_key] = a

if __name__ == "__main__":
    text_width = 38
    t = T()
    d = {"a": 0}

    print(
        "get_class_var_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: get_class_var(T))),
        "get_instance_var_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: get_instance_var(t))),
        "get_instance_func_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: get_instance_func(t))),
        "get_primitive_key_dict_var_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: get_primitive_key_dict_var(d))),
        "get_reference_key_dict_var_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: get_reference_key_dict_var(T, d))),
        "",
        "set_instance_var_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: set_instance_var(t, 0))),
        "set_instance_func_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: set_instance_func(t, 0))),
        "_set_instance_func_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: _set_instance_func(t, 0))),
        "set_primitive_key_dict_var_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: set_primitive_key_dict_var(d, 0))),
        "set_reference_key_dict_var_wrap_time: ".ljust(text_width) + str(timeit.timeit(lambda: set_reference_key_dict_var(T, d, 0))),
        "",
        "get_class_var_time: ".ljust(text_width) + str(timeit.timeit(lambda: T.A)),
        "get_instance_var_time: ".ljust(text_width) + str(timeit.timeit(lambda: t._a)),
        "get_instance_func_time: ".ljust(text_width) + str(timeit.timeit(lambda: t.a())),
        "get_primitive_key_dict_var_time: ".ljust(text_width) + str(timeit.timeit(lambda: d["a"])),
        "get_reference_key_dict_var_time: ".ljust(text_width) + str(timeit.timeit(lambda: d[T.a_key])),
        "",
        # "set_instance_var_time: ".ljust(text_width) + str(timeit.timeit(lambda: t._a = 0)),
        "set_instance_func_time: ".ljust(text_width) + str(timeit.timeit(lambda: t.set_a(0))),
        "_set_instance_func_time: ".ljust(text_width) + str(timeit.timeit(lambda: t._set_a(0))),
        # "set_primitive_key_dict_var_time: ".ljust(text_width) + str(timeit.timeit(lambda: d["a"] = 0))),
        # "set_reference_key_dict_var_time: ".ljust(text_width) + str(timeit.timeit(lambda: d[T] = 0))),
        sep="\n", end="\n\n"
        )
