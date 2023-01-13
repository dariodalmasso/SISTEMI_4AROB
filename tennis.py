import pygame
import sys
import random


pygame.init()
clock = pygame.time.Clock()
#inserisco i suoni

suono_punti = pygame.mixer.Sound('./risorse/audio/goal.wav')
suono_sbaglio = pygame.mixer.Sound('./risorse/audio/sbaglio.wav')

#setto lo schermo
larghezza_schermo = 1280
altezza_schermo = 700
schermo = pygame.display.set_mode((larghezza_schermo, altezza_schermo))
pygame.display.set_caption("Tennis Game")

palla = pygame.Rect(int(larghezza_schermo/2) - 15, int(altezza_schermo/2) - 15, 30, 30)
giocatore = pygame.Rect(larghezza_schermo - 20, int(altezza_schermo/2) - 70, 10, 140)
nemico = pygame.Rect(10, int(altezza_schermo/2) - 70, 10, 140)
#sfondo
sfondo = pygame.image.load('./risorse/immagini/notte.jpg')

#inizio
def inizio():
    global pos_palla_y, pos_palla_x, score_time

    tempo = pygame.time.get_ticks()
    #posiziona la palla al centro
    palla.center = (int(larghezza_schermo / 2), int(altezza_schermo / 2))
    #per il conto alla rovescia
    if tempo - score_time < 700:
        numero_tre = font.render("3", 1, (200, 200, 200))
        schermo.blit(numero_tre, (int(larghezza_schermo / 2) - 10, int(altezza_schermo / 20) + 20))
    if 700 < tempo - score_time < 1400:
        numero_due = font.render("2", 1, (200, 200, 200))
        schermo.blit(numero_due, (int(larghezza_schermo / 2) - 10, int(altezza_schermo / 20) + 20))
    if 1400 < tempo - score_time < 2100:
        numero_uno = font.render("1", 1, (200, 200, 200))
        schermo.blit(numero_uno, (int(larghezza_schermo / 2) - 10, int(altezza_schermo / 20) + 20))
     #prima  e durante conto alla rovescia la palla sta ferma, a seguito si muove in posizione casuale
    if tempo - score_time < 2100:
        pos_palla_y, pos_palla_x = 0, 0
    else:
        pos_palla_y = 15 * random.choice((1, -1))
        pos_palla_x = 15 * random.choice((1, -1))
        score_time = None


pos_palla_x = 15 * random.choice((1, -1))
pos_palla_y = 15 * random.choice((1, -1))
posizione_giocatore = 0
posizione_nemico = 0
#in primis i punti dei giocatori settati a zero
punti_giocatore = 0
punti_nemico = 0
font = pygame.font.SysFont('comicsans', 30, True)

score_time = True

run = True
while True:

    posizione_nemico = random.randint(0, 30)
#i comandi intercettati dalla keyboard
    for gioco in pygame.event.get():
        if gioco.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if gioco.type == pygame.KEYDOWN:
            if gioco.key == pygame.K_DOWN:
                posizione_giocatore += 10
            if gioco.key == pygame.K_UP:
                posizione_giocatore -= 10
        if gioco.type == pygame.KEYUP:
            if gioco.key == pygame.K_DOWN:
                posizione_giocatore -= 10
            if gioco.key == pygame.K_UP:
                posizione_giocatore += 10

    #animazione della palla
    palla.x += pos_palla_x
    palla.y += pos_palla_y
    # se la palla esce fuori 
    if palla.top <= 0 or palla.bottom >= altezza_schermo:
        pos_palla_y = pos_palla_y * -1

    if palla.left <= 0:
        pygame.mixer.Sound.play(suono_punti)
        punti_giocatore += 1
        score_time = pygame.time.get_ticks()

    if palla.right >= larghezza_schermo:
        pygame.mixer.Sound.play(suono_punti)
        punti_nemico += 1
        score_time = pygame.time.get_ticks()

    if palla.colliderect(giocatore) or palla.colliderect(nemico):
        pygame.mixer.Sound.play(suono_sbaglio)
        pos_palla_x *= -1

    # animazioni del giocatore
    giocatore.y += posizione_giocatore
    if giocatore.top <= 0:
        giocatore.top = 0
    if giocatore.bottom >= altezza_schermo:
        giocatore.bottom = altezza_schermo

    #animazione del nemico
    if nemico.top < palla.y:
        nemico.top += posizione_nemico
    if nemico.bottom > palla.y:
        nemico.bottom -= posizione_nemico
    if nemico.top <= 0:
        nemico.top = 0
    if nemico.bottom >= altezza_schermo:
        nemico.bottom = altezza_schermo

        

    schermo.blit(sfondo, (0, 0))
    pygame.draw.rect(schermo, (255, 0, 0), giocatore)
    pygame.draw.rect(schermo, (255, 0, 0), nemico)
    pygame.draw.ellipse(schermo, (255, 255, 255), palla)
    pygame.draw.aaline(schermo, (95, 99, 104), (int(larghezza_schermo/2), 0), (int(larghezza_schermo/2), altezza_schermo))
#inizio del gioco
    if score_time:
        inizio()
#verifico la vittoria e poi faccio comparire la scritta di chi ha vinto
    if punti_giocatore == 10:
        punti_giocatore = 0
        punti_nemico = 0
        vittoria_giocatore = font.render(f"HAI VINTO", 1, (200, 200, 200))
        schermo.blit(vittoria_giocatore, (618, 330))
        pausa = pygame.time.delay(3000)


    elif punti_nemico == 10:
        punti_nemico = 0
        punti_giocatore = 0
        vittoria_nemico = font.render(f"NEMICO  HA VINTO", 1, (200, 200, 200))
        schermo.blit(vittoria_nemico, (618, 330))
        pausa = pygame.time.delay(300)


    testo_giocatore = font.render(f"{punti_giocatore}", 1, (200, 200, 200))
    schermo.blit(testo_giocatore, (650, 10))

    testo_nemico = font.render(f"{punti_nemico}", 1, (200, 200, 200))
    schermo.blit(testo_nemico, (618, 10))

    pygame.display.update()
    clock.tick(60)


