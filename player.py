import pygame

from map import wall_map
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.flag_rect = 1
        self.image = pygame.Surface((TILE, TILE))
        self.image.fill(YELLOW)
        self.x, self.y = 13.5 * TILE, 26 * TILE
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.center = 13.5 * TILE, 26 * TILE
        self.rectlist = [r.rect for r in wall_map]
        self.direction =  -(TILE * self.speed), 0
        self.next_direction = None
        self.side = TILE
        self.score = 0

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.keys_control()
        self.check_direction()
        self.rect.center = self.x, self.y

    def check_direction(self):
        if self.next_direction != None:
            if self.detect_collision(self.next_direction[0],self.next_direction[1]):
                self.direction = self.next_direction
                self.next_direction = None
        if self.detect_collision(self.direction[0],self.direction[1]):
            self.x+= self.direction[0]
            self.y+=self.direction[1]
        if self.x<0:
            self.x=600
        if self.x>600:
            self.x=0



    def detect_collision(self, dx, dy):
        if self.flag_rect:
            self.rectlist = [r.rect for r in wall_map]
        next_rect = self.rect.copy()
        delta_x, delta_y = 0, 0


        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.rectlist)
        print(hit_indexes)
        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.rectlist[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 20:  # <-------------
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_x < delta_y:
                dx = 0

        if dx == 0 and dy == 0:
            return False
        else:
            return True


    def keys_control(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            dy = -(TILE * self.speed)


            # self.y -= dy
            self.next_direction = 0, dy

            # player_pos[1] -=dy
        if keys[pygame.K_s]:
            dy = TILE * self.speed
            # self.y += dy
            self.next_direction = 0, dy
            player_pos[1] += dy
        if keys[pygame.K_a]:
            dx = -(TILE * self.speed)
            # self.x -= dx
            self.next_direction =dx, 0
            # player_pos[0] -= dx
        if keys[pygame.K_d]:
            dx = TILE * self.speed
            self.next_direction =dx, 0
            # self.x += dx
            # player_pos[0] += dx

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
