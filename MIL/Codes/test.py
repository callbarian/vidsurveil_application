import subprocess
import os 

command = 'ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=avg_frame_rate ' + os.getcwd()+'/101-2_cam01_swoon01_place03_day_winter_resize.mp4'
result = subprocess.Popen(['ffprobe','-v','error','-select_streams','v','-of','default=noprint_wrappers=1:nokey=1','-show_entries','stream=r_frame_rate',os.getcwd()+'/101-2_cam01_swoon01_place03_day_winter_resize.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
result.wait()
out = result.communicate()
message = out[0].decode()
message = message.split('\n')[0]
fps = int(message.split('/')[0])/int(message.split('/')[1])

print(fps)
