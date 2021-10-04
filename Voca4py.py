import numpy as np

"""
00. dynamics\n
01. breathiness\n
02. brightness\n
03. clearness\n
04. opening\n
05. gender_factor\n
06. portamento_timing\n
07. cross_synth\n
08. growl\n
09. pitch_bend\n
10. pitch_bend_sensitivity\n
    
"""

  
def ArrayMaker(parameterType, time, value, duration):

    """
    [0] paramter type \n
    [1] [time, value] \n
    [2] duration

    """
        
    AC = ["R",[0,0],0]

    AC[0] = parameterType
    AC[1][0] = int(time)
    AC[1][1] = int(value)
    AC[2] = duration                # 파싱을 위한 Lead Value

    return AC

def ValueFeeder(barNum, types = "D", _size = 1920):

    ACarray = []

    maxbar = _size * barNum

    import copy

    time = 0 #7680

    while(1):

        _Dynamics = np.random.randint( 0, 127 )

        ACarray.append(copy.deepcopy(ArrayMaker(types, time, _Dynamics, _size)))

        time = time + _size

        if(time >= maxbar):
            break

    return ACarray

class BarSize960():
    
    size = 960

    def CCdynamics(barNum):
        return ValueFeeder(barNum,"D",960)

    def CCbreathiness(barNum):
        return ValueFeeder(barNum,"B",960)

    def CCbrightness(barNum):
        return ValueFeeder(barNum,"R",960)

    def CCclearness(barNum):
        return ValueFeeder(barNum,"C",960)

    def CCgenderFactor(barNum):
        return ValueFeeder(barNum,"G",960) 
        
    def CCportamento(barNum):
        return ValueFeeder(barNum,"F",960)
        
    def CCpitchbend(barNum):
        return ValueFeeder(barNum,"P",960)

    def CCgrwol(barNum):
        return ValueFeeder(barNum,"W",960)

class BarSize1920():
    
    size = 960

    def CCdynamics(barNum):
        return ValueFeeder(barNum,"D",1920)

    def CCbreathiness(barNum):
        return ValueFeeder(barNum,"B",1920)

    def CCbrightness(barNum):
        return ValueFeeder(barNum,"R",1920)

    def CCclearness(barNum):
        return ValueFeeder(barNum,"C",1920)

    def CCgenderFactor(barNum):
        return ValueFeeder(barNum,"G",1920) 
        
    def CCportamento(barNum):
        return ValueFeeder(barNum,"F",1920)
        
    def CCpitchbend(barNum):
        return ValueFeeder(barNum,"P",1920)

    def CCgrwol(barNum):
        return ValueFeeder(barNum,"W",1920)