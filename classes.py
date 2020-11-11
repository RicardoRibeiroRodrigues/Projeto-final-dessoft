import pygame
from Constantes import *
from Load_assets import load_assets
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        #carrega a imagem e configura ela
        img = pygame.transform.scale(img, (PLAYER_WIDTH ,PLAYER_HEIGHT))
        self.image = img
        self.rect =  img.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = GROUND
        #velocidades
        self.speedx = 0
        self.speedy = 0 
        #Define o estado
        self.state = STILL
    def update(self):
        self.speedy += GRAVITY
        #se tiver caindo, muda o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        #Ao chegar ao chao para de cair
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND #volta para o nivel do chao
            #para de cair
            self.speedy = 0
            #atualiza do estado 
            self.state = STILL
        #atualiza a posicao
        self.rect.centerx += self.speedx
        #Para nao sair do mapa
        if self.rect.x > WIDTH:
            self.rect.x = WIDTH - PLAYER_WIDTH
        if self.rect.x + PLAYER_WIDTH < 0:
            self.rect.x = 0 - PLAYER_WIDTH // 4
    #Metodo para pular
    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    def dash(self): #metodo definido para o player dar dash
        self.rect.centerx += DASH_SIZE
    #metodo para andar pra direita  
    def walk_right(self):
        self.speedx += 10
    #metodo para andar pra esquerda
    def stop_walk_right(self):
        self.speedx -= 10
    #metodo pra andar pra esquerda
    def walk_left(self):
        self.speedx -= 10
    #Metodo para parar de andar pra esquerda
    def stop_walk_left(self):
        self.speedx += 10
    def cast_fire_spell(self):
        assets = load_assets()
        magia = Magia_fogo(assets["MAGIA_FOGO_IMG"], self.rect.right, self.rect.centery)
        all_sprites.add(magia)
        all_projectiles.add(magia)
        
class Magia_fogo(pygame.sprite.Sprite):
    def __init__(self, img, right_x , centery):
        pygame.sprite.Sprite.__init__(self)
        #configurando a imagem
        img = pygame.transform.scale(img, (SPELL_WIDTH, SPELL_HEIGHT))
        self.image = img
        self.rect = img.get_rect()
        self.rect.right = right_x
        self.rect.centery = centery
        self.speedx = 10
    def update(self):
        #A magia so se move no eixo x
        self.rect.x += self.speedx
        #
        if self.rect.x > WIDTH:
            self.kill()



        
       




