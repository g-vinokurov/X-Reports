
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

from Config import FONTS_DIR

from Logger import log


class Font:
    def __init__(self, filepath: str):
        self.__filepath = filepath
        self.__family = None

    def __str__(self):
        if self.__family is not None:
            return str(self.__family)
        
        if QApplication.instance() is None:
            log.warning('QApplication not started - impossible to load font')
            return str()
        
        font_id = QFontDatabase.addApplicationFont(self.__filepath)
        if font_id == -1:
            log.warning(f'Could not load font {self.__filepath}')
            return str()

        families = QFontDatabase.applicationFontFamilies(font_id)
        if not families:
            return str()

        self.__family = families[0]
        return str(self.__family)


FONT_SEGOE_UI_EMOJI = Font(os.path.join(FONTS_DIR, 'Segoe-UI-Emoji.ttf'))

FONT_JET_BRAINS_MONO_NL_BOLD = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-Bold.ttf'))
FONT_JET_BRAINS_MONO_NL_EXTRA_BOLD = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-ExtraBold.ttf'))
FONT_JET_BRAINS_MONO_NL_EXTRA_LIGHT = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-ExtraLight.ttf'))
FONT_JET_BRAINS_MONO_NL_LIGHT = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-Light.ttf'))
FONT_JET_BRAINS_MONO_NL_MEDIUM = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-Medium.ttf'))
FONT_JET_BRAINS_MONO_NL_REGULAR = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-Regular.ttf'))
FONT_JET_BRAINS_MONO_NL_SEMI_BOLD = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-SemiBold.ttf'))
FONT_JET_BRAINS_MONO_NL_THIN = Font(os.path.join(FONTS_DIR, 'JetBrainsMonoNL-Thin.ttf'))
