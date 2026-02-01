
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.NoReportSelectedWidget import NoReportSelectedWidget
from Gui.Widgets.Dashboard.ReportWidgetContainer import ReportWidgetContainer

import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportSection(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._report = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-section')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._no_report_selected = NoReportSelectedWidget(self)
        self._report_widget_container = ReportWidgetContainer(self)
        self._report_widget_container.hide()

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._no_report_selected)
        self._layout.addWidget(self._report_widget_container)

        self.setLayout(self._layout)
        self.restyleUI()

    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-report-section {{
                background-color: {Themes.CurrentTheme.DashboardReportSectionBackgroundColor};
                outline: none;
                border: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._no_report_selected.restyleUI(recursive)
        self._report_widget_container.restyleUI(recursive)
    
    @property
    def report(self):
        return self._report
    
    @report.setter
    def report(self, report: Report | None):
        if report == self._report:
            return
        if report is None:
            self._report_widget_container.hide()
            self._no_report_selected.show()
        else:
            self._report_widget_container.show()
            self._no_report_selected.hide()
        self._report_widget_container.report = report
