
import bs4
import re

from State.Models.Content.Content import Content
from State.Models.Content.File import File
from State.Models.Content.Img import Img
from State.Models.Content.P import P
from State.Models.Content.Pre import Pre


class ContentParser:
    @classmethod
    def parse(cls, content: bs4.Tag) -> Content:
        ws = re.compile(r'\s+')

        items = []
        for child in content.children:
            if not isinstance(child, bs4.Tag):
                continue

            if child.name == 'p':
                text = str(child.text).strip()
                text = re.sub(ws, ' ', text)
                items.append(P(text))
                continue

            if child.name == 'pre':
                text = str(child.text).strip()
                items.append(Pre(text))
                continue

            if child.name == 'img':
                name = str(child.text).strip()
                src = child.attrs.get('src', None)
                if src is None:
                    continue
                items.append(Img(src, name))
                continue
            
            if child.name == 'file':
                name = str(child.text).strip()
                src = child.attrs.get('src', None)
                if src is None:
                    continue
                items.append(File(src, name))
                continue
        return Content(items)
