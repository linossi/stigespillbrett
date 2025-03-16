import pygame

# Initialiser Pygame
pygame.init()

# Konstanter
BREDDE, HØYDE = 500, 500
RADER, KOLONNER = 10, 10
RUTE_STØRRELSE = BREDDE // KOLONNER

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
RØD = (255, 0, 0)
GRØNN = (0, 255, 0)

# Opprett vindu
skjerm = pygame.display.set_mode((BREDDE, HØYDE))
pygame.display.set_caption("Stigespill")

def tegn_brett():
    skjerm.fill(HVIT)
    
    # Tegn rutenett
    for rad in range(RADER):
        for kol in range(KOLONNER):
            rect = pygame.Rect(kol * RUTE_STØRRELSE, rad * RUTE_STØRRELSE, RUTE_STØRRELSE, RUTE_STØRRELSE)
            pygame.draw.rect(skjerm, SVART, rect, 1)
    
    # Tegn en stige (som en grønn linje)
    pygame.draw.line(skjerm, GRØNN, (50, 400), (150, 300), 5)
    
    # Tegn en slange (som en rød linje)
    pygame.draw.line(skjerm, RØD, (300, 100), (200, 200), 5)

# Hovedløkke
kjører = True
while kjører:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kjører = False

    tegn_brett()
    pygame.display.flip()

pygame.quit()
