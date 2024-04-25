import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.font = pygame.font.SysFont('comicsans', 40)

    def set_cell_value(self, value):
        self.value = value

    def draw(self):
        cell_size = 60
        x = self.col * cell_size
        y = self.row * cell_size

        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, cell_size, cell_size))
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)
        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 10))
