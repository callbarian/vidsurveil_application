import os
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPen, QBrush
from PyQt5.Qt import Qt
from PyQt5 import QtCore

class Miniview():
    def __init__(self):
        self.scene = QGraphicsScene()
    def draw_anomalous_time(self,time_frame,total_frames):
        time_frame = time_frame.reshape(-1,2)
        #self.scene.setSceneRect(0,0,894,24)
        
        self.scene.addRect(int(886*time_frame[0,0]/total_frames),0,int(886*(time_frame[0,1]-time_frame[0,0])/total_frames),20,QPen(Qt.red),QBrush(Qt.red))
        
        #for i,time in enumerate(time_frame):
            
            # the length of timeline container is 894
            #self.scene.addRect(int(1000*time[0]/total_frames),0,int(1000*(time[1]-time[0])/total_frames),20,QPen(Qt.red),QBrush(Qt.red))
        return self.scene

    def draw_miniview(self,dir):
        image = self.show_miniview(dir)
        #self.imgQ = ImageQt.ImageQt(image)
        #print(image.shape[1],image.shape[0])
        img = QImage(image.data,image.shape[1],image.shape[0],QImage.Format_RGB888).rgbSwapped()
        pixMap =  QPixmap.fromImage(img)
        item = QGraphicsPixmapItem(pixMap)
        self.scene.addItem(item)
        return self.scene
        
    def cal_timeline(self,dir):
        f = cv2.VideoCapture(dir)
        total_frames = f.get(cv2.CAP_PROP_FRAME_COUNT)
        frame_rate = f.get(cv2.CAP_PROP_FPS)
        total_length = int(total_frames/frame_rate)

        time_list = []
        time_interval =int(total_frames/4)
        for i in range(0,4):
            time_list.append(int(i*time_interval/frame_rate))
        time_list.append(int(total_frames/frame_rate))

        return time_list
        
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
