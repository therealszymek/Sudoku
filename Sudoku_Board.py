import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.solution = []

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [row[col] for row in self.board]

    def valid_in_box(self, row_start, col_start, num):
        box = [self.board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
        return num not in box

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and \
               self.valid_in_box(row - row % 3, col - col % 3, num)

    def fill_box(self, row_start, col_start):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while True:
                    num = random.choice(numbers)
                    if self.is_valid(i, j, num):
                        self.board[i][j] = num
                        break
                    else:
                        numbers.remove(num)

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < 3:
            if col < 3:
                col = 3
        elif row < self.row_length - 3:
            if (col // 3) % 3 == 0:
                col += 3
        else:
            if col == self.row_length - 3:
                row += 3
                col = 0
            if row == self.row_length:
                return True
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 3)

    def remove_cells(self):
        for _ in range(self.removed_cells):
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            while self.board[row][col] == 0:
                row = random.randint(0, self.row_length - 1)
                col = random.randint(0, self.row_length - 1)
            self.board[row][col] = 0

    def generate_sudoku(self):
        self.fill_values()
        self.solution = [row[:] for row in self.board]  # Save the solution for later reference
        self.remove_cells()
        return self.board

    def get_solution(self):
        return self.solution
