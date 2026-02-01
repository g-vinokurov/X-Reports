
from PyQt5.QtWidgets import QSplitter

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class Splitter(QSplitter):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('splitter')
        self.setStyleSheet(f'''
            QSplitter#splitter::handle {{
                background-color: {Theme.SplitterBackgroundColor};
            }}
        ''')
