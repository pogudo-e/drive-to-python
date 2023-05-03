def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Меняем строки на столбцы или столбцы на строки в матрице
    :param matrix: Матрица
    :return:
    """
    tr_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tr_matrix[j][i] = matrix[i][j]

    return tr_matrix


def matrix_view(m: list[list[int]]):
    """
    Печать матрицы в консоль
    :param m : Матрица
    :return : Вывод в консоль
    """
    for row in m:
        for elem in row:
            print(elem, end=' ')
        print()


matrix_per = [[1, 2], [3, 4], [5, 6]]
matrix_view(matrix_per)
print()
matrix_view(transpose_matrix(matrix_per))
