import pygame
from Constantes import *
class Botoes_instrucoes():
    def __init__(self, font, window, x, y, comando):
        cor=(0, 255, 0)
        self.texto=font.render(comando, True, cor, (0, 0, 0))
        self.textoRect=self.texto.get_rect()
        self.textoRect.center=(x, y)
    def blits(self, window):
        window.blit(self.texto, self.textoRect)
def regras(window):
    font=pygame.font.Font('freesansbold.ttf', 32)
    clock = pygame.time.Clock()
    while True:
        window.fill((0,0,0))
        cor = (0, 255, 0)
        texto_voltar=Botoes_instrucoes(font, window, WIDTH // 2, HEIGHT //2, 'Voltar')
        texto_espaco = Botoes_instrucoes(font, window, WIDTH, HEIGHT, 'Espaço')
        texto_espaco.blits(window)
        texto_voltar.blits(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if textoRect_voltar.collidepoint(mouse):
                    return INIT
        pygame.display.update()
        clock.tick(240)

#if qualquer tecla do dash la:
#    if a tecla pra tas:
#        dash=-dash
#        pos+=dash
#    else:
#        pos+=dash