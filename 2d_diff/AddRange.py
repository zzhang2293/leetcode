def add_range(matrix: list[list[int]], row1, col1, row2, col2, val) -> None:
    row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
    matrix[row1][col1] += val
    matrix[row2 + 1][col1] -= val
    matrix[row1][col2 + 1] -= val
    matrix[row2 + 1][col2 + 1] += val
    return


def build(matrix: list[list[int]]) -> list[list[int]]:
    row, col = len(matrix) + 2, len(matrix[0]) + 2
    updated = [[0] * row for _ in range(col)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            add_range(updated, i, j, i, j, matrix[i][j])
    return updated


def collect(matrix: list[list[int]]):
    row, col = len(matrix), len(matrix[0])
    for i in range(1, row):
        for j in range(1, col):
            matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]


m = [[0, 0, 0, 1],
     [0, 1, 4, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]]

update = build(m)
add_range(update, 1, 1, 3, 3, 100)
collect(update)
print(update)
