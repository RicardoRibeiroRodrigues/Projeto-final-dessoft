import pygame
from Constantes import *
from game_screen_1 import carrega_musica, carrega_background
pygame.init()

def tela_inicial(window, assets):                                                   #funcão do menu
    """Funcao para gerar a tela inicial, retorna o próximo estado."""
    font=pygame.font.Font('freesansbold.ttf', 32)                           #funto dos textos dentro da tela
    clock = pygame.time.Clock()
    carrega_musica('assets/Sounds/Musica_loop.mp3')
    BACKGROUND, BACKGROUND_RECT = carrega_background("TELA_INICIAL", assets)
    while True:                                                             # loop principal do menu
        window.fill(BLACK)                                                  
        window.blit(BACKGROUND, BACKGROUND_RECT)                            # Coloca a imagem de fundo                         
        texto_jogar=font.render('JOGAR', True, GREEN, (0, 0, 0))            # cria o texto_jogar
        textoRect_jogar = texto_jogar.get_rect()                            # pega a hit-box do texto_jogar
        textoRect_jogar.center = (100, HEIGHT-100)                          # posiciona o texto_jogar
        texto_instrucoes=font.render('INSTRUÇÕES', True, GREEN, (0, 0, 0))  # cria o texto_instrucoes
        textoRect_instrucoes=texto_instrucoes.get_rect()                    # pega a hitbox do texto_instrcoes
        textoRect_instrucoes.center = (WIDTH-150, HEIGHT-100)               # posiciona o texto_instrucoes
        window.blit(texto_jogar, textoRect_jogar)                           # escreve o texto_jogar
        window.blit(texto_instrucoes, textoRect_instrucoes)                 # escreve o texto_instrucoes
        for event in pygame.event.get():                                    # verifica os eventos do pygame
            if event.type == pygame.QUIT:                                   # verifica se o jogador fechou o jogo
                pygame.quit()                                               # fecha o pygame
            if event.type == pygame.MOUSEBUTTONUP:                          # verifica se o jogador apertou e soltou o botao do mouse
                mouse = pygame.mouse.get_pos()                              # verifica a posicao do mouse
                if textoRect_jogar.collidepoint(mouse):                     # verifica se o mouse colido com o texto_jogar
                    return HISTORIA                                         # retorna o estado HISTORIA
                if textoRect_instrucoes.collidepoint(mouse):                # verifica se o mouse colide com o texto_instrcoues
                    return INSTRUCOES                                       # retorna o estado regras
        tecla=pygame.key.get_pressed()                                      # verifica o teclado
        if tecla[pygame.K_ESCAPE]:                                          # verifica se o ESC foi apertado
            pygame.quit()                                                   # fecha o pygame
        pygame.display.update()                                             # da update na janela
        clock.tick(FPS)                                                     # o fps