import pygame

def load_assets():
    assets = {}
    assets["PLAYER_IMG"] = pygame.image.load("assets\Img\mago_pixel_art.png").convert_alpha()
    assets["HIMALAIA_IMG"] = pygame.image.load("assets\Img\Himalaia.png").convert()
    assets["MAGIA_FOGO_IMG"] = pygame.image.load("assets\Img\Magia_fogo.png").convert()
    return assets
    
