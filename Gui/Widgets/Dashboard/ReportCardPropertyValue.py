
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportCardPropertyValue(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-card-property-value')

        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        font = Font(Themes.CurrentTheme.DashboardReportCardPropertyValueFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportCardPropertyValueFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportCardPropertyValueFontWeight)
        self.setFont(font)

        self.adjustHeight()
        self.restyleUI()
    
    # Without this method after word-wrapping QLabel will hide last content rows
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
    def value(self):
        return self.text()
    
    @value.setter
    def value(self, value: str):
        self.setText(value)
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportCardPropertyValueColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
