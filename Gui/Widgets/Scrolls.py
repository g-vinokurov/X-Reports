
from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

import Gui.Themes as Themes

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
        
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
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
                height: {Themes.CurrentTheme.ScrollHorizontalHeight}px;
                margin: 0px;
                border-radius: {Themes.CurrentTheme.ScrollHorizontalBorderRadius}px;
                background-color: {Themes.CurrentTheme.ScrollHorizontalBackgroundColor};
            }}

            QScrollArea#scroll > QWidget > QScrollBar::handle:horizontal {{
                background-color: {Themes.CurrentTheme.ScrollHorizontalHandleBackgroundColor};
                min-width: {Themes.CurrentTheme.ScrollHorizontalMinWidth}px;
                border-radius: {Themes.CurrentTheme.ScrollHorizontalHandleBorderRadius}px;
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
                background-color: {Themes.CurrentTheme.ScrollVerticalBackgroundColor};
                width: {Themes.CurrentTheme.ScrollVerticalWidth}px;
                margin: 0px;
                border-radius: {Themes.CurrentTheme.ScrollVerticalBorderRadius}px;
                border-left: 1px solid {Themes.CurrentTheme.ScrollVerticalBorderColor};
            }}

            QScrollArea#scroll > QWidget > QScrollBar::handle:vertical {{
                background-color: {Themes.CurrentTheme.ScrollVerticalHandleBackgroundColor};
                min-height: {Themes.CurrentTheme.ScrollVerticalMinHeight}px;
                border-radius: {Themes.CurrentTheme.ScrollVerticalHandleBorderRadius}px;
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
        
        self.restyleUI()
    
    def restyleUI(self, recursive: bool = False):
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
                height: {Themes.CurrentTheme.ScrollPreHorizontalHeight}px;
                margin: 0px 0px 0px 0px;
                border-top: 1px transparent {Themes.CurrentTheme.ScrollPreHorizontalBorderColor};
                border-radius: {Themes.CurrentTheme.ScrollPreHorizontalBorderRadius}px;
                background-color: transparent;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::handle:horizontal {{
                background-color: {Themes.CurrentTheme.ScrollPreHorizontalHandleBackgroundColor};
                min-width: {Themes.CurrentTheme.ScrollPreHorizontalMinWidth}px;
                border-radius: {Themes.CurrentTheme.ScrollPreHorizontalHandleBorderRadius}px;
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
                width: {Themes.CurrentTheme.ScrollPreVerticalWidth}px;
                margin: 0px 0px 0px 0px;
                border-left: 1px transparent {Themes.CurrentTheme.ScrollPreVerticalBorderColor};
                border-radius: {Themes.CurrentTheme.ScrollPreVerticalBorderRadius}px;
            }}

            QScrollArea#scroll-pre > QWidget > QScrollBar::handle:vertical {{
                background-color: {Themes.CurrentTheme.ScrollPreVerticalHandleBackgroundColor};
                min-height: {Themes.CurrentTheme.ScrollPreVerticalMinHeight}px;
                border-radius: {Themes.CurrentTheme.ScrollPreVerticalHandleBorderRadius}px;
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
