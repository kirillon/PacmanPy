import pygame

from settings import *


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.logo = pygame.image.load('img/logo.png').convert()

    def menu(self):
        x = 0
        pygame.mixer.music.load('sound/win.mp3')
        pygame.mixer.music.play()
        button_font = pygame.font.Font('font/font.ttf', 72)
        label_font = pygame.font.Font('font/font1.otf', 400)
        start = button_font.render('START', 1, pygame.Color('lightgray'))
        button_start = pygame.Rect(0, 0, 400, 150)
        button_start.center = HALF_WIDTH, HALF_HEIGHT
        exit = button_font.render('EXIT', 1, pygame.Color('lightgray'))
        button_exit = pygame.Rect(0, 0, 400, 150)
        button_exit.center = HALF_WIDTH, HALF_HEIGHT + 200

        while self.menu_trigger:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.sc.blit(self.menu_picture, (0, 0), (x % WIDTH, HALF_HEIGHT, WIDTH, HEIGHT))
            x += 1

            pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25, width=10)
            self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))

            pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25, width=10)
            self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))

            color = randrange(40)
            label = label_font.render('DOOMPy', 1, (color, color, color))
            self.sc.blit(label, (15, -30))

            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_start, border_radius=25)
                self.sc.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:
                    self.menu_trigger = False
            elif button_exit.collidepoint(mouse_pos):
                pygame.draw.rect(self.sc, BLACK, button_exit, border_radius=25)
                self.sc.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(20)
