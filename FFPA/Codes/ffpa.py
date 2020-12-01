import os
import subprocess

class FFPA():

    def __init__(self,path_name,temp_dir,save_dir,env_path_FFPA):
        #input file path array(in full path)
        self.path_name = path_name
        
        # directory to process files temporarily
        self.temp_dir = temp_dir

        # save directory for result videos
        self.save_dir = save_dir

        #temp each file directory array
        self.temp_dir_arr = []

        #environment path for MIL(AnomalyDetection)
        self.env_path_FFPA = env_path_FFPA

        # ffpa path
        self.FFPA_path = os.getcwd()+'/FFPA/ano_pred_cvpr2018/Codes/inference2.py'

        self.save_path = ''

        # GPU to use
        self.gpu_id = 0

        # 8 will be more than 1G, 4 will be less than 1G
        self.batch_size = 8

        self.dataset = 'mini'

        self.test_folder = ''

    def preprocess(self):
        for file in self.path_name:
            assert file.split('.')[-1]=='mp4','the file has to be in mp4 format'
            file_name = file.split('/')[-1]
            #make a new directory for each file
            #save_path = os.path.join(self.temp_dir,file_name.split('.')[0])
            self.save_path = os.path.join(self.temp_dir,'frames')

            #if not os.path.exists(save_path):
            #    os.makedirs(save_path)
            
            #self.temp_dir_arr.append(save_path)

            # if file already exist in save_path, continue
            if os.path.exists(self.save_path):
                continue
            
            # copy each file to each new directory, after resizing it
            command = 'ffmpeg -i ' + file + ' -filter:v scale="360:trunc(ow/a/2)*2" -c:a copy ' + os.path.join(self.temp_dir,file_name)
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            out = result.communicate()
            print(out)


            # cut into multiple segments
            command = 'ffmpeg -i ' + os.path.join(self.temp_dir,file_name)  + ' -c copy -segment_time 8 -reset_timestamps 1 -f segment '+ self.temp_dir+ '/segment%03d.mp4'
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            out = result.communicate()
            print(out)

            # remove resized files
            command = 'rm ' + os.path.join(self.temp_dir,file_name)  
            result = subprocess.Popen([command],shell=True,stderr=subprocess.PIPE)
            result.wait()
            out = result.communicate()
            print(out)
         

            videos = sorted(os.listdir(self.temp_dir))
            #result_path = save_path + '/frames'
            #self.test_folder = result_path

            #if not os.path.exists(result_path):
            #    os.makedirs(result_path)

            for video in videos:
                input_video_path = os.path.join(self.save_path,video)
        
                output_directory_path = os.path.join(self.save_path,video.split('.')[0])

                file_name = video.split('.')[0] +'_%03d.jpg'
                if not os.path.exists(output_directory_path):
                    os.makedirs(output_directory_path)
            
                result = subprocess.Popen(['ffmpeg','-i',input_video_path,'-r','30/1', os.path.join(output_directory_path,file_name)],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                result.wait()
                output = result.communicate()
                print(output)

    def run_FFPA(self):
        result = subprocess.Popen(['sh',os.getcwd()+'/FFPA/Codes/call_environment.sh',self.env_path_FFPA,self.FFPA_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result.wait()
        out = result.communicate()
        print(out)