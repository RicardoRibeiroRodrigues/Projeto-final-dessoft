import pygame

def load_assets():
    assets = {}
    assets["PLAYER_IMG"] = pygame.image.load("assets\Img\Personagem.png").convert_alpha()
    assets["HIMALAIA_IMG"] = pygame.image.load("assets\Img\Himalaia.png").convert()
    assets["HIMALAIA_TEMPLE_IMG"] = pygame.image.load("assets\Img\Templo_himalaia.png").convert()
    assets["MAGIA_FOGO_IMG"] = pygame.image.load("assets\Img\Bola_de_fogo.png").convert_alpha()
    assets["MAGIA_RAIO_IMG"] = pygame.image.load("assets\Img\Magia_raio.png").convert_alpha()
    assets["ENEMIES_IMG"] = pygame.image.load("assets\Img\Inimigos.png").convert_alpha()
    return assets
    
