
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class ReportItemPreContent(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-item-pre-content')
        self.setStyleSheet(f'''
            QWidget#dashboard-report-item-pre-content {{
                padding: 16px;
                background: transparent;
                border: none;
                color: {Theme.DashboardReportItemPreColor};
            }}
        ''')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        font = Font(Theme.DashboardReportItemPreFont)
        font.setPointSize(Theme.DashboardReportItemPreFontSize)
        font.setWeight(Theme.DashboardReportItemPreFontWeight)
        self.setFont(font)
    
    @property
    def value(self):
        return self.text()
    
    @value.setter
    def value(self, value: str):
        self.setText(value)
