
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout

from Gui.Widgets.Screens.Screen import Screen
from Gui.Widgets.Screens.ScreenWelcome import ScreenWelcome
from Gui.Widgets.Screens.ScreenDashboard import ScreenDashboard


class Navigator(QWidget):
    __mapper = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__screens = {}
        self.initUI()

    def initUI(self):
        self.__current_screen = Screen(self)

        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.__current_screen)

        self.setLayout(self.layout)
    
    @property
    def current_screen(self):
        return self.__current_screen

    def load(self, tag: str, *args, **kwargs):
        self.__screens[tag] = self.__mapper.get(tag, Screen)(self, *args, **kwargs)
        self.update(tag, *args, **kwargs)

    def update(self, tag: str, *args, **kwargs):
        screen : Screen = self.__screens.get(tag, Screen(self))
        screen.updateUI(*args, **kwargs)

    def goto(self, tag: str, *args, **kwargs):
        if tag not in self.__screens:
            self.load(tag, *args, **kwargs)

        self.layout.removeWidget(self.__current_screen)
        self.__current_screen.hide()
        self.__current_screen = self.__screens[tag]
        self.__current_screen.show()
        self.layout.addWidget(self.__current_screen)

    @classmethod
    def register(cls, tag: str, screen_cls: type[Screen]):
        if tag in cls.__mapper:
            return
        cls.__mapper[tag] = screen_cls


Navigator.register('welcome', ScreenWelcome)
Navigator.register('dashboard', ScreenDashboard)
