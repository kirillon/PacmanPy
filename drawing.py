import sys

import pygame

from settings import *


class Drawing:
    def __init__(self, sc, clock):
        self.sc = sc
        self.logo = pygame.image.load(' img/logo.png').convert_alpha()
        self.menu_trigger = True
        self.clock = clock
        self.mouse_trigger = False

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
                                    [(HALF_WIDTH - 250, HALF_HEIGHT+130), (HALF_WIDTH - 250, HALF_HEIGHT + 210),
                                     (HALF_WIDTH - 200, HALF_HEIGHT + 170)])
            pygame.draw.rect(self.sc, BLACK, button_start)
            pygame.draw.rect(self.sc, BLACK, button_ext)

            self.sc.blit(self.logo, (0.09 * WIDTH, 0.1 * HEIGHT), )

            self.sc.blit(start, (HALF_WIDTH - 170, HALF_HEIGHT))
            self.sc.blit(ext, (HALF_WIDTH - 115, HALF_HEIGHT + 130))

            pygame.display.flip()
            self.clock.tick(20)
