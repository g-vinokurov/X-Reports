
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Widgets.Dashboard.ReportsListSearch import ReportsListSearch
from Gui.Widgets.Dashboard.ReportsListSearchQueryField import ReportsListSearchQueryField

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

        self._search_query_field = ReportsListSearchQueryField(self)
        self._search = ReportsListSearch(self)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._search_query_field, stretch=1)
        self._layout.addWidget(self._search)

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
        self._search_query_field.restyleUI(recursive)
        self._search.restyleUI(recursive)

    @property
    def search_query_field(self):
        return self._search_query_field
    
    @property
    def search(self):
        return self._search
