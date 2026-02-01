
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.NoReportsFound import NoReportsFound

import Gui.Themes as Themes

from Log import log
from App import app


class NoReportsFoundWidget(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-no-reports-found-widget')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._no_reports_found = NoReportsFound(self)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(64, 64, 64, 64)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout.addWidget(self._no_reports_found)

        self.setLayout(self._layout)
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-no-reports-found-widget {{
                background: transparent;
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._no_reports_found.restyleUI(recursive)
