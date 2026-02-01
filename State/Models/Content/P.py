
class P:
    def __init__(self, text: str):
        self._text = text
    
    @property
    def text(self):
        return self._text
    
    def __str__(self):
        return f'{self.__class__.__name__}(text="{self._text}")'
