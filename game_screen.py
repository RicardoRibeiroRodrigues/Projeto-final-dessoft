import pygame
from classes import *
from Load_assets import load_assets
pygame.init()


def game_screen(janela):  #funcao para a janela do jogo
    clock = pygame.time.Clock()
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem
    BACKGROUND = assets["HIMALAIA_IMG"]
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets["PLAYER_IMG"])
    #Adiciona o player ao grupo de todos os sprites
    all_sprites.add(player)
    
    state = PLAYING
    while state != QUIT:
        clock.tick(FPS)

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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
                
        #Faz o update dos componentes do jogo.       
        all_sprites.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)

        pygame.display.flip()
    return state