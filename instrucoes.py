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
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    while True:
        window.fill((0,0,0))
        VERDE = (0, 255, 0)
        texto_voltar=Botoes_instrucoes(font, window, ((WIDTH*10) // 10)-100, HEIGHT -50, 'Voltar')
        texto_espaco = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/6), 'Espaço')
        texto_C = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/6)*2, 'C')
        texto_UP = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/6)*3, 'UP')
        texto_F = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/6)*4, 'F')
        texto_LEFT = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/6)*5, 'LEFT')
        texto_RIGHT = Botoes_instrucoes(font, window, WIDTH-1000, ((HEIGHT-100)/6)*6, 'RIGHT')
        texto_magia_fogo = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/6), 'Magia de fogo')
        texto_magia_gelo = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/6)*2, 'Magia de gelo')
        texto_pulo = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/6)*3, 'Pula')
        texto_dash = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/6)*4, 'Dash')
        texto_esquerda = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/6)*5, 'Anda para a esquerda')
        texto_direita = Botoes_instrucoes(font, window, WIDTH-700, ((HEIGHT-100)/6)*6, 'Anda para a direita')
        texto_espaco.blits(window)
        texto_voltar.blits(window)
        texto_C.blits(window)
        texto_UP.blits(window)
        texto_F.blits(window)
        texto_LEFT.blits(window)
        texto_RIGHT.blits(window)
        texto_magia_fogo.blits(window)
        texto_magia_gelo.blits(window)
        texto_pulo.blits(window)
        texto_dash.blits(window)
        texto_esquerda.blits(window)
        texto_direita.blits(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if texto_voltar.textoRect.collidepoint(mouse):
                    return INIT
        pygame.display.update()
        clock.tick(240)