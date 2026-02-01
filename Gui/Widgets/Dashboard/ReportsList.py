
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtGui import QCursor

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal

from Gui.Widgets.Dashboard.ReportCard import ReportCard
import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportsList(QWidget):
    report_selected = pyqtSignal(Report)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._reports = []
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-reports-list')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 128)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(self._layout)
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-reports-list {{
                background-color: transparent;
                outline: none;
                border: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        for i in reversed(range(self._layout.count())):
            item = self._layout.itemAt(i)
            if item is None:
                continue
            widget = item.widget()
            if widget is None:
                continue
            if not isinstance(widget, ReportCard):
                continue
            widget.restyleUI(recursive)

    @property
    def reports(self):
        return self._reports[::]
    
    @reports.setter
    def reports(self, reports: list[Report]):
        self._reports = reports[::]
        
        # YOU MUST USE "REVERSED" FOR CORRECT LAYOUT CLEARING!!! 
        for i in reversed(range(self._layout.count())):
            item = self._layout.itemAt(i)
            if item is None:
                continue
            widget = item.widget()
            if widget is None:
                continue
            if not isinstance(widget, ReportCard):
                continue
            widget.selected.disconnect(self.on_report_card_selected)
            widget.hide()
            widget.setParent(None)
        
        for report in reports:
            report_card = ReportCard(self)
            report_card.report = report
            report_card.selected.connect(self.on_report_card_selected)
            self._layout.addWidget(report_card)
    
    @pyqtSlot(Report)
    def on_report_card_selected(self, report: Report):
        self.report_selected.emit(report)
