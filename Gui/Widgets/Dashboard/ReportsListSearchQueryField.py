
from PyQt5.QtWidgets import QLineEdit

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportsListSearchQueryField(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-search-query-field')

        font = Font(Themes.CurrentTheme.DashboardReportsListSearchQueryFieldFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportsListSearchQueryFieldFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportsListSearchQueryFieldFontWeight)
        self.setFont(font)

        self.setPlaceholderText('Query...')
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-search-query-field {{
                background: {Themes.CurrentTheme.DashboardReportsListSearchQueryFieldBackgroundColor};
                color: {Themes.CurrentTheme.DashboardReportsListSearchQueryFieldColor};
                border: none;
                border-left: 1px solid {Themes.CurrentTheme.DashboardReportsListSearchQueryFieldBorderColor};
                border-bottom: 1px solid {Themes.CurrentTheme.DashboardReportsListSearchQueryFieldBorderColor};
                padding-left: 16px;
                padding-right: 16px;
                padding-top: 4px;
                padding-bottom: 4px;
            }}
        ''')
        if not recursive:
            return
