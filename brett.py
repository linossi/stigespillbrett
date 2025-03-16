# Importerer pygame
import pygame

# Initialiser pygame
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

# Opprett vindu og sett tittel
skjerm = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("Stigespill")

# Fonter for tall og tekst
tallFont = pygame.font.Font(None, 24)
tekstFont = pygame.font.Font(None, 19)

# Tegner brettet
def tegnBrett(): 
    skjerm.fill(HVIT) 
    
    # Tegn rutenett og nummer
    for rad in range(RADER):
        for kol in range(KOLONNER):
            rect = pygame.Rect(kol * RUTESTORRELSE, rad * RUTESTORRELSE, RUTESTORRELSE, RUTESTORRELSE) # Rect lager en rektangel
            pygame.draw.rect(skjerm, SVART, rect, 1) # Tegner rektangel

            # Rutenummer 
            rutenummer = (RADER - 1 - rad) * KOLONNER + (kol + 1) # Formel for å regne ut rutenummer
            tekst = tallFont.render(str(rutenummer), True, SVART) # Lager tekst
            skjerm.blit(tekst, (kol * RUTESTORRELSE + 5, rad * RUTESTORRELSE + 5)) # Tegner tekst

    # Markér start (rute 1) og mål (rute 100)
    pygame.draw.rect(skjerm, MULBERRY, (0, (RADER-1) * RUTESTORRELSE, RUTESTORRELSE, RUTESTORRELSE)) # Tegner rektangel
    pygame.draw.rect(skjerm, MULBERRY, ((KOLONNER-1) * RUTESTORRELSE, 0, RUTESTORRELSE, RUTESTORRELSE)) # Tegner rektangel

    # Skriv "START" og "SLUTT"
    startTekst = tekstFont.render("START", True, SVART) # Lager tekst
    skjerm.blit(startTekst, (5, (RADER-1) * RUTESTORRELSE + 20)) # Tegner tekst

    sluttTekst = tekstFont.render("SLUTT", True, SVART) # Lager tekst
    skjerm.blit(sluttTekst, ((KOLONNER-1) * RUTESTORRELSE + 5, 20)) # Tegner tekst

    # Tegn stiger (grønne linjer)
    pygame.draw.line(skjerm, GRONN, (50, 400), (150, 300), 5)   
    pygame.draw.line(skjerm, GRONN, (350, 250), (450, 150), 5)  
    pygame.draw.line(skjerm, GRONN, (100, 300), (200, 150), 5)  

    # Tegn slanger (røde linjer)
    pygame.draw.line(skjerm, ROD, (300, 100), (200, 200), 5)   
    pygame.draw.line(skjerm, ROD, (400, 400), (300, 300), 5)   
    pygame.draw.line(skjerm, ROD, (150, 50), (50, 300), 5)     
    pygame.draw.line(skjerm, ROD, (400, 50), (100, 450), 5)     

# Hovedløkke som kjører til programmet lukkes
kjører = True
while kjører:
    # Sjekker etter eventer, som musetrykk eller tastetrykk
    for event in pygame.event.get(): 
        # Hvis programvinduet lukkes, avsluttes løkken
        if event.type == pygame.QUIT:
            kjører = False

     # Tegner spillebrettet
    tegnBrett()

    # Oppdaterer skjermen for å vise endringer
    pygame.display.flip()

# Når løkken er ferdig, avsluttes pygame
pygame.quit() 