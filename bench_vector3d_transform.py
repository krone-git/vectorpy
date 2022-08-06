from lib import vec3d, mat3d, mat3dlt, mat3dpt
import timeit


if __name__ == "__main__":
    v0 = vec3d.new(1, 1, 1)
    v1 = vec3d.new(1, 1, 1)
    v2 = vec3d.new(1, 1, 1)
    v3 = vec3d.new(1, 1, 1)
    v4 = vec3d.new(1, 1, 1)
    v5 = vec3d.new(1, 1, 1)
    v6 = vec3d.new(1, 1, 1)

    m = mat3d.identity_matrix()
    t = mat3dlt.identity_matrix()
    p = mat3dpt.identity_matrix()

    print(
        "**multiply:             " + str(timeit.timeit(lambda: mat3d.multiply_vector(m, v0))),
        "multiply:               " + str(timeit.timeit(lambda: mat3d.multiply_vector(m, v1))),
        "imultiply:              " + str(timeit.timeit(lambda: mat3d.imultiply_vector(m, v2))),
        "linear transform:       " + str(timeit.timeit(lambda: mat3dlt.transform_vector(t, v3))),
        "linear itransform:      " + str(timeit.timeit(lambda: mat3dlt.itransform_vector(t, v4))),
        "perspective transform:  " + str(timeit.timeit(lambda: mat3dpt.transform_vector(p, v5))),
        "perspective itransform: " + str(timeit.timeit(lambda: mat3dpt.itransform_vector(p, v6))),
        sep="\n",
        end="\n\n"
        )
