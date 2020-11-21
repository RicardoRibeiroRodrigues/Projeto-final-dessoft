import pygame
#tamanhos
WIDTH = 1200  #largura da tela
HEIGHT = 800 #altura da tela
FPS = 120    #frames por segundo
RATE = 0.70
PLAYER_WIDTH = int(100*RATE)
PLAYER_HEIGHT = int(160*RATE)
ENEMIES_WIDTH = int(100*RATE)
ENEMIES_HEIGHT = int(160*RATE)
GAUSS_WIDTH = 300
GAUSS_HEIGHT = 480
PLATAFORM_WIDTH = int(364*0.9)
PLATAFORM_HEIGHT = int(136*RATE)
#Valores do pulo, gravidade e localização do chão
GRAVITY = 1
JUMP_SIZE = 18
DASH_SIZE = 150
GROUND = HEIGHT - 96
#Tamanho das magias
SPELL_WIDTH = int(60*RATE)
SPELL_HEIGHT = int(60*RATE)
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
GAME_2 = 4
QUIT = 2
INSTRUCOES = 5
#estados do jogador 
STILL = 0
JUMPING = 1
FALLING = 2
#Grupos
#Cria o grupo de todos os sprites
all_sprites = pygame.sprite.Group()
all_fire_magic = pygame.sprite.Group()
all_blue_fire_magic = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_plataforms = pygame.sprite.Group()
#lados para o personagem ir
RIGHT = 1
LEFT = 0