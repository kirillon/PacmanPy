import sys
from player import Player
from map import map
from map import wall_map
import pygame
from settings import *
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()



#sprites = Sprites()
drawing = Drawing(sc, clock)
player = Player()
all_sprites.add(player)


# interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
# interaction.play_music()
pygame.mixer.music.load("sound/pacman_beginning.wav")
pygame.mixer.music.play()
map()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    sc.fill(BLACK)
    wall_map.draw(sc)
    all_sprites.update()
    all_sprites.draw(sc)
    player.movement()
    print(player.x)
    # drawing.background()

    pygame.display.flip()
    clock.tick(FPS)
