import pygame
from Constantes import *
class Botoes_instrucoes():                                          #classe que cria os textos
    def __init__(self, font, window, x, y, comando):                
        cor=(0, 255, 0)
        self.texto=font.render(comando, True, cor, (0, 0, 0))
        self.textoRect=self.texto.get_rect()
        self.textoRect.center=(x, y)
    def blits(self, window):                                    #mostra os textsos    
        window.blit(self.texto, self.textoRect)
def regras(window):
    """funcao que mostra os contrles e retorna a funcao INIT"""
    font=pygame.font.Font('freesansbold.ttf', 32)                   #define a fonte do texto
    clock = pygame.time.Clock()
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')        #define uma musica
    pygame.mixer.music.set_volume(0.4)                              #define o volume da musica
    pygame.mixer.music.play(loops=-1)                               #toca a musica em loop
    while True:
        window.fill((0,0,0))                                        #preenche a tela de preto
        VERDE = (0, 255, 0)                                         #define a cor verde
        texto_voltar=Botoes_instrucoes(font, window, ((WIDTH*10) // 10)-100, HEIGHT -50, 'Voltar')              #passa os parametros para criar os textos
        texto_espaco = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/5), 'Espaço')                  #passa os parametros para criar os textos
        texto_C = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/5)*2, 'C')                          #passa os parametros para criar os textos
        texto_UP = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/5)*3, 'UP')                        #passa os parametros para criar os textos
        
        texto_LEFT = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/5)*4, 'LEFT')                    #passa os parametros para criar os textos
        texto_RIGHT = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/5)*5, 'RIGHT')                  #passa os parametros para criar os textos
        texto_magia_fogo = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/5), 'Magia de fogo')        #passa os parametros para criar os textos
        texto_magia_gelo = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/5)*2, 'Magia de fogo azul') #passa os parametros para criar os textos
        texto_pulo = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/5)*3, 'Pula')                     #passa os parametros para criar os textos
        
        texto_esquerda = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/5)*4, 'Anda para a esquerda') #passa os parametros para criar os textos
        texto_direita = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/5)*5, 'Anda para a direita')   #passa os parametros para criar os textos
        texto_espaco.blits(window)                  #chama a funcao que mostra os textos
        texto_voltar.blits(window)                  #chama a funcao que mostra os textos
        texto_C.blits(window)                       #chama a funcao que mostra os textos
        texto_UP.blits(window)                      #chama a funcao que mostra os textos
        
        texto_LEFT.blits(window)                    #chama a funcao que mostra os textos
        texto_RIGHT.blits(window)                   #chama a funcao que mostra os textos
        texto_magia_fogo.blits(window)              #chama a funcao que mostra os textos
        texto_magia_gelo.blits(window)              #chama a funcao que mostra os textos
        texto_pulo.blits(window)                    #chama a funcao que mostra os textos
        
        texto_esquerda.blits(window)                #chama a funcao que mostra os textos
        texto_direita.blits(window)                 #chama a funcao que mostra os textos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if texto_voltar.textoRect.collidepoint(mouse):
                    return INIT
        pygame.display.update()
        clock.tick(240)