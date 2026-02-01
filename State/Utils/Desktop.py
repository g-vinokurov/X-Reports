import os
import sys


class Desktop:
    @classmethod
    def location(cls):
        if sys.platform == 'win32':
            return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        if sys.platform == 'linux':
            return os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        raise RuntimeError(f'Unsupported platform: {sys.platform}')
