import timeit


def inline_unpack_assignment(l, o):
    l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8] = o
    return l

def broken_inline_unpack_assignment(l, o):
    l[0], l[1], l[2], \
    l[3], l[4], l[5], \
    l[6], l[7], l[8] = o
    return l

def inline_index_assignment(l, o):
    l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8] = o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7], o[8]
    return l

def broken_inline_index_assignment(l, o):
    l[0], l[1], l[2], \
    l[3], l[4], l[5], \
    l[6], l[7], l[8] = o[0], o[1], o[2], \
    o[3], o[4], o[5], \
    o[6], o[7], o[8]
    return l

def partial_inline_slice_assignment(l, o):
    l[0] = l[1] = l[2] = o[0:3]
    l[3] = l[4] = l[5] = o[3:6]
    l[6] = l[7] = l[8] = o[6:9]
    return l

def multiline_index_assignment(l, o):
    l[0] = o[0]
    l[1] = o[1]
    l[2] = o[2]
    l[3] = o[3]
    l[4] = o[4]
    l[5] = o[5]
    l[6] = o[6]
    l[7] = o[7]
    l[8] = o[8]
    return l

def multiline_unpack_assignment(l, o):
    a, b, c, d, e, f, g, h, i = o
    l[0] = a
    l[1] = b
    l[2] = c
    l[3] = d
    l[4] = e
    l[5] = f
    l[6] = g
    l[7] = h
    l[8] = i
    return l



def inline_constant_assignment(l, v):
    l[0] = l[1] = l[2] = l[3] = l[4] = l[5] = l[6] = l[7] = l[8] = v
    return l

def broken_inline_constant_assignment(l, v):
    l[0] = l[1] = l[2] = \
    l[3] = l[4] = l[5] = \
    l[6] = l[7] = l[8] = v
    return l

def partial_inline_constant_assignment(l, v):
    l[0] = l[1] = l[2] = v
    l[3] = l[4] = l[5] = v
    l[6] = l[7] = l[8] = v
    return l

def multiline_constant_assignment(l, v):
    l[0] = v
    l[1] = v
    l[2] = v
    l[3] = v
    l[4] = v
    l[5] = v
    l[6] = v
    l[7] = v
    l[8] = v
    return l



def inline_parameter_assignment(l, a, b, c, d, e, f, g, h, i):
    l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8] = a, b, c, d, e, f, g, h, i
    return l

def broken_inline_parameter_assignment(l, a, b, c, d, e, f, g, h, i):
    l[0], l[1], l[2], \
    l[3], l[4], l[5], \
    l[6], l[7], l[8] = a, b, c, \
    d, e, f, \
    g, h, i
    return l

def partial_inline_parameter_assignment(l, a, b, c, d, e, f, g, h, i):
    l[0], l[1], l[2] = a, b, c
    l[3], l[4], l[5] = d, e, f
    l[6], l[7], l[8] = g, h, i
    return l

def multiline_parameter_assignment(l, a, b, c, d, e, f, g, h, i):
    l[0] = a
    l[1] = b
    l[2] = c
    l[3] = d
    l[4] = e
    l[5] = f
    l[6] = g
    l[7] = h
    l[8] = i
    return l



if __name__ == "__main__":
    text_width = 38
    v = 1.0
    l = [v] * 9
    o = l.copy()

    print(
        "**inline_unpack_assignment: ".ljust(text_width)        + str(timeit.timeit(lambda: inline_unpack_assignment(l, o))),
        "broken_inline_unpack_assignment: ".ljust(text_width)   + str(timeit.timeit(lambda : broken_inline_unpack_assignment(l, o))),
        "inline_index_assignment: ".ljust(text_width)           + str(timeit.timeit(lambda: inline_index_assignment(l, o))),
        "broken_inline_index_assignment: ".ljust(text_width)    + str(timeit.timeit(lambda : broken_inline_index_assignment(l, o))),
        "partial_inline_slice_assignment: ".ljust(text_width)   + str(timeit.timeit(lambda: partial_inline_slice_assignment(l, o))),
        "multiline_index_assignment: ".ljust(text_width)        + str(timeit.timeit(lambda: multiline_index_assignment(l, o))),
        "multiline_unpack_assignment: ".ljust(text_width)       + str(timeit.timeit(lambda: multiline_unpack_assignment(l, o))),
        "inline_unpack_assignment: ".ljust(text_width)          + str(timeit.timeit(lambda: inline_unpack_assignment(l, o))),
        sep="\n", end="\n\n"
        )

    print(
        "**inline_constant_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: inline_constant_assignment(l, v))),
        "broken_inline_constant_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: broken_inline_constant_assignment(l, v))),
        "partial_inline_constant_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: partial_inline_constant_assignment(l, v))),
        "multiline_constant_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: multiline_constant_assignment(l, v))),
        "inline_constant_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: inline_constant_assignment(l, v))),
        sep="\n", end="\n\n"
        )

    print(
        "inline_parameter_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: inline_parameter_assignment(l, v, v, v, v, v, v, v, v, v))),
        "broken_inline_parameter_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: broken_inline_parameter_assignment(l, v, v, v, v, v, v, v, v, v))),
        "partial_inline_parameter_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: partial_inline_parameter_assignment(l, v, v, v, v, v, v, v, v, v))),
        "multiline_parameter_assignment: ".ljust(text_width) + str(timeit.timeit(lambda: multiline_parameter_assignment(l, v, v, v, v, v, v, v, v, v))),
        sep="\n", end="\n\n"
        )
