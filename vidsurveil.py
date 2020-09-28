import sys
import os
#<<<<<<< HEAD

#=======
import cv2
from miniview import Miniview
#>>>>>>> 8b7e21e4060da98acf4aee3b5536a2a4c37b737d
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication
'''

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    h, r = divmod(ms, 36000)
    m, r = divmod(r, 60000)
    s, _ = divmod(r, 1000)
    return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)

    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.path_name=[]
        #start
        self.player = QMediaPlayer()

        self.player.error.connect(self.erroralert)
        self.player.play()

        # Setup the playlist.
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)        

        # Set the model
        self.model = PlaylistModel(self.playlist)
        self.ui.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.ui.playlistView.selectionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)



        #print('@@@ui type is ',type(self.ui.actionAdd_Files))  
        #self.ui.~~~
        self.ui.actionAdd_Files.triggered.connect(self.open_file)
        self.show()


        #Adding Video Widget--------------------------#

        self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        self.mediaPlayer.setVideoOutput(self.ui.video_player)
        # fileName = "/Users/chan/Desktop/Anomaly_Detection/app/3.mp4"
        # url = QtCore.QUrl.fromLocalFile(fileName)
        # #url = QtCore.QUrl("http://clips.vorwaerts-gmbh.de/VfE_html5.mp4")
        # self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
        # self.mediaPlayer.play()

        #videoWidget = QVideoWidget()
        #layout = QVBoxLayout()
        #self.viewer.setCentralWidget(videoWidget)
        #self.player.setVideoOutput(videoWidget)

        
        #layout.addWidget(videoWidget)
        #layout.addLayout(controlLayout)
        #layout.addWidget(self.errorLabel)
        #self.centralwidget = QtWidgets.QWidget(mainwindow)
        #self.centralwidget.setObjectName("centralwidget")
        #self.widget = QVideoWidget(self.centralwidget)
        #self.widget.setGeometry(QtCore.QRect(20, 10, 241, 221))
        #self.widget.setObjectName("widget")

        #self.pause_button = QPushButton()
        #self.pause_button.setEnabled(False)
        #self.pause_button.clicked.connect(self.pause)

        #self.ui.pause_button.mousePressEvent = self.pause
        #self.ui.pauseButton.clicked.connect(self.pause)
        self.ui.playButton.pressed.connect(self.play)
        self.ui.pauseButton.pressed.connect(self.pause)
        self.ui.stopButton.pressed.connect(self.stop)
        #self.ui.muteButton.pressed.connect(self.mute(switch=True))
       #self.ui.volumeButton.pressed.connect(self.mute(switch=False))

        #Till here------------------------------------#

    def pause(self):
        self.mediaPlayer.pause()

    def play(self):
        self.mediaPlayer.play()

    def stop(self):
        self.mediaPlayer.stop()
    
    #Resume from here
    def mute(self,switch=False):
        self.mediaPlayer.setMuted(switch)

    def open_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "videos")
        print(path)
        while path:
            video=path.pop()
            self.path_name.append(video)
            self.playlist.addMedia(
                QMediaContent(
                    QUrl.fromLocalFile(video)
                )
            )

        self.model.layoutChanged.emit()        


    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.model.layoutChanged.emit()

        # If not playing, seeking to first of newly added + play.
        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            self.player.play()


    def update_duration(self, duration):
        print("!", duration)
        print("?", self.player.duration())

        self.timeSlider.setMaximum(duration)

        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))

        # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        # We receive a QItemSelection from selectionChanged.
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.ui.playlistView.setCurrentIndex(ix)
            const=self.model.playlist.media(i)
            print(self.path_name[i])
            self.scene = Miniview().draw_miniview(self.path_name[i])
            self.ui.mini_view_1.setScene(self.scene)
            self.ui.mini_view_2.setScene(self.scene)
            fileName = self.path_name[i]
            url = QtCore.QUrl.fromLocalFile(fileName)
            self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
            #self.mediaPlayer.play()

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # window.show()
    window = MainWindow()
    sys.exit(app.exec_())


