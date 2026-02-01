
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportCardPropertyName(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-card-property-name')
        
        self.setContentsMargins(0, 0, 4, 0)
        self.setWordWrap(False)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        font = Font(Themes.CurrentTheme.DashboardReportCardPropertyNameFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportCardPropertyNameFontSize)
        font.setWeight(Themes.CurrentTheme.DashboardReportCardPropertyNameFontWeight)
        self.setFont(font)
        
        self.restyleUI()
    
    @property
    def value(self):
        return self.text()
    
    @value.setter
    def value(self, value: str):
        self.setText(value)
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            color: {Themes.CurrentTheme.DashboardReportCardPropertyNameColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
