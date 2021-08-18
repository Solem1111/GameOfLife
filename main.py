import time
import sys

import pygame

from Models.MapTopo.Map import MapCarre
from Models.Rules import RulesGameOfLife, first_seed
import Models.Define as Define
from view import afficher_pixel

pygame.init()
pygame.display.set_caption("Jeu de la vie 2.0")
screen = pygame.display.set_mode((Define.TAILLEMAP*Define.RESOLUTION, Define.TAILLEMAP*Define.RESOLUTION))
mapActuelle = MapCarre.create_map(size_map=Define.TAILLEMAP)
# riviereActuelle = mapActuelle.create_river()
# riviereActuelle.build_river(mapActuelle.map)
first_seed(mapActuelle.map)
screen.fill((0, 0, 0))
afficher_pixel(screen, mapActuelle.map, Define.TAILLEMAP, Define.RESOLUTION, Define.RESOLUTION)
running = True
while running:
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    RulesGameOfLife(mapActuelle.map)
    afficher_pixel(screen, mapActuelle.map, Define.TAILLEMAP, Define.RESOLUTION, Define.RESOLUTION)
    pygame.display.flip()
    time.sleep(1)

