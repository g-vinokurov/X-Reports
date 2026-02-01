
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
        self._reports_per_page = 1000
        self._pages = 1
        self._page = 1
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-section')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        # self._tools = ReportsListTools(self)
        # self._tools.search_query_field.returnPressed.connect(self._on_search)
        # self._tools.search.clicked.connect(self._on_search)
        # self._tools.curr_page.returnPressed.connect(self._on_curr_page_changed)
        # self._tools.prev_page.clicked.connect(self._on_prev_page_clicked)
        # self._tools.next_page.clicked.connect(self._on_next_page_clicked)

        self._no_reports_found = NoReportsFoundWidget(self)
        self._reports_list_container = ReportsListContainer(self)
        self._reports_list_container.hide()

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        # self._layout.addWidget(self._tools)
        self._layout.addWidget(self._no_reports_found, stretch=1)
        self._layout.addWidget(self._reports_list_container, stretch=1)

        self.setLayout(self._layout)
        
        self.reports = app.state.project.reports
        self.page = 0
        
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
        # self._tools.restyleUI(recursive)
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

        if len(reports) != 0:
            self._pages = (len(reports) - 1) // self._reports_per_page + 1
            self._page = 1
        else:
            self._pages = 0
            self._page = 0
        # self._tools.total_pages.pages = self._pages
        
        if not self._reports:
            self._reports_list_container.reports = []
        else:
            start = 0
            end = min(self._reports_per_page, len(self._reports))
            self._reports_list_container.reports = self._reports[start:end]
        return
    
    @property
    def page(self):
        return self._page
    
    @page.setter
    def page(self, page: int):
        if page < 0:
            page = 0
        if page > self._pages:
            page = self._pages
        if page == 0 and self._pages:
            page = 1
        self._page = page

        if not self._page:
            self._reports_list_container.reports = []
        else:
            start = (self._page - 1) * self._reports_per_page
            end = min(self._page * self._reports_per_page, len(self._reports))
            self._reports_list_container.reports = self._reports[start:end]
        # self._tools.curr_page.setText(str(self._page))
    
    @property
    def pages(self):
        return self._pages
    
    @property
    def reports_list(self):
        return self._reports_list_container.reports_list
    
    def _on_search(self):
        # query = self._tools.search_query_field.text()
        # log.debug(f'Search: {query}')
        # result = app.state.project.search(query)
        # self.reports = result
        pass
    
    def _on_curr_page_changed(self):
        # value = self._tools.curr_page.text().strip()
        # if not str(value).isdigit():
        #     return
        # log.debug(f'Set Current Page: {value}')
        # self.page = int(value)
        pass
    
    def _on_prev_page_clicked(self):
        log.debug(f'Previous Page')
        self.page = self.page - 1

    def _on_next_page_clicked(self):
        log.debug(f'Next Page')
        self.page = self.page + 1
