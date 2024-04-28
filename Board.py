import pygame
from Cell import Cell
from SudokuGenerator import Sudoku_Generator


class Board:
  def __init__(self, width, height, screen, difficulty, sudoku_board):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

    # Constants:
    self.COLOR = (0, 0, 0)
    self.CELL_SIZE = 50
    self.GRID_WIDTH = 450
    self.GRID_HEIGHT = 450
    self.sudoku_board = sudoku_board
    self.original_board = sudoku_board
    
    # Array of Cells
    self.cells = []
    for row in range(9):
        cell_row = []
        for col in range(9):
            cell = Cell(value=sudoku_board[row][col], row=row, col=col, screen=self.screen)
            cell_row.append(cell)
        self.cells.append(cell_row)


  def draw(self):

    for index in range(10):
      if index % 3 == 0:
          pygame.draw.line(self.screen, self.COLOR, (0, index * self.CELL_SIZE), (self.GRID_WIDTH, index * self.CELL_SIZE), 4)
          pygame.draw.line(self.screen, self.COLOR, (index * self.CELL_SIZE, 0), (index * self.CELL_SIZE, self.GRID_HEIGHT), 4)
      else:
          pygame.draw.line(self.screen, self.COLOR, (0, index * self.CELL_SIZE), (self.GRID_WIDTH, index * self.CELL_SIZE), 2)
          pygame.draw.line(self.screen, self.COLOR, (index * self.CELL_SIZE, 0), (index * self.CELL_SIZE, self.GRID_HEIGHT), 2)

    for row in range(9):
      for col in range(9):
          cell = self.cells[col][row]
          cell.draw()
          if cell.selected:
              pygame.draw.rect(self.screen, (255, 0, 0), (col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE), 3)


  def select(self, row, col):

    for cell_row in self.cells:
        for cell in cell_row:
            cell.selected = False
#gets stuck here
    selected_cell = self.cells[col][row]
    selected_cell.selected = True

    return selected_cell


  def reset_to_original(self):
    for row in range(9):
        for col in range(9):
            original_value = self.original_board[row][col]
            self.cells[row][col].set_cell_value(original_value)


def click(self, x, y):
  row = y // self.CELL_SIZE
  col = x // self.CELL_SIZE
  if 0 <= row <= 9 and 0 <= col <= 9:
      return (row, col)
  else:
      return None

def clear(self):
  selected_cell = self.find_selected_cell()
  if selected_cell.value == 0:
      return
  else:
      selected_cell.set_cell_value(0)
      selected_cell.set_sketched_value(0)

def sketch(self, value):
  selected_cell = self.find_selected_cell()
  selected_cell.set_sketched_value(value)

def place_number(self, value):
  selected_cell = self.find_selected_cell()
  selected_cell.set_cell_value(value)


def is_full(self):
  for row in range(9):
      for col in range(9):
          if self.cells[row][col].value == 0:
              return False
  return True

def update_board(self):
  for row in range(9):
      for col in range(9):
          self.board[row][col] = self.cells[row][col].value

def find_empty(self):
  for row in range(9):
      for col in range(9):
          if self.cells[row][col].value == 0:
              return (row, col)
  return None

def check_board(self):
  for row in range(9):
      for col in range(9):
          if self.cells[row][col].value == 0:
              return False
          if not self.is_valid(row, col, self.cells[row][col].value):
              return False
  return True

def find_selected_cell(self):
  for row in range(9):
      for col in range(9):
          if self.cells[row][col].selected:
            if self.cells[row].value >= 9:
              return None
            else:
              return self.cells[row][col]

#def generate_answer()


