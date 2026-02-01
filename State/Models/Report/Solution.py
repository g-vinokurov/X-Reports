
from State.Models.Content.Content import Content


class Solution:
    def __init__(self, content: Content):
        self._content = content
    
    @property
    def content(self):
        return self._content
    
    def __str__(self):
        return str({'content': str(self._content)})
