
import pydub
from pydub import AudioSegment
import math

print('starting...')
class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_file(self.filepath)
    
    def get_duration(self):
        #print('********************audio duration in seconds*****************************************')
        #print(self.audio.duration_seconds)
        return self.audio.duration_seconds
    
    def single_split(self, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000
        t2 = to_sec * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, sec_per_split):
        total_sec = math.ceil(self.get_duration())
        for i in range(0, total_sec, sec_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+sec_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_sec - sec_per_split:
                print('All splited successfully')

                
                              
folder = 'C:\\Users\\Carolle G\\Documents\\Projects\\python\\python\\audio_cut'

file = '20220222_162035.wav'
split_wav = SplitWavAudioMubin(folder, file)
print('object class created')
split_wav.multiple_split(sec_per_split=3600)
print('success!!')