
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.NoReportsFoundWidget import NoReportsFoundWidget
from Gui.Widgets.Dashboard.ReportsListContainer import ReportsListContainer
from Gui.Widgets.Scrolls import Scroll

from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportsListSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-section')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-section {{
                background-color: {Theme.DashboardReportsListSectionBackgroundColor};
                outline: none;
                border: none;
                padding: 0px;
            }}
        ''')

        self._no_reports_found = NoReportsFoundWidget(self)
        self._reports_list_container = ReportsListContainer(self)
        self._reports_list_container.hide()

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        self._layout.addWidget(self._no_reports_found)
        self._layout.addWidget(self._reports_list_container)

        self.setLayout(self._layout)
        
        self.reports = app.state.project.reports
    
    @property
    def reports(self):
        return self._reports_list_container.reports
    
    @reports.setter
    def reports(self, reports: list[Report]):
        if not reports:
            self._reports_list_container.hide()
            self._no_reports_found.show()
        else:
            self._reports_list_container.show()
            self._no_reports_found.hide()
        self._reports_list_container.reports = reports
    
    @property
    def reports_list(self):
        return self._reports_list_container.reports_list
