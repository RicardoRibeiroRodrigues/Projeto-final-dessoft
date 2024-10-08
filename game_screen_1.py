import pygame
from classes import *
import random
from Constantes import *
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

def load_assets():
    """Função para o carregamento dos assets usados no jogo em um dicionário."""
    assets = {}
    #Para o jogo
    assets["PLAYER_IMG"] = pygame.image.load("assets\Img\Personagem.png").convert_alpha()
    assets["HIMALAIA_IMG"] = pygame.image.load("assets\Img\Himalaia.png").convert()
    assets["TEMPLO_GAUSS_IMG"] = pygame.image.load("assets\Img\Templo_gauss.png").convert()
    assets["MONTANHA_IMG"] = pygame.image.load("assets\Img\Imagem_tela2.png").convert()
    assets["MAGIA_FOGO_IMG"] = pygame.image.load("assets\Img\Bola_de_fogo.png").convert_alpha()
    assets["MAGIA_FOGO_AZUL_IMG"] = pygame.image.load("assets\Img\Magia_fogo_azul.png").convert_alpha()
    assets["ENEMIES_IMG"] = pygame.image.load("assets\Img\Inimigos.png").convert_alpha()
    assets["FIREBALL_SOUND"] = pygame.mixer.Sound("assets\Sounds\Bola_de_fogo.wav")
    assets["PLATAFORM_IMG"] = pygame.image.load("assets\Img\Plataforma.png").convert_alpha()
    assets["PLATAFORM_2_IMG"] = pygame.image.load("assets\Img\plataforma_2.png").convert_alpha()
    assets["MAGIA_GELO_IMG"] = pygame.image.load("assets\Img\Magia_Gelo.png").convert_alpha()
    assets["MAGIA_FORMULA"] = pygame.image.load("assets\Img\Magia_gauss.png").convert_alpha()
    assets["GAUSS"] = pygame.image.load("assets\Img\Gauss_img.png").convert_alpha()
    assets["BOLA_ENERGIA"] = pygame.image.load("assets\Img\Bola_de_energia.png").convert_alpha()
    assets["FUNDO_ASSOMBRADO"] = pygame.image.load("assets\Img\Fundo_assombrado.png").convert()
    #Para as telas de historia, iniciais e de intruções.
    assets["TELA_INICIAL"] = pygame.image.load("assets\Img\Historia\Tela_inicial.jpg").convert()
    assets["INTRO_HIST"] = pygame.image.load("assets\Img\Historia\Intro_hist.png").convert()
    assets["PRIMEIRA_HIST"] = pygame.image.load("assets\Img\Historia\primeira_hist.png").convert()
    assets["SEGUNDA_HIST"] = pygame.image.load("assets\Img\Historia\segunda_hist.png").convert()
    assets["TERCEIRA_HIST"] = pygame.image.load("assets\Img\Historia\Rterceira_hist.png").convert()
    assets["QUARTA_HIST"] = pygame.image.load("assets\Img\Historia\quarto_hist.png").convert()
    assets["QUINTA_HIST"] = pygame.image.load("assets\Img\Historia\quinto_hist.png").convert()
    assets["SEXTA_HIST"] = pygame.image.load("assets\Img\Historia\sexto_hist.png").convert()
    assets["SETIMA_HIST"] = pygame.image.load("assets\Img\Historia\setimo_hist.png").convert()
    assets["FINAL_1"] = pygame.image.load("assets\Img\Historia\Imagem_final1.png").convert()
    assets["FINAL_2"] = pygame.image.load("assets\Img\Historia\Imagem_final2.png").convert()
    assets["TELA_FINAL"] = pygame.image.load("assets\Img\Historia\Tela_Final.jpg").convert() 
    #Fantasminha, inimigo animado
    fantasma_atacando = []
    for i in range(7):
        file_name = f"assets\Img\Fantasminha\Ghost_{i}.png"
        img = pygame.image.load(file_name).convert_alpha()
        img = pygame.transform.scale(img, (GHOST_WIDTH, GHOST_HEIGHT))
        img = pygame.transform.flip(img, True, False)
        fantasma_atacando.append(img)
    assets["FANTASMA_ATACANDO"] = fantasma_atacando
    return assets


