#!/usr/bin/env python

'''
Extract C3D features as a csv file from a given video, 
'''

import numpy as np
import sys
import os
from os import path
import subprocess
import array
import cv2
import shutil
import errno
import PyQt5
import functools
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

def clickable(widget):

    class Filter(QObject):

        clicked = pyqtSignal()
         
        def eventFilter(self, obj, event):
            
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
           
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

click = '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/file_dialog.ui'
#click = '/Users/iseongmin/Downloads/gui/application.ui'
class vidsurveil(QDialog):
    def __init__(self):
        #super().__init__()
        QDialog.__init__(self, None)
        #QDialog.__init__(self, None)
        uic.loadUi(click, self)

       
        clickable(self.label_2).connect(self.logo)
        clickable(self.label_3).connect(self.select_Files)
        clickable(self.label_4).connect(self.prepare_videos)
        clickable(self.label_5).connect(self.extract_features)

        #layout = QGridLayout(self)
        #layout.addWidget(self.label_2)
        layout2 = self.verticalLayout_22
        layout3 = self.verticalLayout_3
        layout4 = self.verticalLayout_4
        layout5 = self.verticalLayout_5
        
        layout2.addWidget(self.label_2)
        layout3.addWidget(self.label_3)
        layout4.addWidget(self.label_4)
        layout5.addWidget(self.label_5)
        
        

    def logo(self):
        print("")

    def select_Files(self):
        fname = QFileDialog.getOpenFileName(self)

        #label.setText(fname[0])
        result = subprocess.Popen(['cp', fname[0], '/home/callbarian/C3D/videos'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #result = subprocess.Popen(['cp', fname[0], '/Users/iseongmin/Downloads/qt_projects/project_python_qt'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()
        result_message = out[0].decode()

        #if no error message is returned, then the string should be empty
        if fname[0]:
            if not result_message.strip():
                msg = QMessageBox()
                msg.setWindowTitle("Move Success")
                msg.setText("Files has been successfully moved!")
                msg.setStandardButtons(QMessageBox.Ok)
                x = msg.exec_()
        
    def prepare_videos(self):
        print("preparing videos.......")
        run()

    def extract_features(self):
        count=0
        for file in os.listdir("/home/callbarian/C3D/videos"):
            if file==".DS_Store":
                continue
            for file2 in os.listdir("/home/callbarian/C3D/videos/"+file):
                read_file="/home/callbarian/C3D/videos/"+file+"/"
                write_file= file + "/"
                main_C3D(read_file,file2,write_file)
                print(count)
                count=count+1
        
        #print("extracting........")
        #os.system('sh ' + '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/feature_extraction.sh')
        #result = subprocess.Popen(['sh','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/call_environment.sh','/home/callbarian/bin/miniconda3/envs/c3d_py36/bin/python','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)


        #result = subprocess.Popen(['python', '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #(out, err) = result.communicate()
        #print(out)
        #result.wait()
        #os.popen('python ' + '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py')
        #print("this is after feature extraction....")
        #result_message = out[0]


        result = subprocess.Popen(['sh','/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/call_environment.sh','/home/callbarian/bin/miniconda3/envs/Anomaly_py36/bin/python','/home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        (out,err) = result.communicate()
        #print(out)
        result.wait()
        
         #result_message = out[0].decode()
#        if(result_message.split('::')[1]) is 'Anaconda, Inc.':
#            msg = QMessageBox()
#            msg.setWindowTitle("C3D to Anomaly")
#            msg.setText("switch environment successfully")
#            msg.setStandardButtons(QMessageBox.Ok)
#            x = msg.exec_()

        #result = subprocess.Popen(['python', '/home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
       # out = result.communicate()

##################################################################
#prepare video code section
def prepare_video(video_directory):
    
    #stream = os.popen("cd /home/callbarian/C3D/videos")

    for file in os.listdir(video_directory):
        name , extension = path.splitext(file)
        
        dir_path = video_directory +'/'+ name
        result = subprocess.Popen(['mkdir', dir_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
        
        result = subprocess.Popen(['mv',video_directory +'/'+file, dir_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
     

def split_video(video_directory,move_directory):
    success = 0 
    move_path = '/home/callbarian/C3D/moved_videos/'  
    for file in os.listdir(video_directory):
        for file2 in os.listdir(video_directory +'/'+ file):
            name , extension = path.splitext(file2)
                    
            save_path = video_directory +'/'+ name + '/' + name
            file_path= video_directory +'/'+ name + '/' + file2
            each_video_path = video_directory + '/' + name
 
            result = subprocess.Popen(['ffmpeg', '-i', file_path, '-vf', 'scale=240x320',save_path + '_resize.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            output = result.communicate()
            print(output) 
            result.wait() 

            result = subprocess.Popen(['mv', file_path, move_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            result.wait()
            
            resized_path = save_path + '_resize.mp4'
            
            result = subprocess.Popen(['mv', resized_path, file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            result.wait()
  
            #result = subprocess.Popen(['ffmpeg','-i',file_path, '-c', 'copy', '-map', '0', '-f' , 'segment', '-segment_time', '60','-reset_timestamps','1', '-segment_format_options', 'movflags=+faststart',save_path+'%03d.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #output = result.communicate()
            #print(output)
            #result.wait()

            #result = subprocess.Popen(['rm', file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            #result.wait()
                        
            for file3 in os.listdir(each_video_path):
                name , extension = path.splitext(file3)
                file_path= each_video_path + '/' + file3
                result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                out = result.communicate()
                
                print(file_path)
                print(out)
                result.wait()

                time = out[0].decode().split(':')
                minute = int(time[1])
                seconds = int(time[2].split('.')[0])

                if(seconds<30 and minute is 0):
                    print("executing concatenation.....")
                    empty_path = '/home/callbarian/C3D/empty_frame/Thief_resize001.jpg'
                    concat_path = each_video_path + '/concat_out.mp4'
                    print(concat_path)
                    print(file_path)

                    #command = 'ffmpeg -i ' + file_path + ' -loop 1 -framerate 25 -t 30 -i ' + empty_path + ' -filter_complex \"[0]scale=320x240,setsar=1[im];[1]scale=320x240,setsar=1[vid];[im][vid]concat=n=2:v=1:a=0\" ' + concat_path
                    #result = subprocess.Popen([command],shell=True,stdout=subprocess.PIPE)
                    #(out,err) = result.communicate()
                    #result.wait()
                                
                    #result = subprocess.Popen(['rm',file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    #(out,err) = result.communicate()
                    #result.wait()

                    #result = subprocess.Popen(['mv',concat_path,file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    #(out,err) = result.communicate()
                    #result.wait()
                    #print("processed: ",file_path)
            
            print("breaking through")
            break
     
    success = 1
    return success
                
       
def run():
    video_directory = "/home/callbarian/C3D/videos"
    #input video directory
    move_directory = "/home/callbarian/C3D/move_videos"
    #video directory that will copy your input video after processing
    prepare_video(video_directory)
 
    success = split_video(video_directory,move_directory)
    if success:
        print("video splition succeeded")
   





###################################################################
# Point to the C3D directory


#caffe_root = os.path.abspath(os.path.join(
#        os.path.dirname(os.path.realpath(__file__)),
#        '../..'
#        ))

caffe_root = '/home/callbarian/C3D/C3D-v1.0'


# GPU to use
gpu_id = 1

# 50 should be good for 6GB VRAM. Decrease as needed
batch_size = 50
###################################################################

def check_trained_model(trained_model):
    ''' Check if trained_model is there. otherwise, download '''

    if os.path.isfile(trained_model):
        print ("[Info] trained_model={} found. Good to go!")
    else:
        download_cmd = [
                "wget",
                "-O",
                trained_model,
                "https://www.dropbox.com/s/vr8ckp0pxgbldhs/conv3d_deepnetA_sport1m_iter_1900000?dl=0",
                ]

        print("[Info] Download Sports1m pre-trained model: \"{}\"".format(
                ' '.join(download_cmd)
                ))

        return_code = subprocess.call(download_cmd)

        if return_code != 0:
            print("[Error] Downloading of pretrained model failed. Check!")
            sys.exit(-10)
    return

def get_frame_count(video):
    ''' Get frame counts and FPS for a video '''
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print("[Error] video={} can not be opened.".format(video))
        sys.exit(-6)

    # get frame counts
    #num_frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    #fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)

    num_frames = int(cap.get(7))
    fps = cap.get(5)
    width = cap.get(3)   # float
    height = cap.get(4)
    # print("width = ",end='')
    # print(width)
    # print("height = ",end='')
    # print(height)
    # in case, fps was not available, use default of 29.97
    if not fps or fps != fps:
        fps = 29.97

    return num_frames, fps

def extract_frames(video, start_frame, frame_dir, num_frames_to_extract=16):
    ''' Extract frames from a video using opencv '''

    # check output directory
    if os.path.isdir(frame_dir):
        pass
        #print ("[Warning] frame_dir={} does exist. Will overwrite".format(frame_dir))
    else:
        os.makedirs(frame_dir)

    # get number of frames
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print ("[Error] video={} can not be opened.".format(video))
        sys.exit(-6)

    # move to start_frame
    cap.set(1, start_frame)

    # grab each frame and save
    for frame_count in range(num_frames_to_extract):
        frame_num = frame_count + start_frame
        #print ("{} ".format(frame_num),end='')
        ret, frame = cap.read()
        if not ret:
            print ("[Error] Frame extraction was not successful")
            sys.exit(-7)

        frame_file = os.path.join(
                frame_dir,
                '{0:06d}.jpg'.format(frame_num)
                )
        cv2.imwrite(frame_file, frame)

    return

def run_C3D_extraction(feature_prototxt, ofile, feature_layer, trained_model):
    ''' Extract C3D features by running caffe binary '''

    almost_infinite_num = 9999999

    extract_bin = os.path.join(
            caffe_root,
            "build/tools/extract_image_features.bin"
            )

    if not os.path.isfile(extract_bin):
        print("[Error] Build facebook/C3D first, or make sure caffe_dir is "
              " correct")
        sys.exit(-9)

    feature_extraction_cmd = [
            extract_bin,
            feature_prototxt,
            trained_model,
            str(gpu_id),
            str(batch_size),
            str(almost_infinite_num),
            ofile,
            feature_layer,
            ]

    print ("[Info] Running C3D feature extraction: \"{}\"".format(
            ' '.join(feature_extraction_cmd)
            ))
            
    return_code = subprocess.call(feature_extraction_cmd)

    return return_code

def get_features(feature_files, feature_layer):
    ''' From binary feature files, take an average (for multiple clips) '''

    # in case of a single feature_file, force it to a list
    if isinstance(feature_files, str):
        feature_files = [feature_files]

    # read each feature, take an an average
    for clip_count, feature_file in enumerate(feature_files):
        #print ("clip_count={}, feature_file={}".format(clip_count, feature_file))
        if not os.path.exists(feature_file):
            feature_file += '.' + feature_layer

        if not os.path.exists(feature_file):
            print ("[Error] feature_file={} does not exist!".format(feature_file))
            return None

        # read binary data
        f = open(feature_file, "rb")
        # read all bytes into a string
        s = f.read()
        f.close()
        (n, c, l, h, w) = array.array("i", s[:20])
        feature_vec = np.array(array.array("f", s[20:]))

        if clip_count == 0:
            feature_vec_avg = feature_vec
        else:
            feature_vec_avg += feature_vec

    feature_vec_avg = feature_vec_avg / len(feature_files)

    return feature_vec_avg

def generate_feature_prototxt(out_file, src_file, mean_file=None):
    ''' Generate a model architecture, pointing to the given src_file '''

    # by default, mean file must exist.
    # if for some reason it's missing, get from:
    # https://github.com/facebook/C3D/blob/master/examples/c3d_feature_extraction/sport1m_train16_128_mean.binaryproto?raw=true
    if not mean_file:
        mean_file = os.path.join(
                caffe_root,
                "examples",
                "c3d_feature_extraction",
                "sport1m_train16_128_mean.binaryproto"
                )

    if not os.path.isfile(mean_file):
        print ("[Error] mean cube file={} does not exist.".format(mean_file))
        sys.exit(-8)
    #src_file="prototxt/input_list_frm.txt"
    mean_file="sport1m_train16_128_mean.binaryproto"
    # replace source video clips / mean_file
    prototxt_content = '''
name: "DeepConv3DNet_Sport1M_Val"
layers {{
  name: "data"
  type: VIDEO_DATA
  top: "data"
  top: "label"
  image_data_param {{
    source: "{0}"
    use_image: true
    mean_file: "{1}"
    batch_size: 50
    crop_size: 112
    mirror: false
    show_data: 0
    new_height: 128
    new_width: 171
    new_length: 16
    shuffle: false
  }}
}}
# ----------- 1st layer group ---------------
layers {{
  name: "conv1a"
  type: CONVOLUTION3D
  bottom: "data"
  top: "conv1a"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 64
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 0
    }}
  }}
}}
layers {{
  name: "relu1a"
  type: RELU
  bottom: "conv1a"
  top: "conv1a"
}}
layers {{
  name: "pool1"
  type: POOLING3D
  bottom: "conv1a"
  top: "pool1"
  pooling_param {{
    pool: MAX
    kernel_size: 2
    kernel_depth: 1
    stride: 2
    temporal_stride: 1
  }}
}}
# ------------- 2nd layer group --------------
layers {{
  name: "conv2a"
  type: CONVOLUTION3D
  bottom: "pool1"
  top: "conv2a"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 128
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu2a"
  type: RELU
  bottom: "conv2a"
  top: "conv2a"
}}
layers {{
  name: "pool2"
  type: POOLING3D
  bottom: "conv2a"
  top: "pool2"
  pooling_param {{
    pool: MAX
    kernel_size: 2
    kernel_depth: 2
    stride: 2
    temporal_stride: 2
  }}
}}
# ----------------- 3rd layer group --------------
layers {{
  name: "conv3a"
  type: CONVOLUTION3D
  bottom: "pool2"
  top: "conv3a"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 256
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu3a"
  type: RELU
  bottom: "conv3a"
  top: "conv3a"
}}
layers {{
  name: "conv3b"
  type: CONVOLUTION3D
  bottom: "conv3a"
  top: "conv3b"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 256
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu3b"
  type: RELU
  bottom: "conv3b"
  top: "conv3b"
}}
layers {{
  name: "pool3"
  type: POOLING3D
  bottom: "conv3b"
  top: "pool3"
  pooling_param {{
    pool: MAX
    kernel_size: 2
    kernel_depth: 2
    stride: 2
    temporal_stride: 2
  }}
}}
# --------- 4th layer group
layers {{
  name: "conv4a"
  type: CONVOLUTION3D
  bottom: "pool3"
  top: "conv4a"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 512
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu4a"
  type: RELU
  bottom: "conv4a"
  top: "conv4a"
}}
layers {{
  name: "conv4b"
  type: CONVOLUTION3D
  bottom: "conv4a"
  top: "conv4b"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 512
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu4b"
  type: RELU
  bottom: "conv4b"
  top: "conv4b"
}}
layers {{
  name: "pool4"
  type: POOLING3D
  bottom: "conv4b"
  top: "pool4"
  pooling_param {{
    pool: MAX
    kernel_size: 2
    kernel_depth: 2
    stride: 2
    temporal_stride: 2
  }}
}}
# --------------- 5th layer group --------
layers {{
  name: "conv5a"
  type: CONVOLUTION3D
  bottom: "pool4"
  top: "conv5a"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 512
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu5a"
  type: RELU
  bottom: "conv5a"
  top: "conv5a"
}}
layers {{
  name: "conv5b"
  type: CONVOLUTION3D
  bottom: "conv5a"
  top: "conv5b"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  convolution_param {{
    num_output: 512
    kernel_size: 3
    kernel_depth: 3
    pad: 1
    temporal_pad: 1
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu5b"
  type: RELU
  bottom: "conv5b"
  top: "conv5b"
}}
layers {{
  name: "pool5"
  type: POOLING3D
  bottom: "conv5b"
  top: "pool5"
  pooling_param {{
    pool: MAX
    kernel_size: 2
    kernel_depth: 2
    stride: 2
    temporal_stride: 2
  }}
}}
# ---------------- fc layers -------------
layers {{
  name: "fc6-1"
  type: INNER_PRODUCT
  bottom: "pool5"
  top: "fc6-1"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  inner_product_param {{
    num_output: 4096
    weight_filler {{
      type: "gaussian"
      std: 0.005
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu6"
  type: RELU
  bottom: "fc6-1"
  top: "fc6-1"
}}
layers {{
  name: "drop6"
  type: DROPOUT
  bottom: "fc6-1"
  top: "fc6-1"
  dropout_param {{
    dropout_ratio: 0.5
  }}
}}
layers {{
  name: "fc7-1"
  type: INNER_PRODUCT
  bottom: "fc6-1"
  top: "fc7-1"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  inner_product_param {{
    num_output: 4096
    weight_filler {{
    type: "gaussian"
      std: 0.005
    }}
    bias_filler {{
      type: "constant"
      value: 1
    }}
  }}
}}
layers {{
  name: "relu7"
  type: RELU
  bottom: "fc7-1"
  top: "fc7-1"
}}
layers {{
  name: "drop7"
  type: DROPOUT
  bottom: "fc7-1"
  top: "fc7-1"
  dropout_param {{
    dropout_ratio: 0.5
  }}
}}
layers {{
  name: "fc8-1"
  type: INNER_PRODUCT
  bottom: "fc7-1"
  top: "fc8-1"
  blobs_lr: 1
  blobs_lr: 2
  weight_decay: 1
  weight_decay: 0
  inner_product_param {{
    num_output: 487
    weight_filler {{
      type: "gaussian"
      std: 0.01
    }}
    bias_filler {{
      type: "constant"
      value: 0
    }}
  }}
}}
layers {{
  name: "prob"
  type: SOFTMAX
  bottom: "fc8-1"
  top: "prob"
}}
layers {{
  name: "accuracy"
  type: ACCURACY
  bottom: "prob"
  bottom: "label"
  top: "accuracy"}}'''.format(src_file, mean_file)

    with open(out_file, 'w') as f:
        f.write(prototxt_content)

    return

def main_C3D(file_path,video_file,save):
    
    ''' Extract and save features '''

    # trained model (will be downloaded if missing)
    trained_model = os.path.join(
        caffe_root,
        "examples",
        "c3d_feature_extraction",
        "conv3d_deepnetA_sport1m_iter_1900000"
        )
    # check model
    check_trained_model(trained_model)

    # save extracted frames temporarily
    tmp_dir = "/home/callbarian/C3D/temp"

    # where feature csv file will be saved --
    # where the video is (by default), or second argument
    c3d_feature_outdir = "/home/callbarian/C3D/videos"

    # feature to extract
    feature_layer = 'fc6-1'

    # overwrite feature output?
    force_overwrite = False

    # by default, use 16 frames
    num_frames_per_clip = 16 # ~0.5 second

    # sampling rate (in seconds)
    sample_every_N_sec = 1

    # don't extract beyond this (in seconds)
    max_processing_sec = 599

    # get frame counts and fps
    num_frames, fps = get_frame_count(file_path+video_file)
    print ("[Info] num_frames={}, fps={}".format(num_frames, fps))
    #if num_frames<512:
    #    print("less frame")
    #    return
    if num_frames < int(sample_every_N_sec * fps):
        start_frame = (num_frames - num_frames_per_clip) / 2
        start_frames = [start_frame]
    else:
        frame_inc = int(sample_every_N_sec * fps)
        frame_inc=16
        start_frame = int(frame_inc / 2)
        start_frame = 1
        # make sure not to reach the edge of the video
        end_frame = min(num_frames, int(max_processing_sec * fps)) - \
                    num_frames_per_clip
        start_frames = []
        for frame_index in range(start_frame, end_frame, frame_inc):
            #print "[Debug] adding frame_index={}".format(frame_index)
            start_frames.append(frame_index)

    video_id, video_ext = os.path.splitext(
            os.path.basename(video_file)
            )

    # generate auxilliary files for C3D feature extraction
    input_file = os.path.join(tmp_dir, 'input.txt')
    output_prefix_file = os.path.join(tmp_dir, 'output_prefix.txt')
    feature_prototxt = os.path.join(tmp_dir, 'feature_extraction.prototxt')
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    generate_feature_prototxt(feature_prototxt, input_file)

    # first, populate input.txt, and output_prefix.txt files
    # each line corresponds to a 16-frame video clip
    f_input = open(input_file, 'w')
    f_output_prefix = open(output_prefix_file, 'w')
    for start_frame in start_frames:
        # output feature file (CSV)
        if not os.path.exists(os.path.join(c3d_feature_outdir,save)):
            try:
                os.makedirs(os.path.join(c3d_feature_outdir,save))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        feature_filename = os.path.join(
                c3d_feature_outdir+"/"+save,
                "{}.txt".format(video_id)
                )

        if os.path.isfile(feature_filename) and not force_overwrite:
            #print ("[Warning] feature was already saved. Skipping this video...")
            continue

        # where to save extracted frames
        frame_dir = os.path.join(tmp_dir, video_id)
        extract_frames(file_path+video_file, start_frame, frame_dir)

        # a dummy label
        dummy_label = 0

        # write "input.txt" with just one clip
        f_input.write("{}/ {} {}\n".format(frame_dir, start_frame, dummy_label))

        # write "output_prefix.txt" with one clip
        clip_id = os.path.join(
                tmp_dir,
                video_id + '_{0:06f}'.format(start_frame)
                )
        f_output_prefix.write("{}\n".format(clip_id))
    f_input.close()
    f_output_prefix.close()

    # second, run C3D extraction (with a batch)
    if os.path.isfile(input_file) and os.path.getsize(input_file):
        return_code = run_C3D_extraction(
                feature_prototxt,
                output_prefix_file,
                feature_layer,
                trained_model
                )

        # third, if C3D ran successfully, convert each feature file (binary) to csv
        if return_code == 0:
            print("C3D ran successfully")
            list=[]
            for start_frame in start_frames:
                # output feature file (CSV)
                
                feature_filename = os.path.join(
                        c3d_feature_outdir,
                        "{0}{1:06f}.csv".format("", start_frame)
                        )

                if os.path.isfile(feature_filename) and not force_overwrite:
                    print("[Warning] feature was already saved. Skipping this "
                          "video...")
                    continue

                clip_id = os.path.join(
                        tmp_dir,
                        video_id + '_{0:06f}'.format(start_frame)
                        )
                feature = get_features([clip_id], feature_layer)

                #print ("[Info] Saving C3D feature as {}".format(feature_filename,))
                #print(feature)
                
                # np.savetxt(
                #         feature_filename,
                #         feature[None, :],
                #         fmt='%.16f',
                #         delimiter=','
                #         )
                # save the average feature vector as a CSV
                list.append(feature)
            data=np.array(list)
            print("line 808: total number of data is {}.".format(len(data)),    " each row has {} elements.".format(len(data[0])),data)
            Segments_Features=[]
            thirty2_shots=np.round(np.linspace(1, len(data), num=33))
            count=0
            for i in range(0,len(thirty2_shots)-1):
            
            	ss=int(thirty2_shots[i])
            	ee=int(thirty2_shots[i+1])-1
            
            	if i==len(thirty2_shots):
            		ee=thirty2_shots[i+1]
            
            	if ss==ee:
            		temp_vect=data[ss,:]
            	elif ee<ss:
            		temp_vect=data[ss,:]
            	else:
            		temp_vect=data[ss:ee,:].mean(axis=0);
            
            	temp_vect=temp_vect/np.linalg.norm(temp_vect);
            	if np.linalg.norm==0:
            		print(error)
            		exit()
            	if len(temp_vect)!=0:
            		Segments_Features.append(temp_vect.tolist());
            
            with open(os.path.join(c3d_feature_outdir,save+video_id+".txt"),'w') as f:
                for vec in Segments_Features:
                    rec = ""
                    for item in vec:
                        rec = rec + str("{0:.6f}".format(item)) + " "
                    rec = rec[:-1]
                    rec = rec + "\n"
                    f.write(rec)
            print ("[Info] Saving output as {}".format(video_id))
            shutil.rmtree(os.path.join(tmp_dir, ""))
            
        else:
            print ("[Error] feature extraction failed!")


if __name__ == "__main__":
    app = QApplication([])
    window = vidsurveil()
    window.show()
    sys.exit(app.exec_())


  
    
   
    
