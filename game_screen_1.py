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
    assets["MONTANHA_IMG"] = pygame.image.load("assets\Img\Imagem_tela2.png").convert()
    assets["MAGIA_FOGO_IMG"] = pygame.image.load("assets\Img\Bola_de_fogo.png").convert_alpha()
    assets["MAGIA_FOGO_AZUL_IMG"] = pygame.image.load("assets\Img\Magia_fogo_azul.png").convert_alpha()
    assets["ENEMIES_IMG"] = pygame.image.load("assets\Img\Inimigos.png").convert_alpha()
    assets["FIREBALL_SOUND"] = pygame.mixer.Sound("assets\Sounds\Bola_de_fogo.wav")
    assets["PLATAFORM_IMG"] = pygame.image.load("assets\Img\Plataforma.png").convert_alpha()
    assets["MAGIA_GELO_IMG"] = pygame.image.load("assets\Img\Magia_Gelo.png").convert_alpha()
    return assets

def game_screen(janela):  #funcao para a janela do jogo
    """Função para a primeira tela da primeira fase do jogo, retorna o proximo estado do jogo"""
    #Musica de fundo
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Define a fonte para a escrita na tela
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    fonte_2 = pygame.font.Font('freesansbold.ttf', 20)
    texto_Barra_de_vida = fonte.render("Vida", True, RED)        
    texto_passagem_tela = fonte.render("Para passar de tela, solte os botões de andar e aperte o p", True, RED)
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["HIMALAIA_IMG"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets, all_plataforms)
    #Cria a barra de vida
    barra_de_vida = Life_bar(player)
    #Cria as plataformas
    #posicoes possiveis da parte esquerda da plataforma e parte superior da plataforma.
    pos_x = [300, (300 + PLATAFORM_WIDTH + 20)]
    pos_y = [ (GROUND - WIDTH//5) , ((GROUND - WIDTH//2.5))]
    #Criação das plataformas
    for posição_x in pos_x:
        for posição_y in pos_y: 
            plataformas = Plataform(assets["PLATAFORM_IMG"], posição_x, posição_y)
            all_plataforms.add(plataformas)
            all_sprites.add(plataformas)
            #Cria o inimigo em cima da plataforma
            inimigo = Inimigos(assets["ENEMIES_IMG"], assets ,posição_x, posição_y, player, all_plataforms)
            all_sprites.add(inimigo)
            all_enemies.add(inimigo)
    #Adiciona o player ao grupo de todos os sprites e ao grupo do player
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
                if event.key == pygame.K_SPACE:
                    player.cast_fire_spell()
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
                if len(all_enemies) == 0:
                    if event.key == pygame.K_p:
                        state = GAME_2
                        return GAME_2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Inimigo tenta atirar a cada passagem do loop, porém há um cooldown de 2 segundos
        for enemie in all_enemies:
            enemie.attack()
            enemie.jump()
        #Colisão dos ataques do inimigo com o player
        hits_enemie_attack_player = pygame.sprite.groupcollide(all_enemies_projectiles,all_players, True, False)
        for hit in hits_enemie_attack_player:
            player.take_damage(0)
        #Colisão de projeteis -- A magia de fogo se anula com a magia do inimigo, e a magia de fogo azul apenas anula o ataque.
        hits_fire_enemie_attack = pygame.sprite.groupcollide(all_enemies_projectiles, all_fire_magic, True, True)
        hits_blue_fire_enemie_attack = pygame.sprite.groupcollide(all_enemies_projectiles, all_blue_fire_magic, True, False)
        #Coloca efeitos para os hits, inimigos e player podem morrer
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_blue_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_blue_fire_magic, False, True)
        #hits_enemie_player = pygame.sprite.groupcollide(all_players, all_enemies, False, False)   #Inativo, o player toma dano apenas de tiros
        for enemie in hits_fire_enemies:
            enemie.lives -= 10000
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_blue_fire_enemies:
            enemie.lives -= 20
            if enemie.lives <=0:
                enemie.kill()
        if player.lives <= 0:
            state = QUIT
        #Faz o update dos componentes do jogo.       
        all_sprites.update()
        barra_de_vida.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND, BACKGROUND_RECT)
        all_sprites.draw(janela)
        #Para colocar o texto para proxima tela
        if len(all_enemies) == 0:
            janela.blit(texto_passagem_tela, (400, 0))
        #desenha a barra de vida do personagem
        janela.blit(texto_Barra_de_vida, (80, 0))  
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,30),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state


