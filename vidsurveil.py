# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication
from mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.push_original.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.original))
        self.ui.push_extracted.clicked.connect(lambda: self.ui.stackedWidgetsetCurrentWidget(self.ui.extracted))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.show()
    sys.exit(app.exec_())
    print('aa')
