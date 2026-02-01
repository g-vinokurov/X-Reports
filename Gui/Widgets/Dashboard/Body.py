
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from Gui.Widgets.Dashboard.ReportsListSection import ReportsListSection
from Gui.Widgets.Dashboard.ReportSection import ReportSection
from Gui.Widgets.Splitter import Splitter

import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class Body(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-body')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._reports_list_section = ReportsListSection(self)
        self._report_section = ReportSection(self)
        
        reports = self._reports_list_section.reports_list
        reports.report_selected.connect(self.on_report_selected)

        self._splitter = Splitter(Qt.Orientation.Horizontal)
        self._splitter.addWidget(self._reports_list_section)
        self._splitter.addWidget(self._report_section)
        self._splitter.setStretchFactor(0, 34)
        self._splitter.setStretchFactor(1, 55)

        # setStretchFactor does not work without it
        # https://stackoverflow.com/questions/67789225/qt-stretch-factor-in-qsplitter-does-not-work
        self._splitter.setSizes([340, 550])
        
        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        
        self._layout.addWidget(self._splitter)
        
        # Alternative way - use fixed stretch without splitter:
        # 
        # self._layout.addWidget(self._reports_list_section)
        # self._layout.addWidget(self._report_section)
        # self._layout.setStretch(0, 34)
        # self._layout.setStretch(1, 34)

        self.setLayout(self._layout)
        self.restyleUI()
    
    @property
    def reports_list_section(self):
        return self._reports_list_section
    
    @property
    def report_section(self):
        return self._report_section
    
    @pyqtSlot(Report)
    def on_report_selected(self, report: Report):
        self._report_section.report = report
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-body {{
                background-color: {Themes.CurrentTheme.DashboardBodyBackgroundColor};
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._reports_list_section.restyleUI(recursive)
        self._report_section.restyleUI(recursive)
        self._splitter.restyleUI(recursive)
