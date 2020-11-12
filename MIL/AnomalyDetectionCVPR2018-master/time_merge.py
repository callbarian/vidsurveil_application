import cv2 
import numpy as np
import glob
import shutil
import os

# Python3 program to merge overlapping Intervals  
# in O(n Log n) time and O(1) extra space 
def mergeIntervals(arr): 
    # Sorting based on the increasing order  
    # of the start intervals 
    arr.sort(key = lambda x: x[0])  
    
        # array to hold the merged intervals 
    m = []  
    s = -10000
    max = -100000
    for i in range(len(arr)): 
        a = arr[i] 
        if a[0] > max: 
            if i != 0:  
                m.append([s,max]) 
            max = a[1] 
            s = a[0] 
        else: 
            if a[1] >= max: 
                max = a[1] 
    
        #'max' value gives the last point of  
        # that particular interval 
        # 's' gives the starting point of that interval 
        # 'm' array contains the list of all merged intervals 
  
    if max != -100000 and [s, max] not in m:  
        m.append([s, max]) 
    ''' 
    print("The Merged Intervals are :", end = " ") 
    for i in range(len(m)): 
        print(m[i], end = " ")
    ''' 
    return m


def time_stamp(Total_frames,frame_list):
    #Open the Video file
    #cap=cv2.VideoCapture(video_path)
    #Total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#for each section of the anomaly, expended the time of the video before and after
    time=30*1
    for i in range (len(frame_list)):
        if frame_list[i][0]-time >= 0:
            frame_list[i][0]-=time
        if frame_list[i][0]+time <= Total_frames:
            frame_list[i][1]+=time

#merge the all the Intervals.
    #print(frame_list)
    m=mergeIntervals(frame_list) 
    #print("sorted list of the frame_list :",m)
    return m
