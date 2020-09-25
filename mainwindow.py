# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import show_miniview
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsPixmapItem
import cv2
import os

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(999, 749)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.first_mediaplayer = QtWidgets.QFrame(self.centralwidget)
        self.first_mediaplayer.setGeometry(QtCore.QRect(540, 0, 461, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_mediaplayer.sizePolicy().hasHeightForWidth())
        self.first_mediaplayer.setSizePolicy(sizePolicy)
        self.first_mediaplayer.setStyleSheet("")
        self.first_mediaplayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_mediaplayer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_mediaplayer.setObjectName("first_mediaplayer")
        self.mini_viewer = QtWidgets.QFrame(self.centralwidget)
        self.mini_viewer.setGeometry(QtCore.QRect(10, 300, 991, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mini_viewer.sizePolicy().hasHeightForWidth())
        self.mini_viewer.setSizePolicy(sizePolicy)
        self.mini_viewer.setStyleSheet("\n"
"")
        self.mini_viewer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mini_viewer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mini_viewer.setObjectName("mini_viewer")
        self.timeline_1 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_1.setGeometry(QtCore.QRect(47, 77, 894, 24))
        self.timeline_1.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-color: rgb(250, 240, 242);")
        self.timeline_1.setObjectName("timeline_1")
        self.mini_view_1 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.mini_view_1.setGeometry(QtCore.QRect(47, 107, 894, 84))
        self.mini_view_1.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-color: rgb(146, 130, 229);")
        self.mini_view_1.setObjectName("mini_view_1")
        self.timeline_2 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_2.setGeometry(QtCore.QRect(47, 217, 894, 24))
        self.timeline_2.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-left-color: rgb(255, 150, 150);\n"
                                        "border-right-color: rgb(255, 255, 255);\n"
                                        "border-top-color: rgb(255, 255, 255);\n"
                                        "border-bottom-color: rgb(255, 255, 255);\n")
        self.timeline_2.setObjectName("timeline_2")
        self.mini_view_2 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.mini_view_2.setGeometry(QtCore.QRect(47, 317, 894, 84))
        self.mini_view_2.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-color: rgb(146, 130, 229);")
        self.mini_view_2.setObjectName("mini_view_2")
        self.push_extract_1 = QtWidgets.QPushButton(self.mini_viewer)
        self.push_extract_1.setGeometry(QtCore.QRect(40, 40, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_extract_1.sizePolicy().hasHeightForWidth())
        self.push_extract_1.setSizePolicy(sizePolicy)
        self.push_extract_1.setStyleSheet("")
        self.push_extract_1.setObjectName("push_extract_1")
        self.timeline_3 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_3.setGeometry(QtCore.QRect(47, 251, 894, 24))
        self.timeline_3.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-left-color: rgb(150, 255, 150);\n"
                                        "border-right-color: rgb(255, 255, 255);\n"
                                        "border-top-color: rgb(255, 255, 255);\n"
                                        "border-bottom-color: rgb(255, 255, 255);\n")
        self.timeline_3.setObjectName("timeline_3")
        self.timeline_4 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_4.setGeometry(QtCore.QRect(47, 287, 894, 24))
        self.timeline_4.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-left-color: rgb(150, 150, 255);\n"
                                        "border-right-color: rgb(255, 255, 255);\n"
                                        "border-top-color: rgb(255, 255, 255);\n"
                                        "border-bottom-color: rgb(255, 255, 255);")
        self.timeline_4.setObjectName("timeline_4")
        self.textEdit = QtWidgets.QTextEdit(self.mini_viewer)
        self.textEdit.setGeometry(QtCore.QRect(500, 20, 441, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("background-color: transparent;")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 511, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1.sizePolicy().hasHeightForWidth())
        self.tab1.setSizePolicy(sizePolicy)
        self.tab1.setObjectName("tab1")
        self.treeView1 = QtWidgets.QTreeView(self.tab1)
        self.treeView1.setGeometry(QtCore.QRect(10, 0, 511, 271))
        self.treeView1.setAcceptDrops(True)
        self.treeView1.setObjectName("treeView1")
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.treeView2 = QtWidgets.QTreeView(self.tab_2)
        self.treeView2.setGeometry(QtCore.QRect(10, 0, 511, 271))
        self.treeView2.setAcceptDrops(True)
        self.treeView2.setObjectName("treeView2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 999, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuVidsurveil = QtWidgets.QMenu(self.menuBar)
        self.menuVidsurveil.setObjectName("menuVidsurveil")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAdd_Files = QtWidgets.QAction(MainWindow)
        self.actionAdd_Files.setObjectName("actionAdd_Files")
        #self.actionAdd_Files.triggered.connect(self.showDialog())
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionLicense)
        self.menuFiles.addAction(self.actionAdd_Files)
        self.menuVidsurveil.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuVidsurveil.menuAction())
        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#faf0f2;\">⬤</span><span style=\" color:#ee5262;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">Combined     </span><span style=\" color:#ff9696;\">⬤</span><span style=\" color:#96ff96;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">Model 1</span><span style=\" font-size:20pt; color:#000000; vertical-align:sub;\">      </span><span style=\" color:#96ff96;\">⬤</span><span style=\" font-size:20pt; color:#ee5262; vertical-align:sub;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">Model 2     </span><span style=\" color:#9696ff;\">⬤</span><span style=\" color:#ee5262;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">Model 3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#000000; vertical-align:sub;\"><br /></p></body></html>"))
        self.push_extract_1.setText(_translate("MainWindow", "Extract Videos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Original Videos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Extracted Videos"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuVidsurveil.setTitle(_translate("MainWindow", "Vidsurveil"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionAdd_Files.setText(_translate("MainWindow", "Add Files"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
   
    def draw_miniview(self,dir):
        scene = QGraphicsScene(self)
        image = self.show_miniview(dir)
        #self.imgQ = ImageQt.ImageQt(image)
        img = QImage(image.data,image.shape[1],image.shape[0],QImage.Format_RGB888)
        pixMap =  QPixmap.fromImage(img)
        item = QGraphicsPixmapItem(pixMap)
        scene.addItem(item)
        self.mini_view_1.setScene(scene)
    
    def show_miniview(self,dir):
        f = cv2.VideoCapture(dir)
        total_frames = f.get(cv2.CAP_PROP_FRAME_COUNT)
        frame_rate = f.get(cv2.CAP_PROP_FPS)
        total_length = int(total_frames/frame_rate)
        print('total frames:{}, frame_rate :{} '.format(total_frames,frame_rate))
        print('total length:{} '.format(total_length))
        print(f.get(cv2.CAP_PROP_POS_FRAMES))
        # the size will be 80*80*11 (width 80, length 80, 11 images)
        interval = int(total_frames/11)
        frame_list = []
        for i in range(0,11):
            f_num = i*interval
            f.set(cv2.CAP_PROP_POS_FRAMES,f_num)
            ret,frame = f.read()
            assert ret
            frame_list.append(cv2.resize(frame,(81,81)))
        frame_concat = cv2.hconcat(frame_list)
        return frame_concat

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
