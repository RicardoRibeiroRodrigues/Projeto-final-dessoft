import pygame

def load_assets():
    assets = {}
    assets["PLAYER_IMG"] = pygame.image.load("assets\Img\mago_pixel_art.png").convert_alpha()


    return assets
    
