# D : DYNAMIC
# B : BREATH
# R : BRIGHT
# C : CLEARANCE
# W : GRAWL
# P : PITCH BEND
# S : PITCH BEND SENSE
# X : XROSS SYNTH
# G : GENDER
# T : PORTAMENTO TIMING

class paramter_element:
    
    def dynamic(self, time, value):
        dynamic = list()
        dynamic.append(time)
        dynamic.append(value)
        return dynamic 
    def breath(self, time, value):
        breath = list()
        breath.append(time)
        breath.append(value)
        return breath
    def bright(self, time, value):
        bright = list()
        bright.append(time)
        bright.append(value)
        return bright        
    def clearance(self, time, value):
        clearance = list()
        clearance.append(time)
        clearance.append(value)
        return clearance
    def grawl(self, time, value):
        grawl = list()
        grawl.append(time)
        grawl.append(value)
        return grawl
    def pitch(self, time, value):
        pitch_bend_sense = list()
        pitch_bend_sense.append(time)
        pitch_bend_sense.append(value)
        return pitch_bend_sense
    def gender(self, time, value):
        gender = list()
        gender.append(time)
        gender.append(value)
        return gender

class parameter_set:

    def __init__(self):

        self.data = list()

        dynamic = list()
        breath = list()
        bright = list()
        clearance = list()
        grawl = list()
        pitch_bend = list()
        gender = list()
        
        parameter_set = self.data
        parameter_set.append( dynamic )
        parameter_set.append( breath )
        parameter_set.append( bright )
        parameter_set.append( clearance )
        parameter_set.append( grawl )
        parameter_set.append( pitch_bend )
        parameter_set.append( gender )

class delite:

    def __init__(self, data):

        # variable
        self.data = data

        self._dynamic = self.data[0]
        self._breath = self.data[1]
        self._bright = self.data[2]
        self._clearance = self.data[3]
        self._grawl = self.data[4]
        self._pitch_bend = self.data[5]
        self._gender = self.data[6]

    def Dynamic(self, position):
        del self._dynamic[position]

    def Breath(self, position):
        del self._breath[position]

    def Bright(self, position):
        del self._bright[position]

    def Clear(self, position):
        del self._clearance[position]

    def Grawl(self, position):
        del self._grawl[position]

    def PitchBend(self, position):
        del self._pitch_bend[position]

    def Gender(self, position):
        del self._gender[position]

class repair:

    def __init__(self, data):

        # variable
        self.data = parameter_set().data

        self._dynamic = self.data[0]
        self._breath = self.data[1]
        self._bright = self.data[2]
        self._clearance = self.data[3]
        self._grawl = self.data[4]
        self._pitch_bend = self.data[5]
        self._gender = self.data[6]        

class sort:

    def __init__(self, data):

        # variable
        self.data = parameter_set().data

        self._dynamic = self.data[0]
        self._breath = self.data[1]
        self._bright = self.data[2]
        self._clearance = self.data[3]
        self._grawl = self.data[4]
        self._pitch_bend = self.data[5]
        self._gender = self.data[6]

    def Dynamic(self):
        self._dynamic.sort()

    def Breath(self):
        self._breath.sort()

    def Bright(self):
        self._bright.sort()

    def Clear(self):
        self._clearance.sort()

    def Grawl(self):
        self._grawl.sort()

    def PitchBend(self):
        self._pitch_bend.sort()

    def Gender(self):
        self._gender.sort()

class append:

    def __init__(self, data):

        self._dynamic = data[0]
        self._breath = data[1]
        self._bright = data[2]
        self._clear = data[3]
        self._grawl = data[4]
        self._pitch_bend = data[5]
        self._gender = data[6]
    
    def setMaker(self, time, value):
        aad = list()
        aad.append(time)
        aad.append(value)
        return aad

    def Dynamic(self, time, value):
        self._dynamic.append(self.setMaker(time, value))

    def Breath(self, time, value):
        self._breath.append(self.setMaker(time, value))

    def Bright(self, time, value):
        self._bright.append(self.setMaker(time, value))

    def Clear(self, time, value):
        self._clear.append(self.setMaker(time, value))

    def Grawl(self, time, value):
        self._grawl.append(self.setMaker(time, value))

    def PitchBend(self, time, value):
        self._pitch_bend.append(self.setMaker(time, value))

    def Gender(self, time, value):
        self._gender.append(self.setMaker(time, value))

class newParameter:

    #def pitchBendSensitveExtract(self):
    def __init__(self):

        # variable
        self.data = parameter_set().data
        self.vsqx_list = list()

        self._dynamic = self.data[0]
        self._breath = self.data[1]
        self._bright = self.data[2]
        self._clearance = self.data[3]
        self._grawl = self.data[4]
        self._pitch_bend = self.data[5]
        self._gender = self.data[6]
        
        # function
        self.append = append( self.data )
        self.sort = sort( self.data )
        self.delite = delite( self.data )

    def abake(self, data, data_symbol):
        
        for a in data:
            buffer = list()
            for b in a:
                buffer.append(b)
            buffer.append(data_symbol)
            self.vsqx_list.append(buffer)

    def bake(self):
        
        self.vsqx_list = list()

        self.abake(self._dynamic,"D")
        self.abake(self._breath,"B")
        self.abake(self._bright,"R")
        self.abake(self._clearance,"C")
        self.abake(self._grawl,"W")
        self.abake(self._pitch_bend,"P")
        self.abake(self._gender,"G")

        self.vsqx_list.sort()

        return self.vsqx_list

A1 = newParameter()
A1.append.Gender(3,3)
A1.append.Gender(5,5)
A1.append.Gender(7,1)
A1.append.Gender(1,10)
A1.append.Dynamic(5,5)
A1.append.Dynamic(7,1)
A1.append.Gender(4,4)
A1.append.Gender(3,3)
A1.append.Dynamic(1,10)
A1.append.Dynamic(4,4)

print()
print(A1.bake())

#for cc in A1.data:
#    print(cc)

class note:

    def note(self):

        time = 0
        duration = 0
        melody = 69
        velocity = 127
        y = "a"
        p = "a"
        opening = 127

        note = list()
        note.append(time)
        note.append(duration)
        note.append(melody)
        note.append(velocity)
        note.append(y)
        note.append(p)
        note.append(opening)

        return note

class noteData:

    def aa(self):
        return 1