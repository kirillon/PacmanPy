import pygame

from map import wall_map, point_map, door_map
from settings import *
from ghost import ghost_sprites


class Player(pygame.sprite.Sprite):  # класс игрока
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.flag_rect = 1
        self.image = pygame.image.load('img/circle.png')
        self.image = pygame.transform.scale(self.image, (TILE, TILE))
        self.x, self.y = 13.5 * TILE, 26 * TILE
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.center = 13.5 * TILE, 26 * TILE
        self.rectlist = [r.rect for r in wall_map]
        self.point_list = None
        self.direction = -(TILE * self.speed), 0
        self.next_direction = None
        self.side = TILE
        self.score = 0
        self.flag_music = 0
        self.sound_munch_1 = pygame.mixer.Sound("sound/munch_1.wav")
        self.sound_munch_2 = pygame.mixer.Sound("sound/munch_2.wav")
        self.flag_anim = 0

    def movement(self):

        self.keys_control()
        self.check_direction()
        self.rect.center = self.x, self.y
        self.collision_point()

    def check_direction(self):  # проверка направления
        if self.next_direction is not None:
            if self.detect_collision(self.next_direction[0], self.next_direction[1]):
                self.direction = self.next_direction
                self.next_direction = None

        if self.detect_collision(self.direction[0], self.direction[1]):
            self.x += self.direction[0]
            self.y += self.direction[1]
            if not self.flag_anim:
                if self.direction[0] > 0:
                    self.image = pygame.image.load('img/right_us.png')
                if self.direction[0] < 0:
                    self.image = pygame.image.load('img/left_us.png')
                if self.direction[1] > 0:
                    self.image = pygame.image.load('img/down_us.png')
                if self.direction[1] < 0:
                    self.image = pygame.image.load('img/up_us.png')
                self.flag_anim = 1
            elif self.flag_anim == 1:
                if self.direction[0] > 0:
                    self.image = pygame.image.load('img/right_eat.png')
                if self.direction[0] < 0:
                    self.image = pygame.image.load('img/left_eat.png')
                if self.direction[1] > 0:
                    self.image = pygame.image.load('img/down_eat.png')
                if self.direction[1] < 0:
                    self.image = pygame.image.load('img/up_eat.png')
                self.flag_anim = 2
            else:
                self.image = pygame.image.load('img/circle.png')
                self.flag_anim = 0

        if self.x < 0:
            self.x = 600
        if self.x > 600:
            self.x = 0

    def detect_collision(self, dx, dy):  # проверка на столкновения со стенами
        if self.flag_rect:
            self.rectlist = [r.rect for r in wall_map]
            self.rectlist += [r.rect for r in door_map]
            self.flag_rect = 0
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
        player_pos[0], player_pos[1] = self.x, self.y
        if dx == 0 and dy == 0:
            return False
        else:
            return True

    def keys_control(self):  # проверка на нажатие клавиш движения

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            dy = -(TILE * self.speed)
            self.next_direction = 0, dy

        if keys[pygame.K_s]:
            dy = TILE * self.speed
            self.next_direction = 0, dy
            player_pos[1] += dy
        if keys[pygame.K_a]:
            dx = -(TILE * self.speed)
            self.next_direction = dx, 0
        if keys[pygame.K_d]:
            dx = TILE * self.speed
            self.next_direction = dx, 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def collision_point(self):  # проверка на столкновение с точками

        self.point_list = [r.rect for r in point_map]
        hit_indexes = pygame.sprite.spritecollide(self, point_map, False)

        if len(hit_indexes):

            for hit_index in hit_indexes:
                point_map.remove(hit_index)
                self.score += 10
                if not pygame.mixer.get_busy():

                    if self.flag_music == 0:

                        self.sound_munch_1.play()
                        self.flag_music = 1
                    else:

                        self.sound_munch_2.play()
                        self.flag_music = 0

    def check_die(self):  # проверка на смерть
        ghostlist = [g.rect for g in ghost_sprites]
        next_rect = self.rect.copy()
        hit_indexes = next_rect.collidelistall(ghostlist)

        if len(hit_indexes):
            return True
