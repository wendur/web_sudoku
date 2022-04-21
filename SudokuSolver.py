import copy
import math
import random


class SudokuSolver:
    def __init__(self, grid, size):
        self.grid = grid
        self.size = size

    def generate_sudoku(self, amount):
        for i in range(self.size):
            row = ['.' for j in range(self.size)]
            self.grid.append(row)

        a = 0
        if amount > self.size * self.size:
            amount = self.size * self.size
        while a < amount:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            if self.grid[i][j] == '.':
                values = self.find_possible_values((i, j))
                if len(values) > 0:
                    self.grid[i][j] = values.pop()
                a += 1

    def create_grid(self, filename):
        self.grid = []
        numbers = '.'
        for i in range(self.size):
            numbers += str(i + 1)
        values = [c for c in open(filename).read() if c in numbers]

        index = 0
        for i in range(int(len(values) / self.size)):
            row = []
            for j in range(self.size):
                row.append(values[index])
                index += 1
            self.grid.append(row)

    def display(self):
        str_out = []
        width = 2
        value = int(math.sqrt(self.size))
        line = "+".join(["-" * (width * value + 1)] * value)
        line_str = ''
        delim = ''
        for i in range(value - 1):
            delim += str((i + 1) * value - 1)

        for row in range(self.size):
            str_out.append(' ' + (
                "".join(
                            self.grid[row][col].center(width) + ("| " if str(col) in delim else "") for col in range(self.size)
                        )
                                )
                           )
            if str(row) in delim:
                # str_out += "\n"
                str_out.append(line)
            # str_out += "\n"

        return str_out

    def get_text(self):
        str_out = ''
        for i in range(self.size):
            for j in range(self.size):
                str_out += str(self.grid[i][j]) + ' '
            str_out += '\n'
        return str_out

    def get_row(self, pos, temp_grid=None):
        row, col = pos
        if temp_grid is None:
            return self.grid[row]
        else:
            return temp_grid[row]

    def get_col(self, pos, temp_grid=None):
        row, col = pos
        arr_col = []
        if temp_grid is None:
            for i in range(self.size):
                arr_col.append(self.grid[i][col])
        else:
            for i in range(self.size):
                arr_col.append(temp_grid[i][col])
        return arr_col

    def get_block(self, pos, temp_grid=None):
        row, col = pos
        arr_block = []

        row_s = math.floor(row / 3)
        col_s = math.floor(col / 3)

        for i in range(row_s * 3, (row_s + 1) * 3):
            for j in range(col_s * 3, (col_s + 1) * 3):
                if temp_grid is None:
                    arr_block.append(self.grid[i][j])
                else:
                    arr_block.append(temp_grid[i][j])

        return arr_block

    def check_empty_positions(self, temp_grid=None):
        for i in range(self.size):
            for j in range(self.size):
                if temp_grid is None:
                    if self.grid[i][j] == '':
                        return True
                else:
                    if temp_grid[i][j] == '':
                        return True
        return False

    def find_empty_positions(self, temp_grid=None):
        for i in range(self.size):
            for j in range(self.size):
                if temp_grid is None:
                    if self.grid[i][j] == '':
                        pos = (i, j)
                        return pos
                else:
                    if temp_grid[i][j] == '':
                        pos = (i, j)
                        return pos

    def find_possible_values(self, pos, temp_grid=None):
        numbers = []
        for i in range(self.size):
            numbers.append(str(i + 1))
        values = set(numbers)

        if temp_grid is None:
            row = self.get_row(pos)
            col = self.get_col(pos)
            block = self.get_block(pos)
        else:
            row = self.get_row(pos, temp_grid)
            col = self.get_col(pos, temp_grid)
            block = self.get_block(pos, temp_grid)

        values = values - set(row) - set(col) - set(block)

        return values

    def find_solution(self):
        self.grid = self.__solve(self.grid)

    def __solve(self, grid):
        # grid = self.grid
        # print(self.get_text())
        temp_grid = copy.deepcopy(grid)

        if not self.check_identity():
            return grid

        if self.check_empty_positions(grid):
            pos = self.find_empty_positions(grid)
        else:
            return grid
        values = self.find_possible_values(pos, grid)



        row, col = pos

        while len(values) > 0:
            grid[row][col] = values.pop()
            grid = self.__solve(grid)
            if not self.check_empty_positions(grid):
                break
            else:
                grid = copy.deepcopy(temp_grid)

        return grid

    def check_identity(self):
        rows = []
        cols = []
        block = []
        for i in range(self.size):
            rows = copy.deepcopy(self.get_row((i, i)))
            cols = copy.deepcopy(self.get_col((i, i)))
            for j in range(len(rows)-1, 0, -1):
                if rows[j] == '':
                    rows.pop(j)
            for j in range(len(cols)-1, 0, -1):
                if cols[j] == '':
                    cols.pop(j)
            if len(rows) != len(set(rows)) or len(cols) != len(set(cols)):
                return False

        row = int(math.sqrt(self.size))
        col = int(math.sqrt(self.size))
        for i in range(row):
            for j in range(col):
                block = copy.deepcopy(self.get_block((i * row, j * col)))
                for g in range(len(block)-1, 0, -1):
                    if block[g] == '':
                        block.pop(g)
                if len(block) != len(set(block)):
                    return False

        return True

    def check_solution(self):
        numbers = []

        for i in range(self.size):
            numbers.append(str(i + 1))

        values = set(numbers)

        for i in range(self.size):
            rows = set(self.get_row((i, i)))
            cols = set(self.get_col((i, i)))
            if values != rows or values != cols:
                return False

        row = int(math.sqrt(self.size))
        col = int(math.sqrt(self.size))
        for i in range(row):
            for j in range(col):
                block = set(self.get_block((i * row, j * col)))
                if values != block:
                    return False

        return True
