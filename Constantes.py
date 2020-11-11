import pygame
WIDTH = 1200  #largura da tela
HEIGHT = 652 #altura da tela
FPS = 120    #frames por segundo
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 160
GRAVITY = 1
JUMP_SIZE = 22
DASH_SIZE = 150
GROUND = (HEIGHT * 5 )// 6
#Tamanho das magias
SPELL_WIDTH = 50
SPELL_HEIGHT = 80
#cores basicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#estados do jogo
INIT = 0
PLAYING = 1
GAME = 3
QUIT = 2
INSTRUCOES = 5
#estados do jogador 
STILL = 0
JUMPING = 1
FALLING = 2
#Grupos
#Cria o grupo de todos os sprites
all_sprites = pygame.sprite.Group()
all_projectiles = pygame.sprite.Group()



