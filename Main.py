
import sys

from PyQt5.QtWidgets import QApplication

from Gui.Widgets.Window import Window
from State.State import State

from App import app


if __name__ == '__main__':
    application = QApplication([])
    
    app.state = State()
    
    app.gui = Window()
    app.gui.navigator.goto('welcome')
    app.gui.show()
    
    sys.exit(application.exec())
