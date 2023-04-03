from lib.vector.vector import VectorND as vecnd
from lib.vector.vector2d import Vector2D as vec2d
from lib.vector.vector3d import Vector3D as vec3d
from timeit import timeit


if __name__ == "__main__":
    v2 = vec2d.new(1, 1)
    v3 = vec3d.new(1, 1, 1)
    _v2 = vec2d.new(1, 1)
    _v3 = vec3d.new(1, 1, 1)

    a2 = [1, 1]
    a3 = [1, 1, 1]

    print(
        "n-vector 2d new:       " + str(timeit(lambda: vecnd.new(1, 1))),
        "d-vector 2d new:       " + str(timeit(lambda: vec2d.new(1, 1))),
        "n-vector 3d new:       " + str(timeit(lambda: vecnd.new(1, 1, 1))),
        "d-vector 3d new:       " + str(timeit(lambda: vec3d.new(1, 1, 1))),
        "",
        "n-vector 2d add:       " + str(timeit(lambda: vecnd.add_vector(v2, v2))),
        "d-vector 2d add:       " + str(timeit(lambda: vec2d.add_vector(v2, v2))),
        "n-vector 3d add:       " + str(timeit(lambda: vecnd.add_vector(v3, v3))),
        "d-vector 3d add:       " + str(timeit(lambda: vec3d.add_vector(v3, v3))),
        "",
        "n-vector 2d magnitude: " + str(timeit(lambda: vecnd.magnitude(v2))),
        "d-vector 2d magnitude: " + str(timeit(lambda: vec2d.magnitude(v2))),
        "n-vector 3d magnitude: " + str(timeit(lambda: vecnd.magnitude(v3))),
        "d-vector 3d magnitude: " + str(timeit(lambda: vec3d.magnitude(v3))),
        "",
        "n-vector 2d dot:       " + str(timeit(lambda: vecnd.dot_product(v2, v2))),
        "d-vector 2d dot:       " + str(timeit(lambda: vec2d.dot_product(v2, v2))),
        "n-vector 3d dot:       " + str(timeit(lambda: vecnd.dot_product(v3, v3))),
        "d-vector 3d dot:       " + str(timeit(lambda: vec3d.dot_product(v3, v3))),
        "",
        # "n-vector 2d cross:     " + str(timeit(lambda: vecnd.cross_product(v2, v2))),
        # "d-vector 2d cross:     " + str(timeit(lambda: vec2d.cross_product(v2, v2))),
        # "n-vector 3d cross:     " + str(timeit(lambda: vecnd.cross_product(v3, v3))),
        # "d-vector 3d cross:     " + str(timeit(lambda: vec3d.cross_product(v3, v3))),
        # "",
        "n-vector 2d iterable:  " + str(timeit(lambda: vecnd.from_iterable(a2))),
        "d-vector 2d iterable:  " + str(timeit(lambda: vec2d.from_iterable(a2))),
        "n-vector 3d iterable:  " + str(timeit(lambda: vecnd.from_iterable(a3))),
        "d-vector 3d iterable:  " + str(timeit(lambda: vec3d.from_iterable(a3))),
        "",
        "n-vector 2d zero:      " + str(timeit(lambda: vecnd.zero_vector(2))),
        "d-vector 2d zero:      " + str(timeit(lambda: vec2d.zero_vector())),
        "n-vector 3d zero:      " + str(timeit(lambda: vecnd.zero_vector(3))),
        "d-vector 3d zero:      " + str(timeit(lambda: vec3d.zero_vector())),
        "",
        "n-vector 2d clear:     " + str(timeit(lambda: vecnd.clear(v2))),
        "d-vector 2d clear:     " + str(timeit(lambda: vec2d.clear(_v2))),
        "n-vector 3d clear:     " + str(timeit(lambda: vecnd.clear(v3))),
        "d-vector 3d clear:     " + str(timeit(lambda: vec3d.clear(_v3))),
        sep="\n",
        end="\n\n"
        )
