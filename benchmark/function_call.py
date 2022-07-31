import timeit

class A:
    def a(): pass
    def z(): pass

class Z:
    def a(): pass
    def b(): pass
    def c(): pass
    def d(): pass
    def e(): pass
    def f(): pass
    def g(): pass
    def h(): pass
    def i(): pass
    def j(): pass
    def k(): pass
    def l(): pass
    def m(): pass
    def n(): pass
    def o(): pass
    def p(): pass
    def q(): pass
    def r(): pass
    def s(): pass
    def t(): pass
    def u(): pass
    def v(): pass
    def w(): pass
    def x(): pass
    def y(): pass
    def z(): pass


def no_local_one_function_one_call():
    A.a()

def local_class_one_function_one_call():
    _A = A
    _A.a()

def local_function_one_function_one_call():
    a = A.a
    a()

def local_class_function_one_function_one_call():
    _A = A
    a = _A.a
    a()


def no_local_one_function_two_call():
    A.a()
    A.a()

def local_class_one_function_two_call():
    _A = A
    _A.a()
    _A.a()

def local_function_one_function_two_call():
    a = A.a
    a()
    a()

def local_class_function_one_function_two_call():
    _A = A
    a = _A.a
    a()
    a()


def no_local_one_function_three_call():
    A.a()
    A.a()
    A.a()

def local_class_one_function_three_call():
    _A = A
    _A.a()
    _A.a()
    _A.a()

def local_function_one_function_three_call():
    a = A.a
    a()
    a()
    a()

def local_class_function_one_function_three_call():
    _A = A
    a = _A.a
    a()
    a()
    a()


def no_local_one_function_ten_call():
    A.a()
    A.a()
    A.a()
    A.a()
    A.a()
    A.a()
    A.a()
    A.a()
    A.a()
    A.a()

def local_class_one_function_ten_call():
    _A = A
    _A.a()
    _A.a()
    _A.a()
    _A.a()
    _A.a()
    _A.a()
    _A.a()
    _A.a()
    _A.a()
    _A.a()

def local_function_one_function_ten_call():
    a = A.a
    a()
    a()
    a()
    a()
    a()
    a()
    a()
    a()
    a()
    a()

def local_class_function_one_function_ten_call():
    _A = A
    a = _A.a
    a()
    a()
    a()
    a()
    a()
    a()
    a()
    a()
    a()
    a()


def no_local_two_function_one_call():
    A.a()
    A.z()

def local_class_two_function_one_call():
    _A = A
    _A.a()
    _A.z()

def local_function_two_function_one_call():
    a = A.a
    z = A.z
    a()
    z()

def local_class_function_two_function_one_call():
    _A = A
    a = _A.a
    z = _A.z
    a()
    z()

def no_local_two_function_two_call():
    A.a()
    A.a()
    A.z()
    A.z()

def local_class_two_function_two_call():
    _A = A
    _A.a()
    _A.a()
    _A.z()
    _A.z()

def local_function_two_function_two_call():
    a = A.a
    z = A.z
    a()
    a()
    z()
    z()

def local_class_function_two_function_two_call():
    _A = A
    a = _A.a
    z = _A.z
    a()
    a()
    z()
    z()

def no_local_two_function_three_call():
    A.a()
    A.a()
    A.a()
    A.z()
    A.z()
    A.z()

def local_class_two_function_three_call():
    _A = A
    _A.a()
    _A.a()
    _A.a()
    _A.z()
    _A.z()
    _A.z()

def local_function_two_function_three_call():
    a = A.a
    z = A.z
    a()
    a()
    a()
    z()
    z()
    z()

def local_class_function_two_function_three_call():
    _A = A
    a = _A.a
    z = _A.z
    a()
    a()
    a()
    z()
    z()
    z()


def no_local_ten_function_one_call():
    Z.a()
    Z.b()
    Z.c()
    Z.d()
    Z.e()
    Z.f()
    Z.g()
    Z.h()
    Z.i()
    Z.z()

def local_class_ten_function_one_call():
    _Z = Z
    _Z.a()
    _Z.b()
    _Z.c()
    _Z.d()
    _Z.e()
    _Z.f()
    _Z.g()
    _Z.h()
    _Z.i()
    _Z.z()

