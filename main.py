from pygame import draw
from SudokuGenerator import Sudoku_Generator
from SudokuGenerator import generate_sudoku
from Board import Board
import pygame
import sys

def __main__():
  pygame.init()
  running = True
  WHITE = (255, 255, 255)
  GRAY = (200, 200, 200)
  BLUE = (100, 100, 255)
  BLACK = (0, 0, 0)
  width = 450
  height = 600
  CELL_SIZE = 50
  GRID_SIZE = 9
  GRID_WIDTH = width - 2
  GRID_HEIGHT = height - 60
  BLACK = (0, 0, 0)
  in_menu = True
  screen = pygame.display.set_mode((width, height))
  

  game_on = True
  selected_cell = None



  while running:

    start_title_font = pygame.font.Font(None, 75)
    difficulty_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 50)
    cell_font = pygame.font.Font(None, 30)
    screen.fill(WHITE)

    title_surface = start_title_font.render("Sudoku", 0 , BLACK)
    title_rectangle = title_surface.get_rect(center=(width // 2, height // 2 - 200))
    screen.blit(title_surface, title_rectangle)
    difficulty_surface = difficulty_font.render("Select Your Difficulty:", 0 , BLACK)
    difficulty_rectangle = difficulty_surface.get_rect(center=(width // 2, height // 2 - 135))
    screen.blit(difficulty_surface, difficulty_rectangle)
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] +20))
    easy_surface.fill(BLUE)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] +20))
    medium_surface.fill(BLUE)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] +20))
    hard_surface.fill(BLUE)
    hard_surface.blit(hard_text, (10, 10))


    easy_rectangle = easy_surface.get_rect(center=(width//2, height//2 - 75))
    medium_rectangle = medium_surface.get_rect(center=(width//2, height//2))
    hard_rectangle = hard_surface.get_rect(center=(width//2, height//2 + 75))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)




    def start_game():
      game_board = Board(9, 9, screen, difficulty=None, sudoku_board=sudoku_board)
      game_on = True
      screen.fill(WHITE)
      while game_on:
        screen.fill((255, 255, 255))
        game_board.draw()
        
#restart button
        
        restart_text = button_font.render("Restart", 0, (255, 255, 255))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] +20))
        restart_surface.fill(BLUE)
        restart_surface.blit(restart_text, (10, 10))
        restart_rectangle = restart_surface.get_rect(center=(width//2, height//2 + 200))

        screen.blit(restart_surface, restart_rectangle)

#reset button
        
        reset_text = button_font.render("Reset", 0, (255, 255, 255))
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] +20))
        reset_surface.fill(BLUE)
        reset_surface.blit(reset_text, (10, 10))
        reset_rectangle = reset_surface.get_rect(center=(width//2 - 150, height//2 + 200))

        screen.blit(reset_surface, reset_rectangle)

#exit button

        exit_text = button_font.render("Exit", 0, (255, 255, 255))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] +20))
        exit_surface.fill(BLUE)
        exit_surface.blit(exit_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(center=(width//2 + 150, height//2 + 200))

        screen.blit(exit_surface, exit_rectangle)


  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
              # Get the mouse position
              mouse_x, mouse_y = pygame.mouse.get_pos()
              # Calculate the cell coordinates
              row = mouse_y // (game_board.GRID_HEIGHT // 9)
              # Calculate row index
              col = mouse_x // (game_board.GRID_WIDTH // 9)   # Calculate column index
              # Select the cell
              
              selected_cell = game_board.select(row, col)
              if restart_rectangle.collidepoint(event.pos):
                pass
              if reset_rectangle.collidepoint(event.pos):
                game_board.draw()
              if exit_rectangle.collidepoint(event.pos):
                sys.exit()
                
  
            elif event.type == pygame.KEYDOWN:
              if selected_cell and pygame.K_0 <= event.key <= pygame.K_9:
                if selected_cell.value == 0:
                  value = int(pygame.key.name(event.key))
                  selected_cell.set_cell_value(value)
                  sudoku_board[col][row] = selected_cell.set_cell_value(value)
  
  
        pygame.display.flip()



    if in_menu:
      game_mode = 0
      in_lose = False
      in_win = False

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if easy_rectangle.collidepoint(event.pos):
            game_on = True
            game_mode = 30
            sudoku_board = generate_sudoku(9, game_mode)
            game_board = Board(9, 9, screen, difficulty=None, sudoku_board=sudoku_board)
            start_game()
            in_menu = False
          elif medium_rectangle.collidepoint(event.pos):
            game_on = True
            game_mode = 40
            sudoku_board = generate_sudoku(9, game_mode)
            game_board = Board(9, 9, screen, difficulty=None, sudoku_board=sudoku_board)
            start_game()
            in_menu = False
          elif hard_rectangle.collidepoint(event.pos):
            game_on = True
            game_mode = 50
            sudoku_board = generate_sudoku(9, game_mode)
            game_board = Board(9, 9, screen, difficulty=None, sudoku_board=sudoku_board)
            start_game()
            in_menu = False

        '''
        if Board.is_full(game_board) is True:
          if Board.check_board(game_board) is True:
            game_on = False
            in_win = True
            '''
          
          
          
      pygame.display.flip()

if __name__ == "__main__":
  __main__()