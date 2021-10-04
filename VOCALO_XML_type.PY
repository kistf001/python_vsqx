import pandas as pd
import math
import numpy as np
import gc
import VOCALO_XML_list2vsqx as L2V

def to_ccSet_noteSet( pandas_data_cc_, pandas_data_note_ ):

    skip_CC_1 = 100
    skip_CC_2 = 40

    skip_CC_1 = 50
    skip_CC_2 = 20

    skip_CC_1 = 25
    skip_CC_2 = 10

    _pd_note = pd.read_hdf(pandas_data_note_,'df')
    _pd_cc = pd.read_hdf(pandas_data_cc_,'df')
    
    # 노트 생성
    note_list = _pd_note.values.tolist()[0:]
    cc_list   = _pd_cc.values.tolist()[0:]

    # 판다스 비우기
    del [[_pd_note,_pd_cc]]
    gc.collect()
    
    # note, cc 변환 시작
    note_set = list()
    cc_set = list()
    
    for _notes in note_list:

        time = _notes[0]
        duration = _notes[1]
        note_pitch = _notes[2]
        #note_pitch = 66
        real_pitch = round(cc_list[ int(time) ][6],2)

        note    = [0,0,0,0,"A","g a",[0,0,0,0,0,0,0,0,0]]    # note
        note[0] = int( time ) # time
        note[1] = int( duration ) # duration
        note[2] = int( note_pitch )
        note[3] = 127
        note[4] = real_pitch
        note[5] = _notes[4]
        note[6][5] = _notes[5]
    
        for ahelg in range( note[0], note[0] + note[1], skip_CC_1 ):
        
            cc1 = [ ahelg, "B",  int(cc_list[ahelg][2]) ]
            cc_set.append(cc1)
        
            cc2 = [ ahelg, "R",  int(cc_list[ahelg][3]) ]
            cc_set.append(cc2)
        
            cc3 = [ ahelg, "C",  int(cc_list[ahelg][4]) ]
            cc_set.append(cc3)
        
            cc4 = [ ahelg, "W",  int(0)]#int(cc_list[ahelg][5])  ]
            cc_set.append(cc4)

        for ahelg in range( _notes[0], _notes[0] + _notes[1], skip_CC_2 ):
            
            cc0 = [ ahelg, "D",  int(cc_list[ahelg][1]) ]
            cc_set.append(cc0)

            if ( 0 == 1 ):
                
                # pitch calculation
                cc_pitch = cc_list[ ahelg ][6]              # 오리지널 값
                pitch_difference = cc_pitch - note_pitch    # 오리지널 값 - 노트를 위해 변형된 값
            
                aaa = 0                                     # 피치센서티브
                bbb = 0                                     # 피치값
            
                if( 0 < pitch_difference ):
                    aaa = math.ceil(pitch_difference)
                    bbb = int((pitch_difference / aaa)*(8191))
            
                elif( pitch_difference < 0 ):
                    aaa = math.floor(pitch_difference)
                    bbb = int((pitch_difference / aaa)*(-8192))
                    aaa = -aaa
            
                cc5 = [ ahelg, "P", bbb ]
                cc_set.append(cc5)
            
                cc6 = [ ahelg, "S", aaa ]
                cc_set.append(cc6)

        note_set.append(note)

    return cc_set, note_set
    #return [], note_set

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
        vVoice.append("")
        vVoice.append("")
        vVoice.append(self.vPrm())
        return vVoice

    def vVoiceTable(self):
        vVoiceTable = list()
        return vVoiceTable

