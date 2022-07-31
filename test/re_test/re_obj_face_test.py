import re


content = """f 1 2 3
f 1/2 3/4 5/6
f 1//2 3//4 5//6
f 1/2/3 4/5/6 7/8/9
f v1 v2 v3
f v1/vt1 v2/vt2 v3/vt3
f v1//vn1 v2//vn2 v3//vn3
f v1/vt1/vn1 v2/vt2/vn2 v3/vt3/vn3
"""

if __name__ == "__main__":
    FACE_PATTERN = "f\s+.*"
    PARAMETER_PATTERN = "\d+"

    for face in re.findall(FACE_PATTERN, content):
        print(face)
        for vertex in face.split()[1:]:
            print(" ", vertex)
            parameters = [
                int(p) if p else 0 for p in re.findall(PARAMETER_PATTERN, vertex)
                ]
            parameters.insert(1, 0) if "//" in vertex else None
            print("  ", *parameters)
