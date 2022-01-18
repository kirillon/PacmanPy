import pygame
from settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f"BoardImg/{path}").convert()
        self.image = pygame.transform.scale(self.image, (TILE, TILE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
