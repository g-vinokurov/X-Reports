
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class ReportWidgetSubtitle(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-widget-subtitle')

        self.setStyleSheet(f'''
            color: {Theme.DashboardReportWidgetSubtitleColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        font = Font(Theme.DashboardReportWidgetSubtitleFont)
        font.setPointSize(Theme.DashboardReportWidgetSubtitleFontSize)
        font.setWeight(Theme.DashboardReportWidgetSubtitleFontWeight)
        self.setFont(font)
