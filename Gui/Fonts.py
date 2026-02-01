
import pathlib

from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtGui import QFont

from Config import FONTS_DIR

from Log import log


class Font(QFont):
    Thin       = QFont.Thin
    ExtraLight = QFont.ExtraLight
    Light      = QFont.Light
    Regular    = QFont.Normal
    Medium     = QFont.Medium
    SemiBold   = QFont.DemiBold
    Bold       = QFont.Bold
    ExtraBold  = QFont.ExtraBold
    Black      = QFont.Black
    
    _fonts = {}
    
    def __init__(self, path: str | pathlib.Path):
        path = str(path)
        if path not in self._fonts:
            self._load(path)
        super().__init__(self._fonts.get(path))
    
    @classmethod
    def _load(cls, path: str):

        if QApplication.instance() is None:
            log.warning('App not started - could not load fonts')
            return
        
        font_id = QFontDatabase.addApplicationFont(path)
        if font_id == -1:
            log.warning(f'Could not load font {path}')
            return

        families = QFontDatabase.applicationFontFamilies(font_id)
        if not families:
            return

        cls._fonts[path] = font = families[0]
        log.info(f'Font {font} loaded')


FONT_SEGOE_UI_EMOJI = FONTS_DIR / 'Segoe-UI-Emoji.ttf'

FONT_GEOLOGICA_BLACK       = FONTS_DIR / 'Geologica-Black.ttf'
FONT_GEOLOGICA_BOLD        = FONTS_DIR / 'Geologica-Bold.ttf'
FONT_GEOLOGICA_EXTRA_BOLD  = FONTS_DIR / 'Geologica-ExtraBold.ttf'
FONT_GEOLOGICA_EXTRA_LIGHT = FONTS_DIR / 'Geologica-ExtraLight.ttf'
FONT_GEOLOGICA_LIGHT       = FONTS_DIR / 'Geologica-Light.ttf'
FONT_GEOLOGICA_MEDIUM      = FONTS_DIR / 'Geologica-Medium.ttf'
FONT_GEOLOGICA_REGULAR     = FONTS_DIR / 'Geologica-Regular.ttf'
FONT_GEOLOGICA_SEMI_BOLD   = FONTS_DIR / 'Geologica-SemiBold.ttf'
FONT_GEOLOGICA_THIN        = FONTS_DIR / 'Geologica-Thin.ttf'

FONT_JET_BRAINS_MONO_NL_BOLD        = FONTS_DIR / 'JetBrainsMonoNL-Bold.ttf'
FONT_JET_BRAINS_MONO_NL_EXTRA_BOLD  = FONTS_DIR / 'JetBrainsMonoNL-ExtraBold.ttf'
FONT_JET_BRAINS_MONO_NL_EXTRA_LIGHT = FONTS_DIR / 'JetBrainsMonoNL-ExtraLight.ttf'
FONT_JET_BRAINS_MONO_NL_LIGHT       = FONTS_DIR / 'JetBrainsMonoNL-Light.ttf'
FONT_JET_BRAINS_MONO_NL_MEDIUM      = FONTS_DIR / 'JetBrainsMonoNL-Medium.ttf'
FONT_JET_BRAINS_MONO_NL_REGULAR     = FONTS_DIR / 'JetBrainsMonoNL-Regular.ttf'
FONT_JET_BRAINS_MONO_NL_SEMI_BOLD   = FONTS_DIR / 'JetBrainsMonoNL-SemiBold.ttf'
FONT_JET_BRAINS_MONO_NL_THIN        = FONTS_DIR / 'JetBrainsMonoNL-Thin.ttf'

FONT_JOST_BLACK       = FONTS_DIR / 'Jost-Black.ttf'
FONT_JOST_BOLD        = FONTS_DIR / 'Jost-Bold.ttf'
FONT_JOST_EXTRA_BOLD  = FONTS_DIR / 'Jost-ExtraBold.ttf'
FONT_JOST_EXTRA_LIGHT = FONTS_DIR / 'Jost-ExtraLight.ttf'
FONT_JOST_LIGHT       = FONTS_DIR / 'Jost-Light.ttf'
FONT_JOST_MEDIUM      = FONTS_DIR / 'Jost-Medium.ttf'
FONT_JOST_REGULAR     = FONTS_DIR / 'Jost-Regular.ttf'
FONT_JOST_SEMI_BOLD   = FONTS_DIR / 'Jost-SemiBold.ttf'
FONT_JOST_THIN        = FONTS_DIR / 'Jost-Thin.ttf'

FONT_MONTSERRAT_BLACK       = FONTS_DIR / 'Montserrat-Black.ttf'
FONT_MONTSERRAT_BOLD        = FONTS_DIR / 'Montserrat-Bold.ttf'
FONT_MONTSERRAT_EXTRA_BOLD  = FONTS_DIR / 'Montserrat-ExtraBold.ttf'
FONT_MONTSERRAT_EXTRA_LIGHT = FONTS_DIR / 'Montserrat-ExtraLight.ttf'
FONT_MONTSERRAT_LIGHT       = FONTS_DIR / 'Montserrat-Light.ttf'
FONT_MONTSERRAT_MEDIUM      = FONTS_DIR / 'Montserrat-Medium.ttf'
FONT_MONTSERRAT_REGULAR     = FONTS_DIR / 'Montserrat-Regular.ttf'
FONT_MONTSERRAT_SEMI_BOLD   = FONTS_DIR / 'Montserrat-SemiBold.ttf'
FONT_MONTSERRAT_THIN        = FONTS_DIR / 'Montserrat-Thin.ttf'
