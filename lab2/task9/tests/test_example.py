def read(num_len, file_A, file_B):
    A = []
    B = []
    d = []
    for x in file_A:
        d.append(int(x))
        if len(d) == num_len:
            A.append(d) 
            d = []
    for x in file_B:
        d.append(int(x))
        if len(d) == num_len:
            B.append(d) 
            d = []
    return [A, B]


def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))


def ikj_matrix_product(num_len, file_A, file_B):
    g = read(num_len, file_A, file_B)
    n = len(g[0])
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += g[0][i][k] * g[1][k][j]
    return C
a = '1 2 3 4 5 6 7 8 9'
b = '9 8 7 6 5 4 3 2 1'
print(ikj_matrix_product(3, list(map(int, list(a.split(' ')))), list(map(int, list(b.split(' '))))))