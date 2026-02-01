
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Gui.Fonts import Font
from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class Logo(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('welcome-logo')

        self.setStyleSheet(f'''
            color: {Theme.WelcomeLogoColor};
            background: none;
            border: none;
            outline: none;
            padding: 0px;
        ''')
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setWordWrap(True)
        
        font = Font(Theme.WelcomeLogoFont)
        font.setPointSize(Theme.WelcomeLogoFontSize)
        font.setWeight(Theme.WelcomeLogoFontWeight)
        self.setFont(font)

        self.setText('THE X-FILES')