def local_function_ten_function_one_call():
    a = Z.a
    b = Z.b
    c = Z.c
    d = Z.d
    e = Z.e
    f = Z.f
    g = Z.g
    h = Z.h
    i = Z.i
    z = Z.z
    a()
    b()
    c()
    d()
    e()
    f()
    g()
    h()
    i()
    z()

def local_class_function_ten_function_one_call():
    _Z = Z
    a = _Z.a
    b = _Z.b
    c = _Z.c
    d = _Z.d
    e = _Z.e
    f = _Z.f
    g = _Z.g
    h = _Z.h
    i = _Z.i
    z = _Z.z
    a()
    b()
    c()
    d()
    e()
    f()
    g()
    h()
    i()
    z()


def large_function_class():
    Z.a()
    Z.z()

def small_function_class():
    A.a()
    A.z()


if __name__ == "__main__":
    text_width = 46

    no_local_one_function_one_call_time = timeit.timeit(no_local_one_function_one_call)
    local_class_one_function_one_call_time = timeit.timeit(local_class_one_function_one_call)
    local_function_one_function_one_call_time = timeit.timeit(local_function_one_function_one_call)
    local_class_function_one_function_one_call_time = timeit.timeit(local_class_function_one_function_one_call)
    print(
        "no_local_one_function_one_call: ".ljust(text_width) + str(no_local_one_function_one_call_time),
        "local_class_one_function_one_call: ".ljust(text_width) + str(local_class_one_function_one_call_time),
        "local_function_one_function_one_call: ".ljust(text_width) + str(local_function_one_function_one_call_time),
        "local_class_function_one_function_one_call: ".ljust(text_width) + str(local_class_function_one_function_one_call_time),
        sep="\n", end="\n\n"
        )


    no_local_one_function_two_call_time = timeit.timeit(no_local_one_function_two_call)
    local_class_one_function_two_call_time = timeit.timeit(local_class_one_function_two_call)
    local_function_one_function_two_call_time = timeit.timeit(local_function_one_function_two_call)
    local_class_function_one_function_two_call_time = timeit.timeit(local_class_function_one_function_two_call)
    print(
        "no_local_one_function_two_call: ".ljust(text_width) + str(no_local_one_function_two_call_time),
        "local_class_one_function_two_call: ".ljust(text_width) + str(local_class_one_function_two_call_time),
        "local_function_one_function_two_call: ".ljust(text_width) + str(local_function_one_function_two_call_time),
        "local_class_function_one_function_two_call: ".ljust(text_width) + str(local_class_function_one_function_two_call_time),
        sep="\n", end="\n\n"
        )


    no_local_one_function_three_call_time = timeit.timeit(no_local_one_function_three_call)
    local_class_one_function_three_call_time = timeit.timeit(local_class_one_function_three_call)
    local_function_one_function_three_call_time = timeit.timeit(local_function_one_function_three_call)
    local_class_function_one_function_three_call_time = timeit.timeit(local_class_function_one_function_three_call)
    print(
        "no_local_one_function_three_call: ".ljust(text_width) + str(no_local_one_function_three_call_time),
        "local_class_one_function_three_call: ".ljust(text_width) + str(local_class_one_function_three_call_time),
        "local_function_one_function_three_call: ".ljust(text_width) + str(local_function_one_function_three_call_time),
        "local_class_function_one_function_three_call: ".ljust(text_width) + str(local_class_function_one_function_three_call_time),
        sep="\n", end="\n\n"
        )

    no_local_one_function_ten_call_time = timeit.timeit(no_local_one_function_ten_call)
    local_class_one_function_ten_call_time = timeit.timeit(local_class_one_function_ten_call)
    local_function_one_function_ten_call_time = timeit.timeit(local_function_one_function_ten_call)
    local_class_function_one_function_ten_call_time = timeit.timeit(local_class_function_one_function_ten_call)
    print(
        "no_local_one_function_ten_call: ".ljust(text_width) + str(no_local_one_function_ten_call_time),
        "local_class_one_function_ten_call: ".ljust(text_width) + str(local_class_one_function_ten_call_time),
        "local_function_one_function_ten_call: ".ljust(text_width) + str(local_function_one_function_ten_call_time),
        "local_class_function_one_function_ten_call: ".ljust(text_width) + str(local_class_function_one_function_ten_call_time),
        sep="\n", end="\n\n"
        )

    no_local_two_function_one_call_time = timeit.timeit(no_local_two_function_one_call)
    local_class_two_function_one_call_time = timeit.timeit(local_class_two_function_one_call)
    local_function_two_function_one_call_time = timeit.timeit(local_function_two_function_one_call)
    local_class_function_two_function_one_call_time = timeit.timeit(local_class_function_two_function_one_call)
    print(
        "no_local_two_function_one_call: ".ljust(text_width) + str(no_local_two_function_one_call_time),
        "local_class_two_function_one_call: ".ljust(text_width) + str(local_class_two_function_one_call_time),
        "local_function_two_function_one_call: ".ljust(text_width) + str(local_function_two_function_one_call_time),
        "local_class_function_two_function_one_call: ".ljust(text_width) + str(local_class_function_two_function_one_call_time),
        sep="\n", end="\n\n"
        )

    no_local_two_function_two_call_time = timeit.timeit(no_local_two_function_two_call)
    local_class_two_function_two_call_time = timeit.timeit(local_class_two_function_two_call)
    local_function_two_function_two_call_time = timeit.timeit(local_function_two_function_two_call)
    local_class_function_two_function_two_call_time = timeit.timeit(local_class_function_two_function_two_call)
    print(
        "no_local_two_function_two_call: ".ljust(text_width) + str(no_local_two_function_two_call_time),
        "local_class_two_function_two_call: ".ljust(text_width) + str(local_class_two_function_two_call_time),
        "local_function_two_function_two_call: ".ljust(text_width) + str(local_function_two_function_two_call_time),
        "local_class_function_two_function_two_call: ".ljust(text_width) + str(local_class_function_two_function_two_call_time),
        sep="\n", end="\n\n"
        )

    no_local_two_function_three_call_time = timeit.timeit(no_local_two_function_three_call)
    local_class_two_function_three_call_time = timeit.timeit(local_class_two_function_three_call)
    local_function_two_function_three_call_time = timeit.timeit(local_function_two_function_three_call)
    local_class_function_two_function_three_call_time = timeit.timeit(local_class_function_two_function_three_call)
    print(
        "no_local_two_function_three_call: ".ljust(text_width) + str(no_local_two_function_three_call_time),
        "local_class_two_function_three_call: ".ljust(text_width) + str(local_class_two_function_three_call_time),
        "local_function_two_function_three_call: ".ljust(text_width) + str(local_function_two_function_three_call_time),
        "local_class_function_two_function_three_call: ".ljust(text_width) + str(local_class_function_two_function_three_call_time),
        sep="\n", end="\n\n"
        )

    no_local_ten_function_one_call_time = timeit.timeit(no_local_ten_function_one_call)
    local_class_ten_function_one_call_time = timeit.timeit(local_class_ten_function_one_call)
    local_function_ten_function_one_call_time = timeit.timeit(local_function_ten_function_one_call)
    local_class_function_ten_function_one_call_time = timeit.timeit(local_class_function_ten_function_one_call)
    print(
        "no_local_ten_function_one_call: ".ljust(text_width) + str(no_local_ten_function_one_call_time),
        "local_class_ten_function_one_call: ".ljust(text_width) + str(local_class_ten_function_one_call_time),
        "local_function_ten_function_one_call: ".ljust(text_width) + str(local_function_ten_function_one_call_time),
        "local_class_function_ten_function_one_call: ".ljust(text_width) + str(local_class_function_ten_function_one_call_time),
        sep="\n", end="\n\n"
        )

    large_function_class_time = timeit.timeit(large_function_class)
    small_function_class_time = timeit.timeit(small_function_class)
    print(
        "large_function_class: ".ljust(text_width) + str(large_function_class_time),
        "small_function_class: ".ljust(text_width) + str(small_function_class_time),
        sep="\n", end="\n\n"
        )
