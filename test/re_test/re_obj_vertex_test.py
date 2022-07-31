import re


content = """ v 1 2 3
v 4 5 6 7
v 1.0 12.10 123.120
v 4.4 45.45 456.456 4567.4567
"""

if __name__ == "__main__":
    VERTEX_PARAMETER_PATTERN = "\d+(\.\d*)?"
    VERTEX_PATTERN = "v\s+.*"

    for vertex in re.findall(VERTEX_PATTERN, content):
        print(vertex)
        for point in re.finditer(VERTEX_PARAMETER_PATTERN, vertex):
            print(point.group(0))
