
import pathlib

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QCursor

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from State.Models.Content.Img import Img

from Log import log
from App import app


class ReportItemImg(QWidget):
    def __init__(self, img: Img, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._img = img
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-item-img')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self._image = ReportItemImgContent(self._img.src, self)

        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 16)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout.addWidget(self._image)

        self.setLayout(self._layout)
    
    @property
    def img(self):
        return self._img


class ReportItemImgContent(QWidget):
    def __init__(self, path: str | pathlib.Path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._path = str(path)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('dashboard-report-item-img-content')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self._pixmap = QPixmap.fromImage(QImage(self._path))
        
        # This code allows show image via QLabel in layout
        # If image is too large it will fit to layout size
        # Usage: if we need scale image to full layout width
        self._image = QLabel("", self)
        self._image.setMinimumSize(1, 1)

        size_policy = QSizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        size_policy.setVerticalPolicy(QSizePolicy.Policy.Expanding)
        self._image.setSizePolicy(size_policy)

        self._image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._layout.addWidget(self._image)

        self.setLayout(self._layout)

        self._image.setPixmap(self._pixmap)

    def resizeEvent(self, event):
        pixmap = self._pixmap.scaledToWidth(self._image.width(), Qt.TransformationMode.SmoothTransformation)
        self._image.setPixmap(pixmap)
