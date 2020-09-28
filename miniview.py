import os
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class Miniview():
    def __init__(self):
        self.scene = QGraphicsScene()
    def draw_miniview(self,dir):
        image = self.show_miniview(dir)
        #self.imgQ = ImageQt.ImageQt(image)
        #print(image.shape[1],image.shape[0])
        img = QImage(image.data,image.shape[1],image.shape[0],QImage.Format_RGB888).rgbSwapped()
        pixMap =  QPixmap.fromImage(img)
        item = QGraphicsPixmapItem(pixMap)
        self.scene.addItem(item)
        return self.scene
        
    
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
