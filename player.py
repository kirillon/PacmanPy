import pygame

from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))


        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.x, self.y = player_pos
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        self.side = TILE



    @property
    def pos(self):
        return (self.x, self.y)



    def movement(self):
        self.keys_control()

        self.rect.center = self.x, self.y




    def keys_control(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            dy = self.y-TILE*self.speed
            self.y += dy

            self.x += self.rect.x

        if keys[pygame.K_s]:
            dy = self.y + TILE * self.speed
            self.y += dy
        if keys[pygame.K_a]:
            dx =self.x + TILE * self.speed
            self.x += dx
        if keys[pygame.K_d]:
            dx = self.x + TILE * self.speed
            self.x += dx

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()



