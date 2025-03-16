# Importerer pygame
import pygame

# Initialiser Pygame
pygame.init()

# Konstanter
BREDDE, HOYDE = 500, 500
RADER, KOLONNER = 10, 10
RUTESTORRELSE = BREDDE // KOLONNER

# Farger
HVIT = (255, 255, 255)
SVART = (0, 0, 0)
ROD = (255, 0, 0)
GRONN = (0, 255, 0)
MULBERRY = (197, 75, 140)


# Opprett vindu
skjerm = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("Stigespill")

# Font
tallFont = pygame.font.Font(None, 24)
tekstFont = pygame.font.Font(None, 19)

# Tegner brettet
def tegnBrett(): 
    skjerm.fill(HVIT)
    
    # Tegn rutenett og nummer
    for rad in range(RADER):
        for kol in range(KOLONNER):
            rect = pygame.Rect(kol * RUTESTORRELSE, rad * RUTESTORRELSE, RUTESTORRELSE, RUTESTORRELSE)
            pygame.draw.rect(skjerm, SVART, rect, 1)

            # Rutenummer 
            # render er en funksjon som lager en tekst
            # blit er en funksjon som tegner teksten på skjermen
            rutenummer = (RADER - 1 - rad) * KOLONNER + (kol + 1)
            tekst = tallFont.render(str(rutenummer), True, SVART)
            skjerm.blit(tekst, (kol * RUTESTORRELSE + 5, rad * RUTESTORRELSE + 5))

    # Markér start (rute 1) og mål (rute 100)
    pygame.draw.rect(skjerm, MULBERRY, (0, (RADER-1) * RUTESTORRELSE, RUTESTORRELSE, RUTESTORRELSE))
    pygame.draw.rect(skjerm, MULBERRY, ((KOLONNER-1) * RUTESTORRELSE, 0, RUTESTORRELSE, RUTESTORRELSE))

    # Skriv "START" og "SLUTT"
    startTekst = tekstFont.render("START", True, SVART) 
    skjerm.blit(startTekst, (5, (RADER-1) * RUTESTORRELSE + 20))

    sluttTekst = tekstFont.render("SLUTT", True, SVART)
    skjerm.blit(sluttTekst, ((KOLONNER-1) * RUTESTORRELSE + 5, 20))

    # Tegn stiger (grønne linjer)
    pygame.draw.line(skjerm, GRONN, (50, 400), (150, 300), 5)   
    pygame.draw.line(skjerm, GRONN, (350, 250), (450, 150), 5)  
    pygame.draw.line(skjerm, GRONN, (100, 300), (200, 150), 5)  

    # Tegn slanger (røde linjer)
    pygame.draw.line(skjerm, ROD, (300, 100), (200, 200), 5)   
    pygame.draw.line(skjerm, ROD, (400, 400), (300, 300), 5)   
    pygame.draw.line(skjerm, ROD, (150, 50), (50, 300), 5)     
    pygame.draw.line(skjerm, ROD, (400, 50), (100, 450), 5)     

# Hovedløkke
kjører = True
while kjører:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kjører = False

    tegnBrett()

pygame.quit() 