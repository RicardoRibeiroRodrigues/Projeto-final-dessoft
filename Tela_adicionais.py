import pygame
from Constantes import *
pygame.init()

def tela_das_hist(janela, assets):
    """Função para a história do jogo, returna ao final o estado para GAME"""
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Carrega o background inicial
    BACKGROUND = assets["INTRO_HIST"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    #Fonte para escrita na tela
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    texto_passar_diag = fonte.render("Para passar o dialogo aperte p (uma vez)", True, RED)
    texto_pular_tela = fonte.render("Para pular a historia, aperte ESC", True, RED)
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
            BACKGROUND = assets["PRIMEIRA_HIST"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #segunda tela
        elif i == 2:
            BACKGROUND = assets["SEGUNDA_HIST"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #Terceira tela
        elif i == 3:
            BACKGROUND = assets["TERCEIRA_HIST"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #Quarta tela
        elif i == 4:
            BACKGROUND = assets["QUARTA_HIST"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #Quinta tela
        elif i == 5:
            BACKGROUND = assets["QUINTA_HIST"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #Sexta tela
        elif i == 6:
            BACKGROUND = assets["SEXTA_HIST"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #Ultima tela
        elif i == 7:
            BACKGROUND = assets["SETIMA_HIST"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
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
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Carrega o background inicial
    BACKGROUND = assets["FINAL_1"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    #Fonte para escrita na tela
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    texto_passar_diag = fonte.render("Para passar o dialogo aperte p (uma vez)", True, RED)
    texto_pular_tela = fonte.render("Para sair, aperte ESC", True, RED)
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
            BACKGROUND = assets["FINAL_2"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #Tela final
        elif i == 2:
            BACKGROUND = assets["TELA_FINAL"]
            BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
            BACKGROUND_RECT = BACKGROUND.get_rect()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND, BACKGROUND_RECT)
        #Pega o tempo
        now = pygame.time.get_ticks()
        #Tira as instruções da tela
        if (now - começo) < 7000: 
            janela.blit(texto_passar_diag, (400,0))
            janela.blit(texto_pular_tela,(400, 50))
        pygame.display.flip()
    return state
