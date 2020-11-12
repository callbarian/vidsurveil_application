#import shlex
#import pipes
#from subprocess import check_call
import subprocess

def cut(filename,save_path):
    result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', '-sexagesimal', filename],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = result.communicate()
    time = out[0].decode().split(':')
    hour = int(time[0])
    minute = int(time[1])
    seconds = int(time[2].split('.')[0])

    start = '00:00:00'
    end = '00:01:00'

    starthour = int(start.split(':')[0])
    startminute = int(start.split(':')[1])
    startseconds = int(start.split(':')[2])

    endhour = int(end.split(':')[0])
    endminute = int(end.split(':')[1])
    endseconds = int(end.split(':')[2])

    count = 23
    for i in range(30):
        print(endhour)
        print(hour)
        if(endhour>=hour and endminute>=minute and endseconds>0):
            flag = 1
            #print('entered if............................................')

            if(endseconds<seconds):
                flag = 0
                start = str(starthour).zfill(2)+':'+str(startminute).zfill(2)+':'+str(startseconds).zfill(2)
                end = str(endhour).zfill(2)+':'+str(endminute).zfill(2)+':'+str(endseconds).zfill(2)

                name = start.replace(':','') + '_' + end.replace(':','') + '.mp4'
                name = save_path + name
                result = subprocess.Popen(['ffmpeg','-ss', start, '-i', filename, '-t', '00:01:00', '-c', 'copy', name],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                out = result.communicate()
                print(out)
                startseconds=startseconds+30
                if(startseconds==60):
                    startseconds = 0
                    startminute +=1
                if(startminute==60):
                    startminute = 0
                    starthour +=1

                endseconds=endseconds+30
                if(endseconds==60):
                    endseconds = 0
                    endminute +=1
                if(endminute==60):
                    endminute = 0
                    endhour +=1
            
            
            start = str(starthour).zfill(2)+':'+str(startminute).zfill(2)+':'+str(startseconds).zfill(2)
            end = str(hour).zfill(2)+':'+str(minute).zfill(2)+':'+str(seconds).zfill(2)
            name = start.replace(':','') + '_' + end.replace(':','') + '.mp4'
            name = save_path + name
            finalseconds = '00:00:00'
            if(flag):
                finalseconds = '00:00:'+ str(seconds+30)
            else:
                finalseconds = '00:00:'+str(seconds)

            result = subprocess.Popen(['ffmpeg','-ss', start, '-i', filename, '-t', finalseconds, '-c', 'copy', name],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out = result.communicate()
            print(out)
            break
            
                
        else:
            #print('entered else............................................')
            start = str(starthour).zfill(2)+':'+str(startminute).zfill(2)+':'+str(startseconds).zfill(2)
            end = str(endhour).zfill(2)+':'+str(endminute).zfill(2)+':'+str(endseconds).zfill(2)

            name = start.replace(':','') + '_' + end.replace(':','') + '.mp4'
            name = save_path + name
            result = subprocess.Popen(['ffmpeg','-ss', start, '-i', filename, '-t', '00:01:00', '-c', 'copy', name],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out = result.communicate()
            print(out)
            startseconds=startseconds+30
            if(startseconds==60):
                startseconds = 0
                startminute +=1
            if(startminute==60):
                startminute = 0
                starthour +=1

            endseconds=endseconds+30
            if(endseconds==60):
                endseconds = 0
                endminute +=1
            if(endminute==60):
                endminute = 0
                endhour +=1
            
            
    print('complete')

