import pygame as pg

from map import wall_map, map_orig
from settings import TILE, player_pos


ghost_sprites = pg.sprite.Group()


class Ghost(pg.sprite.Sprite):  # класс призрака
    def __init__(self, x, y, speed, delay, image, color):
        pg.sprite.Sprite.__init__(self)
        self.flag_rect = 1
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (TILE, TILE))
        self.x, self.y = x * TILE, y * TILE
        self.rect = self.image.get_rect()
        self.rect.center = x * TILE, y * TILE
        self.speed = speed
        self.direction = -1, 0
        self.rectlist = [r.rect for r in wall_map]
        self.start_ticks = pg.time.get_ticks()
        self.delay = delay
        self.flag_anim = 0
        self.color = color

    def move(self):  # класс движения
        if pg.time.get_ticks() - self.start_ticks - 4000 >= self.delay:
            self.rect.center = self.x, self.y

            poz_in = (int(self.x // TILE), int(self.y // TILE))
            poz_out = (int(player_pos[1] // TILE), int(player_pos[0] // TILE))

            path = [[0 if not x == 3 else -1 for x in y] for y in map_orig]
            path[poz_in[1]][poz_in[0]] = 1

            self.found(path, poz_out)

            result = self.print_path(path, poz_out)
            if not len(result) == 0 and not type(result[0]) != tuple:
                if self.detect_collision(result[0][0], result[0][1]):
                    self.x += result[0][0] * self.speed * TILE
                    self.y += result[0][1] * self.speed * TILE
                    self.direction = (result[0][0], result[0][1])
                    if not self.flag_anim:
                        if self.direction[0] > 0:
                            self.image = pg.image.load(f'img/{self.color}_right_1.png')
                        if self.direction[0] < 0:
                            self.image = pg.image.load(f'img/{self.color}_left_1.png')
                        if self.direction[1] > 0:
                            self.image = pg.image.load(f'img/{self.color}_down_1.png')
                        if self.direction[1] < 0:
                            self.image = pg.image.load(f'img/{self.color}_up_1.png')
                        self.flag_anim = 1
                    else:
                        if self.direction[0] > 0:
                            self.image = pg.image.load(f'img/{self.color}_right_2.png')
                        if self.direction[0] < 0:
                            self.image = pg.image.load(f'img/{self.color}_left_2.png')
                        if self.direction[1] > 0:
                            self.image = pg.image.load(f'img/{self.color}_down_2.png')
                        if self.direction[1] < 0:
                            self.image = pg.image.load(f'img/{self.color}_up_2.png')
                        self.flag_anim = 0
                else:
                    self.x += self.direction[0] * self.speed * TILE
                    self.y += self.direction[1] * self.speed * TILE
                    if not self.flag_anim:
                        if self.direction[0] > 0:
                            self.image = pg.image.load(f'img/{self.color}_right_1.png')
                        if self.direction[0] < 0:
                            self.image = pg.image.load(f'img/{self.color}_left_1.png')
                        if self.direction[1] > 0:
                            self.image = pg.image.load(f'img/{self.color}_down_1.png')
                        if self.direction[1] < 0:
                            self.image = pg.image.load(f'img/{self.color}_up_1.png')
                        self.flag_anim = 1
                    else:
                        if self.direction[0] > 0:
                            self.image = pg.image.load(f'img/{self.color}_right_2.png')
                        if self.direction[0] < 0:
                            self.image = pg.image.load(f'img/{self.color}_left_2.png')
                        if self.direction[1] > 0:
                            self.image = pg.image.load(f'img/{self.color}_down_2.png')
                        if self.direction[1] < 0:
                            self.image = pg.image.load(f'img/{self.color}_up_2.png')
                        self.flag_anim = 0

    def detect_collision(self, dx, dy):  # нахождения столкновений
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

    def found(self, path_arr, fin_point):  # волновой алгоритм поиска кратчайшего пути
        weight = 1
        for i in range(len(path_arr) * len(path_arr[0])):
            weight += 1
            for y in range(len(path_arr)):
                for x in range(len(path_arr[y])):
                    if path_arr[y][x] == (weight - 1):
                        if y > 0 and path_arr[y - 1][x] == 0:
                            path_arr[y - 1][x] = weight
                        if y < (len(path_arr) - 1) and path_arr[y + 1][x] == 0:
                            path_arr[y + 1][x] = weight
                        if x > 0 and path_arr[y][x - 1] == 0:
                            path_arr[y][x - 1] = weight
                        if x < (len(path_arr[y]) - 1) and path_arr[y][x + 1] == 0:
                            path_arr[y][x + 1] = weight

                        if (abs(y - fin_point[0]) + abs(x - fin_point[1])) == 1:
                            path_arr[fin_point[0]][fin_point[1]] = weight
                            return True
        return False

    def print_path(self, path_arr, fin_point):  # обработка информации из алгоритма поиска пути
        y = fin_point[0]
        x = fin_point[1]
        weight = path_arr[y][x]
        result = list(range(weight))
        while weight:
            weight -= 1
            if y > 0 and path_arr[y - 1][x] == weight:
                y -= 1
                result[weight] = (0, 1)
            elif y < (len(path_arr) - 1) and path_arr[y + 1][x] == weight:
                result[weight] = (0, -1)
                y += 1
            elif x > 0 and path_arr[y][x - 1] == weight:
                result[weight] = (1, 0)
                x -= 1
            elif x < (len(path_arr[y]) - 1) and path_arr[y][x + 1] == weight:
                result[weight] = (-1, 0)
                x += 1

        return result[1:]
