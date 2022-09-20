import os 
import subprocess
from pydub import AudioSegment 
from datetime import datetime

def resp(input_text):
    global is_authorised, p1, p2,p 
    if input_text == '9CGhGcAwCarqvepHRxNn' and not is_authorised:
        is_authorised = True
        p1 = subprocess.Popen(["python", "screenrec.py"])
        p2 = subprocess.Popen(["python","audiorec.py"])
        print("Access granted")
        return "Acces granted"
    elif input_text == 'stop' and is_authorised:
        is_authorised = False
        p1.terminate()
        p2.terminate()
        record = AudioSegment.from_wav("result.wav")
        record = record+20
        record.export("output.wav", "wav")
        outname = datetime.now().strftime("%I%M%p%B%d%Y")+'.mov'
        subprocess.call(
            f'ffmpeg -v debug -i output.wav -i output.avi -c:a libmp3lame -qscale 20 -shortest {outname}', shell=True)
        print('Execution stopped')
        os.remove('output.avi')
        os.remove('output.wav') 
        os.remove('result.wav')
        return 'Execution stopped'
    else:
        return 'GTFO'

is_authorised=False



