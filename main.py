import pygame
from Constantes import *
from game_screen import game_screen
from init_screen import tela_inicial
from instrucoes import regras

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo')

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_inicial(window)
    if state == INSTRUCOES:
        state = regras(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados