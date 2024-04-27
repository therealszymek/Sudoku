import pygame
import random

pygame.init()
height = 730
width = 630
rect_height = 50
rect_width = 125
rect_x = 100
rect_y = 425
original_pos = pygame.Rect((height + 100, width + 100, 1, 1))
ending_rect = original_pos
rect_easy = original_pos
rect_medium = original_pos
rect_hard = original_pos
restarting_rect = original_pos
finished = False
in_main_menu = True
game_over_loose = False
game_over_win = False
screen = pygame.display.set_mode((width, height), flags=pygame.SCALED)
pygame.display.set_caption('Sudoku')
text_f = pygame.font.Font(None, 70)
option_font = pygame.font.Font(None, 35)
icon = pygame.image.load(
    'image.png').convert()
screen.blit(icon, (0, 0))
board = None
random.seed(random.randint(0, 100000000))

def write_text(text, pos, color='Grey', text_font=text_f):
  text_surf = text_font.render(text, 0, color)
  text_rect = text_surf.get_rect(center=pos)
  screen.blit(text_surf, text_rect)

def draw_rect(pos, color='Grey', width=0):
  pygame.draw.rect(screen, color, pos, width)

  return pygame.Rect(pos)


def display_main_menu():
  draw_rect((50, (height // 2 - 225), 540, 50), 'black')
  draw_rect((50, (height // 2 - 125), 540, 50), 'black')
  write_text('Welcome To Sudoku', (width // 2, height // 2 - 200))
  write_text('Select Game Mode', (width // 2, height // 2 - 100))
  rect_easy = draw_rect((rect_x, rect_y + 50, rect_width, rect_height))
  rect_medium = draw_rect((rect_x + 150, rect_y + 50, rect_width, rect_height))
  rect_hard = draw_rect((rect_x + 300, rect_y + 50, rect_width, rect_height))
  write_text('Easy', (rect_x + 60, rect_y + 75), 'Black', text_font=option_font)
  write_text('Medium', (rect_x + 210, rect_y + 75), 'Black', text_font=option_font)
  write_text('Hard', (rect_x + 360, rect_y + 75), 'Black', text_font=option_font)
  return rect_easy, rect_medium, rect_hard
  