def renderiza_texto(texto, cor, tamanho_fonte):
    fonte = pygame.font.Font('freesansbold.ttf', tamanho_fonte)
    return fonte.render(texto, True, cor)


def carrega_musica(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)


def carrega_background(img_path, assets):
    BACKGROUND = assets[img_path]
    BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
    BACKGROUND_RECT = BACKGROUND.get_rect()
    return BACKGROUND, BACKGROUND_RECT


def game_screen(janela, assets):  #funcao para a janela do jogo
    """Função para a primeira tela da primeira fase do jogo, retorna o proximo estado do jogo"""
    #Musica de fundo
    carrega_musica('assets/Sounds/Musica_loop.mp3')
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    # Renderiza o texto para ser usado no loop da fase.
    texto_Barra_de_vida = renderiza_texto("Vida", RED, 32)
    texto_passagem_tela = renderiza_texto("Para passar de tela, aperte o p", RED, 25)
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND, BACKGROUND_RECT = carrega_background("HIMALAIA_IMG", assets)
    player = Player(assets, all_plataforms)
    #Cria a barra de vida
    barra_de_vida = Life_bar(20, 35, player)
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
            player.take_damage(100)
        #Colisão de projeteis -- A magia de fogo se anula com a magia do inimigo, e a magia de fogo azul apenas anula o ataque.
        pygame.sprite.groupcollide(all_enemies_projectiles, all_fire_magic, True, True)
        pygame.sprite.groupcollide(all_enemies_projectiles, all_blue_fire_magic, True, False)
        #Coloca efeitos para os hits, inimigos e player podem morrer
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_blue_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_blue_fire_magic, False, True)
        #hits_enemie_player = pygame.sprite.groupcollide(all_players, all_enemies, False, False)   #Inativo, o player toma dano apenas de tiros
        for enemie in hits_fire_enemies:
            enemie.lives -= DAMAGE_FIRESPELL
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_blue_fire_enemies:
            enemie.lives -= DAMAGE_BLUESPELL
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
            janela.blit(texto_passagem_tela, (300, 0))
        #desenha a barra de vida do personagem
        janela.blit(texto_Barra_de_vida, (80, 0))  
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,30),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state


def game_screen_2(janela,assets):
    """Funcao para a segunda tela da primeira fase do jogo, retorna o proximo estado do jogo"""
    #Musica de fundo
    carrega_musica('assets/Sounds/Musica_loop.mp3')
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Define a fonte para a escrita na tela
    texto_Barra_de_vida = renderiza_texto("Vida", RED, 32)
    texto_passagem_tela = renderiza_texto("Para passar de tela, aperte o p", RED, 25)
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND, BACKGROUND_RECT = carrega_background("MONTANHA_IMG", assets)
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
    barra_de_vida = Life_bar(20, 35, player)
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
                if event.key == pygame.K_SPACE:
                    player.cast_fire_spell()
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
                if len(all_enemies) == 0:
                    if event.key == pygame.K_p:
                        state = GAME_3
                        return GAME_3
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
            player.take_damage(200)
        #Colisão de projeteis -- A magia de fogo se anula com a magia do inimigo, e a magia de fogo azul apenas anula o ataque.
        pygame.sprite.groupcollide(all_enemies_projectiles, all_fire_magic, True, True)
        pygame.sprite.groupcollide(all_enemies_projectiles, all_blue_fire_magic, True, False)
        #Coloca efeitos para os hits, inimigos e player levam dano
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_blue_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_blue_fire_magic, False, True)
        for enemie in hits_fire_enemies:
            enemie.lives -= DAMAGE_FIRESPELL
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_blue_fire_enemies:
            enemie.lives -= DAMAGE_BLUESPELL
            if enemie.lives <=0:
                enemie.kill()
        if player.lives <= 0:
            state = QUIT     
        #Faz o update dos componentes do jogo.       
        all_sprites.update()
        barra_de_vida.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)
        #Coloca o texto para passar pra prox tela
        if len(all_enemies) == 0:
            janela.blit(texto_passagem_tela, (300, 0))
        #desenha a barra de vida do personagem
        janela.blit(texto_Barra_de_vida, (80, 0))
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,30),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state

