import pygame
from board import Board

def game_start_screen(screen):
    screen.fill((255, 255, 255))  # Fill screen with white color

    # Draw buttons for difficulty levels
    font = pygame.font.SysFont('comicsans', 40)
    easy_button = pygame.Rect(150, 200, 200, 50)
    medium_button = pygame.Rect(150, 300, 200, 50)
    hard_button = pygame.Rect(150, 400, 200, 50)

    pygame.draw.rect(screen, (0, 255, 0), easy_button)
    pygame.draw.rect(screen, (0, 255, 0), medium_button)
    pygame.draw.rect(screen, (0, 255, 0), hard_button)

    text = font.render("Easy", True, (0, 0, 0))
    screen.blit(text, (210, 210))
    text = font.render("Medium", True, (0, 0, 0))
    screen.blit(text, (185, 310))
    text = font.render("Hard", True, (0, 0, 0))
    screen.blit(text, (210, 410))

    pygame.display.update()

def game_over_screen(screen):
    screen.fill((255, 255, 255))  # Fill screen with white color

    # Display game over message
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(text, (150, 250))

    pygame.display.update()

def game_in_progress_screen(screen, board):
    screen.fill((255, 255, 255))  # Fill screen with white color

    # Draw Sudoku board
    board.draw()

    pygame.display.update()

def main():
    pygame.init()
    width = 540
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")

    running = True
    current_screen = "start"  # Initial screen is the game start screen

    # Create a Sudoku board
    board = Board(width, height, screen, "easy")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_screen == "start":
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if 150 <= mouse_pos[0] <= 350:
                            if 200 <= mouse_pos[1] <= 250:
                                current_screen = "game"
                                board = Board(width, height, screen, "easy")
                            elif 300 <= mouse_pos[1] <= 350:
                                current_screen = "game"
                                board = Board(width, height, screen, "medium")
                            elif 400 <= mouse_pos[1] <= 450:
                                current_screen = "game"
                                board = Board(width, height, screen, "hard")
                elif current_screen == "game":
                    # Handle mouse click on the Sudoku board
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_cell = board.click(mouse_pos[0], mouse_pos[1])
                    if clicked_cell:
                        row, col = clicked_cell
                        board.select(row, col)
                elif current_screen == "game_over":
                    if event.button == 1:
                        current_screen = "start"
            elif event.type == pygame.KEYDOWN:
                if current_screen == "game":
                    # Handle number input for selected cell
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        value = int(pygame.key.name(event.key))
                        board.place_number(value)
                    elif event.key == pygame.K_RETURN:
                        # Submit guess for selected cell
                        pass

        if current_screen == "start":
            game_start_screen(screen)
        elif current_screen == "game":
            game_in_progress_screen(screen, board)
            if board.is_full() and board.check_board():
                current_screen = "game_over"
        elif current_screen == "game_over":
            game_over_screen(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
