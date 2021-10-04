import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
import Data_Generator_X_SAMPA as sampa
import datetime 

def timeStemp():
    now = datetime.datetime.now()
    a1 = str(now.year).zfill(4)
    a2 = str(now.month).zfill(2)
    a3 = str(now.day).zfill(2)
    a4 = str(now.hour).zfill(2)
    a5 = str(now.minute).zfill(2)
    a6 = str(now.second).zfill(2)
    return a1+a2+a3+"_"+a4+a5+a6

class noteGenerator:

    def random_key_bunch_maker(self, length, mu = 1, sigma = 0.3):

        y = np.random.normal( mu, sigma, length ) * 64

        y = np.clip(y, 0, 127)

        return y
    
    def random_XSAMPA_bunch_maker( self, length ):

        #sam = sampa.japanese_list().all
        sam = sampa.dd().data

        cs = np.random.randint( 0, len(sam), length ) 

        Array = list()

        for _cs in cs:
        
            a = sam[_cs]
            
            Array.append(a)
        
        return Array
        
    def time_duration_maker(self):
        
        # make empty array for appending
        time_Array = np.array([])
        duration_Array = np.array([])
        
        # setup initial value
        time = 0
        duration = self.note_length
        
        # append first note
        time_Array = np.append(time_Array, time)
        duration_Array = np.append(duration_Array, duration)
        
        while(1):
            
            # make next value
            time = time + self.note_length
            duration = self.note_length

            # detect track overflow
            if( self.max_length_track >= time ):

                time_Array = np.append(time_Array, time)
                duration_Array = np.append(duration_Array, duration)

            else:

                # compress over value
                nextduration__value = time_Array[-1] + duration_Array[-1]
                overflowed_duration_value = nextduration__value - self.max_length_track
                duration_Array[-1] = duration_Array[-1] - overflowed_duration_value
                
                # remove zero duration note
                if(duration_Array[-1] == 0):

                    duration_Array = duration_Array[0:-1]
                    time_Array = time_Array[0:-1]
                
                break
            
        return time_Array, duration_Array, time_Array.shape[0]
      
    def simple_random(self, size, inclination):
        
        x = np.linspace( 0, size, int(size / inclination) )
        y = np.random.randint( 100, 127, int(size / inclination) )

        # B-spline 계산
        spl = splrep(x, y)
        
        # spline 드로잉
        x2 = np.linspace(0, size, size)
        y2 = splev(x2, spl)
        y2 = np.clip(y2, 0, 127)
        
        return y2
        
    def nominalDistribution(self, size, inclination, mu = 1, sigma = 0.3):
        
        x = np.linspace( 0, size, int(size/inclination) )
        y = np.random.normal( mu, sigma, int(size/inclination) ) * 64

        # B-spline 계산
        spl = splrep(x, y)

        # spline 드로잉
        x2 = np.linspace(0, size, size)
        y2 = splev(x2, spl)
        
        #y2 = np.around(y2)
        y2 = np.clip(y2, 0, 127)
        
        return y2

    def maker(self):

        # make data
        time, dur, length = self.time_duration_maker()
        melody = self.random_key_bunch_maker(length)

        opening = np.full(length, 127, dtype=int)

        user_name = np.zeros(length)
        smapa = self.random_XSAMPA_bunch_maker( length )

        start_skip = np.zeros(length)
        end_skip = self.simple_random(length, 10)

        # empty pandas dataframe
        note = ["time", "duration", "melodyTearing", "y", "p", "opening", "startSkip", "endSkip"]
        note = pd.DataFrame(np.random.randn(length,len(note)), columns=note)

        # inject value
        note["time"] = pd.Series( time ).astype('uint32')
        note["duration"] = pd.Series( dur ).astype('uint16')
        note["melodyTearing"] = pd.Series( melody ).astype('int8')
        note["y"] = pd.Series( user_name ).astype('int8')
        note["p"] = pd.Series( smapa )
        note["opening"] = pd.Series( opening ).astype('int8')
        note["startSkip"] = pd.Series( start_skip ).astype('int16')
        note["endSkip"] = pd.Series( end_skip ).astype('int16')

        return note

    def make(self, noteLangth = 960, maxTrackLangth = 1536000):

        self.note_length = noteLangth

        self.max_length_track = maxTrackLangth
    
        self.data = self.maker()

        return self.data

    def __init__(self):
        
        noteLangth = 240*5
        maxTrackLangth = 1536000
        
        self.note_length = noteLangth
        self.max_length_track = maxTrackLangth

