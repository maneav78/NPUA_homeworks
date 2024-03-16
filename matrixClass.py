import random
#I tried to import generate_random_matrix function from my matrix_operation.py file(from matrix_operation.py import generate_random_matrix, but for some reasons its starting to execute the other part of code too)
class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mat = generate_random_matrix(self.n, self.m)

    def print_matrix(self):
        for row in self.mat:
            print(" ".join(map(str, row)))

    def calc_mean(self):
        sum_of_elems = sum(sum(row) for row in self.mat)
        return sum_of_elems / (self.n*self.m)

    def sum_of_row(self, row):
        return sum(self.mat[row])

    def calc_average_column(self, col):
        return sum(self.mat[i][col] for i in range(self.n)) / self.n

    def subMatrix(self, col1, col2, row1, row2):
        if not (0 <= row1 <= row2 < self.n) or not (0 <= col1 <= col2 < self.m):
            print("Invalid indices provided.")
            return

        self.submat = []
        for i in range(row1, row2+1):
            self.submat.append(self.mat[i][col1:col2+1])
        return self.submat


def generate_random_matrix(rows, cols):
    matrix = []
    for row in range(rows):
        matrix.append([random.randint(1, 100) for _ in range(cols)])
    return matrix

m = Matrix(5,5)
m.print_matrix()
print(m.calc_mean())
print(m.sum_of_row(1))
print(m.calc_average_column(1))
m1 = m.subMatrix(1, 3, 1, 3)
for row in m1:
    print(" ".join(map(str, row)))