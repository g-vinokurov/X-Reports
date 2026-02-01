
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class ReportWidgetPropertyName(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget-property-name')
        
        self.setStyleSheet(f'''
            color: {Theme.DashboardReportWidgetPropertyNameColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setContentsMargins(0, 0, 8, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        font = Font(Theme.DashboardReportWidgetPropertyNameFont)
        font.setPointSize(Theme.DashboardReportWidgetPropertyNameFontSize)
        font.setWeight(Theme.DashboardReportWidgetPropertyNameFontWeight)
        self.setFont(font)
    
    @property
    def value(self):
        return self.text()
    
    @value.setter
    def value(self, value: str):
        self.setText(value)
