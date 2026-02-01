
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportWidgetPropertyEmoji(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget-property-emoji')
        
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        font = Font(Themes.CurrentTheme.DashboardReportWidgetPropertyEmojiFont)
        font.setPointSize(Themes.CurrentTheme.DashboardReportWidgetPropertyEmojiFontSize)
        font.setHintingPreference(Font.HintingPreference.PreferNoHinting)
        self.setFont(font)

        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        pass
