def check(mat: list[list[float | int]]) -> None:
    """
    Проверяет, что матрица прямоугольная (все строки одной длины).
    Пустая матрица [] считается корректной.

    Исключения:
        ValueError - матрица рваная (строки разной длины).
    """
    if not mat:
        return
    k = len(mat[0])
    for row in mat:
        if len(row) != k:
            raise ValueError("рваная матрица")

def transpose(mat: list[list[float | int]]) -> list[list]:
    """
    Транспонирует прямоугольную матрицу (строки и столбцы меняются местами).
    Для пустой матрицы [] возвращает [].

    Исключения:
        ValueError - матрица рваная (строки разной длины).
    """
    check(mat)
    if len(mat) == 0:
        return []

    new_mat = []
    num_rows = len(mat)
    num_cols = len(mat[0])

    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(mat[i][j])
        new_mat.append(new_row)
    return new_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Возвращает список сумм по каждой строке матрицы.
    Для пустой матрицы [] возвращает [].

    Исключения:
        ValueError - матрица рваная (строки разной длины).
    """
    check(mat)
    if len(mat) == 0:
        return []

    res = []
    num_rows = len(mat)
    for i in range(num_rows):
        res.append(sum(mat[i]))
    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """
    Возвращает список сумм по каждому столбцу матрицы.
    Для пустой матрицы [] возвращает [].

    Исключения:
        ValueError - матрица рваная (строки разной длины).
    """
    check(mat)
    if len(mat) == 0:
        return []
    
    num_rows = len(mat)
    num_cols = len(mat[0])
    res = [0] * num_cols

    for i in range(num_rows):
        row = mat[i]
        for j in range(num_cols):
            res[j] += row[j]
    return res

# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))