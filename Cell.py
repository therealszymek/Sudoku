import pygame

class Cell:

  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen
    self.selected = False
    self.sketched_value = 0

  def set_cell_value(self, value):
    self.value = value
    return value

  def set_sketched_value(self, value):
    self.sketched_value = value
    return value

  def draw(self):
    if self.sketched_value == 0:
      sketched_value = ''
    if self.value == 0:
      value = ''
    if self.sketched_value != 0:
      sketched_value = str(self.sketched_value)
    if self.value != 0:
      value = str(self.value)
    square_size = 50  # sets size of square
    cell_font = pygame.font.Font(None, 30)
    sketch_font = pygame.font.Font(None, 30)
    sketch_rect = pygame.Rect((self.row * square_size) + 5, (self.col * square_size) + 5, square_size + 5,
                     square_size + 5)
    value_temp = pygame.Rect((self.row * square_size), (self.col * square_size), square_size,
                      square_size)
    # creates a rectangle object with arguments (row,col,
    # square_size,square_size) to draw the cell
    sketch_surf = sketch_font.render(sketched_value, True, (122, 122, 122))
    value_surf = cell_font.render(value, True, (0, 0, 0))  # draws value with
    # arguments for value, True and color
    value_rect = value_surf.get_rect(center=value_temp.center)  # defines rectangle center
    self.screen.blit(sketch_surf, sketch_rect)
    self.screen.blit(value_surf, value_rect)  # uses .blit function to add image to screen
