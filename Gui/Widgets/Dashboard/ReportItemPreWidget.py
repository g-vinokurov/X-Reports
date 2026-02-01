
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Widgets.Dashboard.ReportItemPreContent import ReportItemPreContent
from Gui.Widgets.Scrolls import ScrollPre

from Gui.Fonts import Font
import Gui.Themes as Themes

from Log import log
from App import app


class ReportItemPreWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-item-pre-widget')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self._content = ReportItemPreContent(self)

        self._scroll = ScrollPre(app.gui)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._content)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        if not recursive:
            return
        self._content.restyleUI(recursive)
        self._scroll.restyleUI(recursive)
    
    @property
    def value(self):
        return self._content.value
    
    @value.setter
    def value(self, value: str):
        self._content.value = value
