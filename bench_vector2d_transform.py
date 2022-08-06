from lib import vec2d, mat2d, mat2dt
import timeit


if __name__ == "__main__":
    v0 = vec2d.new(1, 1)
    v1 = vec2d.new(1, 1)
    v2 = vec2d.new(1, 1)
    v3 = vec2d.new(1, 1)
    v4 = vec2d.new(1, 1)

    m = mat2d.identity_matrix()
    t = mat2dt.identity_matrix()

    print(
        "**multiply: " + str(timeit.timeit(lambda: mat2d.multiply_vector(m, v0))),
        "multiply:   " + str(timeit.timeit(lambda: mat2d.multiply_vector(m, v1))),
        "imultiply:  " + str(timeit.timeit(lambda: mat2d.imultiply_vector(m, v2))),
        "transform:  " + str(timeit.timeit(lambda: mat2dt.transform_vector(t, v3))),
        "itransform: " + str(timeit.timeit(lambda: mat2dt.itransform_vector(t, v4))),
        sep="\n",
        end="\n\n"
        )
