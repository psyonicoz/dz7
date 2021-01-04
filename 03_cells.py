class Cell:
    cells = 55

    def __init__(self, cell_num):
        self.cell_num = int(cell_num)

    def __add__(self, other):
        Cell.cells -= 1
        return Cell(f'{self.cell_num + other.cell_num}')

    def __sub__(self, other):
        Cell.cells -= 1
        if self.cell_num > other.cell_num:
            return Cell(f'{self.cell_num - other.cell_num}')
        else:
            return f'Разность количества ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        Cell.cells -= 1
        return Cell(f'{self.cell_num * other.cell_num}')

    def __truediv__(self, other):
        Cell.cells -= 1
        return Cell(f' {self.cell_num // other.cell_num}')

    def make_order(self, cells_in_row):
        rows = ''
        for i in range(int(self.cell_num / cells_in_row)):
            rows += f'{"*" * cells_in_row}\n'
        rows += f'{"*" * (self.cell_num % cells_in_row)}'
        return f'{rows}'

    def __str__(self):
        return f'{self.cell_num}'


a = Cell(2)
b = Cell(30)
c = a + b
d = a - b
e = a * b
f = a / b

print(c.make_order(12))
print(e.make_order(10))
print(c)
print(d)
print(e)
print(f)
print(Cell.cells)
