import sys

import pygame
from pygame.sprite import Sprite
from wall import Wall
from settings import *
from player import Player
from map import point_map


class Drawing:
    def __init__(self, sc, clock, player):
        self.sc = sc
        self.logo = pygame.image.load(' img/logo.png').convert_alpha()
        self.menu_trigger = True
        self.clock = clock
        self.mouse_trigger = False
        self.wall_map = pygame.sprite.Group()
        self.player = player
        self.game_ov = 0
        self.w = 0

    def menu(self):
        button_font = pygame.font.Font('font/8bit.otf', 72)
        start = button_font.render('START', True, pygame.Color('WHITE'))
        ext = button_font.render('EXIT', True, pygame.Color('WHITE'))
        button_ext = pygame.Rect(0, 0, 250, 100)
        button_ext.center = HALF_WIDTH, HALF_HEIGHT + 155
        button_start = pygame.Rect(0, 0, 400, 100)
        button_start.center = HALF_WIDTH, HALF_HEIGHT + 50

        self.sc.fill(BLACK)

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            mouse_click = pygame.mouse.get_pressed(3)
            mouse_pos = pygame.mouse.get_pos()
            self.sc.fill(BLACK)
            if button_start.collidepoint(mouse_pos):
                if mouse_click[0]:

                    self.mouse_trigger = True
                else:
                    if self.mouse_trigger:
                        self.mouse_trigger = False
                        self.menu_trigger = False

                pygame.draw.polygon(self.sc, WHITE,
                                    [(HALF_WIDTH - 250, HALF_HEIGHT), (HALF_WIDTH - 250, HALF_HEIGHT + 80),
                                     (HALF_WIDTH - 200, HALF_HEIGHT + 40)])
            if button_ext.collidepoint(mouse_pos):
                if mouse_click[0]:

                    self.mouse_trigger = True
                else:
                    if self.mouse_trigger:
                        self.mouse_trigger = False
                        pygame.quit()
                        sys.exit()

                pygame.draw.polygon(self.sc, WHITE,
                                    [(HALF_WIDTH - 250, HALF_HEIGHT + 130), (HALF_WIDTH - 250, HALF_HEIGHT + 210),
                                     (HALF_WIDTH - 200, HALF_HEIGHT + 170)])
            pygame.draw.rect(self.sc, BLACK, button_start)
            pygame.draw.rect(self.sc, BLACK, button_ext)

            self.sc.blit(self.logo, (0.09 * WIDTH, 0.1 * HEIGHT), )

            self.sc.blit(start, (HALF_WIDTH - 170, HALF_HEIGHT))
            self.sc.blit(ext, (HALF_WIDTH - 115, HALF_HEIGHT + 130))
            file_db = open('database.txt', 'r')
            score_font = pygame.font.Font('font/8bit.otf', 36)
            score = score_font.render(f"HIGH SCORE   {file_db.read()}", True, pygame.Color('WHITE'))
            file_db.close()
            self.sc.blit(score, (120, 10))

            pygame.display.flip()
            self.clock.tick(20)

    def ready(self):
        ready_font = pygame.font.Font('font/8bit.otf', 36)
        ready = ready_font.render("READY", True, pygame.Color('YELLOW'))
        self.sc.blit(ready, (610 // 3, 420))

    def score_viewer(self):
        score_font = pygame.font.Font('font/8bit.otf', 36)
        score = score_font.render(f'1 UP   {self.player.score}', True, pygame.Color('WHITE'))
        self.sc.blit(score, (10, 5))

    def check_win(self):

        if len(point_map) == 0:
            return True

    def win(self):
        win_font = pygame.font.Font('font/8bit.otf', 32)
        win = win_font.render("YOU ARE WIN", True, pygame.Color('YELLOW'))
        self.sc.blit(win, (610 // 4.3, 420))
        if not self.w:
            file_database = open('database.txt', 'r+')
            max_score = max(self.player.score, int(file_database.read()))
            file_database.close()
            file_database = open('database.txt', 'w')
            file_database.write(str(max_score))
            file_database.close()
            self.w = 1

    def game_over(self):
        win_font = pygame.font.Font('font/8bit.otf', 32)
        win = win_font.render("GAME OVER", True, pygame.Color('YELLOW'))
        self.sc.blit(win, (610 // 4.3, 420))
        if not self.game_ov:
            file_database = open('database.txt', 'r+')
            max_score = max(self.player.score, int(file_database.read()))
            file_database.close()
            file_database = open('database.txt', 'w')
            file_database.write(str(max_score))
            file_database.close()
            self.game_ov = 1
