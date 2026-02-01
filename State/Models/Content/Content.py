
from State.Models.Content.File import File
from State.Models.Content.Img import Img
from State.Models.Content.P import P
from State.Models.Content.Pre import Pre


class Content:
    def __init__(self, items: list[File | Img | P | Pre] = []):
        self._items = tuple(items)
    
    @property
    def items(self):
        return self._items
    
    def __str__(self):
        return str(list(map(str, self._items)))
