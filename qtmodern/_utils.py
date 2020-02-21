import platform

from qtpy.QtCore import QFile, QIODevice, QTextStream, QT_VERSION

import qtmodern._resources_rc

QT_VERSION = tuple(int(v) for v in QT_VERSION.split('.'))
""" tuple: Qt version. """


FRAMELESS_STYLESHEET = ':/stylesheets/frameless.qss'
MODERN_STYLESHEET = ':/stylesheets/style.qss'


PLATFORM = platform.system().lower()
PLATFORM_WINDOWS = "windows"
PLATFORM_MACOS = "darwin"


def __get_stylesheet(style):
    style = QFile(style)
    style.open(QIODevice.ReadOnly)
    stylesheet = QTextStream(style).readAll()
    style.close()
    return stylesheet


def get_modern_stylesheet():
    return __get_stylesheet(MODERN_STYLESHEET)


def get_frameless_stylesheet():
    return __get_stylesheet(FRAMELESS_STYLESHEET)
