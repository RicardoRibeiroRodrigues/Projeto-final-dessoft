import pygame
from Constantes import *
from random import choice
pygame.init()
pygame.mixer.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, assets, grupos_plataformas):
        pygame.sprite.Sprite.__init__(self)
        #carrega a imagem e configura ela
        self.assets = assets
        img = pygame.transform.scale(assets['PLAYER_IMG'], (PLAYER_WIDTH ,PLAYER_HEIGHT))
        self.imgs = {
            RIGHT: img,
            LEFT: pygame.transform.flip(img, True, False),
        }
        #Plataformas
        self.plataforms = grupos_plataformas
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
        self.last_shot = 0
        self.dash_cooldown = 5000
        self.last_dash = 0
        self.last_blue_fire_spell = 0
        self.blue_cooldown = 10000
        self.last_damage = 0
        self.damage_cooldown = 500
        #Vida inicial do player
        self.lives = 2000
        #Variação de tempo
        self.dt = 0
    def update(self):
        #Atualiza a imagem para a direção em que está olhando
        self.image = self.imgs[self.facing_way]
        #Contabiliza a gravidade
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
        #Para ficar na plataforma
        collisions = pygame.sprite.spritecollide(self, self.plataforms , False)
        #Corrige a posição do player pra antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
        #Ultrapassa a plataforma, se estiver indo para cima, mas nao se estiver caindo.
        if self.speedy > 0:  # Está indo para baixo
            collisions = pygame.sprite.spritecollide(self, self.plataforms, False)
            # Para cada tile de plataforma que colidiu com o personagem
            # verifica se ele estava aproximadamente na parte de cima
            for platform in collisions:
                # Verifica se a altura alcançada durante o pulo está acima da
                # plataforma.
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    # Atualiza a altura no mapa
                    self.highest_y = self.rect.bottom
                    # Para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL
        #Atualiza a posição do eixo x.
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
    #Metodo para pular
    def jump(self):
        """Método para o personagem pular"""
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    #metodo para andar pra direita  
    def walk_right(self):
        """Método para andar para direita e definir o lado que o personagem está olhando"""
        self.speedx += 6
        self.facing_way = RIGHT
    #metodo para andar pra esquerda
    def stop_walk_right(self):
        """Método para o personagem parar de andar para direita"""
        self.speedx -= 6
    #metodo pra andar pra esquerda
    def walk_left(self):
        """Método para esquerda para direita e definir o lado que o personagem está olhando"""
        self.speedx -= 6
        self.facing_way = LEFT
    #Metodo para parar de andar pra esquerda
    def stop_walk_left(self):
        """Método para o personagem parar de andar para esquerda"""
        self.speedx += 6
    def cast_fire_spell(self):
        """Método para o personagem lançar a magia de fogo para a direção que está olhando"""
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
                #Adiciona um som para a magia
                self.assets["FIREBALL_SOUND"].play()
            else:
                img = self.assets["MAGIA_FOGO_IMG"]
                img = pygame.transform.flip(img, True, False)
                magia = Magias(img, self.rect.left, self.rect.top, -10)
                all_sprites.add(magia)
                all_fire_magic.add(magia)
                #Adiciona o som para a magia
                self.assets["FIREBALL_SOUND"].play()
    def cast_blue_flame_spell(self):
        """Método para o personagem lançar a magia de fogo azul para a direção que está olhando"""
        #cooldown da magia 
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_blue_fire_spell
        #cria a magia 
        if elapsed_ticks > self.blue_cooldown:
            self.last_blue_fire_spell = now
            #cria a magia na direcao que esta olhando
            if self.facing_way == RIGHT: 
                magia = Magias(self.assets["MAGIA_FOGO_AZUL_IMG"], self.rect.right, self.rect.top, 10)
                all_sprites.add(magia)
                all_blue_fire_magic.add(magia)
            else:
                #vira a magia para ela ir para o lado certo
                img = self.assets["MAGIA_FOGO_AZUL_IMG"]
                img = pygame.transform.flip(img, True, False)
                magia = Magias(img , self.rect.left, self.rect.top, -10)
                all_sprites.add(magia)
                all_blue_fire_magic.add(magia)
    def take_damage(self, damage):
        """Método para o personagem tomar dano com intervalo entre os danos, para nao morrer instantaneamente"""
        now = pygame.time.get_ticks()
        if now - self.last_damage > self.damage_cooldown:
            self.lives -= damage
    def update_dt(self,speed):
        self.dt = speed

    def dash(self):
        self.rect.x += 50 * self.dt

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
        if self.rect.x < 0:
            self.kill()

