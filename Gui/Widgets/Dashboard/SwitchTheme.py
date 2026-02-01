
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font

import Gui.Themes as Themes
from Gui.Themes import THEME_DARK, THEME_LIGHT
from Gui.Themes import set_theme

from Log import log
from App import app


class SwitchTheme(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-switch-theme')
        
        self.restyleUI()
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Themes.CurrentTheme.DashboardSwitchThemeFont)
        font.setPointSize(Themes.CurrentTheme.DashboardSwitchThemeFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardSwitchThemeFontWeight)
        self.setFont(font)
        
        self.clicked.connect(self._on_clicked)
    
    def _on_clicked(self):
        if Themes.CurrentTheme.NAME == THEME_DARK:
            set_theme(THEME_LIGHT)
        elif Themes.CurrentTheme.NAME == THEME_LIGHT:
            set_theme(THEME_DARK)
        else:
            pass
        app.gui.navigator.restyleAll()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QPushButton#dashboard-switch-theme {{
                color: {Themes.CurrentTheme.DashboardSwitchThemeColor};
                background: {Themes.CurrentTheme.DashboardSwitchThemeBackgroundColor};
                border: 1px solid {Themes.CurrentTheme.DashboardSwitchThemeBorderColor};
                outline: none;
                padding-left: 32px;
                padding-top: 4px;
                padding-right: 32px;
                padding-bottom: 4px;
            }}

            QPushButton#dashboard-switch-theme:hover {{
                color: {Themes.CurrentTheme.DashboardSwitchThemeHoverColor};
                background: {Themes.CurrentTheme.DashboardSwitchThemeHoverBackgroundColor};
            }}
        ''')
        if Themes.CurrentTheme.NAME == THEME_DARK:
            self.setText('Light Theme')
        if Themes.CurrentTheme.NAME == THEME_LIGHT:
            self.setText('Dark Theme')
