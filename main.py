from SudokuGenerator import Sudoku_Generator

sudoku = Sudoku_Generator(9, 70)
sudoku.fill_values()
sudoku.remove_cells()
sudoku.print_board()


