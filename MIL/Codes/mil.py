import os 
import numpy as np
import subprocess

class MIL():
    def __init__(self,path_name,temp_dir,save_dir,env_path_c3d,env_path_mil):
        #input file path array(in full path)
        self.path_name = path_name
        
        # directory to process files temporarily
        self.temp_dir = temp_dir

        # save directory for result videos
        self.save_dir = save_dir

        #temp each file directory array
        self.temp_dir_arr = []

        #environment path for C3D
        self.env_path_c3d = env_path_c3d

        #environment path for MIL(AnomalyDetection)
        self.env_path_mil = env_path_mil

        # c3d path
        self.c3d_path = os.getcwd()+'/MIL/C3D/C3D-v1.0/examples/c3d_feature_extraction/extract_C3D_feature.py'

    def preprocess(self):
        for file in self.path_name:
            assert file.split('.')[-1]=='mp4','the file has to be in mp4 format'
            file_name = file.split('/')[-1]
            #make a new directory for each file
            save_path = os.path.join(self.temp_dir,file_name.split('.')[0])
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            
            self.temp_dir_arr.append(save_path)

            # if file already exist in save_path, continue
            if os.path.exists(os.path.join(save_path,file_name)):
                continue
            
            # copy each file to each new directory, after resizing it
            command = 'ffmpeg -i ' + file + ' -filter:v scale="360:trunc(ow/a/2)*2" -c:a copy ' + os.path.join(save_path,file_name)
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            out = result.communicate()
            print(out)


            # cut into multiple segments
            command = 'ffmpeg -i ' + os.path.join(save_path,file_name)  + ' -c copy -segment_time 8 -reset_timestamps 1 -f segment '+ save_path+ '/segment%03d.mp4'
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            out = result.communicate()
            print(out)

    
    def run_c3d(self):

        result = subprocess.Popen(['sh',os.getcwd()+'/MIL/Codes/call_environment.sh',self.env_path_c3d,self.c3d_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
        out = result.communicate()
        print(out)




            


            
