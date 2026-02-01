
class File:
    def __init__(self, src: str, name: str):
        self._src = src
        self._name = name
    
    @property
    def src(self):
        return self._src
    
    @property
    def name(self):
        return self._name
    
    def __str__(self):
        return f'{self.__class__.__name__}(src="{self._src}",name="{self._name}")'
