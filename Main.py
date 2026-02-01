
import sys

from Gui.Widgets.Welcome.Screen import WelcomeScreen
from Gui.Widgets.Dashboard.Screen import DashboardScreen

from App import app


if __name__ == '__main__':
    app.gui.navigator.register('welcome', WelcomeScreen)
    app.gui.navigator.register('dashboard', DashboardScreen)
    app.gui.navigator.goto('welcome')
    app.gui.show()
    sys.exit(app.exec())
