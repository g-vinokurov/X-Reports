
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QCursor

from State.Utils.ProjectLoader import ProjectLoader
from State.Utils.Desktop import Desktop

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class OpenProject(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('welcome-open-project')

        self.setStyleSheet(f'''
            color: {Theme.WelcomeOpenProjectColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        font = Font(Theme.WelcomeOpenProjectFont)
        font.setPointSize(Theme.WelcomeOpenProjectFontSize)
        font.setWeight(Theme.WelcomeOpenProjectFontWeight)
        self.setFont(font)

        self.clicked.connect(self.on_clicked)
        self.setText('Open Project')
    
    def on_clicked(self, event):
        title = 'Open directory with reports'
        cwd = Desktop.location()

        dir = str(QFileDialog.getExistingDirectory(self, title, cwd))
        if not dir:
            return
        log.info(f'Open Project: {dir}')

        try:
            app.state.project = ProjectLoader.load(dir)
        except Exception as err:
            log.debug(f'{err}', exc_info=True)
            log.error('Could not load project')
            return
        
        app.gui.navigator.goto('dashboard')
