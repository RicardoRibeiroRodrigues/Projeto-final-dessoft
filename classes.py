import pygame
from Constantes import PLAYER_HEIGHT, PLAYER_WIDTH
from Load_assets import load_assets
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, img , x , y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.transform.scale(img, (PLAYER_WIDTH ,PLAYER_HEIGHT))
        self.image = img
        self.rect =  img.get_rect()
        self.rect.x = x
        self.rect.y = y
        #velocidades
        self.speedx = 0
        self.speedy = 0 

    def update(self):



print(3)