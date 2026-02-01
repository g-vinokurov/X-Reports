
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Dashboard.ReportWidget import ReportWidget
from Gui.Widgets.Scrolls import Scroll

from Gui.Themes import CurrentTheme as Theme

from State.Models.Report.Report import Report

from Log import log
from App import app


class ReportWidgetContainer(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._report = None
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-report-widget-container')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            QWidget#dashboard-report-widget-container {{
                background: transparent;
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')

        self._report_widget = ReportWidget(self)

        self._scroll = Scroll(app.gui)
        self._scroll.setWidgetResizable(True)
        self._scroll.setWidget(self._report_widget)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._scroll)

        self.setLayout(self._layout)
    
    @property
    def report(self):
        return self._report
    
    @report.setter
    def report(self, report: Report | None):
        if report == self._report:
            return
        if report is None:
            return
        log.info(f'Report {report.id} selected')

        self._report_widget = ReportWidget(self)
        self._report_widget.report = report
        self._scroll.setWidget(self._report_widget)
        return
