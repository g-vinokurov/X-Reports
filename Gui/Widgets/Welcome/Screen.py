
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter

from PyQt5.QtCore import Qt

from Gui.Widgets.Screen import Screen

from Gui.Widgets.Welcome.Header import Header
from Gui.Widgets.Welcome.Body import Body
from Gui.Widgets.Welcome.Footer import Footer

from Gui.Images import IMG_WELCOME

from Log import log
from App import app


class WelcomeScreen(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('welcome-screen')
        
        self._background = QPixmap(IMG_WELCOME)

        self._header = Header(self)
        self._body = Body(self)
        self._footer = Footer(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._header)
        self._layout.addWidget(self._body)
        self._layout.addWidget(self._footer)
        
        self.setLayout(self._layout)

        app.gui.setWindowTitle('The X-Files')
    
    def paintEvent(self, event):
        screen_size = self.size()
        screen_width = screen_size.width()
        screen_height = screen_size.height()
        screen_ratio = screen_width / screen_height

        image_width = self._background.width()
        image_height = self._background.height()
        image_ratio = image_width / image_height

        painter = QPainter(self)

        if image_ratio > screen_ratio:
            w = int(screen_height * image_ratio)
            h = screen_height
            x = (w - screen_width) // -2
            y = 0
        else:
            w = screen_width
            h = int(screen_width / image_ratio)
            x = 0
            y = (h - screen_height) // -2
        painter.drawPixmap(x, y, w, h, self._background)
    
    @property
    def header(self):
        return self._header
    
    @property
    def body(self):
        return self._body
    
    @property
    def footer(self):
        return self._footer
    
    def restyleUI(self, recursive: bool = False):
        pass
