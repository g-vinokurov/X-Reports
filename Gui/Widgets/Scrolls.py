
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Gui.Themes import CurrentTheme as Theme

from Log import log
from App import app


class Scroll(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('scroll')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.setStyleSheet(f'''
            QScrollArea#scroll {{ 
                background: transparent;
                border: none;
            }}
            
            QScrollArea#scroll > QWidget > QWidget {{
                background: transparent; 
                border: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar:horizontal {{
                height: {Theme.ScrollHorizontalHeight}px;
                margin: 0px;
                border-top: 1px solid {Theme.ScrollHorizontalBorderColor};
                border-radius: {Theme.ScrollHorizontalBorderRadius}px;
                background-color: transparent;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::handle:horizontal {{
                background-color: {Theme.ScrollHorizontalHandleBackgroundColor};
                min-width: {Theme.ScrollHorizontalMinWidth}px;
                border-radius: {Theme.ScrollHorizontalHandleBorderRadius}px;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::add-line:horizontal {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::sub-line:horizontal {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::up-arrow:horizontal {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::down-arrow:horizontal {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::add-page:horizontal {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::sub-page:horizontal {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar:vertical {{
                background-color: transparent;
                width: {Theme.ScrollVerticalWidth}px;
                margin: 0px;
                border-left: 1px solid {Theme.ScrollVerticalBorderColor};
                border-radius: {Theme.ScrollVerticalBorderRadius}px;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::handle:vertical {{
                background-color: {Theme.ScrollVerticalHandleBackgroundColor};
                min-height: {Theme.ScrollVerticalMinHeight}px;
                border-radius: {Theme.ScrollVerticalHandleBorderRadius}px;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::add-line:vertical {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::sub-line:vertical {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::up-arrow:vertical {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::down-arrow:vertical {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::add-page:vertical {{
                background: none;
            }}

            QScrollArea#scroll > QWidget > QScrollBar::sub-page:vertical {{
                background: none;
            }}
        ''')


class ScrollPre(QScrollArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
    
    def initUI(self):
        self.setObjectName('scroll-pre')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.setStyleSheet(f'''
            QScrollArea#scroll-pre {{ 
                background: transparent;
                border: none;
            }}
            
            QScrollArea#scroll-pre > QWidget > QWidget {{
                background: transparent; 
                border: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar:horizontal {{
                height: {Theme.ScrollPreHorizontalHeight}px;
                margin: 0px 0px 0px 0px;
                border-top: 1px transparent {Theme.ScrollPreHorizontalBorderColor};
                border-radius: {Theme.ScrollPreHorizontalBorderRadius}px;
                background-color: transparent;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::handle:horizontal {{
                background-color: {Theme.ScrollPreHorizontalHandleBackgroundColor};
                min-width: {Theme.ScrollPreHorizontalMinWidth}px;
                border-radius: {Theme.ScrollPreHorizontalHandleBorderRadius}px;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::add-line:horizontal {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::sub-line:horizontal {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::up-arrow:horizontal {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::down-arrow:horizontal {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::add-page:horizontal {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::sub-page:horizontal {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar:vertical {{
                background-color: transparent;
                width: {Theme.ScrollPreVerticalWidth}px;
                margin: 0px 0px 0px 0px;
                border-left: 1px transparent {Theme.ScrollPreVerticalBorderColor};
                border-radius: {Theme.ScrollPreVerticalBorderRadius}px;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::handle:vertical {{
                background-color: {Theme.ScrollPreVerticalHandleBackgroundColor};
                min-height: {Theme.ScrollPreVerticalMinHeight}px;
                border-radius: {Theme.ScrollPreVerticalHandleBorderRadius}px;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::add-line:vertical {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::sub-line:vertical {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::up-arrow:vertical {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::down-arrow:vertical {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::add-page:vertical {{
                background: none;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::sub-page:vertical {{
                background: none;
            }}
        ''')
