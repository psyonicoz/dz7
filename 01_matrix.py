class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __add__(self, other):
        result = []
        for lines in zip(self.arr, other.arr):
            temp = []
            for numbers in zip(lines[0], lines[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return result

    def __str__(self):
        return f'{self.arr}'

matrix1 = Matrix([[1, 2, 3, ], [7, 5, 6, ], [7, 5, 6, ]])
matrix2 = Matrix([[2, 3, 4, ], [5, 6, 7, ], [8, 6, 7, ]])
matrix3 = matrix1 + matrix2

print(matrix3)
