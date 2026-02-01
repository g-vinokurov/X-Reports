
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font

import Gui.Themes as Themes

from Log import log
from App import app


class ReportWidgetSubtitle(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-widget-subtitle')

        self.setContentsMargins(0, 0, 0, 8)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        font = Font(Themes.CurrentTheme.DashboardReportWidgetSubtitleFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportWidgetSubtitleFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportWidgetSubtitleFontWeight)
        self.setFont(font)

        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportWidgetSubtitleColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
