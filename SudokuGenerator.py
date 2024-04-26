import math
import random

class Sudoku_Generator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length] * row_length
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
      return self.board

    def print_board(self):
      for row in self.board:
        print(row)

    def valid_in_row(self, row, num):
      inRow = False
      for row in self.board:
        if num in row:
          inRow = True
          break
      return not inRow

    def valid_in_col(self, col, num):
      inCol = False
      for col in self.board:
        if num in col:
          inCol = True
          break
        return not inCol

    def valid_in_box(self, row_start, col_start, num):
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
      if self.valid_in_row(row_start, num) and self.valid_in_col(col, num) and self.valid_in_box(row_start, col_start, num):
        return True
      else:
        return False

    def fill_box(self, row_start, col_start):
      
      
      
    