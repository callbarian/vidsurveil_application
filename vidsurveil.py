import sys
import os
import cv2
from miniview import Miniview
from MIL.Codes.mil import MIL
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

        #where to save result videos
        self.save_dir = os.getcwd()+'/save_dir'
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        ##---------------MIL begin------------------##
        # temporary directory to process files (MIL)
        self.temp_dir_MIL = os.getcwd()+'/MIL/temp_dir'
        if not os.path.exists(self.temp_dir_MIL):
            os.makedirs(self.temp_dir_MIL)
        
        # environment for c3d
        self.env_path_c3d = '/home/callbarian/bin/miniconda3/envs/c3d_py36/bin/python'
        

        # environment for MIL(AnomalyDetection)
        self.env_path_mil = '/home/callbarian/bin/miniconda3/envs/Anomaly_py36/bin/python'

        #run model
        self.ui.run_mil_button.pressed.connect(self.run_mil)

        ##---------------MIL end------------------##

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
        
        self.ui.video_player.resize(420,210)
        self.ui.playButton.pressed.connect(self.play)
        self.ui.pauseButton.pressed.connect(self.pause)
        self.ui.stopButton.pressed.connect(self.stop)
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
            view = Miniview()
            self.scene = view.draw_miniview(self.path_name[i])
            self.ui.mini_view_1.setScene(self.scene)
            self.ui.mini_view_2.setScene(self.scene)
            time_line = view.cal_timeline(self.path_name[i])
            print('time line: {}'.format(time_line))
            self.ui.lcdNumber_1.display(str(int(time_line[0]/60))+':'+str(int(time_line[0]%60)))
            self.ui.lcdNumber_2.display(str(int(time_line[1]/60))+':'+str(int(time_line[1]%60)))
            self.ui.lcdNumber_4.display(str(int(time_line[2]/60))+':'+str(int(time_line[2]%60)))
            self.ui.lcdNumber_5.display(str(int(time_line[3]/60))+':'+str(int(time_line[3]%60)))
            self.ui.lcdNumber_6.display(str(int(time_line[4]/60))+':'+str(int(time_line[4]%60)))

            fileName = self.path_name[i]
            url = QtCore.QUrl.fromLocalFile(fileName)
            self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(url))
            
         

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)

    def run_mil(self):
        assert self.path_name,'please select file first!'
        mil = MIL(self.path_name,self.temp_dir_MIL,self.save_dir,self.env_path_c3d,self.env_path_mil)
        #mil.preprocess()
        #mil.run_C3D()
        mil.run_MIL()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # window.show()
    window = MainWindow()
    sys.exit(app.exec_())


