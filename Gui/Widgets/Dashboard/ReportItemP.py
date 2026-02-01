
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from State.Models.Content.P import P

from Log import log
from App import app


class ReportItemP(QLabel):
    def __init__(self, p: P, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._p = p
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-item-p')

        self.setStyleSheet(f'''
            color: {Theme.DashboardReportItemPColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setContentsMargins(0, 0, 0, 0)
        self.setWordWrap(True)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        font = Font(Theme.DashboardReportItemPFont)
        font.setPointSize(Theme.DashboardReportItemPFontSize)
        font.setWeight(Theme.DashboardReportItemPFontWeight)
        self.setFont(font)

        self.setText(self._p.text)
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

    @property
    def p(self):
        return self._p
