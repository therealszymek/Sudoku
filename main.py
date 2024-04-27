from pygame import draw
from SudokuGenerator import Sudoku_Generator
"""from Board import Board"""
import pygame
import sys
from Button import Button

def main():
  pygame.init()
  screen = pygame.display.set_mode((540, 540))
  running = True
  
  WHITE = (255, 255, 255)
  GRAY = (200, 200, 200)
  BLUE = (100, 100, 255)
  BLACK = (0, 0, 0)
  width = 540
  height = 540
  CELL_SIZE = 60
  GRID_SIZE = 9
  GRID_WIDTH = width - 2
  GRID_HEIGHT = height - 60
  BLACK = (0, 0, 0)
  in_menu = True
  game_mode = 0
     
  
  
  while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    start_title_font = pygame.font.Font(None, 75)
    difficulty_font = pygame.font.Font(None, 55)
    button_font = pygame.font.Font(None, 50)
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
      screen.fill(WHITE)
      cell_font = pygame.font.Font(None, 30)
      square_size = width // 9

      for i in range(1, 9):
          line_width = 1
          if i % 3 == 0:
              line_width = 2
          pygame.draw.line(screen, (0, 0, 0), (0, i * square_size), (width, i * square_size), line_width)
          pygame.draw.line(screen, (0, 0, 0), (i * square_size, 0), (i * square_size, height), line_width)
  
    if in_menu:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if easy_rectangle.collidepoint(event.pos):
            start_game()
            game_mode = 30
            in_menu = False
          elif medium_rectangle.collidepoint(event.pos):
            start_game()
            game_mode = 40
            in_menu = False
          elif hard_rectangle.collidepoint(event.pos):
            start_game()
            game_mode = 50
            in_menu = False
      pygame.display.update()

if __name__ == "__main__":
  main()