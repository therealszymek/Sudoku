from SudokuGenerator import Sudoku_Generator, generate_sudoku

size = 9
removed = 40

# Generate a Sudoku puzzle
sudoku_board = generate_sudoku(size, removed)

print(sudoku_board)