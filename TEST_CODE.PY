
# vender
# version
# vVoiceTable
# mixer
# masterTrack
# vsTrack
# monoTrack
# stTrack
# aux

class vender:

    def vender(self):
        vender = "Yamaha corporation"
        return vender

class version:

    def version(self):
        version = "4.0.0.3"
        return version

class vVoiceTable:

    def vPrm(self):
        vPrm = list()
        vPrm.append(0)
        vPrm.append(0)
        vPrm.append(0)
        vPrm.append(0)
        vPrm.append(0)
        return vPrm

    def vVoice(self):
        vVoice = list()
        vVoice.append(0)
        vVoice.append(0)
        vVoice.append(0)
        vVoice.append(0)
        vVoice.append(self.vPrm())
        return vVoice

    def vVoiceTable(self):
        vVoiceTable = list()
        vVoiceTable.append(self.vVoice())
        return vVoiceTable

class mixer:

    def masterUnit(self):
        masterUnit = list()
        masterUnit.append(0)
        masterUnit.append(0)
        masterUnit.append(0)
        return masterUnit

    def vsUnit_element(self):
        vsUnit = list()
        vsUnit.append(0)
        vsUnit.append(0)
        vsUnit.append(-898)
        vsUnit.append(0)
        vsUnit.append(0)
        vsUnit.append(0)
        vsUnit.append(64)
        vsUnit.append(0)
        return vsUnit

    def monoUnit(self):
        monoUnit = list()
        monoUnit.append(0)
        monoUnit.append(-898)
        monoUnit.append(0)
        monoUnit.append(0)
        monoUnit.append(0)
        monoUnit.append(64)
        monoUnit.append(0)
        return monoUnit

    def stUnit(self):
        stUnit = list()
        stUnit.append(0)
        stUnit.append(-898)
        stUnit.append(0)
        stUnit.append(0)
        return stUnit

    def mixer(self):
        make = list()
        make.append(self.masterUnit())
        make.append(list())
        make.append(self.monoUnit())
        make.append(self.stUnit())
        return make

class masterTrack:

    def timeSig(self):
        timeSig = list()
        timeSig.append(0)
        timeSig.append(4)
        timeSig.append(4)
        return timeSig

    def tempo(self):
        tempo = list()
        tempo.append(0)
        tempo.append(12000)
        return tempo

    def masterTrack(self):
        masterTrack = list()
        masterTrack.append("Untitled0")
        masterTrack.append("New VSQ File")
        masterTrack.append(480)
        masterTrack.append(4)
        masterTrack.append(self.timeSig())
        masterTrack.append(self.tempo())
        return masterTrack

class vsTrack:

    def __nStyle(self):

        accent = 0
        bendDep = 0
        bendLen = 0
        decay = 0
        fallPort = 0
        opening = 0
        risePort = 0
        vibLen = 0
        vibType = 0

        nStyle = list()
        nStyle.append(accent)
        nStyle.append(bendDep)
        nStyle.append(bendLen)
        nStyle.append(decay)
        nStyle.append(fallPort)
        nStyle.append(opening)
        nStyle.append(risePort)
        nStyle.append(vibLen)
        nStyle.append(vibType)

        return nStyle

    def note(self):
		
        t = 0
        dur = 0
        n = 0
        v = 0
        y = ""
        p = ""
        nStyle = self.__nStyle()
        
        note = list()
        note.append(t)
        note.append(dur)
        note.append(n)
        note.append(v)
        note.append(y)
        note.append(p)
        note.append(nStyle)

        return note

    def cc(self):

        parameter_name = 0
        parameter_value = 0

        cc = list()
        cc.append(parameter_name)
        cc.append(parameter_value)

        return cc

    def singer(self):
        singer = list()
        singer.append(0)
        singer.append(0)
        singer.append(0)
        return singer

    def pStyle(self):
        pStyle = list()
        pStyle.append(0)
        pStyle.append(0)
        pStyle.append(0)
        pStyle.append(0)
        pStyle.append(0)
        pStyle.append(0)
        pStyle.append(0)
        return pStyle

    def sPlug(self):
        sPlug = list()
        sPlug.append("ACA9C502-A04B-42b5-B2EB-5CEA36D16FCE")
        sPlug.append("VOCALOID2 Compatible Style")
        sPlug.append("3.0.0.1")
        return sPlug
    
    def vsPart(self):

        t = 7680
        playTime = 61440
        name = "NewPart"
        comment = "New Musical Part"
        sPlug = self.sPlug()
        pStyle = self.pStyle()
        singer = self.singer()
        cc_bunch = list()
        note_bunch = list()
        plane = 0

        vsPart = list()
        vsPart.append(t)
        vsPart.append(playTime)
        vsPart.append(name)
        vsPart.append(comment)
        vsPart.append(sPlug)
        vsPart.append(pStyle)
        vsPart.append(singer)
        vsPart.append(cc_bunch)
        vsPart.append(note_bunch)
        vsPart.append(plane)

        return vsPart

    def vsTrack(self):

        tNo = 0
        name = ""
        comment = ""

        vsTrack = list()
        vsTrack.append(tNo)
        vsTrack.append(name)
        vsTrack.append(comment)
        vsTrack.append(self.vsPart())

        return vsTrack

class monoTrack:

    def monoTrack(self):
        monoTrack = ""
        return monoTrack

class stTrack:

    def stTrack(self):
        stTrack = ""
        return stTrack

class aux:

    def aux(self):

        _id = "AUX_VST_HOST_CHUNK_INFO"
        content = "VlNDSwAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="

        aux = list()
        aux.append(_id)
        aux.append(content)

        return aux

class empty_vsqx:
    
    def __init__(self):

        vender = list()
        version = list()
        vVoiceTable = list()
        mixer = list()
        masterTrack = list()
        vsTrack = list()
        monoTrack = list()
        stTrack = list()
        aux = list()

        self.data = list()

        vsq = self.data
        vsq.append(vender)
        vsq.append(version)
        vsq.append(vVoiceTable)
        vsq.append(mixer)
        vsq.append(masterTrack)
        vsq.append(vsTrack)
        vsq.append(monoTrack)
        vsq.append(stTrack)
        vsq.append(aux)

class vsqx:

    def make_empty_vsqx(self):
        return empty_vsqx().data

    def write_basic_data_vsqx(self, vsqx):
        
        vsqx[0] = vender().vender()
        vsqx[1] = version().version()
        vsqx[2] = mixer().mixer()
        vsqx[3] = vVoiceTable().vVoiceTable()
        vsqx[4] = masterTrack().masterTrack()

        vsqx[6] = monoTrack().monoTrack()
        vsqx[7] = stTrack().stTrack()
        vsqx[8] = aux().aux()

        return 0

    def __init__(self, *args, **kwargs):

        vsqx = self.make_empty_vsqx()
        self.write_basic_data_vsqx(vsqx)
        self.data = vsqx

for a in vsqx().data:
    print(a)