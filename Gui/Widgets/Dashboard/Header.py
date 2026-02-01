
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReloadProject import ReloadProject
from Gui.Widgets.Dashboard.SwitchTheme import SwitchTheme

import Gui.Themes as Themes

from Log import log
from App import app


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-header')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        # self._reload_project = ReloadProject('Reload Project', self)
        # self._switch_theme = SwitchTheme(self)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(32)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        # self._layout.addWidget(self._reload_project)
        # self._layout.addWidget(self._switch_theme)

        self.setLayout(self._layout)
        self.restyleUI()
    
    def _on_reload_project_clicked(self):
        pass
    
    def _on_switch_theme_clicked(self):
        pass
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-header {{
                background-color: {Themes.CurrentTheme.DashboardHeaderBackgroundColor};
                border-bottom: 1px solid {Themes.CurrentTheme.DashboardHeaderBorderColor};
                border-top: 1px solid {Themes.CurrentTheme.DashboardHeaderBorderColor};
                outline: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        # self._reload_project.restyleUI(recursive)
        # self._switch_theme.restyleUI(recursive)