def game_screen_3(janela, assets):  
    """Função para a terceira tela do jogo, onde o player enfrenta um mini boss, o fantasminha"""
    #Musica de fundo
    carrega_musica('assets/Sounds/Musica_loop.mp3')
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Define a fonte para a escrita na tela
    texto_Barra_de_vida = renderiza_texto("Vida", RED, 32)
    texto_passagem_tela = renderiza_texto("Para passar de tela, aperte o p", RED, 25)
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND, BACKGROUND_RECT = carrega_background("FUNDO_ASSOMBRADO", assets)
    player = Player(assets, all_plataforms)
    #Esvazia os grupos anteriores e cria os novos.
    all_plataforms.empty()
    all_players.empty()
    all_sprites.empty()
    all_sprites.add(player)
    all_players.add(player)
    #Cria a barra de vida
    barra_de_vida = Life_bar(20, 35, player)
    #Cria o fantasma e coloca em sprites
    fantasma = Fantasma(assets, player)
    all_sprites.add(fantasma)
    all_enemies.add(fantasma)
    # Cria as plataformas
    # Posicoes possiveis da parte esquerda da plataforma e parte superior da plataforma.
    pos_x = [300, (300 + PLATAFORM_WIDTH + 20)]
    pos_y = [ (GROUND - WIDTH//5) , ((GROUND - WIDTH//2.5))]
    # Criação das plataformas
    for posição_x in pos_x:
        for posição_y in pos_y: 
            plataformas = Plataform(assets["PLATAFORM_IMG"], posição_x, posição_y)
            all_plataforms.add(plataformas)
            all_sprites.add(plataformas)
    state = PLAYING
    while state != QUIT:
        #Limita o FPS.
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
                if event.key == pygame.K_SPACE:
                    player.cast_fire_spell()
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
                if len(all_enemies) == 0:
                    if event.key == pygame.K_p:
                        state = GAME_2
                        return GAME_4
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #Fantasma ataca sempre que possivel
        fantasma.attack()
        #Colisão dos ataques do inimigo com o player
        hits_enemie_attack_player = pygame.sprite.groupcollide(all_enemies_projectiles,all_players, True, False)
        for hit in hits_enemie_attack_player:
            player.take_damage(400)
        #Colisão de projeteis -- A magia de fogo se anula com a magia do inimigo, e a magia de fogo azul apenas anula o ataque.
        pygame.sprite.groupcollide(all_enemies_projectiles, all_fire_magic, True, True)
        pygame.sprite.groupcollide(all_enemies_projectiles, all_blue_fire_magic, True, False)
        #Coloca efeitos para os hits, inimigos e player podem morrer
        hits_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_fire_magic, False, True)
        hits_blue_fire_enemies = pygame.sprite.groupcollide(all_enemies,all_blue_fire_magic, False, True)
        for enemie in hits_fire_enemies:
            enemie.lives -= DAMAGE_FIRESPELL
            if enemie.lives <=0:
                enemie.kill()
        for enemie in hits_blue_fire_enemies:
            enemie.lives -= DAMAGE_BLUESPELL
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
            janela.blit(texto_passagem_tela, (300, 0))
        #desenha a barra de vida do personagem
        janela.blit(texto_Barra_de_vida, (80, 0))  
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,30),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.display.flip()
    return state

