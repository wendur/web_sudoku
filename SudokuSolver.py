import math


class SudokuSolver:
    def __init__(self, filename="puzzle.txt", size=9):
        self.size = size
        self.grid = []
        self.create_grid(filename)

    def create_grid(self, filename):
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
        str_out = ''
        width = 2
        value = int(math.sqrt(self.size))
        line = "+".join(["-" * (width * value+1)] * value)
        delim = ''
        for i in range(value - 1):
            delim += str((i + 1) * value - 1)

        for row in range(self.size):
            str_out += ' ' + (
                "".join(
                    self.grid[row][col].center(width) + ("| " if str(col) in delim else "") for col in range(self.size)
                )
            )
            if str(row) in delim:
                str_out += "\n"
                str_out += line
            str_out += "\n"

        return str_out

