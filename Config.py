
import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

FONTS_DIR = os.path.join(PROJECT_DIR, 'Gui', 'Fonts')
ICONS_DIR = os.path.join(PROJECT_DIR, 'Gui', 'Icons')
IMAGES_DIR = os.path.join(PROJECT_DIR, 'Gui', 'Images')

LOG_LVL = 'DEBUG'
LOG_FILE = 'App.log'
LOG_FMT = '%(asctime)s %(levelname)s %(message)s'
