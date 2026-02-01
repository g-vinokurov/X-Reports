
from PyQt5.QtWidgets import QSplitter

import Gui.Themes as Themes

from Log import log
from App import app


class Splitter(QSplitter):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('splitter')

        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QSplitter#splitter {{
                width: 1px;
            }}
            QSplitter#splitter::handle {{
                width: 1px;
                background-color: {Themes.CurrentTheme.SplitterBackgroundColor};
            }}
        ''')
