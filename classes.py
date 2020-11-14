import pygame
from Constantes import *
from Load_assets import load_assets
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        #carrega a imagem e configura ela
        self.assets = assets
        img = pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH ,PLAYER_HEIGHT))
        self.imgs = {
            RIGHT: img,
            LEFT: pygame.transform.flip(img, True, False),
        }
        #define o lado que esta olhando
        self.facing_way = RIGHT
        #atualiza imagem
        self.image = self.imgs[self.facing_way]
        self.rect =  img.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = GROUND
        #velocidades
        self.speedx = 0
        self.speedy = 0 
        #Define o estado
        self.state = STILL
        #para o cooldown das magias e do dash e do dano
        self.fire_spell_cooldown = 1000
        self.last_shot = pygame.time.get_ticks()
        self.dash_cooldown = 5000
        self.last_dash = pygame.time.get_ticks()
        self.last_lightning_spell = pygame.time.get_ticks()
        self.light_cooldown = 10000
        self.last_damage = pygame.time.get_ticks()
        self.damage_cooldown = 500
        #Vida inicial do player
        self.lives = 1000
    def update(self):
        self.image = self.imgs[self.facing_way]
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
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_dash
        if elapsed_ticks > self.dash_cooldown:
            self.last_dash = now
            #dash para direcao em que esta olhando o personagem
            if self.facing_way == RIGHT:
                self.rect.centerx += DASH_SIZE
            else:
                self.rect.centerx -= DASH_SIZE  
    #metodo para andar pra direita  
    def walk_right(self):
        self.speedx += 10
        self.facing_way = RIGHT
    #metodo para andar pra esquerda
    def stop_walk_right(self):
        self.speedx -= 10
    #metodo pra andar pra esquerda
    def walk_left(self):
        self.speedx -= 10
        self.facing_way = LEFT
    #Metodo para parar de andar pra esquerda
    def stop_walk_left(self):
        self.speedx += 10
    def cast_fire_spell(self):
        #Para fazer o cooldown
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_shot
        if elapsed_ticks > self.fire_spell_cooldown:
            self.last_shot = now
            #cria a magia na direcao que esta olhando
            if self.facing_way == RIGHT: 
                magia = Magias(self.assets["MAGIA_FOGO_IMG"], self.rect.right, self.rect.top, 10)
                all_sprites.add(magia)
                all_fire_magic.add(magia)
            else:
                magia = Magias(self.assets["MAGIA_FOGO_IMG"], self.rect.right, self.rect.top, -10)
                all_sprites.add(magia)
                all_fire_magic.add(magia)
    def cast_lightning_spell(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_lightning_spell
        #cria a magia 
        if elapsed_ticks > self.light_cooldown:
            self.last_lightning_spell = now
            #cria a magia na direcao que esta olhando
            if self.facing_way == RIGHT: 
                magia = Magias(self.assets["MAGIA_RAIO_IMG"], self.rect.right, self.rect.top, 10)
                all_sprites.add(magia)
                all_lightning_magic.add(magia)
            else:
                magia = Magias(self.assets["MAGIA_RAIO_IMG"], self.rect.right, self.rect.top, -10)
                all_sprites.add(magia)
                all_lightning_magic.add(magia)
    def take_damage(self, damage):
        now = pygame.time.get_ticks()
        if now - self.last_damage > self.dash_cooldown:
            self.lives -= damage

class Magias(pygame.sprite.Sprite):
    def __init__(self, img, right_x , centery, speedx):
        pygame.sprite.Sprite.__init__(self)
        #configurando a imagem
        img = pygame.transform.scale(img, (SPELL_WIDTH, SPELL_HEIGHT))
        self.image = img
        self.rect = img.get_rect()
        self.rect.right = right_x
        self.rect.centery = centery
        self.speedx = speedx
    def update(self):
        #A magia so se move no eixo x
        self.rect.x += self.speedx
        #A magia deixa de existir quando sai da tela
        if self.rect.x > WIDTH:
            self.kill()

class Inimigos(pygame.sprite.Sprite):
    def __init__(self, img, x, player):
        pygame.sprite.Sprite.__init__(self)
        #Muda a imagem pro tamanho do inimigo e pega o retangulo dela.
        img = pygame.transform.scale(img, (ENEMIES_WIDTH, ENEMIES_HEIGHT))
        self.image = img
        self.rect = img.get_rect()
        self.rect.bottom = GROUND
        self.rect.x = x
        self.speedx = 0
        self.player = player
        self.lives = 20
    def update(self):
        # Atualiza velocidade para ir em direção ao jogador
        if self.player.rect.centerx < self.rect.centerx:
            self.speedx = -2
        else:
            self.speedx = 2

        self.rect.x += self.speedx


