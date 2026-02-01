
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class NoReportsFound(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-no-reports-found')

        self.setStyleSheet(f'''
            color: {Theme.DashboardNoReportsFoundColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setWordWrap(False)
        
        font = Font(Theme.DashboardNoReportsFoundFont)
        font.setPointSize(Theme.DashboardNoReportsFoundFontSize)
        font.setWeight(Theme.DashboardNoReportsFoundFontWeight)
        self.setFont(font)

        self.setText('No reports found')
        self.adjustHeight()

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