def game_screen_4(janela,assets):
    """Função para a terceira parte da primeira fase do jogo, 
    onde há a luta com o boss e retorna o proximo estado do jogo"""
    #Musica de fundo
    carrega_musica('assets/Sounds/Musica_loop.mp3')
    #variavel para controlar o FPS
    clock = pygame.time.Clock()
    #Define a fonte para a escrita na tela
    texto_Barra_de_vida = renderiza_texto("Vida", RED, 32)
    texto_Barra_de_vida_gauss = renderiza_texto("Gauss, o grande", WHITE, 27)
    #cria o player com a imagem do personagem e carrega a imagem do plano de fundo
    BACKGROUND, BACKGROUND_RECT = carrega_background("TEMPLO_GAUSS_IMG", assets)
    player = Player(assets, all_plataforms)
    #Cria a barra de vida do player
    barra_de_vida = Life_bar(20, 35, player)
    #Cria gauss e sua barra de vida
    gauss = Gauss(assets["GAUSS"], assets, player)
    barra_de_vida_gauss = Life_bar(950, 35, gauss)
    #Adiciona o player ao grupo de todos os sprites e ao grupo do player e remove os sprites da tela passada
    all_plataforms.empty()
    all_players.empty()
    all_sprites.empty()
    all_sprites.add(gauss)
    all_sprites.add(player)
    all_players.add(player)
    #Cria as plataformas
    #posicoes possiveis da parte esquerda da plataforma e parte superior da plataforma.
    pos_x = [200, (200 + PLATAFORM_WIDTH + 20)]
    pos_y = [(GROUND - WIDTH//5) , ((GROUND - WIDTH//2.5))]
    #Criação das plataformas
    for posição_x in pos_x:
        for posição_y in pos_y: 
            plataformas = Plataform(assets["PLATAFORM_2_IMG"], posição_x, posição_y)
            all_plataforms.add(plataformas)
            all_sprites.add(plataformas)
    #loop da tela
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
                if event.key == pygame.K_SPACE:
                    player.cast_fire_spell()
                if event.key == pygame.K_c:
                    player.cast_blue_flame_spell()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop_walk_left()
                if event.key == pygame.K_RIGHT:
                    player.stop_walk_right()
        #O player leva dano ao encostar em gauss.
        hits_gauss_player = pygame.sprite.spritecollide(gauss, all_players, False)
        for hit in hits_gauss_player:
            player.take_damage(20)
        #Hits das magias do player em gauss
        hits_fire_gauss = pygame.sprite.spritecollide(gauss, all_fire_magic, True)
        for hit in hits_fire_gauss:
            gauss.lives -= DAMAGE_FIRESPELL * 5
        hits_blue_fire_gauss = pygame.sprite.spritecollide(gauss, all_blue_fire_magic, True)
        for hit in hits_blue_fire_gauss:
            gauss.lives -= DAMAGE_BLUESPELL * 5  
        #Gauss tenta atirar a cada passagem do loop, mas há um cooldown em seus ataques 
        gauss.ataque_normal()
        gauss.ataque_especial()
        #Hits dos ataques de gauss no player
        hits_gaussatack_player = pygame.sprite.spritecollide(player, all_gauss_projectiles, True)
        for hit in hits_gaussatack_player:
            player.take_damage(100)
        hits_specialattack_player = pygame.sprite.spritecollide(player, all_gauss_special_attacks, True)
        for hit in hits_specialattack_player:
            player.take_damage(300)
        #O ataque do player anula o ataque especial
        pygame.sprite.groupcollide(all_gauss_special_attacks, all_fire_magic, True, True)
        #Jogo acaba se o player morre
        if player.lives <= 0:
            state = QUIT
        #Se gauss morrer, acaba a fase
        if gauss.lives <= 0:
            return TELA_FINAL 
        #Faz o update dos componentes do jogo.
        all_sprites.update()
        barra_de_vida.update()
        barra_de_vida_gauss.update()
        #desenha os elementos na tela.
        janela.fill(BLACK)
        janela.blit(BACKGROUND,BACKGROUND_RECT)
        all_sprites.draw(janela)
        #desenha a barra de vida do personagem e de gauss
        janela.blit(texto_Barra_de_vida, (80, 0))
        janela.blit(texto_Barra_de_vida_gauss, ((960), 0))
        pygame.draw.rect(janela, BLACK, pygame.Rect((10,30),(220,60)))
        pygame.draw.rect(janela, BLACK, pygame.Rect((940,30),(220,60)))
        pygame.draw.rect(janela, RED, barra_de_vida.rect)
        pygame.draw.rect(janela, BLUE, barra_de_vida_gauss.rect)
        pygame.display.flip()
    return state