class ccGenerator:

    def spline(self, data, duration):

        x = np.linspace( 0, duration, len(data)  )
        y = data

        # B-spline 계산
        spl = splrep(x, y)

        # spline 드로잉
        x2 = np.linspace(0, duration, duration)
        y2 = splev(x2, spl)

        return y2

    def simpleRandom(self, size, inclination):
        
        x = np.linspace( 0, size, int(size / inclination) )
        y = np.random.randint( 0, 127, int(size / inclination) )

        # B-spline 계산
        spl = splrep(x, y)
        
        # spline 드로잉
        x2 = np.linspace(0, size, size)
        y2 = splev(x2, spl)
        y2 = np.clip(y2, 0, 127)
        
        return pd.Series( y2 )
       
    def pitchMaker(self, dur, note):
        
        pitch = np.array([])
        
        for a in range( 0, len(dur) ):
            
            base = note[a]
            new = np.random.randint( base - 3, base + 3, 10 )
            a_ = self.spline( new, dur[a] )
            pitch = np.append(pitch, a_)

            pitch = np.clip(pitch, 0, 127)

        return pd.Series(pitch)

    def _pitchMaker(self, dur, note):
        
        pitch = np.array([])

        pitch = self.simpleRandom(1536000, 600)

        return pd.Series(pitch)

    def _pitchMaker1(self, data):

        length = 1536000

        x = np.linspace( 0, 1536000, len(data["time"]) )
        y = np.random.randint( 0, 127, len(data["time"]) )

        # B-spline calcuration
        spl = splrep(x, y)

        # spline drawing
        x2 = np.linspace(0, length, length)
        y2 = splev(x2, spl)

        #print(len(y2))

        y2 = np.clip(y2, 0, 127)

        y2 = pd.Series(y2)

        return y2

    def _pitchMaker2(self, data):

        length = 1536000

        y = np.repeat(data["melodyTearing"], 2)

        x = np.linspace( 0, 1536000, len(y) )

        # B-spline calcuration
        spl = splrep(x, y)

        # spline drawing
        x2 = np.linspace(0, length, length)
        y2 = splev(x2, spl)

        #print(len(y2))

        y2 = np.clip(y2, 0, 127)

        y2 = pd.Series(y2)

        return y2

    def timeMaker(self, size):

        return  pd.Series( np.arange(size) )

    def nominalDistribution(self, size, inclination, mu = 1, sigma = 0.3):
        
        x = np.linspace( 0, size, int(size/inclination) )
        y = np.random.normal( mu, sigma, int(size/inclination) ) * 64

        # B-spline 계산
        spl = splrep(x, y)

        # spline 드로잉
        x2 = np.linspace(0, size, size)
        y2 = splev(x2, spl)
        
        #y2 = np.around(y2)
        y2 = np.clip(y2, 0, 127)
        
        return pd.Series( y2 )

    def maker(self,cc):
    
        cc3 = ["time", "dynamics", "breath", "bright", "clearance", "grawl", "pitch", "gender"]
        cc3 = pd.DataFrame(np.random.randn(self.name, len(cc3)), columns=cc3)

        cc3["time"] = self.timeMaker(self.name)
        cc3['dynamics'] = self.simpleRandom(self.name,600).astype('uint8')
        cc3['breath'] = self.simpleRandom(self.name,600).astype('uint8')
        cc3['bright'] = self.simpleRandom(self.name,600).astype('uint8')
        cc3['clearance'] = self.simpleRandom(self.name,600).astype('uint8')
        cc3['grawl'] = self.simpleRandom(self.name,600).astype('uint8')
        #cc3['pitch'] = self.pitchMaker( cc["duration"],cc["melodyTearing"] ).astype("float32")
        cc3['pitch'] = self._pitchMaker2( cc ).astype("float32")
        cc3['gender'] = self.simpleRandom(self.name,600).astype('uint8')

        return cc3

    def make(self, Array = []):

        self.data = self.maker(Array)

    def __init__(self):

        self.name = 1536000

class generator:

    def __init__(self, directory = ""):

        time_stemp = timeStemp()

        note = noteGenerator()
        noteData = note.make()

        cc = ccGenerator()
        cc.make(noteData)

        dir = directory + "/" + time_stemp

        cc.data.to_hdf( dir + '.cc.h5','df')
        note.data.to_hdf( dir + '.note.h5','df')