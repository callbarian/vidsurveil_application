import os
import cv2
import numpy as np
import subprocess
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
        
        #self.scene.addRect(int(886*time_frame[0,0]/total_frames),0,int(886*(time_frame[0,1]-time_frame[0,0])/total_frames),20,QPen(Qt.red),QBrush(Qt.red))
        mat = np.zeros((18,880,3),np.uint8)
       
        for i,time in enumerate(time_frame):
            if i==0:
                # the length of timeline container is 894
                start_frame = int(880*time[0]/total_frames)
                end_frame = int(880*time[1]/total_frames)
                
                pixels = [255,0,0]  # red,green,blue
                for j,pixel in enumerate(pixels):
                    mat[:18,start_frame:end_frame+1,j] = pixel
                
                if time[0]>0:
                    # draw white for previous frame if first start_frame is bigger than 0
                    mat[:18,0:start_frame-1,:] = 255
                
            else:
                # the length of timeline container is 894
                start_frame = int(880*time[0]/total_frames)
                end_frame = int(880*time[1]/total_frames)
                
                pixels = [255,0,0] # red,green,blue
                for j,pixel in enumerate(pixels):
                    mat[:18,start_frame:end_frame+1,j] = pixel
                
                # draw white for previous empty timeline
                end_frame = int(880*time_frame[i-1,1]/total_frames) + 1 # previous end frame +1
                start_frame = int(880*time[0]/total_frames) - 1 # current start frame -1
                # white is [255,255,255] but rgbwill be swapped
                mat[:18,end_frame:start_frame,:] = 255

        img = QImage(mat,mat.shape[1],mat.shape[0],QImage.Format_RGB888).rgbSwapped()
        pixMap =  QPixmap.fromImage(img)
        item = QGraphicsPixmapItem(pixMap)
        self.scene.addItem(item)
        return self.scene

    def merge_frame(self,curr_fileName,npy_merge,interval=500):
        # find fps
        result = subprocess.Popen(['ffprobe','-v','error','-select_streams','v','-of','default=noprint_wrappers=1:nokey=1','-show_entries','stream=r_frame_rate',curr_fileName],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
        out = result.communicate()
        message = out[0].decode()
        message = message.split('\n')[0]
        fps = int(message.split('/')[0])/int(message.split('/')[1])
        print('fps: ',fps)
        # initial start and end frame
        final_time = []
        start_frame = npy_merge[0,0]
        end_frame = npy_merge[0,1]

        added_frame = 0
        for i in range(1,len(npy_merge)):
            if (npy_merge[i,0] - start_frame)  > (interval+added_frame):
                # if the difference of start frames are more than 
                #    interval (default=500) frames, then they are regarded as independent(different) incidents
                final_time.append([start_frame,end_frame])
                start_frame = npy_merge[i,0]
                end_frame = npy_merge[i,1]

                # reset added_frame 
                added_frame = 0
            # the most inclusive end frame to include as many incidents(frames)
            elif npy_merge[i,1] > end_frame:
                end_frame = npy_merge[i,1]
                added_frame += npy_merge[i,0]-npy_merge[i-1,0]
            # add frame to allow including consecutive events.    
            print('start frame: {}, end frame: {}, added_frame: {},total_frame: {}'.format(start_frame,end_frame,added_frame,final_time))
        final_time.append([start_frame,end_frame])
        final_time = np.array(final_time)
        
        return fps,final_time

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
