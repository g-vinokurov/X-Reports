
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Log import log
from App import app


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('welcome-header')
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)