class mixer:

    def masterUnit(self):
        masterUnit = list()
        masterUnit.append(0)
        masterUnit.append(0)
        masterUnit.append(0)
        return masterUnit

    def vsUnit(self):
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

    def vsUnit_set(self):
        vsUnit = list()
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
        stUnit.append(0)
        stUnit.append(0)
        stUnit.append(-129)
        return stUnit

    def mixer(self):
        make = list()
        make.append( self.masterUnit() )
        make.append( self.vsUnit_set() )
        make.append( self.monoUnit() )
        make.append( self.stUnit() )
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
        tempo.append(30000)
        return tempo

    def masterTrack(self):

        seqName = "Untitled1"
        comment = "New VSQ File"
        resolution = 480
        preMeasure = 4
        timeSig = self.timeSig()
        tempo = self.tempo()

        masterTrack = list()
        masterTrack.append(seqName)
        masterTrack.append(comment)
        masterTrack.append(resolution)
        masterTrack.append(preMeasure)
        masterTrack.append(timeSig)
        masterTrack.append(tempo)

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

        parameter_time = 0
        parameter_name = 0
        parameter_value = 0

        cc = list()
        cc.append(parameter_time)
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
        playTime = 1536000
        name = "Part"
        comment = "New"
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
    
    def vsPart_set(self):
        return list()

    def vsTrack(self):

        tNo = 0
        name = "48k"
        comment = "C"

        vsTrack = list()
        vsTrack.append(tNo)
        vsTrack.append(name)
        vsTrack.append(comment)
        vsTrack.append(self.vsPart_set())

        return vsTrack

    def vsTrack_set(self):
        return list()

class monoTrack:

    def monoTrack(self):
        monoTrack = list()
        monoTrack.append("")
        return monoTrack

class stTrack:

    def stTrack(self):
        stTrack = list()
        stTrack.append("")
        return stTrack

class aux:

    def aux(self):

        _id = "AUX_VST_HOST_CHUNK_INFO"
        content = "VlNDSwAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="

        aux = list()
        aux.append(_id)
        aux.append(content)

        return aux

class vsqx:

    def to_vsqx4(self, dir = "./Sample"):

        L2V.list2vsqx(self.vsqx4).to_file(dir)

    def new_vVoiceTable(self, list, productName):
        self.product_name = productName
        name = self.product_name
        newVoice = vVoiceTable().vVoice()
        newVoice[0] = self.exist_number - 1
        newVoice[1] = 0
        newVoice[2] = str(name)
        newVoice[3] = str(name)

        return newVoice

    def new_mixer(self, list):

        new_vsUnit = mixer().vsUnit()
        new_vsUnit[0] = self.exist_number - 1

        return new_vsUnit

    def new_vsTrack(self, cc, note):

        new_vsTrack = vsTrack().vsTrack()

        new_vsTrack[0] = self.exist_number - 1
        
        access_vsPart_set = new_vsTrack[3]
        
        new_vsPart = vsTrack().vsPart()
        
        access_vsPart_set.append(new_vsPart)

        new_vsPart[7], new_vsPart[8] = to_ccSet_noteSet(cc, note)
        
        return new_vsTrack

    def addTrack(self, ___cc, ___note, productName):

        # 최대 트랙 수가 차면 -1 반환
        if(self.exist_number > 16 ):
            return -1

        # 트랙의 총 수 기록
        self.exist_number = self.exist_number + 1
        
        # 보이스 테이블 추가
        vVoiceTable = self.vsqx4[2]
        vVoiceTable.append(self.new_vVoiceTable([0], productName))

        # 믹서 추가
        mixer = self.vsqx4[3]
        vsUnit_set = mixer[1]
        vsUnit_set.append(self.new_mixer([0]))

        # 트랙 추가
        vsTrack_set = self.vsqx4[5]
        vsTrack_set.append(self.new_vsTrack(___cc, ___note))

    def __init__(self):

        self.product_name = "BCNFCY43LB2LZCD4"
        
        self.exist_number = 0
        
        self.vsqx4 = list()
        self.vsqx4.append( vender().vender() )
        self.vsqx4.append( version().version() )
        self.vsqx4.append( vVoiceTable().vVoiceTable() )
        self.vsqx4.append( mixer().mixer() )
        self.vsqx4.append( masterTrack().masterTrack() )
        self.vsqx4.append( vsTrack().vsTrack_set() )
        self.vsqx4.append( monoTrack().monoTrack() )
        self.vsqx4.append( stTrack().stTrack() )
        self.vsqx4.append( aux().aux() )
