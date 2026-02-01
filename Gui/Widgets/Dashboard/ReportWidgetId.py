
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportWidgetId(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget-id')

        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        font = Font(Themes.CurrentTheme.DashboardReportWidgetIdFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportWidgetIdFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportWidgetIdFontWeight)
        self.setFont(font)

        self.restyleUI()

    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportWidgetIdColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
    
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
        text = f'{report.id}'
        self.setText(text)
