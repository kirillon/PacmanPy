import sys

import pygame
from settings import *
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()
k = 1

# sprites = Sprites()
player = Player(sprites)
drawing = Drawing(sc, clock)
# interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
# interaction.play_music()
pygame.mixer.music.load("sound/pacman_beginning.wav")
pygame.mixer.music.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

            # player.movement()
    # drawing.background()

    pygame.display.flip()
    clock.tick(FPS)
