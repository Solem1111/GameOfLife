import random

from ..rules import concat_int, deconcat_int


class River:
    def __init__(self, source_x=-1, source_y=-1):
        self._sourceX = source_x
        self._sourceY = source_y

    # method
    def build_river(self, land, x=None, y=None):
        x = self._sourceX if x is None else x
        y = self._sourceY if y is None else y
        choice_next = [neighbour
                       for neighbour in land[concat_int(x, y)].inondable_neighbours(land)]
        if choice_next:
            choosen = random.choice(choice_next)
            land[choosen].etat = "River"
            self.build_river(land, deconcat_int(choosen)[0], deconcat_int(choosen)[1])

    # ? getter
    def _get_source_x(self):
        try:
            return self._sourceX
        except:
            print("Valeur de source_x mal retourner")

    def _get_source_y(self):
        try:
            return self._sourceY
        except:
            print("Valeur de source_y mal retourner")

    def _get_direction(self):
        try:
            return self._direction
        except:
            print("Valeur de direction mal retourner")

    # ? setter
    def _set_source_x(self, value):
        try:
            self._sourceX = value
        except:
            print("Valeur de source_x mal attribuer")

    def _set_source_y(self, value):
        try:
            self._sourceY = value
        except:
            print("Valeur de source_y mal attribuer")

    def _set_direction(self, value):
        try:
            self._direction = value
        except:
            print("Valeur de direction mal attribuer")

    # ?deleter
    def _del_source_x(self):
        try:
            del self._sourceX
        except:
            print("Variable source_x mal supprimer")

    def _del_source_y(self):
        try:
            del self._sourceY
        except:
            print("Variable source_y mal supprimer")

    def _del_direction(self):
        try:
            del self._direction
        except:
            print("Variable direction mal supprimer")

    source_x = property(_get_source_x, _set_source_x, _del_source_x, "Position de la source de la rivière en X")
    source_y = property(_get_source_y, _set_source_y, _del_source_y, "Position de la source de la rivière en Y")
    direction = property(_get_direction, _set_direction, _del_direction,
                         "Directino de la rivière : 0 haut/1 droite/2 bas/3 gauche")
