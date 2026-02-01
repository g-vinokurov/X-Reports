
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class ReportWidgetPropertyEmoji(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget-property-emoji')
        
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        font = Font(Theme.DashboardReportWidgetPropertyEmojiFont)
        font.setPointSize(Theme.DashboardReportWidgetPropertyEmojiFontSize)
        font.setHintingPreference(Font.HintingPreference.PreferNoHinting)
        self.setFont(font)
