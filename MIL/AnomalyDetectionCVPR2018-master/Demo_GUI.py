from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.regularizers import l2
from keras.optimizers import SGD ,Adagrad
from scipy.io import loadmat, savemat
from keras.models import model_from_json
import theano.tensor as T
import theano
import csv
import configparser
import collections
import time
import csv
from math import factorial
import os
from os import listdir
import skimage.transform
from skimage import color
from os.path import isfile, join
import numpy as np
import numpy
from numpy import matlib
from datetime import datetime
from scipy.spatial.distance import cdist,pdist,squareform
import theano.sandbox
import codecs

#import c3D_model
#import Initialization_function
#from moviepy.editor import VideoFileClip
#from IPython.display import Image, display
import matplotlib.pyplot as plt
import cv2
import os, sys
import pickle
from PyQt5 import QtWidgets   # If PyQt4 is not working in your case, you can try PyQt5, 
seed = 7
numpy.random.seed(seed)
from keras import backend as K
import os
import math
#import time_merge
import glob
import shutil
import subprocess
import decimal

total_frame=0
time_series=[]
final_time_series=[]

def save_video(save_path,video_path,frame_list):
    temp_path= save_path
    file_name = video_path.split('/')[-1]
    file_name = file_name.split('.')[0]
    '''
    if not os.path.isdir(temp_path):
        os.mkdir(temp_path)
    result_path='./result/'
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
    '''
    fps = 30
    print("frame_list : ",frame_list)
    print("video_path : "+video_path)
    
    frame_to_seconds = []
    frame_to_seconds.append("timestamps in seconds")
    for each_framelists in frame_list:
        start_frame = decimal.Decimal(each_framelists[0]/fps)
        end_frame = decimal.Decimal(each_framelists[1]/fps)
        frames_to_string = '[' + str('{:.2f}'.format(start_frame)) + ',' + str('{:.2f}'.format(end_frame)) + ']'
        frame_to_seconds.append(frames_to_string)
    
    #print(frame_to_seconds)
    
    #'i' is the wanomaly video number 
    i=0  
    for frame_set in frame_list: 
        #print('frame set :', frame_set)
        #frame to time
        frame_set[1]=(frame_set[1]-frame_set[0])/fps
        frame_set[0]/=fps
        #ffmpeg video extractiont
        result=subprocess.Popen(['ffmpeg','-y','-ss',str(frame_set[0]),'-i',video_path, '-t',str(frame_set[1]), '-c', 'copy', save_path+file_name+str(i).zfill(4)+'.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)  
        output = result.communicate()
        print(output)
        result.wait()
        i+=1
   
   

    
    timestamp_name = file_name + '.txt'
    
    print(timestamp_name)

    timestamp_path = save_path + timestamp_name

    print(timestamp_path)

    with open(timestamp_path,"w") as f:
        for i in frame_to_seconds:
            
            f.write(str(i))
            print(str(i))

    print('save_video done')
    
    return

def set_keras_backend(backend):

    if K.backend()!=backend:
        os.environ['KERAS_BACKEND']=backend
        importlib.reload(K)
        assert K.backend()==backend

    
set_keras_backend("theano")

def load_model(json_path):
    model = model_from_json(open(json_path).read())
    return model

def load_weights(model, weight_path):
    dict2 = loadmat(weight_path)
    dict = conv_dict(dict2)
    i = 0
    for layer in model.layers:
        weights = dict[str(i)]
        layer.set_weights(weights)
        i += 1
    return model

def conv_dict(dict2): # Helper function to save the model
    i = 0
    dict = {}
    for i in range(len(dict2)):
        if str(i) in dict2:
            if dict2[str(i)].shape == (0, 0):
                dict[str(i)] = dict2[str(i)]
            else:
                weights = dict2[str(i)][0]
                weights2 = []
                for weight in weights:
                    if weight.shape in [(1, x) for x in range(0, 5000)]:
                        weights2.append(weight[0])
                    else:
                        weights2.append(weight)
                dict[str(i)] = weights2
    return dict


def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    #try:
    window_size = np.abs(np.int(window_size))
    order = np.abs(np.int(order))
    #except ValueError, msg:
    #    raise ValueError("window_size and order have to be of type int")

    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")

    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")

    order_range = range(order + 1)

    half_window = (window_size - 1) // 2
    b = np.mat([[k ** i for i in order_range] for k in range(-half_window, half_window + 1)])
    m = np.linalg.pinv(b).A[deriv] * rate ** deriv * factorial(deriv)
    firstvals = y[0] - np.abs(y[1:half_window + 1][::-1] - y[0])
    lastvals = y[-1] + np.abs(y[-half_window - 1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve(m[::-1], y,mode='valid')






# Load Video

def load_dataset_One_Video_Features(Test_Video_Path):
    
    print(Test_Video_Path)
    VideoPath =Test_Video_Path
    f = open(VideoPath, "r")
    #words = ''
    #with codecs.open(VideoPath,'r') as f:
    words = f.read().split()
    #words = words.encode('us-ascii')
    num_feat = len(words) /4096
    # Number of features per video to be loaded. In our case num_feat=32, as we divide the video into 32 segments. Npte that
    # we have already computed C3D features for the whole video and divide the video features into 32 segments.

    count = -1;
    VideoFeatues = []
    for feat in range(0, int(num_feat)):
        feat_row1 = np.float32(words[feat * 4096:feat * 4096 + 4096])
        count = count + 1
        if count == 0:
            VideoFeatues = feat_row1
        if count > 0:
            VideoFeatues = np.vstack((VideoFeatues, feat_row1))
    AllFeatures = VideoFeatues

    return  AllFeatures

#class PrettyWidget(QtWidgets.QWidget):
class PrettyWidget():
    #def __init__(self):
        #super(PrettyWidget, self).__init__()
        #self.initUI()

    def __init__(self):
        #self.setGeometry(500, 100, 500, 500)
        #self.setWindowTitle('Anomaly Detection')
        #btn = QtWidgets.QPushButton('ANOMALY DETECTION SYSTEM \n Please select video', self)

        Model_dir = os.getcwd()
        weights_path = Model_dir + '/weights_L1L2.mat'
        model_path = Model_dir + '/model.json'
        ########################################
        ######    LOAD ABNORMALITY MODEL   ######
        global model
        model = load_model(model_path)
        load_weights(model, weights_path)

        #####   LOAD C3D Pre-Trained Network #####
       # global score_function
       # score_function = Initialization_function.get_prediction_function()

        global time_series
        global total_frame
         
        time_series = []
        #save_path = '/home/callbarian/C3D/saved_videos/'
        #original_path = '/home/callbarian/C3D/moved_videos/'
        #btn.resize(btn.sizeHint())
        feature_path = os.getcwd()+'/Test/test'
        gt_path = './Test/gt_test'
        feature_list = sorted(os.listdir(feature_path))
        gt_list = sorted(os.listdir(gt_path))
        for feature,gt in zip(feature_list,gt_list):
            #video_format = ''
            #for file2 in os.listdir("/home/callbarian/C3D/videos/" + file):
                #if(file2.split('.')[1] != 'txt'):
                    #video_format = file2
                #read_file = "/home/callbarian/C3D/videos/"+ file + "/" + file2  
                single_feature = os.path.join(feature_path,feature)
                single_gt = os.path.join(gt_path,gt)
                self.SingleBrowse(single_feature,single_gt)
                #btn.move(150, 200)
                #self.show() #uncomment if want to pop up the GUI Window
           # video_format = '.' + video_format.split('.')[1]    
            #print("video format : " + video_format)
            #video_path = original_path + file + video_format   
            #save_video(save_path,video_path,time_series)
            #print(time_series)
            #time_series = []
            #total_frame = 0    
        #time_series=time_merge.time_stamp(total_frame,time_series)
        #print("time series : ",time_series)
        
       #save_video(save_path,time_series)
       # btn.clicked.connect(self.SingleBrowse)
       # btn.move(150, 200)
       #  self.show()







    def SingleBrowse(self,single_feature,single_gt):
        global total_frame
        #verify_path = video_path[-4:]
        #print(verify_path)
        #if(verify_path==".txt"):
        #        print("skipping.........................")
        #        return
        #print(video_path)
        #cap = cv2.VideoCapture(video_path)
        #Total_frames = cap.get(cv2.CV_CAP_PROP_FRAME_COUNT)
        #print(cv2)
        #FeaturePath=(video_path)
        file_name = single_feature[0:-4]
        file_name = file_name.split('/')[-1]

        root_feature_path = './Test/test'
        save_path = './Model_Res/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)        
        #Feature_name = FeaturePath.split('/')[-1]
        #FeaturePath = root_feature_path + Feature_name + '.txt'
        inputs = load_dataset_One_Video_Features(single_feature)
        #Total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        gt_data = np.load(single_gt)
        Total_frames = len(gt_data)
        total_segments = np.linspace(1, Total_frames, num=len(inputs)+1)
        total_segments = total_segments.round()
        #inputs = np.reshape(inputs, (32, 4096))
        predictions = model.predict_on_batch(inputs)
        
        #print("line 288. predictions: {}, inputs: {}, total_segnments".format(len(predictions),len(inputs),len(total_segments)))
        #print("predictions: ",predictions)
        Frames_Score = []
        count = -1;
        for iv in range(0, len(inputs)):
            F_Score = np.matlib.repmat(predictions[iv],1,(int(total_segments[iv+1])-int(total_segments[iv])))
            count = count + 1
            if count == 0:
              Frames_Score = F_Score
            if count > 0:
              Frames_Score = np.hstack((Frames_Score, F_Score))
        
        scores = Frames_Score
        scores1=scores.reshape((scores.shape[1],))
        print('len of gt: ',len(gt_data))
       #print('len of scores before savitzky golay {}'.format(len(scores1)))
        scores1 = savitzky_golay(scores1, 101, 3)
        print('len of scores after savitzky golay {}'.format(len(scores1)))
        savemat(save_path+file_name+'.mat',{'Score':scores1})
        print("saving {}.mat".format(file_name))
        
        '''
        cap = cv2.VideoCapture((video_path))
        while not cap.isOpened():
            cap = cv2.VideoCapture((video_path))
            cv2.waitKey(1000)
            print ("Wait for the header")

        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        Total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        print ("Anomaly Prediction")
        x = np.linspace(1, Total_frames, Total_frames)
        scores = Frames_Score
        scores1=scores.reshape((scores.shape[1],))
        scores1 = savitzky_golay(scores1, 101, 3)
        plt.close()
        break_pt=min(scores1.shape[0], x.shape[0])
        plt.axis([0, Total_frames, 0, 1])
        i=0;
        
        Anomaly_Detected = 0
        flag = Total_frames
        print(Total_frames)
        #temp,flag,anomaly_start,anomaly_finish  is list of the frame that present the anomaly
        flag_of_frame=0
        anomaly_start=0
        anomaly_finish=0
        temp=[]
        while True:
            #flag, frame = cap.read()
            flag = flag - 1
            #print(flag)
            if flag>0:
                i = i + 1
                #cv2.imshow('video', frame)
               
                sensitivity=0.4
                #if the score >=0.4, we append the frame number of the video to the list temp.
                if scores1[i-1]>=sensitivity and flag_of_frame==0:
                    flag_of_frame=1
                    anomaly_start=i-1+total_frame
                if scores1[i-1]<=sensitivity and flag_of_frame==1:
                    flag_of_frame=0
                    anomaly_finish=i-1+total_frame
                    time_series.append([int(anomaly_start),int(anomaly_finish)])
                

                jj=i%25
                if jj==1:
                    #if i>1:
                        #print(scores1[i-25:i])
                    plt.plot(x[:i], scores1[:i], color='g',marker="o",ms=5,mec="g",mfc="g", linewidth=3)
                    plt.draw()
                    plt.pause(0.000000000000000000000001)

                #pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                #print (str(pos_frame) + " frames")
            else:
                # The next frame is not ready, so we try to read it again
                pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame - 1)
                print("frame is not ready")
                # It is better to wait for a while for the next frame to be ready
                cv2.waitKey(1000)
            if flag<0:
                break
            if cv2.waitKey(10) == 27:
                break
            if cap.get(cv2.CAP_PROP_POS_FRAMES)== break_pt:
                #cap.get(cv2.CAP_PROP_FRAME_COUNT):
                # If the number of captured frames is equal to the total number of frames,
                # we stop
                break

        
        total_frame+=i
        print(time_series)
        print("total frame : ", total_frame)
        '''
        
def main():
    #app = QtWidgets.QApplication(sys.argv)
    w = PrettyWidget()
    #app.exec_()


main()

'''
                if(scores1[i-1]>0.4):
                    #print("Anomaly Detected......")
                    Anomaly_Detected = Anomaly_Detected + 1
                    #print("Anomaly Detected: "+ str(Anomaly_Detected))
                    if(Anomaly_Detected==1):
                        os.popen('cp '+ video_path + ' /home/callbarian/C3D/saved_videos/')
                        print("Anomaly Detected.........")

'''
