
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from Gui.Widgets.Dashboard.ReportItemP import ReportItemP
from Gui.Widgets.Dashboard.ReportItemPre import ReportItemPre
from Gui.Widgets.Dashboard.ReportItemImg import ReportItemImg
from Gui.Widgets.Dashboard.ReportItemFile import ReportItemFile

from Gui.Fonts import Font
import Gui.Themes as Themes

from State.Models.Content.Content import Content
from State.Models.Content.File import File
from State.Models.Content.Img import Img
from State.Models.Content.P import P
from State.Models.Content.Pre import Pre

from Log import log
from App import app


class ReportWidgetContent(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._content = None
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-widget-content')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(16)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(self._layout)
        
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-report-widget-content {{
                background-color: transparent;
                border: none;
                padding: 0px;
                outline: none;
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
            widget.restyleUI(recursive)
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content: Content | None):
        if content == self._content:
            return 
        if content is None:
            return
        self._content = content

        for i in reversed(range(self._layout.count())):
            item = self._layout.itemAt(i)
            if item is None:
                continue
            widget = item.widget()
            if widget is None:
                continue
            widget.hide()
            widget.setParent(None)
        
        for item in self._content.items:
            if isinstance(item, P):
                widget = ReportItemP(item, self)
                self._layout.addWidget(widget)
                continue
        
            if isinstance(item, Pre):
                widget = ReportItemPre(self)
                widget.pre = item
                self._layout.addWidget(widget)
                continue

            if isinstance(item, Img):
                widget = ReportItemImg(item, self)
                self._layout.addWidget(widget)
                continue
            
            if isinstance(item, File):
                widget = ReportItemFile(self)
                widget.file = item
                self._layout.addWidget(widget)
                continue
        return
