import math
import random

class Sudoku_Generator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for row in range(row_length)]
        self.box_length = 3


    def get_board(self):
      return self.board

    def print_board(self): # Returns None ?
      for row in self.board:
        print(" ".join(map(str, row)))

    def valid_in_row(self, row, num):
      inRow = False
      for i in range(0, len(self.board[row])):
        if self.board[row][i] == num:
          inRow = True

          break
      return not inRow

    def valid_in_col(self, col, num):
      inCol = False
      for i in range(0, len(self.board)):
        if self.board[i][col] == num:
          inCol = True
          break
      return not inCol
        
      

    def valid_in_box(self, row_start, col_start, num):
      row_start = (row_start // 3) * 3
      col_start = (col_start // 3) * 3
      inBox = False
      for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
          if num == self.board[row][col]:
            inBox = True
            break
      return not inBox

    def is_valid(self, row, col, num):
      row_start = (row // 3) * 3
      col_start = (col // 3) * 3
      if self.valid_in_row(row_start, num) is True:
        
        if self.valid_in_col(col, num) is True:
          
          if self.valid_in_box(row_start, col_start, num) is True:
            return True
      return False
      

    def fill_box(self, row_start, col_start):
      numbers = list(range(1, self.row_length + 1))
      random.shuffle(numbers)

      for x in range(row_start, row_start + self.box_length):
          for y in range(col_start, col_start + self.box_length):
              if self.is_valid(x, y, numbers):
                  self.board[x][y] = numbers.pop(0)
              else:
                  continue

    def fill_diagonal(self):
      self.fill_box(6, 6)
      self.fill_box(3, 3)
      self.fill_box(0, 0)
    

    def fill_remaining(self, row, col):
      if (col >= self.row_length and row < self.row_length - 1):
        row += 1
        col = 0
      if row >= self.row_length and col >= self.row_length:
        return True
      if row < self.box_length:
        if col < self.box_length:
            col = self.box_length
      elif row < self.row_length - self.box_length:
        if col == int(row // self.box_length * self.box_length):
            col += self.box_length
      else:
        if col == self.row_length - self.box_length:
            row += 1
            col = 0
            if row >= self.row_length:
                return True

      for num in range(1, self.row_length + 1):
        if self.is_valid(row, col, num):
          self.board[row][col] = num
          if self.fill_remaining(row, col + 1):
            return True
          self.board[row][col] = 0
      return False

    def fill_values(self):
      self.fill_diagonal()
      self.fill_remaining(0, self.box_length)

    def remove_cells(self):
      num_removed = 0
      while num_removed < self.removed_cells:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if self.board[row][col] != 0:
          self.board[row][col] = 0
          num_removed += 1

def generate_sudoku(size, removed):
  sudoku = Sudoku_Generator(size, removed)
  sudoku.fill_values()
  board = sudoku.get_board()
  sudoku.remove_cells()
  board = sudoku.get_board()
  return board




