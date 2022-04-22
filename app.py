from flask import Flask, render_template, request
from SudokuSolver import *


app = Flask(__name__)

def get_start_grid():
    return [['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '']]

@app.route('/', methods=['GET', 'POST', 'CLEAR'])
def index():
    sudoku = SudokuSolver(get_start_grid(), 9)
    flag = None
    if request.method == 'POST':
        grid = [[request.form["cell_0_0"], request.form["cell_0_1"], request.form["cell_0_2"], request.form["cell_0_3"], request.form["cell_0_4"], request.form["cell_0_5"], request.form["cell_0_6"], request.form["cell_0_7"], request.form["cell_0_8"]],
                [request.form["cell_1_0"], request.form["cell_1_1"], request.form["cell_1_2"], request.form["cell_1_3"], request.form["cell_1_4"], request.form["cell_1_5"], request.form["cell_1_6"], request.form["cell_1_7"], request.form["cell_1_8"]],
                [request.form["cell_2_0"], request.form["cell_2_1"], request.form["cell_2_2"], request.form["cell_2_3"], request.form["cell_2_4"], request.form["cell_2_5"], request.form["cell_2_6"], request.form["cell_2_7"], request.form["cell_2_8"]],
                [request.form["cell_3_0"], request.form["cell_3_1"], request.form["cell_3_2"], request.form["cell_3_3"], request.form["cell_3_4"], request.form["cell_3_5"], request.form["cell_3_6"], request.form["cell_3_7"], request.form["cell_3_8"]],
                [request.form["cell_4_0"], request.form["cell_4_1"], request.form["cell_4_2"], request.form["cell_4_3"], request.form["cell_4_4"], request.form["cell_4_5"], request.form["cell_4_6"], request.form["cell_4_7"], request.form["cell_4_8"]],
                [request.form["cell_5_0"], request.form["cell_5_1"], request.form["cell_5_2"], request.form["cell_5_3"], request.form["cell_5_4"], request.form["cell_5_5"], request.form["cell_5_6"], request.form["cell_5_7"], request.form["cell_5_8"]],
                [request.form["cell_6_0"], request.form["cell_6_1"], request.form["cell_6_2"], request.form["cell_6_3"], request.form["cell_6_4"], request.form["cell_6_5"], request.form["cell_6_6"], request.form["cell_6_7"], request.form["cell_6_8"]],
                [request.form["cell_7_0"], request.form["cell_7_1"], request.form["cell_7_2"], request.form["cell_7_3"], request.form["cell_7_4"], request.form["cell_7_5"], request.form["cell_7_6"], request.form["cell_7_7"], request.form["cell_7_8"]],
                [request.form["cell_8_0"], request.form["cell_8_1"], request.form["cell_8_2"], request.form["cell_8_3"], request.form["cell_8_4"], request.form["cell_8_5"], request.form["cell_8_6"], request.form["cell_8_7"], request.form["cell_8_8"]]]

        sudoku = SudokuSolver(grid, 9)
        sudoku.find_solution()
        flag = sudoku.check_identity()
        if flag:
            flag = sudoku.check_solution()


    return render_template('index.html', sudoku=sudoku, flag=flag)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
