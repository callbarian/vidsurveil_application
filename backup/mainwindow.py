# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setGeometry(QRect(0, 0, 1211, 51))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush = QBrush(QColor(249, 252, 253))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush = QBrush(QColor(121, 124, 125))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        brush = QBrush(QColor(162, 166, 167))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush = QBrush(QColor(249, 252, 253))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(255, 255, 220))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush = QBrush(QColor(249, 252, 253))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(121, 124, 125))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        brush = QBrush(QColor(162, 166, 167))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        brush = QBrush(QColor(249, 252, 253))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(255, 255, 220))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(121, 124, 125))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        brush = QBrush(QColor(249, 252, 253))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        brush = QBrush(QColor(121, 124, 125))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        brush = QBrush(QColor(162, 166, 167))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        brush = QBrush(QColor(121, 124, 125))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        brush = QBrush(QColor(121, 124, 125))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush = QBrush(QColor(243, 249, 251))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(255, 255, 220))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.top_frame.setPalette(palette)
        self.top_frame.setStyleSheet("#top_frame{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/top_frame.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.push_original = QPushButton(self.top_frame)
        self.push_original.setGeometry(QRect(20, 10, 141, 41))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush = QBrush(QColor(252, 255, 244))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush = QBrush(QColor(125, 127, 117))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        brush = QBrush(QColor(166, 170, 156))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush = QBrush(QColor(252, 255, 244))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(255, 255, 220))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush = QBrush(QColor(252, 255, 244))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush)
        brush = QBrush(QColor(125, 127, 117))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        brush = QBrush(QColor(166, 170, 156))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        brush = QBrush(QColor(252, 255, 244))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(255, 255, 220))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(125, 127, 117))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        brush = QBrush(QColor(252, 255, 244))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        brush = QBrush(QColor(125, 127, 117))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        brush = QBrush(QColor(166, 170, 156))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush)
        brush = QBrush(QColor(125, 127, 117))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        brush = QBrush(QColor(125, 127, 117))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush = QBrush(QColor(250, 255, 234))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        brush = QBrush(QColor(255, 255, 220))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush)
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.push_original.setPalette(palette)
        self.push_original.setStyleSheet("#push_original{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/buttons/original.png);\n"
"background:none;\n"
"border:none;\n"
"background-repeat:none;\n"
"}\n"
"#push_original:pressed\n"
"{\n"
"border-image:url(resources/buttons/original_videos.png)\n"
"}")
        self.push_original.setText("")
        self.push_original.setObjectName("push_original")
        self.push_extracted = QPushButton(self.top_frame)
        self.push_extracted.setGeometry(QRect(160, 10, 141, 41))
        self.push_extracted.setStyleSheet("#push_extracted{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/buttons/extracted.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"#push_extracted:pressed\n"
"{\n"
"border-image:url(resources/buttons/extracted_videos.png)\n"
"}")
        self.push_extracted.setText("")
        self.push_extracted.setObjectName("push_extracted")
        self.second_mediaplayer = QFrame(self.centralwidget)
        self.second_mediaplayer.setGeometry(QRect(810, 50, 391, 301))
        self.second_mediaplayer.setStyleSheet("#second_mediaplayer{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/media_player.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.second_mediaplayer.setFrameShape(QFrame.StyledPanel)
        self.second_mediaplayer.setFrameShadow(QFrame.Raised)
        self.second_mediaplayer.setObjectName("second_mediaplayer")
        self.first_mediaplayer = QFrame(self.centralwidget)
        self.first_mediaplayer.setGeometry(QRect(420, 50, 391, 301))
        self.first_mediaplayer.setStyleSheet("#first_mediaplayer{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/media_player.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.first_mediaplayer.setFrameShape(QFrame.StyledPanel)
        self.first_mediaplayer.setFrameShadow(QFrame.Raised)
        self.first_mediaplayer.setObjectName("first_mediaplayer")
        self.view_file = QFrame(self.centralwidget)
        self.view_file.setGeometry(QRect(0, 50, 421, 301))
        self.view_file.setStyleSheet("#view_file{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/box_frame.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.view_file.setFrameShape(QFrame.StyledPanel)
        self.view_file.setFrameShadow(QFrame.Raised)
        self.view_file.setObjectName("view_file")
        self.stackedWidget = QStackedWidget(self.view_file)
        self.stackedWidget.setGeometry(QRect(59, 9, 361, 281))
        self.stackedWidget.setObjectName("stackedWidget")
        self.original_filepage = QWidget()
        self.original_filepage.setObjectName("original_filepage")
        self.stackedWidget.addWidget(self.original_filepage)
        self.extracted_filepage = QWidget()
        self.extracted_filepage.setObjectName("extracted_filepage")
        self.stackedWidget.addWidget(self.extracted_filepage)
        self.push_add_files = QPushButton(self.view_file)
        self.push_add_files.setGeometry(QRect(0, 10, 61, 81))
        self.push_add_files.setStyleSheet("#push_add_files{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/buttons/add_files.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"#push_add_files:pressed\n"
"{\n"
"border-image:url(resources/buttons/add_files_small.png)\n"
"}")
        self.push_add_files.setText("")
        self.push_add_files.setObjectName("push_add_files")
        self.mini_viewer = QFrame(self.centralwidget)
        self.mini_viewer.setGeometry(QRect(0, 350, 1201, 291))
        self.mini_viewer.setStyleSheet("#mini_viewer{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/mini_viewer.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.mini_viewer.setFrameShape(QFrame.StyledPanel)
        self.mini_viewer.setFrameShadow(QFrame.Raised)
        self.mini_viewer.setObjectName("mini_viewer")
        self.timeline_1 = QGraphicsView(self.mini_viewer)
        self.timeline_1.setGeometry(QRect(90, 20, 1091, 21))
        self.timeline_1.setStyleSheet("#timeline_1{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/timeline.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.timeline_1.setObjectName("timeline_1")
        self.mini_view_1 = QGraphicsView(self.mini_viewer)
        self.mini_view_1.setGeometry(QRect(90, 50, 1091, 81))
        self.mini_view_1.setStyleSheet("#mini_view_1{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/mini_view.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.mini_view_1.setObjectName("mini_view_1")
        self.timeline_2 = QGraphicsView(self.mini_viewer)
        self.timeline_2.setGeometry(QRect(90, 160, 1091, 21))
        self.timeline_2.setStyleSheet("#timeline_2{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/timeline.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}")
        self.timeline_2.setObjectName("timeline_2")
        self.mini_view_2 = QGraphicsView(self.mini_viewer)
        self.mini_view_2.setGeometry(QRect(90, 190, 1091, 81))
        self.mini_view_2.setStyleSheet("#mini_view_2{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/frames/mini_view.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"")
        self.mini_view_2.setObjectName("mini_view_2")
        self.push_extract_1 = QPushButton(self.mini_viewer)
        self.push_extract_1.setGeometry(QRect(10, 20, 81, 31))
        self.push_extract_1.setStyleSheet("#push_extract_1{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/buttons/extract.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"#push_extract_1:pressed\n"
"{\n"
"border-image:url(resources/buttons/extract_small.png)\n"
"}")
        self.push_extract_1.setText("")
        self.push_extract_1.setObjectName("push_extract_1")
        self.push_extract_2 = QPushButton(self.mini_viewer)
        self.push_extract_2.setGeometry(QRect(10, 160, 81, 31))
        self.push_extract_2.setStyleSheet("#push_extract_2{\n"
"background-clolor:transparent;\n"
"border-image:url(resources/buttons/extract.png);\n"
"border:none;\n"
"background:none;\n"
"background-repeat:none;\n"
"}\n"
"#push_extract_2:pressed\n"
"{\n"
"border-image:url(resources/buttons/extract_small.png)\n"
"}")
        self.push_extract_2.setText("")
        self.push_extract_2.setObjectName("push_extract_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push_original.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
