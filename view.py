import pygame
from colour import Color

from models.rules import deconcat_int
from models import define


def afficher_pixel(screen, land, size_map_buffer_x, size_map_buffer_y):
    color_river_lowest = Color(rgb=(14/255, 93/255, 171/255))
    color_river_highest = Color(rgb=(85/255, 170/255, 255/255))
    colors_river = list(color_river_lowest.range_to(color_river_highest, len(define.ALTITUDE)))
    color_vegetal_lowest = Color(rgb=(15/255, 160/255, 65/255))
    color_vegetal_highest = Color(rgb=(71/255, 255/255, 135/255))
    colors_vegetal = list(color_vegetal_lowest.range_to(color_vegetal_highest, len(define.ALTITUDE)))
    color_none_lowest = Color(rgb=(0, 0, 0))
    color_none_highest = Color(rgb=(255/255, 255/255, 255/255))
    colors_none = list(color_none_lowest.range_to(color_none_highest, len(define.ALTITUDE)))
    etat_key = {"None": colors_none, "River": colors_river, "Vegetal": colors_vegetal}
    for key in land.keys():
        i, j = deconcat_int(key)
        create_rect(i, j, size_map_buffer_x, size_map_buffer_y, screen, etat_key[land[key].etat], land[key].topology)


def create_rect(i, j, size_map_buffer_x, size_map_buffer_y, screen, color, topology):
    red = int(color[topology].red*255)
    green = int(color[topology].green*255)
    blue = int(color[topology].blue*255)
    pygame.draw.rect(screen, (red, green, blue),
                     pygame.Rect(i * size_map_buffer_x, j * size_map_buffer_y, size_map_buffer_x,
                                 size_map_buffer_y))
