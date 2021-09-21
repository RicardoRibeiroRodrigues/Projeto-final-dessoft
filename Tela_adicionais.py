import pygame
from Constantes import *
from game_screen_1 import renderiza_texto, carrega_background
pygame.init()

def tela_das_hist(janela, assets):
    """Função para a história do jogo, returna ao final o estado para GAME"""
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Carrega o background inicial
    BACKGROUND, BACKGROUND_RECT = carrega_background("INTRO_HIST", assets)
    #Fonte para escrita na tela
    texto_passar_diag = renderiza_texto("Para passar o dialogo aperte p (uma vez)", RED, 32)
    texto_pular_tela = renderiza_texto("Para pular a historia, aperte ESC", RED, 32)
    #Contador para as telas
    i = 0
    #loop da tela
    state = PLAYING
    while state != QUIT:
        #Limita o FPS
        clock.tick(FPS)
        #Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    #Passa de tela
                    i += 1
                if event.key == pygame.K_ESCAPE:
                    return GAME
        #primeira tela
        if i == 1:
            BACKGROUND, BACKGROUND_RECT = carrega_background("PRIMEIRA_HIST", assets)
        #segunda tela
        elif i == 2:
            BACKGROUND, BACKGROUND_RECT = carrega_background("SEGUNDA_HIST", assets)
        #Terceira tela
        elif i == 3:
            BACKGROUND, BACKGROUND_RECT = carrega_background("TERCEIRA_HIST", assets)
        #Quarta tela
        elif i == 4:
            BACKGROUND, BACKGROUND_RECT = carrega_background("QUARTA_HIST", assets)
        #Quinta tela
        elif i == 5:
            BACKGROUND, BACKGROUND_RECT = carrega_background("QUINTA_HIST", assets)
        #Sexta tela
        elif i == 6:
            BACKGROUND, BACKGROUND_RECT = carrega_background("SEXTA_HIST", assets)
        #Ultima tela
        elif i == 7:
            BACKGROUND, BACKGROUND_RECT = carrega_background("SETIMA_HIST", assets)
        #Vai para o jogo
        elif i == 8:
            return GAME
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND, BACKGROUND_RECT)
        #Pega o tempo
        now = pygame.time.get_ticks()
        #Tira as instruções da tela
        if now < 7000:
            janela.blit(texto_passar_diag, (400,0))
            janela.blit(texto_pular_tela,(400, 50))
        pygame.display.flip()
    return state

def tela_final(janela, assets):
    """Função para a tela final do jogo"""
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Carrega o background inicial
    BACKGROUND, BACKGROUND_RECT = carrega_background("FINAL_1", assets)
    #Fonte para escrita na tela
    texto_passar_diag = renderiza_texto("Para passar o dialogo aperte p (uma vez)", RED, 32)
    texto_pular_tela = renderiza_texto("Para sair, aperte ESC", RED, 32)
    #Tempo que começa
    começo = pygame.time.get_ticks()
    #Limpa os grupos da tela passada.
    all_plataforms.empty()
    all_players.empty()
    all_sprites.empty()
    #Contador para as telas
    i = 0
    #loop da tela
    state = PLAYING
    while state != QUIT:
        #Limita o FPS
        clock.tick(FPS)
        #Processa os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    #Passa de tela
                    i += 1
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
        #primeira tela
        if i == 1:
            BACKGROUND, BACKGROUND_RECT = carrega_background("FINAL_2", assets)
        #Tela final
        elif i == 2:
            BACKGROUND, BACKGROUND_RECT = carrega_background("TELA_FINAL", assets)
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND, BACKGROUND_RECT)
        #Pega o tempo
        now = pygame.time.get_ticks()
        #Tira as instruções da tela
        if (now - começo) < 7000: 
            janela.blit(texto_passar_diag, (400,0))
            janela.blit(texto_pular_tela, (400, 50))
        pygame.display.flip()
    return state
