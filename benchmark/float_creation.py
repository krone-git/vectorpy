import timeit


def f(x):
    return x / 1

def g(x):
    return x / 1.0

def h(x):
    return float(x)


if __name__ == "__main__":
    text_width = 16

    float_float_f = timeit.timeit(lambda: f(1.0))
    int_float_f = timeit.timeit(lambda: f(1))
    print(
        "float_float_f: ".ljust(text_width) + str(float_float_f),
        "int_float_f: ".ljust(text_width) + str(int_float_f),
        sep="\n", end="\n\n"
        )

    float_float_g = timeit.timeit(lambda: g(1.0))
    int_float_g = timeit.timeit(lambda: g(1))
    print(
        "float_float_g: ".ljust(text_width) + str(float_float_g),
        "int_float_g: ".ljust(text_width) + str(int_float_g),
        sep="\n", end="\n\n"
        )

    float_float_h = timeit.timeit(lambda: h(1.0))
    int_float_h = timeit.timeit(lambda: h(1))
    print(
        "float_float_h: ".ljust(text_width) + str(float_float_h),
        "int_float_h: ".ljust(text_width) + str(int_float_h),
        sep="\n", end="\n\n"
        )