class Inimigos(pygame.sprite.Sprite):
    def __init__(self, img, assets, x, y , player, Plataformas):
        pygame.sprite.Sprite.__init__(self)
        #Muda a imagem pro tamanho do inimigo e pega o retangulo dela.
        self.assets = assets #recebe assets
        img = pygame.transform.scale(img, (ENEMIES_WIDTH, ENEMIES_HEIGHT))
        self.rect = img.get_rect()
        #Pode virar para direita e para esquerda
        self.imgs = {
            RIGHT: img,
            LEFT: pygame.transform.flip(img, True, False),
        }
        #Olha para direita por padrão
        self.facing_way = RIGHT
        #vira a imagem para onde está olhando
        self.image = self.imgs[self.facing_way]
        #Atributo plataforma, para ficar na plataforma.
        self.plataforms = Plataformas
        #Posições iniciais dele
        self.rect.bottom = y
        self.rect.x = x
        #Velocidade iniciais
        self.speedy = 0
        self.speedx = 0
        #passa o player para os inimigos
        self.player = player
        #Vida dos inimigos
        self.lives = 20
        #Estado inicial
        self.state = STILL
        #Cooldown da magia do inimigo
        self.last_attack = 0
        self.attack_cooldown = 1000
    def update(self):
        #Sofrem ação da gravidade
        self.speedy += GRAVITY
        #se tiver caindo, muda o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        #Atualiza a posição no eixo y
        self.rect.y += self.speedy
        #Ao chegar ao chao para de cair
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND #volta para o nível do chão
            #para de cair
            self.speedy = 0
            #atualiza do estado 
            self.state = STILL
        # Atualiza velocidade para ir em direção ao jogador
        if self.player.rect.centerx < self.rect.centerx:
            #Anda para esquerda, vira para esquerda
            self.speedx = -2
            self.facing_way = LEFT
        else:
            #Anda para direia, vira para direita
            self.speedx = 2
            self.facing_way = RIGHT
        #Atualiza a posição no eixo x
        self.rect.x += self.speedx
        #Para ficar na plataforma
        collisions = pygame.sprite.spritecollide(self, self.plataforms , False)
        #Corrige a posição do player pra antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
        #Ultrapassa a plataforma, se estiver indo para cima, mas nao se estiver caindo.
        if self.speedy > 0:  # Está indo para baixo
            collisions = pygame.sprite.spritecollide(self, self.plataforms, False)
            # Para cada tile de plataforma que colidiu com o personagem
            # verifica se ele estava aproximadamente na parte de cima
            for platform in collisions:
                # Verifica se a altura alcançada durante o pulo está acima da
                # plataforma.
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    # Atualiza a altura no mapa
                    self.highest_y = self.rect.bottom
                    # Para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL
    def attack(self):
        """Método para os inimigos atacarem"""
        #Chance do ataque sair.
        chances = [0]*60
        chances.append(1)
        numero = choice(chances)
        #cooldown da magia
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_attack
        if (elapsed_ticks > self.attack_cooldown) and numero == 1:
            #Se está olhando para direita, atira para direita
            if self.facing_way == RIGHT:
                ataque = Magias(self.assets["MAGIA_GELO_IMG"], self.rect.right, self.rect.centery, 10)
                all_enemies_projectiles.add(ataque)
                all_sprites.add(ataque)
                self.last_attack = now
            #Se não, atira para esquerda
            else:
                img = self.assets["MAGIA_GELO_IMG"]
                img = pygame.transform.flip(img, True, False)
                ataque = Magias(img, self.rect.left, self.rect.centery, -10)
                all_enemies_projectiles.add(ataque)
                all_sprites.add(ataque)
                self.last_attack = now
    def jump(self):
        """Método para o inimigo pular"""
        chance = [0]*400
        chance.append(1)
        num = choice(chance)
        if self.player.rect.y < self.rect.y and num == 1:
            if self.state == STILL:
                self.speedy -= JUMP_SIZE
                self.state = JUMPING
    
