import VOCALO_XML_edit as vsqxE

# import numpy as np

class vsqx:

    def __init__(self, *args, **kwargs):
        self.data = vsqxE.empty_vsqx().start()

    def appendTrack(self):
        vsqxE.track_Append(self.data)
    
    def delTrack(self, position):
        vsqxE.track_delite(self.data, position)

A = vsqx()
A.appendTrack()
A.appendTrack()
A.appendTrack()
A.appendTrack()
A.appendTrack()
A.appendTrack()
A.appendTrack()
A.appendTrack()
A.appendTrack()
A.appendTrack()

for acc in A.data:
    print(acc)

vsTrack_set = A.data[5]
print("\n\n vsTrack_set : ")
for acc in vsTrack_set:
    print(acc)

mixer = A.data[3][1]
print("\n\n mixer : ")
for acc in mixer:
    print(acc)

# "P" 피치밴드
# "R" Bright
# "W" Grawol
# "X" XrossSynth
# "S" PitchBend Sense
# "C" Clearance
# "T" Portamento Timing
# "B" Breath
# "G" gender
# "D" dynamic