def game_screen_2(janela):
    """Funcao para a segunda tela da primeira fase do jogo, retorna o proximo estado do jogo"""
    #Musica de fundo
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Define a fonte para a escrita na tela
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    fonte_2 = pygame.font.Font('freesansbold.ttf', 20)
    texto_Barra_de_vida = fonte_2.render("Vida", True, RED)
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["MONTANHA_IMG"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets, all_plataforms)
    #Esvazia os grupos anteriores e cria os novos.
    all_plataforms.empty()
    all_players.empty()
    all_sprites.empty()
    all_sprites.add(player)
    all_players.add(player)
    #Cria as plataformas
    #posicoes possiveis da parte esquerda da plataforma e parte superior da plataforma.
    pos_x = [300, (300 + PLATAFORM_WIDTH + 20)]
    pos_y = [ (GROUND - WIDTH//5) , ((GROUND - WIDTH//2.5))]
    #Criação das plataformas
    for posição_x in pos_x:
        for posição_y in pos_y: 
            plataformas = Plataform(assets["PLATAFORM_IMG"], posição_x, posição_y)
            all_plataforms.add(plataformas)
            all_sprites.add(plataformas)
            #Cria o inimigo em cima da plataforma
            inimigo = Inimigos(assets["ENEMIES_IMG"],assets, posição_x, posição_y, player, all_plataforms)
            all_sprites.add(inimigo)
            all_enemies.add(inimigo)
    #Cria a barra de vida
    barra_de_vida = Life_bar(player)
    #Loop da tela.
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
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Inimigo tenta atirar a cada passagem do loop, porém há um cooldown de 2 segundos
        for enemie in all_enemies:
            enemie.attack()
        #Colisão dos ataques do inimigo com o player
        hits_enemie_attack_player = pygame.sprite.groupcollide(all_enemies_projectiles,all_players, True, False)
        for hit in hits_enemie_attack_player:
            player.take_damage(200)
        #Colisão de projeteis -- A magia de fogo se anula com a magia do inimigo, e a magia de fogo azul apenas anula o ataque.
        pygame.sprite.groupcollide(all_enemies_projectiles, all_fire_magic, True, True)
        pygame.sprite.groupcollide(all_enemies_projectiles, all_blue_fire_magic, True, False)
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
        janela.blit(texto_Barra_de_vida, (80, 0))
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,30),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state


def game_screen_3(janela):
    """Função para a terceira parte da primeira fase do jogo, 
    onde há a luta com o boss e retorna o proximo estado do jogo"""
    #Musica de fundo
    pygame.mixer.music.load('assets/Sounds/Musica_loop.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Define a fonte para a escrita na tela
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    texto_Barra_de_vida = fonte.render("Vida", True, RED)
    #carrega os assets 
    assets = load_assets()
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND = assets["TEMPLO_LUTA_IMG"]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    player = Player(assets, all_plataforms)
    #Cria a barra de vida
    barra_de_vida = Life_bar(player)
    #Adiciona o player ao grupo de todos os sprites e ao grupo do player e remove os sprites da tela passada
    all_plataforms.empty()
    all_players.empty()
    all_sprites.empty()
    all_sprites.add(player)
    all_players.add(player)
    #Cria as plataformas
    #posicoes possiveis da parte esquerda da plataforma e parte superior da plataforma.
    pos_x = [300, (300 + PLATAFORM_WIDTH + 20)]
    pos_y = [ (GROUND - WIDTH//5) , ((GROUND - WIDTH//2.5))]
    #Criação das plataformas
    for posição_x in pos_x:
        for posição_y in pos_y: 
            plataformas = Plataform(assets["PLATAFORM_IMG"], posição_x, posição_y)
            all_plataforms.add(plataformas)
            all_sprites.add(plataformas)
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
        janela.blit(texto_Barra_de_vida, (80, 0))
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,30),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state
