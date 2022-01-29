import pygame
from settings import *


class Point(pygame.sprite.Sprite):  # класс точки
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILE // 5, TILE // 5))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
