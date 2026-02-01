
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportWidgetPropertyName(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget-property-name')
        
        self.setContentsMargins(0, 0, 8, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        font = Font(Themes.CurrentTheme.DashboardReportWidgetPropertyNameFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportWidgetPropertyNameFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportWidgetPropertyNameFontWeight)
        self.setFont(font)

        self.restyleUI()

    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportWidgetPropertyNameColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
    
    @property
    def value(self):
        return self.text()
    
    @value.setter
    def value(self, value: str):
        self.setText(value)
