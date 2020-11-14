import pygame
from classes import *
from Load_assets import load_assets
import random
pygame.init()


def game_screen(janela):  #funcao para a janela do jogo
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["HIMALAIA_IMG"]
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets)
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
                if event.key == pygame.K_SPACE:
                    player.cast_fire_spell()
                if event.key == pygame.K_l:
                    player.cast_lightning_spell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Coloca efeitos para os hits, inimigos e player podem morrer
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_lightning_enemies = pygame.sprite.groupcollide(all_enemies,all_lightning_magic, False, True)
        hits_enemie_player = pygame.sprite.groupcollide(all_players, all_enemies, False, False)
        for enemie in hits_fire_enemies:
            enemie.lives -= 10
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_lightning_enemies:
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
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)
        pygame.display.flip()
    return state


def game_screen_2(janela):
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["HIMALAIA_TEMPLE_IMG"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets)
    #Adiciona o player ao grupo de todos os sprites e ao grupo do player
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
                if event.key == pygame.K_SPACE:
                    player.cast_fire_spell()
                if event.key == pygame.K_l:
                    player.cast_lightning_spell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Coloca efeitos para os hits, inimigos e player podem morrer
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_lightning_enemies = pygame.sprite.groupcollide(all_enemies,all_lightning_magic, False, True)
        hits_enemie_player = pygame.sprite.groupcollide(all_players, all_enemies, False, False)
        for enemie in hits_fire_enemies:
            enemie.lives -= 10
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_lightning_enemies:
            enemie.lives -= 20
            if enemie.lives <=0:
                enemie.kill()
        if len(hits_enemie_player) > 0:
            player.take_damage(10)
        if player.lives <= 0:
            state = QUIT     
        #Faz o update dos componentes do jogo.       
        all_sprites.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)
        pygame.display.flip()
    return state
