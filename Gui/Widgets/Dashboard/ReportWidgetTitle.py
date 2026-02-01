
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportWidgetTitle(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report = None
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-widget-title')

        self.setStyleSheet(f'''
            color: {Theme.DashboardReportWidgetTitleColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        font = Font(Theme.DashboardReportWidgetTitleFont)
        font.setPointSize(Theme.DashboardReportWidgetTitleFontSize)
        font.setWeight(Theme.DashboardReportWidgetTitleFontWeight)
        self.setFont(font)
    
    @property
    def report(self):
        return self._report
    
    @report.setter
    def report(self, report: Report | None):
        if report == self._report:
            return
        if report is None:
            return 
        self._report = report

        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.id}'
        self.setText(text)
