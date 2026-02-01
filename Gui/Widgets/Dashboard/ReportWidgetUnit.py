
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtCore import Qt

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class ReportWidgetUnit(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget-unit')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-report-widget-unit {{
                background: transparent;
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.setLayout(self._layout)

    def add(self, widget: QWidget):
        self._layout.addWidget(widget)
    
    @property
    def layout(self):
        return self._layout
