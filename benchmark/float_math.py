import timeit


def fpf(): return 1.0 + 1.0
def fpi(): return 1.0 + 1
def ipi(): return 1 + 1
def ipf(): return 1 + 1.0

if __name__ == "__main__":
    text_width = 12

    fpf_time = timeit.timeit(fpf)
    fpi_time = timeit.timeit(fpi)
    ipi_time = timeit.timeit(ipi)
    ipf_time = timeit.timeit(ipf)

    print(
        "fpf_time: ".ljust(text_width) + str(fpf_time),
        "fpi_time: ".ljust(text_width) + str(fpi_time),
        "ipi_time: ".ljust(text_width) + str(ipi_time),
        "ipf_time: ".ljust(text_width) + str(ipf_time),
        sep="\n", end="\n\n"
        )
