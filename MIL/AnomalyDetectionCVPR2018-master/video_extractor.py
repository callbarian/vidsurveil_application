import subprocess
import os  
import shutil


def save_video(video_path,frame_list):
    temp_path='./temp/'
    if not os.path.isdir(temp_path):
        os.mkdir(temp_path)
    result_path='./result/'
    if not os.path.isdir(result_path):
        os.mkdir(result_path)
   
    print("frame_list : ",frame_list)
    print("video_path : "+video_path)
    
    #'i' is the wanomaly video number 
    i=0  
    for frame_set in frame_list: 
        #print('frame set :', frame_set)
        #frame to time
        frame_set[1]=(frame_set[1]-frame_set[0])/30
        frame_set[0]/=30
        #ffmpeg video extractiont
        result=subprocess.Popen(['ffmpeg','-y','-ss',str(frame_set[0]),'-i',video_path, '-t',str(frame_set[1]), '-c', 'copy', temp_path+'Anomaly_videos'+str(i).zfill(4)+'.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)  
    
        result.wait()
        i+=1
        #(output,err)=result.communicate()
        print("video_split_done")

    
    
    
''' 
    #this part is made to concatnate the Anomaly_videos
    show_segment_file=subprocess.Popen(['ls',temp_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)  
    show_segment_file.wait()
    
    output,err=show_segment_file.communicate()
    output=output.decode('utf-8')
    result_list=output.split('\n')
    result_list.pop()


    with open("result.txt","w") as f:
        for i in result_list:
            i='file \'./temp/'+i+'\'\n'
            f.write(i)

    
    
    concatnate_videos=subprocess.Popen(['ffmpeg','-y','-f','concat','-safe','0','-i','result.txt','-c','copy',result_path+'output.mp4'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)   
    concatnate_videos.wait()

    print('save_vide done')
    shutil.rmtree(r"./temp")
    rm_txt=subprocess.Popen(['rm','result.txt'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    rm_txt.wait()
    return
'''


if __name__ == "__main__":
    #level1 
    #frame_list=[[50,150]]
    #level2 
    frame_list=[[50,150],[500,750]]
    save_video("/Users/gicheol/Downloads/play/ffmp/Fighting015_x264.mp4",frame_list)

