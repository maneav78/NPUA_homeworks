import random

def generate_random_matrix(rows, cols):
    matrix = []
    for row in range(rows):
        matrix.append([random.randint(1, 100) for _ in range(cols)])
    return matrix


def get_column_sum(mat, col_ind):
    return sum(mat[i][col_ind] for i in range(len(mat)))


def get_row_average(mat, row_index):
    return sum(mat[row_index][i] for i in range(len(mat[0]))) / len(mat[0])


mat = generate_random_matrix(4, 3)
print(mat)
print(get_column_sum(mat, 0))
print(get_row_average(mat, 0))
