import time
import sys

import pygame

from models.maptopo import map
from models.rules import rules_game_of_life, first_seed
from models import define
from view import afficher_pixel

pygame.init()
pygame.display.set_caption("Jeu de la vie 2.0")
screen = pygame.display.set_mode((define.TAILLEMAP*define.RESOLUTION, define.TAILLEMAP*define.RESOLUTION))
mapActuelle = map.MapCarre.create_map(size_map=define.TAILLEMAP)
# riviereActuelle = mapActuelle.create_river()
# riviereActuelle.build_river(mapActuelle.map)
first_seed(mapActuelle.map)
screen.fill((0, 0, 0))
afficher_pixel(screen, mapActuelle.map, define.RESOLUTION, define.RESOLUTION)
running = True
while running:
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    rules_game_of_life(mapActuelle.map)
    afficher_pixel(screen, mapActuelle.map, define.RESOLUTION, define.RESOLUTION)
    pygame.display.flip()
    time.sleep(1)
