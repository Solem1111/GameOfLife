import random

import Models.Define as Define
from Models.Rules import ConcatInt, nearest_higher_multiple, nearest_lower_multiple


class Cell:
    def __init__(self, etat=None, topology=-3, x=-1, y=-1):
        self._etat = etat
        self.humidity = False
        self.topology = topology
        self.x = x
        self.y = y

    @classmethod
    def create_cell(cls, state, x, y):
        topology = -1
        return Cell(etat=state, topology=topology, x=x, y=y)

    @property
    def cells_in_same_area(self):
        lower_x = nearest_lower_multiple(self.x, Define.TAILLEAREA)
        lower_y = nearest_lower_multiple(self.y, Define.TAILLEAREA)
        higher_x = nearest_higher_multiple(self.x, Define.TAILLEAREA)
        higher_y = nearest_higher_multiple(self.y, Define.TAILLEAREA)
        return [ConcatInt(i, j)
                for i in range(lower_x, higher_x)
                for j in range(lower_x, higher_x)]

    @property
    def neighbours_keys(self):
        return [ConcatInt(self.x + i, self.y + j)
                for i in range(-1, 2)
                for j in range(-1, 2)
                if ((i, j) != (0, 0) and 0 <= self.x + i < Define.TAILLEMAP and 0 <= self.y + j < Define.TAILLEMAP)]

    def lowest_height_of_neighbours(self, land):
        return min([land[element].topology
                    for element in self.neighbours_keys] or -1)

    def inondable_neighbours(self, land):
        return [neighbour
                for neighbour in self.neighbours_keys
                if land[neighbour].etat != "River" and land[neighbour].topology == self.lowest_height_of_neighbours(land)]

    def Neighbours_fertilizer(self, land):
        i = 0
        for neighbour_key in self.neighbours_keys:
            if land[neighbour_key].etat == "River" or land[neighbour_key].etat == "Vegetal":
                i += 1
        return i
    # getter
    def _get_etat(self):
        try:
            return self._etat
        except:
            print("Valeur d'état mal retourner")

    # setter
    def _set_etat(self, value):
        try:
            self._etat = value
        except:
            print("Valeur de état mal attribuer")

    # deleter
    def _del_etat(self):
        try:
            del self._etat
        except:
            print("Variable état mal supprimer")

    etat = property(_get_etat, _set_etat, _del_etat,
                    "Etat du sol : 0 terre sérile/1 Terre fertile/2 terre humide/3 rivière")
