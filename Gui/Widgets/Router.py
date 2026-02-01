
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QGridLayout

from Gui.Widgets.Page import Page


class Router(QWidget):
    _mapper = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pages : dict[str, Page] = {}
        
        self.initUI()

    def initUI(self):
        self._current_page = Page(self)

        self._layout = QGridLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self._current_page)

        self.setLayout(self._layout)
    
    @property
    def page(self):
        return self._current_page

    def load(self, tag: str, *args, **kwargs):
        self._pages[tag] = self._mapper.get(tag, Page)(self, *args, **kwargs)
        self.updateUI(tag, *args, **kwargs)

    def updateUI(self, tag: str, *args, **kwargs):
        page : Page = self._pages.get(tag, Page(self))
        page.updateUI(*args, **kwargs)

    def goto(self, tag: str, *args, **kwargs):
        if tag not in self._pages:
            self.load(tag, *args, **kwargs)

        self._layout.removeWidget(self._current_page)
        self._current_page.hide()
        self._current_page : Page = self._pages[tag]
        self._current_page.show()
        self._layout.addWidget(self._current_page)

    @classmethod
    def register(cls, tag: str, page_cls: type[Page]):
        if tag in cls._mapper:
            return
        cls._mapper[tag] = page_cls
