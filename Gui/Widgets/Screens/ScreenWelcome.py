
import os
import traceback

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter

from PyQt5.QtCore import Qt

from Gui.Widgets.Screens.Screen import Screen

from Gui.Colors import COLOR_WHITE
from Gui.Colors import COLOR_BLACK
from Gui.Colors import COLOR_VSC_PRIMARY
from Gui.Colors import COLOR_BS_LIGHT

from Gui.Fonts import FONT_JET_BRAINS_MONO_NL_EXTRA_BOLD

from Gui.Images import IMG_WELCOME

from State.Utils.ProjectLoader import ProjectLoader

from Logger import log

from App import app


class Logo(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setStyleSheet(f'''
            padding-left: 0px;
            padding-right: 0px;
            padding-top: 0px;
            padding-bottom: 0px;
            color: {COLOR_BS_LIGHT};
        ''')
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_EXTRA_BOLD), 48))
    
    def updateUI(self, *args, **kwargs):
        self.setText('THE X-FILES')


class OpenProject(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(f'''
            background: none;
            border: none;
            outline: none;
            padding-top: 16px;
            color: {COLOR_BS_LIGHT};
        ''')
        self.setFont(QFont(str(FONT_JET_BRAINS_MONO_NL_EXTRA_BOLD), 18))

    def updateUI(self, *args, **kwargs):
        self.setText('Open Project')


class ScreenWelcome(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self._background = QPixmap(IMG_WELCOME)
        self._logo = Logo(self)
        self._btn_open_project = OpenProject(self)

        self._btn_open_project.clicked.connect(self.on_btn_open_project_clicked)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignCenter)

        self._layout.addWidget(self._logo)
        self._layout.addWidget(self._btn_open_project)
        
        self.setLayout(self._layout)

    def updateUI(self, *args, **kwargs):
        app.gui.setWindowTitle('The X-Files')
        self._logo.updateUI(*args, **kwargs)
        self._btn_open_project.updateUI(*args, **kwargs)
    
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
    
    def on_btn_open_project_clicked(self, event):
        __title = 'Open directory with reports'
        __path = os.getcwd()
        dir = str(QFileDialog.getExistingDirectory(self, __title, __path))
        if not dir:
            return
        log.info(f'Open Project: {dir}')

        try:
            app.state.project = ProjectLoader.load(dir)
        except Exception:
            log.error('Could not load project')
            log.debug(f'{traceback.format_exc()}')
            return
        
        log.debug('Go to Dashboard')
        app.gui.navigator.goto('dashboard')
