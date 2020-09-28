import sys
import os
import cv2
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

from PyQt5 import QtCore, QtGui, QtWidgets
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
            self.draw_miniview(self.path_name[i])

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)

    def draw_miniview(self,dir):
        scene = QGraphicsScene(self)
        image = self.show_miniview(dir)
        #self.imgQ = ImageQt.ImageQt(image)
        #print(image.shape[1],image.shape[0])
        img = QImage(image.data,image.shape[1],image.shape[0],QImage.Format_RGB888).rgbSwapped()
        pixMap =  QPixmap.fromImage(img)
        item = QGraphicsPixmapItem(pixMap)
        scene.addItem(item)
        self.ui.mini_view_1.setScene(scene)
        self.ui.mini_view_2.setScene(scene)
    
    def show_miniview(self,dir):
        f = cv2.VideoCapture(dir)
        total_frames = f.get(cv2.CAP_PROP_FRAME_COUNT)
        frame_rate = f.get(cv2.CAP_PROP_FPS)
        total_length = int(total_frames/frame_rate)
        print('total frames:{}, frame_rate :{} '.format(total_frames,frame_rate))
        print('total length:{} '.format(total_length))
        #print(f.get(cv2.CAP_PROP_POS_FRAMES))
        # the size will be 80*80*11 (width 80, length 80, 11 images)
        interval = int(total_frames/11)
        frame_list = []
        for i in range(0,11):
            f_num = i*interval
            f.set(cv2.CAP_PROP_POS_FRAMES,f_num)
            ret,frame = f.read()
            assert ret
            frame_list.append(cv2.resize(frame,(80,80)))
        frame_concat = cv2.hconcat(frame_list)
        return frame_concat

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # window.show()
    window = MainWindow()
    sys.exit(app.exec_())


