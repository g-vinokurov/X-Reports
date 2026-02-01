
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportsListPageControl(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-page-control')

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Themes.CurrentTheme.DashboardReportsListPageControlFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportsListPageControlFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportsListPageControlFontWeight)
        self.setFont(font)

        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QPushButton#dashboard-reports-list-page-control {{
                color: {Themes.CurrentTheme.DashboardReportsListPageControlColor};
                background: {Themes.CurrentTheme.DashboardReportsListPageControlBackgroundColor};
                border: none;
                border-left: 1px solid {Themes.CurrentTheme.DashboardReportsListPageControlBorderColor};
                outline: none;
                padding-left: 20px;
                padding-right: 20px;
                padding-top: 4px;
                padding-bottom: 4px;
            }}

            QPushButton#dashboard-reports-list-page-control:hover {{
                color: {Themes.CurrentTheme.DashboardReportsListPageControlHoverColor};
                background: {Themes.CurrentTheme.DashboardReportsListPageControlHoverBackgroundColor};
            }}
        ''')
        if not recursive:
            return
