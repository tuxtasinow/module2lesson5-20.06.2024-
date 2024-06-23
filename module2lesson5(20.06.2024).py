def get_matrix(n, m, value):
    matrix_1 = []
    for i in range(n):
        matrix_2 = []
        matrix_1.append(matrix_2)
        for j in range(m):
            matrix_2.append(value)
    return matrix_1

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)