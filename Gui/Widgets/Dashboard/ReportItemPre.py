
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Widgets.Dashboard.ReportItemPreWidget import ReportItemPreWidget

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from State.Models.Content.Pre import Pre

from Log import log
from App import app


class ReportItemPre(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pre = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-item-pre')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.setStyleSheet(f'''
            QWidget#dashboard-report-item-pre {{
                padding: 0px;
                background-color: {Theme.DashboardReportItemPreBackgroundColor};
                border-radius: {Theme.DashboardReportItemPreBorderRadius}px;
                border-color: none;
                color: {Theme.DashboardReportItemPreColor};
            }}
        ''')

        self._widget = ReportItemPreWidget(self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self._layout.addWidget(self._widget)

        self.setLayout(self._layout)

    @property
    def pre(self):
        return self._pre
    
    @pre.setter
    def pre(self, pre: Pre | None):
        if pre == self._pre:
            return
        if pre is None:
            return
        self._pre = pre
        self._widget.value = pre.text
