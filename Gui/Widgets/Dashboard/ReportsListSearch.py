
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportsListSearch(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-search')

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Themes.CurrentTheme.DashboardReportsListSearchFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportsListSearchFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportsListSearchFontWeight)
        self.setFont(font)
        
        self.setText('Search')
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QPushButton#dashboard-reports-list-search {{
                color: {Themes.CurrentTheme.DashboardReportsListSearchColor};
                background: {Themes.CurrentTheme.DashboardReportsListSearchBackgroundColor};
                border: none;
                border-left: 1px solid {Themes.CurrentTheme.DashboardReportsListSearchBorderColor};
                outline: none;
                padding-left: 16px;
                padding-right: 16px;
                padding-top: 4px;
                padding-bottom: 4px;
            }}

            QPushButton#dashboard-reports-list-search:hover {{
                color: {Themes.CurrentTheme.DashboardReportsListSearchHoverColor};
                background: {Themes.CurrentTheme.DashboardReportsListSearchHoverBackgroundColor};
            }}
        ''')
        if not recursive:
            return
