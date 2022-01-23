from random import choice

import pygame as pg

from map import wall_map
from settings import TILE, ghost_speed

ghost_spites = pg.sprite.Group()


class Ghost(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.flag_rect = 1
        self.image = pg.Surface([TILE, TILE])
        self.image.fill(pg.Color("red"))
        self.x, self.y = 15 * TILE, 14 * TILE
        self.rect = self.image.get_rect()
        self.rect.center = 15 * TILE, 14 * TILE
        self.speed = ghost_speed
        self.direction = -1, 0
        self.next_direction = None
        self.rectlist = [r.rect for r in wall_map]
        self.dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        self.check_direction()
        self.rect.center = self.x, self.y

    def check_direction(self):
        if self.next_direction is not None:
            if self.detect_collision(self.next_direction[0], self.next_direction[1]):
                self.direction = self.next_direction
                self.next_direction = None
        if self.detect_collision(self.direction[0], self.direction[1]):
            self.x += self.direction[0] * ghost_speed * TILE
            self.y += self.direction[1] * ghost_speed * TILE
        else:
            dir_r = list()
            for i in range(len(self.dir)):
                #print(self.detect_collision(self.dir[i][0], self.dir[i][1]))
                if self.detect_collision(self.dir[i][0], self.dir[i][1]):
                    dir_r.append(self.dir[i])
                    #print(dir_r)
            self.next_direction = choice(dir_r)
        if self.x < 0:
            self.x = 600
        if self.x > 600:
            self.x = 0

    def detect_collision(self, dx, dy):
        if self.flag_rect:
            self.rectlist = [r.rect for r in wall_map]
        next_rect = self.rect.copy()
        delta_x, delta_y = 0, 0

        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.rectlist)
        #print(hit_indexes)
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
