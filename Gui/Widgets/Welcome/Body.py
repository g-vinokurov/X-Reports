
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Welcome.Logo import Logo
from Gui.Widgets.Welcome.OpenProject import OpenProject

from Log import log
from App import app


class Body(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('welcome-body')

        self._logo = Logo(self)
        self._open_project = OpenProject(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout.addWidget(self._logo)
        self._layout.addWidget(self._open_project)

        self.setLayout(self._layout)
    
    @property
    def logo(self):
        return self._logo
    
    @property
    def open_project(self):
        return self._open_project
