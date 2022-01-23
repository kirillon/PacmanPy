import sys
from player import Player
from map import build_map
from map import wall_map, point_map,door_map
import pygame
from settings import *
from drawing import Drawing
from ghost import Ghost, ghost_spites

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
died = 0

gameflag = 1

# sprites = Sprites()

player = Player()
ghost_r = Ghost()
drawing = Drawing(sc, clock, player)
ghost_spites.add(ghost_r)
all_sprites.add(player)

# interaction = Interaction(player, sprites, drawing)

drawing.menu()
pygame.mouse.set_visible(False)
# interaction.play_music()
pygame.mixer.music.load("sound/pacman_beginning.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
sc = pygame.display.set_mode((610, HEIGHT), pygame.RESIZABLE)
build_map()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    if not gameflag:
        sc.fill(BLACK)
        wall_map.draw(sc)
        point_map.draw(sc)
        door_map.draw(sc)

        drawing.score_viewer()
        if drawing.check_win():
            drawing.win()
        elif player.check_die() and not died:
            sc.fill(BLACK)
            wall_map.draw(sc)
            point_map.draw(sc)
            door_map.draw(sc)

            all_sprites.draw(sc)
            drawing.score_viewer()
            pygame.display.flip()
            pygame.time.delay(1000)

            pygame.mixer.music.load("sound/pacman_death.wav")
            pygame.mixer.music.play()
            died = 1
            for i in range(11):
                sc.fill(BLACK)
                wall_map.draw(sc)
                point_map.draw(sc)
                door_map.draw(sc)
                drawing.score_viewer()
                pygame.display.flip()
                player.image = pygame.image.load(f"img/die{i}.png")
                all_sprites.update()
                all_sprites.draw(sc)
                pygame.display.flip()
                pygame.time.delay(150)
                clock.tick(FPS)
        if died:
            sc.fill(BLACK)
            wall_map.draw(sc)
            point_map.draw(sc)
            door_map.draw(sc)
            drawing.game_over()
            drawing.score_viewer()
            pygame.display.flip()

        else:

            player.movement()
            ghost_r.movement()
            ghost_spites.update()
            ghost_spites.draw(sc)
            all_sprites.update()
            all_sprites.draw(sc)
            pygame.display.flip()
        clock.tick(FPS)

    else:
        sc.fill(BLACK)
        wall_map.draw(sc)
        door_map.draw(sc)
        point_map.draw(sc)
        drawing.score_viewer()
        all_sprites.update()
        drawing.ready()
        ghost_spites.update()
        ghost_spites.draw(sc)
        pygame.display.flip()

        pygame.time.delay(2000)

        all_sprites.update()

        all_sprites.draw(sc)
        pygame.display.flip()
        pygame.time.delay(2000)
        gameflag = 0
