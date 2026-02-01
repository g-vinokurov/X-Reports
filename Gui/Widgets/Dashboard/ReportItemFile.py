
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Widgets.Dashboard.ReportWidgetPropertyEmoji import ReportWidgetPropertyEmoji
from Gui.Widgets.Dashboard.ReportWidgetPropertyName import ReportWidgetPropertyName
from Gui.Widgets.Dashboard.ReportWidgetPropertyValue import ReportWidgetPropertyValue

from Gui.Fonts import Font
import Gui.Themes as Themes

from State.Models.Content.File import File

from Log import log
from App import app


class ReportItemFile(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._file = None
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-item-file')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(8)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self._report_file_emoji = ReportWidgetPropertyEmoji('📌', self)
        self._report_file_name = ReportWidgetPropertyName(self)
        self._report_file_value = ReportWidgetPropertyValue(self)

        self.restyleUI()

        self._layout.addWidget(self._report_file_emoji)
        self._layout.addWidget(self._report_file_name)
        self._layout.addWidget(self._report_file_value)

        self._layout.setStretch(2, 1)

        self.setLayout(self._layout)
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-report-item-file {{
                padding: 0px;
                background: none;
                border: none;
                outline: none;
            }}
        ''')
        if not recursive:
            return
        self._report_file_emoji.restyleUI(recursive)
        self._report_file_name.restyleUI(recursive)
        self._report_file_value.restyleUI(recursive)
    
    @property
    def file(self):
        return self._file
    
    @file.setter
    def file(self, file: File | None):
        if file == self._file:
            return
        if file is None:
            return
        self._file = file
        self._report_file_name.value = f'{file.name}:'
        self._report_file_value.value = file.src
        return
