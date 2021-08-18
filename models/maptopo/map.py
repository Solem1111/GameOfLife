import random

from .cell import Cell
from ..rules import concat_int, deconcat_int
from .river import River


class MapCarre:
    def __init__(self, size_map=0):
        self._size_map = size_map
        self.map = {concat_int(i, j): Cell.create_cell("None", i, j) for i in range(size_map) for j in range(size_map)}
        self.max_altitude = max([self.map[cle].topology for cle in self.map.keys()])

    @classmethod
    def create_map(cls, size_map):
        return MapCarre(size_map)

    def create_river(self):
        mountains = [key for key in self.map.keys() if self.map[key].topology == self.max_altitude]
        key_source = random.choice(mountains)
        temporary_x, temporary_y = deconcat_int(key_source)
        return River(temporary_x, temporary_y)

    # getter
    def _getsize_map(self):
        try:
            return self._size_map
        except:
            print("Valeur d'état mal retourner")

    # setter
    def _setsize_map(self, value):
        try:
            self._size_map = value
        except:
            print("Valeur de état mal attribuer")

    # deleter
    def _delsize_map(self):
        try:
            del self._size_map
        except:
            print("Variable état mal supprimer")

    size_map = property(_getsize_map, _setsize_map, _delsize_map, "size_map de la map")
