
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReportWidgetUnit import ReportWidgetUnit
from Gui.Widgets.Dashboard.ReportWidgetTitle import ReportWidgetTitle
from Gui.Widgets.Dashboard.ReportWidgetId import ReportWidgetId
from Gui.Widgets.Dashboard.ReportWidgetProperties import ReportWidgetProperties
from Gui.Widgets.Dashboard.ReportWidgetSubtitle import ReportWidgetSubtitle
from Gui.Widgets.Dashboard.ReportWidgetContent import ReportWidgetContent

import Gui.Themes as Themes

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportWidget(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._report = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self._report_title = ReportWidgetTitle(self)
        self._report_id = ReportWidgetId(self)
        self._unit_0 = ReportWidgetUnit(self)
        self._unit_0.add(self._report_title)
        self._unit_0.add(self._report_id)
        
        self._report_properties = ReportWidgetProperties(self)
        self._unit_1 = ReportWidgetUnit(self)
        self._unit_1.add(self._report_properties)

        self._report_task_subtitle = ReportWidgetSubtitle('Задача', self)
        self._report_task = ReportWidgetContent(self)
        self._unit_2 = ReportWidgetUnit(self)
        self._unit_2.add(self._report_task_subtitle)
        self._unit_2.add(self._report_task)

        self._report_solution_subtitle = ReportWidgetSubtitle('Решение', self)
        self._report_solution = ReportWidgetContent(self)
        self._unit_3 = ReportWidgetUnit(self)
        self._unit_3.add(self._report_solution_subtitle)
        self._unit_3.add(self._report_solution)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(*Themes.CurrentTheme.DashboardReportWidgetMargins)
        self._layout.setSpacing(32)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._layout.addWidget(self._unit_0)
        self._layout.addWidget(self._unit_1)
        self._layout.addWidget(self._unit_2)
        self._layout.addWidget(self._unit_3)

        self.setLayout(self._layout)
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-report-widget {{
                background: transparent;
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._unit_0.restyleUI(recursive)
        self._unit_1.restyleUI(recursive)
        self._unit_2.restyleUI(recursive)
        self._unit_3.restyleUI(recursive)
    
    @property
    def report(self):
        return self._report
    
    @report.setter
    def report(self, report: Report | None):
        if report == self._report:
            return
        if report is None:
            return
        self._report = report

        self._report_title.report = report
        self._report_id.report = report
        self._report_properties.report = report
        if report.task is not None:
            self._report_task.content = report.task.content
        if report.solution is not None:
            self._report_solution.content = report.solution.content
        return
