
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportsListNewReport(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-new-report')

        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Themes.CurrentTheme.DashboardReportsListNewReportFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportsListNewReportFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportsListNewReportFontWeight)
        self.setFont(font)
        
        self.setText('+')
        self.clicked.connect(self._on_clicked)
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QPushButton#dashboard-reports-list-new-report {{
                color: {Themes.CurrentTheme.DashboardReportsListNewReportColor};
                background: {Themes.CurrentTheme.DashboardReportsListNewReportBackgroundColor};
                border: none;
                outline: none;
                padding-left: 20px;
                padding-right: 20px;
                padding-top: 4px;
                padding-bottom: 4px;
            }}

            QPushButton#dashboard-reports-list-new-report:hover {{
                color: {Themes.CurrentTheme.DashboardReportsListNewReportHoverColor};
                background: {Themes.CurrentTheme.DashboardReportsListNewReportHoverBackgroundColor};
            }}
        ''')
        if not recursive:
            return
    
    def _on_clicked(self):
        pass
