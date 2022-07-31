import timeit


STR_KEY_SHORT = "a"
STR_KEY_LONG = "a" * 24

INT_KEY = 0

def str_key_short(d):
    return d[STR_KEY_SHORT]

def str_key_long(d):
    return d[STR_KEY_LONG]

def int_key(d):
    return d[INT_KEY]

if __name__ == "__main__":
    text_width = 24
    d = {
        STR_KEY_SHORT: 0,
        STR_KEY_LONG: 0,
        INT_KEY: 0
        }

    print(
        "**str_key_short_time: ".ljust(text_width) + str(timeit.timeit(lambda: str_key_short(d))),
        "str_key_long_time: ".ljust(text_width) + str(timeit.timeit(lambda: str_key_long(d))),
        "int_key_time: ".ljust(text_width) + str(timeit.timeit(lambda: int_key(d))),
        "str_key_short_time: ".ljust(text_width) + str(timeit.timeit(lambda: str_key_short(d))),
        sep="\n", end="\n\n"
        )
