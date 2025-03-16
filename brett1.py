import pygame

# Initialiser pygame
pygame.init()

# Definer skjermstørrelse
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10  # 10x10 brett
CELL_SIZE = WIDTH // COLS

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Opprett skjerm
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stigespill")

# Tegn brettet
def draw_board():
    screen.fill(WHITE)
    
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)
    
    # Stiger (start_x, start_y, end_x, end_y)
    ladders = [((1, 8), (3, 6)), ((2, 5), (4, 2)), ((6, 9), (8, 7))]
    
    for start, end in ladders:
        start_x = start[0] * CELL_SIZE + CELL_SIZE // 2
        start_y = start[1] * CELL_SIZE + CELL_SIZE // 2
        end_x = end[0] * CELL_SIZE + CELL_SIZE // 2
        end_y = end[1] * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.line(screen, GREEN, (start_x, start_y), (end_x, end_y), 5)

    # Slanger (hvis ønskelig)
    snakes = [((8, 1), (6, 4)), ((7, 6), (5, 9))]
    
    for start, end in snakes:
        start_x = start[0] * CELL_SIZE + CELL_SIZE // 2
        start_y = start[1] * CELL_SIZE + CELL_SIZE // 2
        end_x = end[0] * CELL_SIZE + CELL_SIZE // 2
        end_y = end[1] * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), 5)

# Spill-løkke
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board()
    pygame.display.flip()

pygame.quit()
