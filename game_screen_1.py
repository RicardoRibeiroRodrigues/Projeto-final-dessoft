import pygame
from classes import *
import random
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

def load_assets():
    """Função para o carregamento dos assets usados no jogo em um dicionário."""
    assets = {}
    assets["PLAYER_IMG"] = pygame.image.load("assets\Img\Personagem.png").convert_alpha()
    assets["HIMALAIA_IMG"] = pygame.image.load("assets\Img\Himalaia.png").convert()
    assets["HIMALAIA_TEMPLE_IMG"] = pygame.image.load("assets\Img\Templo_himalaia.png").convert()
    assets["MAGIA_FOGO_IMG"] = pygame.image.load("assets\Img\Bola_de_fogo.png").convert_alpha()
    assets["MAGIA_FOGO_AZUL_IMG"] = pygame.image.load("assets\Img\Magia_fogo_azul.png").convert_alpha()
    assets["ENEMIES_IMG"] = pygame.image.load("assets\Img\Inimigos.png").convert_alpha()
    assets["FIREBALL_SOUND"] = pygame.mixer.Sound("assets\Sounds\Bola_de_fogo.wav")
    return assets

def game_screen(janela):  #funcao para a janela do jogo
    """Função para a primeira tela da primeira fase do jogo, retorna o proximo estado do jogo"""
    #Musica de fundo
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["HIMALAIA_IMG"]
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets)
    #Cria a barra de vida
    barra_de_vida = Life_bar(player)
    #Adiciona o player ao grupo de todos os sprites e ao grupo do player
    all_sprites.add(player)
    all_players.add(player)
    #cria os inimigos
    for i in range(3):
        x = random.randint(0, 1200)
        inimigo = Inimigos(assets["ENEMIES_IMG"], x, player)
        all_sprites.add(inimigo)
        all_enemies.add(inimigo)
    state = PLAYING
    while state != QUIT:
        #Limita o FPS
        clock.tick(FPS)
        #Faz a interação dos eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_LEFT:
                    player.walk_left()
                if event.key == pygame.K_RIGHT:
                    player.walk_right()
                if event.key == pygame.K_f:
                    player.dash()
                if event.key == pygame.K_x:
                    player.cast_fire_spell()
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Coloca efeitos para os hits, inimigos e player podem morrer
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_blue_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_blue_fire_magic, False, True)
        hits_enemie_player = pygame.sprite.groupcollide(all_players, all_enemies, False, False)
        for enemie in hits_fire_enemies:
            enemie.lives -= 10
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_blue_fire_enemies:
            enemie.lives -= 20
            if enemie.lives <=0:
                enemie.kill()
        if len(hits_enemie_player) > 0:
            player.take_damage(10)
        if player.lives <= 0:
            state = QUIT
        if len(all_enemies) == 0:
            state = GAME_2
            break
        #Faz o update dos componentes do jogo.       
        all_sprites.update()
        barra_de_vida.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)
        #desenha a barra de vida do personagem
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,5),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state


def game_screen_2(janela):
    """Funcao para a segunda tela da primeira fase do jogo, retorna o proximo estado do jogo"""
    #Musica de fundo
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["HIMALAIA_TEMPLE_IMG"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets)
    #Cria a barra de vida
    barra_de_vida = Life_bar(player)
    #Adiciona o player ao grupo de todos os sprites e ao grupo do player e remove os sprites da tela passada
    all_players.empty()
    all_sprites.empty()
    all_sprites.add(player)
    all_players.add(player)
    #cria os inimigos
    for i in range(3):
        x = random.randint(0, 1200)
        inimigo = Inimigos(assets["ENEMIES_IMG"], x, player)
        all_sprites.add(inimigo)
        all_enemies.add(inimigo)
    state = PLAYING
    while state != QUIT:
        #Limita o FPS
        clock.tick(FPS)
        #Faz a interação dos eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_LEFT:
                    player.walk_left()
                if event.key == pygame.K_RIGHT:
                    player.walk_right()
                if event.key == pygame.K_f:
                    player.dash()
                if event.key == pygame.K_x:
                    player.cast_fire_spell()
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Coloca efeitos para os hits, inimigos e player levam dano
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_blue_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_blue_fire_magic, False, True)
        hits_enemie_player = pygame.sprite.groupcollide(all_players, all_enemies, False, False)
        for enemie in hits_fire_enemies:
            enemie.lives -= 10
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_blue_fire_enemies:
            enemie.lives -= 20
            if enemie.lives <=0:
                enemie.kill()
        if len(hits_enemie_player) > 0:
            player.take_damage(10)
        if player.lives <= 0:
            state = QUIT     
        #Faz o update dos componentes do jogo.       
        all_sprites.update()
        barra_de_vida.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)
        #desenha a barra de vida do personagem
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,5),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state


def game_screen_3(janela):
    """Função para a terceira parte da primeira fase do jogo, 
    onde há a luta com o boss e retorna o proximo estado do jogo"""
    #Musica de fundo
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["TEMPLO_LUTA_IMG"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets)
    #Cria a barra de vida
    barra_de_vida = Life_bar(player)
    #Adiciona o player ao grupo de todos os sprites e ao grupo do player e remove os sprites da tela passada
    all_players.empty()
    all_sprites.empty()
    all_sprites.add(player)
    all_players.add(player)
    state = PLAYING
    while state != QUIT:
        #Limita o FPS
        clock.tick(FPS)
        #Faz a interação dos eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_LEFT:
                    player.walk_left()
                if event.key == pygame.K_RIGHT:
                    player.walk_right()
                if event.key == pygame.K_f:
                    player.dash()
                if event.key == pygame.K_x:
                    player.cast_fire_spell()
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Coloca efeitos para os hits, inimigos e player levam dano
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_blue_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_blue_fire_magic, False, True)
        hits_enemie_player = pygame.sprite.groupcollide(all_players, all_enemies, False, False)
        for enemie in hits_fire_enemies:
            enemie.lives -= 10
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_blue_fire_enemies:
            enemie.lives -= 20
            if enemie.lives <=0:
                enemie.kill()
        if len(hits_enemie_player) > 0:
            player.take_damage(10)
        if player.lives <= 0:
            state = QUIT     
        #Faz o update dos componentes do jogo.
        all_sprites.update()
        barra_de_vida.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)
        #desenha a barra de vida do personagem
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,5),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state
