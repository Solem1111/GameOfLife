from . import define
from .maptopo import areas


def rules_game_of_life(land):
    for index, value in land.items():
        if value.etat == "None" and value.neighbours_fertilizer(land) >= 3:
            if land[index].humidity:
                value.etat = "Vegetal"
            else:
                land[index].humidity = True


def concat_int(a, b):
    if type(a) != int or type(b) != int:
        return "Error a ou b ne sont pas des int"
    try:
        lenght_max_coordinate = len(str(define.TAILLEMAP-1))
    except:
        return "TAILLEMAP n'est pas transformable en string"
    try:
        c = str(a)
    except:
        return "a mal caster"
    try:
        d = str(b)
    except:
        return "b mal caster"
    lenght_a = len(c)
    lenght_b = len(d)
    for _ in range(lenght_max_coordinate-lenght_a):
        try:
            c = str(0)+c
        except:
            return "zéro mal ajouter à a"
    for _ in range(lenght_max_coordinate - lenght_b):
        try:
            d = str(0) + d
        except:
            return "zéro mal ajouter à b"
    try:
        return c+d
    except:
        return "probème de cast"


def deconcat_int(a):
    try:
        lenght_max_coordinate = len(str(define.TAILLEMAP - 1))
    except:
        return "TAILLEMAP n'est pas transformable en string"
    return int(a[:lenght_max_coordinate]), int(a[lenght_max_coordinate:])


def nearest_lower_multiple(number_to_flank, multiple):
    for i in range(0, multiple+1):
        if (number_to_flank - i) % multiple == 0:
            return number_to_flank - i


def nearest_higher_multiple(number_to_flank, multiple):
    for i in range(1, multiple+1):
        if (number_to_flank + i) % multiple == 0:
            return number_to_flank + i


def first_seed(land):
    for i in range(0, define.TAILLEMAP//define.TAILLEAREA):
        for j in range(0, define.TAILLEMAP // define.TAILLEAREA):
            areas.lake(land, i*define.TAILLEAREA, j*define.TAILLEAREA)
