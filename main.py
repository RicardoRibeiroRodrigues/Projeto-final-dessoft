import pygame
from Constantes import WIDTH, HEIGHT, INIT, INSTRUCOES, GAME, QUIT, GAME_2
from game_screen_1 import game_screen, game_screen_2
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
    elif state == INSTRUCOES:
        state = regras(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == GAME_2:
        state = game_screen_2(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados