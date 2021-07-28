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

    window_size = np.abs(np.int(window_size))
    order = np.abs(np.int(order))

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
    
    #print(Test_Video_Path)
    VideoPath =Test_Video_Path
    f = open(VideoPath, "r")


    words = f.read().split()

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


class PrettyWidget():
    def __init__(self):
        Model_dir = os.getcwd()+'/MIL/AnomalyDetectionCVPR2018-master'

        weights_path = Model_dir + '/weights_L1L2.mat'
        model_path = Model_dir + '/model.json'
        ########################################
        ######    LOAD ABNORMALITY MODEL   ######
        global model
        model = load_model(model_path)
        load_weights(model, weights_path)
        
        temp_dir = os.getcwd()+'/MIL/temp_dir'



        video_dir = sorted(os.listdir(temp_dir))

        
        # array of anomalous frames
        anomaly_arr = []
        for video in video_dir:
            if os.path.exists(os.path.join(temp_dir,video,'MIL_'+video+'.npy')):
                continue
            # for each original videos, process and retrieve anamolous frames
            files = sorted(os.listdir(os.path.join(temp_dir,video)))
            total_frame_arr = [] # count how many segments to analyze
            total_frame_arr.append(0) # initialize as 0
            anomalous_frames = [] # array for anomalous_frames
            for file in files:
                original_path = ""
                if file.split('.')[0] == video:
                    original_path = os.path.join(os.path.join(temp_dir,video,file)) 
                elif file.split('.')[1] != 'mp4':   
                    continue
                else:
                    self.SingleBrowse(os.path.join(os.path.join(temp_dir,video,file)),total_frame_arr,anomalous_frames)
            
            if any(anomalous_frames):
                anomaly_arr.append(anomalous_frames)
        
            if np.any(anomaly_arr):
                save_dir = os.getcwd()+'/save_dir/'+video
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                np.save(save_dir+'/MIL_'+video+'.npy',np.array(anomaly_arr))
                #btn.move(150, 200)
                #self.show() #uncomment if want to pop up the GUI Window
            
            #save_video(save_path,video_path,time_series)
            #print(time_series)
            #time_series = []
            #total_frame = 0    
        #time_series=time_merge.time_stamp(total_frame,time_series)
        #print("time series : ",time_series)
        
       
       # btn.clicked.connect(self.SingleBrowse)
       # btn.move(150, 200)
       #  self.show()




    def SingleBrowse(self,single_video,total_frame_arr,anomalous_frames):

        # where to save result videos(anomalous videos)
        save_path = os.getcwd()+'/save_dir'

        if not os.path.exists(save_path):
            os.makedirs(save_path) 

        single_feature = single_video.split('.')[0] + '.txt'
       
       
        inputs = load_dataset_One_Video_Features(single_feature)

        cap = cv2.VideoCapture(single_video)
        Total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print('frames of this segment: {}\n'.format(Total_frames))
        
        total_segments = np.linspace(1, Total_frames, num=len(inputs)+1)
        total_segments = total_segments.round()
        total_segments[-1] = total_segments[-1]+1
        #inputs = np.reshape(inputs, (32, 4096))
        predictions = model.predict_on_batch(inputs)
        
        
        #print("predictions: ",predictions)
        Frames_Score = []
        count = -1
        for iv in range(0, len(inputs)):
            F_Score = np.matlib.repmat(predictions[iv],1,(int(total_segments[iv+1])-int(total_segments[iv])))
            count = count + 1
            if count == 0:
              Frames_Score = F_Score
            if count > 0:
              Frames_Score = np.hstack((Frames_Score, F_Score))
        
        scores = Frames_Score
        scores1=scores.reshape((scores.shape[1],))
        
        
       #print('len of scores before savitzky golay {}'.format(len(scores1)))
        scores1 = savitzky_golay(scores1, 101, 3)
        #print('len of scores after savitzky golay {}\n'.format(len(scores1)))
        #savemat(save_path+file_name+'.mat',{'Score':scores1})
        #print("saving {}.mat".format(file_name))
        
        '''
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

        print ("Anomaly Prediction")
        x = np.linspace(1, Total_frames, Total_frames)
        scores = Frames_Score
        scores1=scores.reshape((scores.shape[1],))
        scores1 = savitzky_golay(scores1, 101, 3)
        plt.close()
        break_pt=min(scores1.shape[0], x.shape[0])
        plt.axis([0, Total_frames, 0, 1])
        '''

        #anomaly_start,anomaly_finish is the beginning and the end frame that present the anomaly
        flag_of_frame=0
        anomaly_start=0
        anomaly_finish=0
        for i in range(Total_frames):
            sensitivity=0.4
            #if the score >=0.4, we append the frame number of the video to the list temp.
            if scores1[i]>=sensitivity and flag_of_frame==0:
                flag_of_frame = 1
                anomaly_start = sum(total_frame_arr) + i
                print('anomaly found! begining frame: {}'.format(anomaly_start))
            if scores1[i]<=sensitivity and flag_of_frame==1:
                flag_of_frame = 0
                anomaly_finish = sum(total_frame_arr) + i
                print('anomaly ended! end frame: {}'.format(anomaly_finish))
                # append anomalous frames
                anomalous_frames.append([anomaly_start,anomaly_finish])
       
        total_frame_arr.append(Total_frames)
    
        
def main():
    #app = QtWidgets.QApplication(sys.argv)
    w = PrettyWidget()
    #app.exec_()


main()

