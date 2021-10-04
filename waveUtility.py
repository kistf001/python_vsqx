import scipy.io.wavfile as wav
import numpy as np
import nameUtility as nu
import scipy.signal as sps

#   1536000,   30,720,000‬
#      1920,       38,400

class trashBar:

    def __init__(self):
        self.trash_start = 38400*4

    def open_file(self, src_directory = "None"):
        self.sample_rate, self.data = wav.read(src_directory)

    def remove(self, dst_directory = "None" ):
        self.data = self.data[self.trash_start:]
        self.data = np.asarray(self.data, dtype=np.int16)
        wav.write(dst_directory, self.sample_rate, self.data)

class downSample():
    
    def __init__(self):
        self.in_rate = 48000
        self.out_rate = 16000
        
    def open_file(self, src_directory):

        self.sample_rate, self.data = wav.read(src_directory)

        if self.sample_rate != self.in_rate:
            print("Frame rate is not %d (it's %d)" % \
                  (self.sample_rate, self.data) )
            return False

    def resample(self, dst_directory):
        nroutsamples = int(round(len(self.data) * self.out_rate/self.in_rate))
        audio_out = sps.resample(self.data, nroutsamples)
        data = np.asarray(audio_out, dtype=np.int16)
        wav.write(dst_directory, self.out_rate, data)

#listt = nu.fileNameSpliter().wav48k.scan("H:/Dataset")
#
#for ss in listt:
#    src = "H:/Dataset/"+ss+".wav"
#    dst = "H:/downSample/"+ss+".wav"
#    ds = downSample()
#    ds.open_file(src)
#    ds.resample(dst)
#    print(ss[0:-5])