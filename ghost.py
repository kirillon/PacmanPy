import pygame as pg

from map import wall_map, map_orig
from settings import TILE, player_pos

ghost_sprites = pg.sprite.Group()


class Ghost(pg.sprite.Sprite):
    def __init__(self, x, y, speed, delay):
        pg.sprite.Sprite.__init__(self)
        self.flag_rect = 1
        self.image = pg.Surface([TILE, TILE])
        self.x, self.y = x * TILE, y * TILE
        self.rect = self.image.get_rect()
        self.rect.center = x * TILE, y * TILE
        self.speed = speed
        self.direction = -1, 0
        self.rectlist = [r.rect for r in wall_map]
        self.start_ticks = pg.time.get_ticks()
        self.delay = delay

    def move(self):
        if pg.time.get_ticks() - self.start_ticks - 4000 >= self.delay:
            self.rect.center = self.x, self.y

            pozIn = (int(self.x // TILE), int(self.y // TILE))
            pozOut = (int(player_pos[1] // TILE), int(player_pos[0] // TILE))

            path = [[0 if not x == 3 else -1 for x in y] for y in map_orig]
            path[pozIn[1]][pozIn[0]] = 1

            self.found(path, pozOut)

            result = self.printPath(path, pozOut)
            print(result)
            if not len(result) == 0 and not type(result[0]) != tuple:
                if self.detect_collision(result[0][0], result[0][1]):
                    self.x += result[0][0] * self.speed * TILE
                    self.y += result[0][1] * self.speed * TILE
                    self.direction = (result[0][0], result[0][1])
                else:
                    self.x += self.direction[0] * self.speed * TILE
                    self.y += self.direction[1] * self.speed * TILE

    def detect_collision(self, dx, dy):
        if self.flag_rect:
            self.rectlist = [r.rect for r in wall_map]
        next_rect = self.rect.copy()

        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.rectlist)
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

            if abs(delta_x - delta_y) < 20:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_x < delta_y:
                dx = 0

        if dx == 0 and dy == 0:
            return False
        else:
            return True

    def found(self, pathArr, finPoint):
        weight = 1
        for i in range(len(pathArr) * len(pathArr[0])):
            weight += 1
            for y in range(len(pathArr)):
                for x in range(len(pathArr[y])):
                    if pathArr[y][x] == (weight - 1):
                        if y > 0 and pathArr[y - 1][x] == 0:
                            pathArr[y - 1][x] = weight
                        if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                            pathArr[y + 1][x] = weight
                        if x > 0 and pathArr[y][x - 1] == 0:
                            pathArr[y][x - 1] = weight
                        if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                            pathArr[y][x + 1] = weight

                        if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                            pathArr[finPoint[0]][finPoint[1]] = weight
                            return True
        return False

    def printPath(self, pathArr, finPoint):
        y = finPoint[0]
        x = finPoint[1]
        weight = pathArr[y][x]
        result = list(range(weight))
        while weight:
            weight -= 1
            if y > 0 and pathArr[y - 1][x] == weight:
                y -= 1
                result[weight] = (0, 1)
            elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
                result[weight] = (0, -1)
                y += 1
            elif x > 0 and pathArr[y][x - 1] == weight:
                result[weight] = (1, 0)
                x -= 1
            elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
                result[weight] = (-1, 0)
                x += 1

        return result[1:]
