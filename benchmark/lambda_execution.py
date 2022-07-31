import timeit

lambda_none = lambda: None

def inline_function_none(): return None
def multiline_function_none():
    return None
def inline_function_pass(): pass
def multiline_function_pass():
    pass

lambda_1p1 = lambda: 1 + 1

def inline_function_1p1(): return 1 + 1
def multiline_function_1p1():
    return 1 + 1

lambda_xpx = lambda x: x + x

def inline_function_xpx(x): return x + x
def multiline_function_xpx(x):
    return x + x


if __name__ == "__main__":
    text_width = 30
    lambda_none_time = timeit.timeit(lambda: lambda_none())

    inline_function_none_time = timeit.timeit(lambda: inline_function_none())
    multiline_function_none_time = timeit.timeit(lambda: multiline_function_none())

    inline_function_pass_time = timeit.timeit(lambda: inline_function_pass())
    multiline_function_pass_time = timeit.timeit(lambda: multiline_function_pass())

print(
    "lambda_none_time: ".ljust(text_width) + str(lambda_none_time),
    "inline_function_none_time: ".ljust(text_width) + str(inline_function_none_time),
    "multiline_function_none_time: ".ljust(text_width) + str(multiline_function_none_time),
    "inline_function_pass_time: ".ljust(text_width) + str(inline_function_pass_time),
    "multiline_function_pass_time: ".ljust(text_width) + str(multiline_function_pass_time),
    sep="\n", end="\n\n"
    )

lambda_1p1_time = timeit.timeit(lambda: lambda_1p1())

inline_function_1p1_time = timeit.timeit(lambda: inline_function_1p1())
multiline_function_1p1_time = timeit.timeit(lambda: multiline_function_1p1())

print(
    "lambda_1p1_time: ".ljust(text_width) + str(lambda_1p1_time),
    "inline_function_1p1_time: ".ljust(text_width) + str(inline_function_1p1_time),
    "multiline_function_1p1_time: ".ljust(text_width) + str(multiline_function_1p1_time),
    sep="\n", end="\n\n"
    )

lambda_xpx_time = timeit.timeit(lambda: lambda_xpx(1))

inline_function_xpx_time = timeit.timeit(lambda: inline_function_xpx(1))
multiline_function_xpx_time = timeit.timeit(lambda: multiline_function_xpx(1))

print(
    "lambda_xpx_time: ".ljust(text_width) + str(lambda_xpx_time),
    "inline_function_xpx_time: ".ljust(text_width) + str(inline_function_xpx_time),
    "multiline_function_xpx_time: ".ljust(text_width) + str(multiline_function_xpx_time),
    sep="\n", end="\n\n"
    )
