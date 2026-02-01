
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportsListCurrentPage(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-current-page')

        font = Font(Themes.CurrentTheme.DashboardReportsListCurrentPageFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportsListCurrentPageFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportsListCurrentPageFontWeight)
        self.setFont(font)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setFixedWidth(self.minimumSizeHint().width())
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-current-page {{
                background: {Themes.CurrentTheme.DashboardReportsListCurrentPageBackgroundColor};
                color: {Themes.CurrentTheme.DashboardReportsListCurrentPageColor};
                border: none;
                border-left: 1px solid {Themes.CurrentTheme.DashboardReportsListCurrentPageBorderColor};
                border-bottom: 1px solid {Themes.CurrentTheme.DashboardReportsListCurrentPageBorderColor};
                padding-left: 4px;
                padding-right: 4px;
                padding-top: 4px;
                padding-bottom: 4px;
            }}
        ''')
        if not recursive:
            return
