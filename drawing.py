import sys

import pygame
from settings import *
from map import point_map


class Drawing:
    def __init__(self, sc, clock, player, ghost_r, ghost_b, ghost_p, ghost_o):
        self.sc = sc
        self.logo = pygame.image.load('img/logo.png').convert_alpha()
        self.menu_trigger = True
        self.clock = clock
        self.mouse_trigger = False
        self.wall_map = pygame.sprite.Group()
        self.player = player
        self.game_ov = 0
        self.w = 0
        self.ghost_r = ghost_r
        self.ghost_b = ghost_b
        self.ghost_p = ghost_p
        self.ghost_o = ghost_o
        self.difficult = "Normal"

    def menu(self):  # меню
        button_font = pygame.font.Font('font/8bit.otf', 72)
        start = button_font.render('START', True, pygame.Color('WHITE'))
        ext = button_font.render('EXIT', True, pygame.Color('WHITE'))
        button_ext = pygame.Rect(0, 0, 250, 100)
        button_ext.center = HALF_WIDTH, HALF_HEIGHT + 155
        button_start = pygame.Rect(0, 0, 400, 100)
        button_start.center = HALF_WIDTH, HALF_HEIGHT + 50
        dif_fort = pygame.font.Font('font/8bit.otf', 36)

        button_dif = pygame.Rect(0, 0, 230, 70)
        button_dif.center = HALF_WIDTH + 260, 10
        self.sc.fill(BLACK)
        dif_flag = 1

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
            if button_dif.collidepoint(mouse_pos):

                if mouse_click[0]:

                    self.mouse_trigger = True
                else:
                    if self.mouse_trigger:

                        self.mouse_trigger = False
                        if dif_flag == 1:
                            self.difficult = "UNREAL"
                            self.ghost_r.speed = 1 / 4
                            self.ghost_b.speed = 1 / 8
                            self.ghost_p.speed = 1 / 4
                            self.ghost_o.speed = 1 / 8
                            self.ghost_r.delay = 1000
                            self.ghost_b.delay = 7000
                            self.ghost_p.delay = 15000
                            self.ghost_o.delay = 25000

                            dif_flag = 2
                        elif dif_flag == 2:
                            self.difficult = "EASY"
                            dif_flag = 0
                            self.ghost_r.speed = 1 / 11
                            self.ghost_b.speed = 1 / 16
                            self.ghost_p.speed = 1 / 16
                            self.ghost_o.speed = 1 / 16
                            self.ghost_r.delay = 1000
                            self.ghost_b.delay = 5000
                            self.ghost_p.delay = 7000
                            self.ghost_o.delay = 9000
                        elif not dif_flag:
                            self.difficult = "NORMAL"
                            self.ghost_r.speed = 1 / 8
                            self.ghost_b.speed = 1 / 11
                            self.ghost_p.speed = 1 / 11
                            self.ghost_o.speed = 1 / 16
                            self.ghost_r.delay = 0
                            self.ghost_b.delay = 4000
                            self.ghost_p.delay = 6000
                            self.ghost_o.delay = 8000
                            dif_flag = 1
                pygame.draw.polygon(self.sc, WHITE,
                                    [(HALF_WIDTH + 100, 10), (HALF_WIDTH + 100, 50),
                                     (HALF_WIDTH + 130, 30)])

            dif = dif_fort.render(self.difficult, True, pygame.Color('WHITE'))
            pygame.draw.rect(self.sc, BLACK, button_start)
            pygame.draw.rect(self.sc, BLACK, button_ext)
            pygame.draw.rect(self.sc, BLACK, button_dif)

            self.sc.blit(self.logo, (0.09 * WIDTH, 0.1 * HEIGHT), )
            self.sc.blit(dif, (HALF_WIDTH + 150, 10))

            self.sc.blit(start, (HALF_WIDTH - 170, HALF_HEIGHT))
            self.sc.blit(ext, (HALF_WIDTH - 115, HALF_HEIGHT + 130))
            file_db = open('database.txt', 'r')
            score_font = pygame.font.Font('font/8bit.otf', 36)
            score = score_font.render(f"HIGH SCORE   {file_db.read()}", True, pygame.Color('WHITE'))
            file_db.close()
            self.sc.blit(score, (120, 10))

            pygame.display.flip()
            self.clock.tick(20)

    def ready(self):  # вывод надписи начала игры
        ready_font = pygame.font.Font('font/8bit.otf', 36)
        ready = ready_font.render("READY", True, pygame.Color('YELLOW'))
        self.sc.blit(ready, (610 // 3, 420))

    def score_viewer(self):  # вывод количества очков
        score_font = pygame.font.Font('font/8bit.otf', 36)
        score = score_font.render(f'1 UP   {self.player.score}', True, pygame.Color('WHITE'))
        self.sc.blit(score, (10, 5))

    def check_win(self):  # проверка на победу

        if len(point_map) == 0:
            return True

    def win(self):  # вывод  надписи победы
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

    def game_over(self):  # вывод  надписи проигрыша
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
