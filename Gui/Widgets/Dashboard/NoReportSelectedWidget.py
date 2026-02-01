
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.NoReportSelected import NoReportSelected

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class NoReportSelectedWidget(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-no-report-selected-widget')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-no-report-selected-widget {{
                background: transparent;
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')

        self._no_report_selected = NoReportSelected(self)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(64, 64, 64, 64)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout.addWidget(self._no_report_selected)

        self.setLayout(self._layout)
