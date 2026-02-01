
from PyQt5.QtWidgets import QScrollArea

from PyQt5.QtGui import QCursor

from PyQt5.QtCore import Qt

from Gui.Colors import COLOR_VSC_PRIMARY
from Gui.Colors import COLOR_VSC_SECONDARY
from Gui.Colors import COLOR_VSC_TERTIARY
from Gui.Colors import COLOR_BS_LIGHT
from Gui.Colors import COLOR_BS_GRAY_400


class Scroll(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(f'''
            QScrollArea {{ 
                background: transparent;
                border: none;
            }}
                           
            QScrollArea > QWidget > QWidget {{
                background: transparent; 
                border: none;
            }}

            QScrollBar:horizontal {{
                height: 15px;
                margin: 3px 15px 3px 15px;
                border: 1px transparent {COLOR_BS_LIGHT};
                border-radius: 4px;
                background-color: transparent;
            }}

            QScrollBar::handle:horizontal {{
                background-color: {COLOR_BS_LIGHT};
                min-width: 5px;
                border-radius: 4px;
            }}

            QScrollBar::add-line:horizontal {{
                background: none;
            }}

            QScrollBar::sub-line:horizontal {{
                background: none;
            }}

            QScrollBar::up-arrow:horizontal {{
                background: none;
            }}

            QScrollBar::down-arrow:horizontal {{
                background: none;
            }}

            QScrollBar::add-page:horizontal {{
                background: none;
            }}

            QScrollBar::sub-page:horizontal {{
                background: none;
            }}

            QScrollBar:vertical {{
                background-color: transparent;
                width: 15px;
                margin: 15px 3px 15px 3px;
                border: 1px transparent {COLOR_BS_LIGHT};
                border-radius: 4px;
            }}

            QScrollBar::handle:vertical {{
                background-color: {COLOR_BS_LIGHT};
                min-height: 5px;
                border-radius: 4px;
            }}

            QScrollBar::add-line:vertical {{
                background: none;
            }}

            QScrollBar::sub-line:vertical {{
                background: none;
            }}

            QScrollBar::up-arrow:vertical {{
                background: none;
            }}

            QScrollBar::down-arrow:vertical {{
                background: none;
            }}

            QScrollBar::add-page:vertical {{
                background: none;
            }}

            QScrollBar::sub-page:vertical {{
                background: none;
            }}
        ''')


class ScrollSecondary(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet(f'''
            QScrollArea {{ 
                background: transparent;
                border: none;
            }}
                           
            QScrollArea > QWidget > QWidget {{
                background: transparent; 
                border: none;
            }}

            QScrollBar:horizontal {{
                height: 15px;
                margin: 3px 15px 3px 15px;
                border: 1px transparent {COLOR_BS_GRAY_400};
                border-radius: 4px;
                background-color: transparent;
            }}

            QScrollBar::handle:horizontal {{
                background-color: {COLOR_BS_GRAY_400};
                min-width: 5px;
                border-radius: 4px;
            }}

            QScrollBar::add-line:horizontal {{
                background: none;
            }}

            QScrollBar::sub-line:horizontal {{
                background: none;
            }}

            QScrollBar::up-arrow:horizontal {{
                background: none;
            }}

            QScrollBar::down-arrow:horizontal {{
                background: none;
            }}

            QScrollBar::add-page:horizontal {{
                background: none;
            }}

            QScrollBar::sub-page:horizontal {{
                background: none;
            }}

            QScrollBar:vertical {{
                background-color: transparent;
                width: 15px;
                margin: 15px 3px 15px 3px;
                border: 1px transparent {COLOR_BS_GRAY_400};
                border-radius: 4px;
            }}

            QScrollBar::handle:vertical {{
                background-color: {COLOR_BS_GRAY_400};
                min-height: 5px;
                border-radius: 4px;
            }}

            QScrollBar::add-line:vertical {{
                background: none;
            }}

            QScrollBar::sub-line:vertical {{
                background: none;
            }}

            QScrollBar::up-arrow:vertical {{
                background: none;
            }}

            QScrollBar::down-arrow:vertical {{
                background: none;
            }}

            QScrollBar::add-page:vertical {{
                background: none;
            }}

            QScrollBar::sub-page:vertical {{
                background: none;
            }}
        ''')
