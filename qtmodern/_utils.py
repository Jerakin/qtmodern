import sys
from os.path import join, dirname, abspath
import qtpy
import platform

QT_VERSION = tuple(int(v) for v in qtpy.QT_VERSION.split('.'))
""" tuple: Qt version. """

PLATFORM = platform.system()


def resource_path(relative_path):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS', False):  # PyInstaller
        return join(sys._MEIPASS, dirname(abspath(__file__)), relative_path)
    elif getattr(sys, 'frozen', False):  # cx_Freeze
        return join(dirname(abspath(sys.executable)), relative_path)
    return join(dirname(abspath(__file__)), relative_path)
