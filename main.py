import sys
from player import Player
from map import map
from map import wall_map,point_map
import pygame
from settings import *
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
gameflag = 1


#sprites = Sprites()

player = Player()
drawing = Drawing(sc, clock,player)
all_sprites.add(player)


# interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
# interaction.play_music()
pygame.mixer.music.load("sound/pacman_beginning.wav")
pygame.mixer.music.play()
sc = pygame.display.set_mode((610, HEIGHT),pygame.RESIZABLE)
map()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    if not gameflag:
        sc.fill(BLACK)
        wall_map.draw(sc)
        point_map.draw(sc)
        all_sprites.update()
        all_sprites.draw(sc)
        player.movement()
        print(player.x)
        # drawing.background()
        drawing.score_viewer()
        pygame.display.flip()
        clock.tick(FPS)

    else:
        sc.fill(BLACK)
        wall_map.draw(sc)
        point_map.draw(sc)
        drawing.score_viewer()
        all_sprites.update()
        drawing.ready()
        pygame.display.flip()
        pygame.time.delay(2000)

        all_sprites.update()

        all_sprites.draw(sc)
        pygame.display.flip()
        pygame.time.delay(2000)
        gameflag = 0





