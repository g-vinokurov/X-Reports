
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportCardTitle(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._report = None
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-card-title')

        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        font = Font(Themes.CurrentTheme.DashboardReportCardTitleFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportCardTitleFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportCardTitleFontWeight)
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

        if report.provider is not None and report.provider.name:
            text = f'{report.provider.name}. '
        else:
            text = ''
        if report.name:
            text = text + f'{report.name}'
        else:
            text = f'{report.id}'
        self.setText(text)
     
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportCardTitleColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