class Gauss(pygame.sprite.Sprite):
    def __init__(self, img, assets, player):
        pygame.sprite.Sprite.__init__(self)
        #imagem e localizacao
        img = pygame.transform.scale(img, (GAUSS_WIDTH, GAUSS_HEIGHT))
        self.player = player
        self.image = img
        self.rect = img.get_rect()
        self.rect.bottom = GROUND
        self.rect.right = WIDTH
        #Salva os assets
        self.assets = assets
        #Numero de vidas iniciais
        self.lives = 2000
        #Cooldown
        self.last_attack = 0
        self.attack_cd = 3000
        self.last_especial_attack = 0
        self.special_cd = 6000
    def ataque_normal(self):
        """Funcao para o ataque padrao de gauss, atira em 10 projeteis em ys aleatorios"""
        #cooldown da magia 
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_attack
        if elapsed_ticks > self.attack_cd:
            for i in range(10):
                #Opcoes de y para os ataques
                max_y = int((GROUND - WIDTH//2.5) - PLAYER_HEIGHT)
                pos_y = range(GROUND, max_y, -50)
                posic = choice(pos_y)
                #Criação do projetil
                img = self.assets["MAGIA_FORMULA"]
                img = pygame.transform.scale(img, (SPELL_WIDTH, SPELL_HEIGHT))
                img = pygame.transform.flip(img, True, False)
                magia = Magias(img, self.rect.left, posic, -6)
                all_sprites.add(magia)
                all_gauss_projectiles.add(magia)
                self.last_attack = now
    def ataque_especial(self):
        #cooldown da magia 
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_especial_attack
        if elapsed_ticks > self.special_cd:
            #Cooldown do ataque
            ataque = Special_attack(self.assets["MAGIA_FORMULA"], self.player, now, self.rect.centerx , self.rect.centery)
            all_sprites.add(ataque)
            all_gauss_special_attacks.add(ataque)
            self.last_especial_attack = now

class Special_attack(pygame.sprite.Sprite):
    def __init__(self, img, player, time, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        #Transformação da imagem.
        img = pygame.transform.scale(img, (GAUSS_SPECIAL_WIDTH,GAUSS_SPECIAL_HEIGHT))
        self.imgs = {
            RIGHT: img,
            LEFT: pygame.transform.flip(img, True, False),
        }
        self.cast_time = time
        self.facing_way = RIGHT
        self.image = self.imgs[self.facing_way]
        self.rect = img.get_rect()
        #Posição
        self.rect.centerx = centerx
        self.rect.centery = centery
        #Coloca o player como atributo do objeto
        self.player = player
        #Velocidade inicial
        self.speedx = 0
    def update(self):
        #Atualiza imagem.
        self.image = self.imgs[self.facing_way]
        #Tempo de perseguição
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.cast_time
        #Persegue o player so por determinado tempo
        if elapsed_ticks <= 4000:
            # Atualiza velocidade para ir em direção ao jogador
            if self.player.rect.centerx < self.rect.centerx:
                #Vai para cima para perseguir o player
                if self.player.rect.centery < self.rect.centery:
                    self.speedy = -2
                #Vai para baixo para perseguir o player
                elif self.player.rect.centery > self.rect.centery:
                    self.speedy = 2
                #Anda para esquerda, vira para esquerda
                self.speedx = -2
                self.facing_way = LEFT
            else:
                #Vai para cima para perseguir o player
                if self.player.rect.centery < self.rect.centery:
                    self.speedy = -2
                #Vai para baixo para perseguir o player
                elif self.player.rect.centery > self.rect.centery:
                    self.speedy = 2
                #Anda para direia, vira para direita
                self.speedx = 2
                self.facing_way = RIGHT
        else:
            self.kill()
        #Atualiza a posição no eixo x e no eixo y
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Life_bar(pygame.sprite.Sprite):
    def __init__(self, x, y, entity):
        pygame.sprite.Sprite.__init__(self)
        #guarda a entidade no self.
        self.entity = entity
        #X e Y onde deve ser desenhado
        self.x = x
        self.y = y
    def update(self):
        #Atualiza a barra de vida com a vida da entidade passada.
        self.rect = pygame.Rect((self.x, self.y),((self.entity.lives)//10,50))

class Plataform(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        #imagem
        img = pygame.transform.scale(img, (PLATAFORM_WIDTH, PLATAFORM_HEIGHT))
        self.image = img
        #localizacao
        self.rect = img.get_rect()
        self.rect.left = x
        self.rect.top = y 

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, assets, player):
        pygame.sprite.Sprite.__init__(self)
        #
        self.assets = assets
        self.image = assets["FANTASMA_NORMAL"]