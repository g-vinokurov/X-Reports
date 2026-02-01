
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QSizePolicy

from Gui.Widgets.Router import Router


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        size_policy = QSizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Policy.Preferred)
        size_policy.setVerticalPolicy(QSizePolicy.Policy.Preferred)

        self._router = Router(self)
        self._router.setSizePolicy(size_policy)

        self.setCentralWidget(self._router)
        self.setSizePolicy(size_policy)

        primary_screen = QApplication.primaryScreen()
        
        if primary_screen:
            screen_geometry = primary_screen.availableGeometry()
            screen_w = screen_geometry.width()
            screen_h = screen_geometry.height()

            window_w = screen_w * 3 // 4
            window_h = screen_h * 3 // 4
            self.resize(window_w, window_h)
        else:
            self.showMaximized()
    
    @property
    def router(self):
        return self._router
