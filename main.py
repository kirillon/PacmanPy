import pygame
from settings import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()

# sprites = Sprites()
# player = Player(sprites)
# drawing = Drawing(sc, sc_map, player, clock)
# interaction = Interaction(player, sprites, drawing)

# drawing.menu()
pygame.mouse.set_visible(False)
# interaction.play_music()

while True:
    # player.movement()
    # drawing.background()

    pygame.display.flip()
    clock.tick(FPS)
