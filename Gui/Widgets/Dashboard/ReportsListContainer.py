
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReportsList import ReportsList
from Gui.Widgets.Scrolls import Scroll

from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportsListContainer(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-container')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-container {{
                background: transparent;
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')

        self._reports_list = ReportsList(self)
        
        # i can't set stylesheet to scroll when 'self' is set as parent
        self._scroll = Scroll(app.gui)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._reports_list)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
    
        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)
    
    @property
    def reports(self):
        return self._reports_list.reports
    
    @reports.setter
    def reports(self, reports: list[Report]):
        self._reports_list.reports = reports
    
    @property
    def reports_list(self):
        return self._reports_list
