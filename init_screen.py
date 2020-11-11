import pygame
from Constantes import *
pygame.init()

def tela_inicial(window):                                                   #funcão do menu
    font=pygame.font.Font('freesansbold.ttf', 32)                           #funto dos textos dentro da tela
    a=(0,0,0)
    clock = pygame.time.Clock()                                                               #cor q é a tela
    while True:                                                             #loop principal do menu
        window.fill(a)                                                      #preenche  tela com a cor definida em a
        cor=(0, 255, 0)                                                     #cor dos escritos
        texto_jogar=font.render('JOGAR', True, cor, (0, 0, 0))              #cria o texto_jogar
        textoRect_jogar=texto_jogar.get_rect()                              #pega a hit-box do texto_jogar
        textoRect_jogar.center = (100, 600)                                 #posiciona o texto_jogar
        texto_instrucoes=font.render('INSTRUÇÕES', True, cor, (0, 0, 0))    #cria o texto_instrucoes
        textoRect_instrucoes=texto_instrucoes.get_rect()                    #pega a hitbox do texto_instrcoes
        textoRect_instrucoes.center = (585, 600)                            #posiciona o texto_instrucoes
        window.blit(texto_jogar, textoRect_jogar)                           #escreve o texto_jogar
        window.blit(texto_instrucoes, textoRect_instrucoes)                 #escreve o texto_instrucoes
        for event in pygame.event.get():                                    #verifica os eventos do pygame
            if event.type == pygame.QUIT:                                   #verifica se o jogador fechou o johgo
                pygame.quit()                                               #fecha o pygame
            if event.type == pygame.MOUSEBUTTONUP:                          #verifica se o jogador apertou e soltou o botao do mouse
                mouse = pygame.mouse.get_pos()                              #verifica a posicao do mouse
                if textoRect_jogar.collidepoint(mouse):                     #verifica se o mouse colido com o texto_jogar
                    return GAME                                             #retorn o estado GAME
                if textoRect_instrucoes.collidepoint(mouse):                #verifica se o mouse colide com o texto_instrcoues
                    return INSTRUCOES                                       #retorna o estado regras
        tecla=pygame.key.get_pressed()                                      #verifica o teclado
        if tecla[pygame.K_ESCAPE]:                                          #verific se o ESC foi apertado
            pygame.quit()                                                   #fecha o pygame
        pygame.display.update()                                             #da update na jenala
        clock.tick(FPS)                                                     #o fps