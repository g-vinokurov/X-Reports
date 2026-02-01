
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportCardId(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-card-id')

        self.setContentsMargins(0, 0, 0, 4)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        font = Font(Themes.CurrentTheme.DashboardReportCardIdFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportCardIdFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportCardIdFontWeight)
        self.setFont(font)
        
        self.adjustHeight()
        self.restyleUI()
    
    # If word-wrap is True, QLabel does not resize automatically and hide parts of text
    def adjustHeight(self):
        font_metrics = self.fontMetrics()
        width = self.width()
        text = self.text()
        text_rect = font_metrics.boundingRect(0, 0, width, 0, Qt.TextFlag.TextWordWrap, text)
        required_height = text_rect.height()
        self.setMinimumHeight(required_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustHeight()
    
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
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportCardIdColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        if not recursive:
            return
