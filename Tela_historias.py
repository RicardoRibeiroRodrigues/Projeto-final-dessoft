import pygame
pygame.init()
from Constantes import *
from game_screen_1 import load_assets
def tela_das_hist(janela):
    #carrega os assets
    assets = load_assets()
    BACKGROUND = assets["HIMALAIA_IMG"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    #loop da tela
    state = PLAYING
    while state != QUIT:
        #Limita o FPS
        
        clock.tick(FPS)
        pass