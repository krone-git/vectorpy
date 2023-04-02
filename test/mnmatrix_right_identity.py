

def right_identity_matrix(m, n):
    matrix = [0.0] * (m * n)
    rows = min(m, n)
    for i in range(rows):
        matrix[m * i + i + m - rows] = 1.0
    return matrix

def mn_matrix_to_string(matrix, m, n):
    string = ""
    for i in range(n):
        string += "\t".join([str(v) for v in matrix[m * i: m * (i + 1)]]) + "\n"
    return string

if __name__ == "__main__":
    m, n = 10, 2
    matrix = right_identity_matrix(m, n)
    print(mn_matrix_to_string(matrix, m, n), end="\n\n")

    m, n = n, m
    matrix = right_identity_matrix(m, n)
    print(mn_matrix_to_string(matrix, m, n))
