
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Widgets.Dashboard.ReportsListCurrentPage import ReportsListCurrentPage
from Gui.Widgets.Dashboard.ReportsListNewReport import ReportsListNewReport
from Gui.Widgets.Dashboard.ReportsListPageControl import ReportsListPageControl
from Gui.Widgets.Dashboard.ReportsListPagesLabel import ReportsListPagesLabel
from Gui.Widgets.Dashboard.ReportsListSearch import ReportsListSearch
from Gui.Widgets.Dashboard.ReportsListSearchQueryField import ReportsListSearchQueryField
from Gui.Widgets.Dashboard.ReportsListTotalPages import ReportsListTotalPages
from Gui.Widgets.Dashboard.ReportsListOfPagesLabel import ReportsListOfPagesLabel

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportsListTools(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list-tools')

        self._new_report = ReportsListNewReport(self)
        self._search_query_field = ReportsListSearchQueryField(self)
        self._search = ReportsListSearch(self)
        self._pages = ReportsListPagesLabel(self)
        self._prev_page = ReportsListPageControl('<', self)
        self._curr_page = ReportsListCurrentPage(self)
        self._of = ReportsListOfPagesLabel(self)
        self._total_pages = ReportsListTotalPages(self)
        self._next_page = ReportsListPageControl('>', self)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self._layout.addWidget(self._new_report)
        self._layout.addWidget(self._search_query_field, stretch=1)
        self._layout.addWidget(self._search)

        self._pagination = QHBoxLayout()
        self._pagination.setContentsMargins(0, 0, 0, 0)
        self._pagination.setSpacing(0)
        self._pagination.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self._pagination.addWidget(self._pages)
        self._pagination.addWidget(self._prev_page)
        self._pagination.addWidget(self._curr_page)
        self._pagination.addWidget(self._of)
        self._pagination.addWidget(self._total_pages)
        self._pagination.addWidget(self._next_page)

        self._layout.addLayout(self._pagination)
        
        self.setLayout(self._layout)
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list-tools {{
                background: transparent;
                border: none;
                border-bottom: 1px solid {Themes.CurrentTheme.DashboardReportsListToolsBorderColor};
                outline: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._new_report.restyleUI(recursive)
        self._search_query_field.restyleUI(recursive)
        self._search.restyleUI(recursive)
        self._pages.restyleUI(recursive)
        self._prev_page.restyleUI(recursive)
        self._curr_page.restyleUI(recursive)
        self._of.restyleUI(recursive)
        self._total_pages.restyleUI(recursive)
        self._next_page.restyleUI(recursive)
    
    @property
    def new_report(self):
        return self._new_report
    
    @property
    def search_query_field(self):
        return self._search_query_field
    
    @property
    def search(self):
        return self._search
    
    @property
    def pages_label(self):
        return self._pages
    
    @property
    def prev_page(self):
        return self._prev_page
    
    @property
    def curr_page(self):
        return self._curr_page
    
    @property
    def total_pages(self):
        return self._total_pages
    
    @property
    def next_page(self):
        return self._next_page
