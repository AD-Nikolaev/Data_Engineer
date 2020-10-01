class Matrix():

    def __init__(self, mat):
        self.a = '\n'.join(['\t'.join([str(j) for j in i]) for i in mat])
        List = []
        for i in mat:
            List.append([j for j in i])
        self.mat = List

    def __str__(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                print(f'{self.mat[i][j]}', end=" ")
            print()
        return f""

    def __add__(self, other):
        result = []
        numbers = []
        a = len(self.mat)
        b = len(self.mat[0])
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other.mat[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

mat_1 = Matrix([[1, 2], [3, 4], [5, 6]])
mat_2 = Matrix([[2, 3], [4, 5], [6, 7]])

print(mat_1)
print(mat_2)

print(mat_1 + mat_2)
