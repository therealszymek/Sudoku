import pygame
import sys
from Cell import Cell
from main import main
from SudokuGenerator import Sudoku_Generator, generate_sudoku


class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = 30
    self.mode = ''
      
    self.board = [[0 for i in range(9)] for i in range(9)]
    sq_size = self.width // 9
    self.selected_row = 0
    self.selected_col = 0
    self.sudoku = Sudoku_Generator(9, self.difficulty)
    self.ans_board_temp = self.sudoku.create_ans()
    self.ans_board = [[0 for i in range(9)] for i in range(9)]
    
    for i in range(0, len(self.ans_board_temp)):
        for j in range(0, len(self.ans_board_temp[i])):
            self.ans_board[i][j] = self.ans_board_temp[i][j]
    temporary_brd = self.sudoku.create_board(self.difficulty)
    self.board = [[0 for i in range(9)] for i in range(9)]
        for i in range(0, len(temporary_brd)):
          for j in range(0, len(temporary_brd[i])):
            if temporary_brd[i][j] == 0:
              self.board[i][j] = Cell(0, i, j, self.screen)
            else:
              self.board[i][j] = temporary_brd[i][j]

  
  def draw(self):
      cell_font = pygame.font.Font(None, 30)
      square_size = self.width // 9

      for i in range(1, 9):
          line_width = 1
          if i % 3 == 0:
              line_width = 2
          pygame.draw.line(self.screen, (0, 0, 0), (0, i * square_size), (self.width, i * square_size), line_width)
          pygame.draw.line(self.screen, (0, 0, 0), (i * square_size, 0), (i * square_size, self.height), line_width)

      for j in range(9):
          for k in range(9):
              if isinstance(self.board[j][k], Cell):
                  self.board[j][k].draw()
              else:
                  cell_surf = cell_font.render(str(self.board[j][k]), True, (0, 0, 0))
                  rect = pygame.Rect(j * square_size, k * square_size, square_size, square_size)
                  cell_rect = cell_surf.get_rect(center=rect.center)
                  self.screen.blit(cell_surf, cell_rect)


  
  def select(self, row, col):
    red = (255, 0, 0)
    square_size = (self.width // 9, self.height // 9)
    line_width = 3
    self.screen.fill((128, 170, 255))
    self.draw()
    self.selected_row = row - 1
    self.selected_col = col - 1
    rect = pygame.Rect((row - 1) * square_size[0], (col - 1) * square_size[1], square_size[0], square_size[1])
    pygame.draw.rect(self.screen, red, rect, line_width)
    
  def click(self, x, y):
    pass
    
  def clear(self):
    self.board[self.selected_row][self.selected_col].set_cell_value(0)

  def sketch(self, value):
    self.board[self.selected_row][self.selected_col].set_sketched_value(value)

  def place_number(self, value):
    self.board[self.selected_row][self.selected_col].set_cell_value(value)

  def reset_to_original(self):
    self.selected_row = 0
    self.selected_col = 0
    for i in range(0, len(self.board)):
        for j in range(0, len(self.board[i])):
            if type(self.board[i][j]) == Cell:
                self.board[i][j].set_cell_value(0)
                self.board[i][j].set_sketched_value(0)

  def is_full(self):
    for i in range(9):
        for j in range(9):
            if type(self.board[i][j]) == Cell and self.board[i][j].value == 0:
                return False
    return True

  def update_board(self):
    pass

  def find_empty(self):
    for i in range(9):
        for j in range(9):
            if type(self.board[i][j]) == Cell and self.board[i][j].value == 0:
                return i, j
    return None

  def check_board(self):
    win = False
    for i in range(9):
        for j in range(9):
            if type(self.board[i][j]) == Cell:
                if int(self.board[i][j].value) == self.ans_board[i][j]:
                    win = True
                elif int(self.board[i][j].value) != self.ans_board[i][j]:
                    return False
    return win