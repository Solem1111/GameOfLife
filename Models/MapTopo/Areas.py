import random

import Models.Rules as Rules
import Models.Define as Define


def nw(size_lake):
    x = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    y = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    return [x, y, 0, size_lake, 0, size_lake]


def ne(size_lake):
    x = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    y = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    return [Define.TAILLEAREA - 1 - x, y, -size_lake+1, 1, 0, size_lake]


def sw(size_lake):
    x = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    y = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    return [x, Define.TAILLEAREA - 1 - y,  0, size_lake, -size_lake+1, 1]


def se(size_lake):
    x = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    y = random.randint(0, Define.TAILLEAREA - 1 - size_lake) if 0 <= (Define.TAILLEAREA - 1 - size_lake) else 0
    return [Define.TAILLEAREA - 1 - x, Define.TAILLEAREA - 1 - y, -size_lake+1, 1, -size_lake+1, 1]


def up_slop_for_lake(land, lake_altitude, cell_up_left):
    i = 0
    altitude = lake_altitude + 1
    while altitude > lake_altitude:
        altitude = random.choice(Define.ALTITUDE)
    for value in cell_up_left.cells_in_same_area:
        for neighbour_key in land[value].neighbours_keys:
            if land[value].etat != "River" and land[neighbour_key].topology >= altitude \
                    and neighbour_key in cell_up_left.cells_in_same_area:
                land[value].topology = altitude
        if land[value].topology == -1:
            i += 1

    if i != 0:
        up_slop_for_lake(land, altitude, cell_up_left)


def down_slop_for_lake(land, lake_altitude, cell_up_left, first_call=True):
    i = 0
    if first_call:
        for value in cell_up_left.cells_in_same_area:
            if land[value].etat != "River":
                land[value].topology = max(Define.ALTITUDE)+1
    altitude = lake_altitude - 1
    while altitude < lake_altitude:
        altitude = random.choice(Define.ALTITUDE)
    for value in cell_up_left.cells_in_same_area:
        for neighbour_key in land[value].neighbours_keys:
            if land[value].etat != "River" and land[neighbour_key].topology <= altitude \
                    and neighbour_key in cell_up_left.cells_in_same_area:
                land[value].topology = altitude
        if land[value].topology == max(Define.ALTITUDE) + 1:
            i += 1
    if i != 0:
        down_slop_for_lake(land, altitude, cell_up_left, first_call=False)


# LAC
def lake(land, x_up_left, y_up_left):  # au sommet d'une montagne au au fond d'une cuvette
    size_lake = random.randint(2, Define.TAILLEAREA)
    position = random.choice(["north-east", "north-west", "south-east", "south-west"])
    cardinal_points = {"north-east": ne,
                       "north-west": nw,
                       "south-east": se,
                       "south-west": sw}

    coordinate_and_sroll = cardinal_points[position](size_lake)
    coordinate_x = coordinate_and_sroll[0]
    coordinate_y = coordinate_and_sroll[1]
    scroll_x_start = coordinate_and_sroll[2]
    scroll_x_end = coordinate_and_sroll[3]
    scroll_y_start = coordinate_and_sroll[4]
    scroll_y_end = coordinate_and_sroll[5]
    lake_altitude = random.choice(Define.ALTITUDE)
    for i in range(scroll_x_start, scroll_x_end):  # a modifier selon l'orientation
        for j in range(scroll_y_start, scroll_y_end):
            key = Rules.ConcatInt(x_up_left+coordinate_x+i, y_up_left+coordinate_y+j)
            land[key].etat = "River"
            land[key].topology = lake_altitude
    slop = random.choice(["up", "down"])
    if slop == "up":
        up_slop_for_lake(land, lake_altitude, land[Rules.ConcatInt(x_up_left, y_up_left)])
    elif slop == "down":
        down_slop_for_lake(land, lake_altitude, land[Rules.ConcatInt(x_up_left, y_up_left)])



