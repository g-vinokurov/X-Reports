
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.NoReportsFoundWidget import NoReportsFoundWidget
from Gui.Widgets.Dashboard.ReportsListContainer import ReportsListContainer
from Gui.Widgets.Dashboard.ReportsListTools import ReportsListTools
from Gui.Widgets.Scrolls import Scroll

import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportsListSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._reports = []
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-section')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self._tools = ReportsListTools(self)
        self._tools.search_query_field.returnPressed.connect(self._on_search)
        self._tools.search.clicked.connect(self._on_search)

        self._no_reports_found = NoReportsFoundWidget(self)
        self._reports_list_container = ReportsListContainer(self)
        self._reports_list_container.hide()

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        self._layout.addWidget(self._tools)
        self._layout.addWidget(self._no_reports_found, stretch=1)
        self._layout.addWidget(self._reports_list_container, stretch=1)

        self.setLayout(self._layout)
        
        self.reports = app.state.project.reports
        
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-section {{
                background-color: {Themes.CurrentTheme.DashboardReportsListSectionBackgroundColor};
                outline: none;
                border: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._tools.restyleUI(recursive)
        self._no_reports_found.restyleUI(recursive)
        self._reports_list_container.restyleUI(recursive)
    
    @property
    def reports(self):
        return self._reports[::]
    
    @reports.setter
    def reports(self, reports: list[Report]):
        if not reports:
            self._reports_list_container.hide()
            self._no_reports_found.show()
        else:
            self._reports_list_container.show()
            self._no_reports_found.hide()
        
        self._reports = sorted(reports, key=lambda r: r.id, reverse=True)

        self._reports_list_container.reports = self._reports
        return

    @property
    def reports_list(self):
        return self._reports_list_container.reports_list
    
    def _on_search(self):
        query = self._tools.search_query_field.text()
        log.debug(f'Search: {query}')
        result = app.state.project.search(query)
        self.reports = result
        pass
