
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from State.Utils.ProjectLoader import ProjectLoader

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReloadProject(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reload-project')

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Themes.CurrentTheme.DashboardReloadProjectFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReloadProjectFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReloadProjectFontWeight)
        self.setFont(font)

        self.clicked.connect(self._on_clicked)
        self.restyleUI()
    
    def _on_clicked(self):
        try:
            app.state.project = ProjectLoader.load(app.state.project.dir)
        except Exception as err:
            log.debug(f'{err}', exc_info=True)
            log.error('Could not reload project')
            return
        app.gui.navigator.load('dashboard')
        app.gui.navigator.goto('dashboard')
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QPushButton#dashboard-reload-project {{
                color: {Themes.CurrentTheme.DashboardReloadProjectColor};
                background: {Themes.CurrentTheme.DashboardReloadProjectBackgroundColor};
                border: 1px solid {Themes.CurrentTheme.DashboardReloadProjectBorderColor};
                outline: none;
                padding-left: 32px;
                padding-top: 4px;
                padding-right: 32px;
                padding-bottom: 4px;
            }}

            QPushButton#dashboard-reload-project:hover {{
                color: {Themes.CurrentTheme.DashboardReloadProjectHoverColor};
                background: {Themes.CurrentTheme.DashboardReloadProjectHoverBackgroundColor};
            }}
        ''')
        if not recursive:
            return
