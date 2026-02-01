
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QGridLayout

from PyQt5.QtCore import Qt

from Gui.Widgets.Navigator import Navigator

from Logger import log
from App import app


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        size_policy = QSizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Preferred)
        size_policy.setVerticalPolicy(QSizePolicy.Preferred)

        self.central_widget = QWidget(self)
        self.central_widget.setSizePolicy(size_policy)

        self.navigator = Navigator(self.central_widget)

        self.central_layout = QGridLayout()
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addWidget(self.navigator)

        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)
        self.setSizePolicy(size_policy)

        display_geometry = QDesktopWidget().availableGeometry()
        display_w = display_geometry.width()
        display_h = display_geometry.height()

        window_w = display_w * 3 // 4
        window_h = display_h * 3 // 4
        self.resize(window_w, window_h)

        self.showMaximized()
    
    def closeEvent(self, event):
        app.state.quit()
        log.info('Close app')
        event.accept()
