from lxml import etree

example_cc_array =[]
example_cc = ['P',[7680,1]]

# 0=>시작타임번호, 1=>지속길이, 2=>, 3=>벨로서티, 4=>,5=>
example_note_array = []
example_note = [7680,3420,58,64,"gam","g a 4",[50,0,0,50,0,127,0,66,1,[[123123],[64]],[[123123],[50]]]]
                #0    1   2  3   4   5   6 6 6  6 6   6 6  6 6 6

#===============================================
def cc(Array):
    """
    Array[0] => id
    Array[1][0] => time Point
    Array[1][1] => value 
    """

    cc = etree.Element("cc")

    if Array[0] == "P":
        # 피치밴드
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="P") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])

    elif Array[0] == "R":
        # Bright
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="R") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])

    elif Array[0]=="W":
        # Grawol
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="W") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])

    elif(Array[0]=="X"):
        # XrossSynth
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="X") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])

    elif(Array[0]=="S"):
        # PitchBend Sense
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="S") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])
        
    elif(Array[0]=="C"):
        # Clearance
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="C") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])
        
    elif(Array[0]=="T"):
        # Portamento Timing
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="T") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])
        
    elif(Array[0]=="B"):
        # Breath
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="B") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])
        
    elif(Array[0]=="G"):
        # gender
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="G") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])
        
    elif(Array[0]=="D"):
        # dynamic
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id="D") )
        cc[0].text = str(Array[1][0])
        cc[1].text = str(Array[1][1])
    
    return cc

def note(Array):
    """
    Array
    [] => t
    [] => dur
    [] => n
    [] => v
    [] => y
    [] => p
    [] => nStyle

    """
    # (1노트세트데이터)를 처리하여 note로 만들어줌

    # */
    note = etree.Element("note")
    
    # */*/
    # note에 엘레멘트를 추가
    note.append( etree.Element("t") )
    note.append( etree.Element("dur") )
    note.append( etree.Element("n") )
    note.append( etree.Element("v") )
    note.append( etree.Element("y") )       # 눈깔에 들어가는 것
    #note.append( etree.Element("p", lock="1") )       # 엔진에 돌어가는 것
    note.append( etree.Element("p") )       # 엔진에 돌어가는 것
    note.append( etree.Element("nStyle") )

    # */*/*/
    
    # 이름변경
    nStyle = note[6]
    
    # note의 엘레멘트의 엘리멘트를 추가 
    nStyle.append( etree.Element("v", id="accent") )
    nStyle.append( etree.Element("v", id="bendDep") )
    nStyle.append( etree.Element("v", id="bendLen") )
    nStyle.append( etree.Element("v", id="decay") )
    nStyle.append( etree.Element("v", id="fallPort") )
    nStyle.append( etree.Element("v", id="opening") )
    nStyle.append( etree.Element("v", id="risePort") )
    nStyle.append( etree.Element("v", id="vibLen") )
    nStyle.append( etree.Element("v", id="vibType") )

    nStyle.append( etree.Element("seq", id = "vibDep") )   # vibDep
    nStyle[9].append( etree.Element("cc"))
    nStyle[9][0].append( etree.Element("p"))
    nStyle[9][0].append( etree.Element("v"))

    nStyle.append( etree.Element("seq", id = "vibRate") )   # vibRate
    nStyle[10].append( etree.Element("cc"))
    nStyle[10][0].append( etree.Element("p"))
    nStyle[10][0].append( etree.Element("v"))

    note[0].text = str(Array[0])
    note[1].text = str(Array[1])
    note[2].text = str(Array[2])
    note[3].text = str(Array[3])
    #note[4].text = etree.CDATA(str(Array[4]))
    #note[5].text = etree.CDATA(str(Array[5]))
    note[4].text = "!@!@!@!!!" + Array[4] + "!!!@!@!@!"
    note[5].text = "!@!@!@!!!" + Array[5] + "!!!@!@!@!"
    note[6][0].text = str(Array[6][0])
    note[6][1].text = str(Array[6][1])
    note[6][2].text = str(Array[6][2])
    note[6][3].text = str(Array[6][3])
    note[6][4].text = str(Array[6][4])
    note[6][5].text = str(Array[6][5])
    note[6][6].text = str(Array[6][6])
    note[6][7].text = str(Array[6][7])
    note[6][8].text = str(Array[6][8])
    note[6][ 9][0][0].text = str(Array[6][ 9][0][0])
    note[6][ 9][0][1].text = str(Array[6][ 9][1][0])
    note[6][10][0][0].text = str(Array[6][10][0][0])
    note[6][10][0][1].text = str(Array[6][10][1][0])

    return note

def vsPart(vsPartArray):

    ccDataArray = vsPartArray[0]
    NoteDataArray = vsPartArray[1]
    vsPartSetup = vsPartArray[2]
    # */
    vsPart = etree.Element("vsPart")

    # */*/
    #vsPart에 엘레멘트 추가
    vsPart.append( etree.Element("t") )
    vsPart.append( etree.Element("playTime") )
    vsPart.append( etree.Element("name") )
    vsPart.append( etree.Element("comment") )
    vsPart.append( etree.Element("sPlug") )
    vsPart.append( etree.Element("pStyle") )
    vsPart.append( etree.Element("singer") )

    for _ccDataArray in ccDataArray:
        vsPart.append(cc(_ccDataArray))

    for _NoteDataArray in NoteDataArray:
        vsPart.append(note(_NoteDataArray))

    vsPart.append( etree.Element("plane") )

    # */*/*/
    
    # 이름 변경
    t = vsPart[0]
    playTime = vsPart[1]
    name = vsPart[2]
    comment = vsPart[3]
    sPlug = vsPart[4]
    pStyle = vsPart[5]
    singer = vsPart[6]
    plane = vsPart[-1]

    # vsPart의 엘레멘트의 엘레멘트를 추가
    sPlug.append( etree.Element("id") )
    sPlug.append( etree.Element("name") )
    sPlug.append( etree.Element("version") )

    pStyle.append( etree.Element("v", id = "accent") )
    pStyle.append( etree.Element("v", id = "bendDep") )
    pStyle.append( etree.Element("v", id = "bendLen") )
    pStyle.append( etree.Element("v", id = "decay") )
    pStyle.append( etree.Element("v", id = "fallPort") )
    pStyle.append( etree.Element("v", id = "opening") )
    pStyle.append( etree.Element("v", id = "risePort") )

    singer.append( etree.Element("t") )
    singer.append( etree.Element("bs") )
    singer.append( etree.Element("pc") )

    # vsPart의 엘레멘트의 엘레멘트의 값을 변경
    t.text = str(vsPartSetup[0])
    playTime.text = str(vsPartSetup[1])
    name.text = etree.CDATA("NewPart")
    comment.text = etree.CDATA("New Musical Part")
    sPlug[0].text = etree.CDATA("ACA9C502-A04B-42b5-B2EB-5CEA36D16FCE")
    sPlug[1].text = etree.CDATA("VOCALOID2 Compatible Style")
    sPlug[2].text = etree.CDATA("3.0.0.1")
    pStyle[0].text = str(50)
    pStyle[1].text = str(8)
    pStyle[2].text = str(0)
    pStyle[3].text = str(50)
    pStyle[4].text = str(0)
    pStyle[5].text = str(127)
    pStyle[6].text = str(0)
    singer[0].text = str(0)
    singer[1].text = str(0)
    # 사용자가 커스텀한 제품 값의 선택 값
    singer[2].text = str(vsPartArray[3])
    plane.text = str(0)

    return vsPart

def vsUnit(Number = 0):
    
    vsUnit = etree.Element("vsUnit")
    
    vsUnit.append( etree.Element("tNo") )
    vsUnit.append( etree.Element("iGin") )
    vsUnit.append( etree.Element("sLvl") )
    vsUnit.append( etree.Element("sEnable") )
    vsUnit.append( etree.Element("m") )
    vsUnit.append( etree.Element("s") )
    vsUnit.append( etree.Element("pan") )
    vsUnit.append( etree.Element("vol") )

    vsUnit[0].text = str(Number)
    vsUnit[1].text = str(0)
    vsUnit[2].text = str(-898)
    vsUnit[3].text = str(0)
    vsUnit[4].text = str(0)
    vsUnit[5].text = str(0)
    vsUnit[6].text = str(64)
    vsUnit[7].text = str(0)

    return vsUnit

def vVoice(vVoiceValue):
    """
    유저 커스텀 보이스를 저장함
    """
    vVoice = etree.Element("vVoice")

    vVoice.append( etree.Element("bs") )
    vVoice.append( etree.Element("pc") )
    vVoice.append( etree.Element("id") )
    vVoice.append( etree.Element("name") )
    vVoice.append( etree.Element("vPrm") )

    vPrm = vVoice[4]
    vPrm.append( etree.Element("bre") )
    vPrm.append( etree.Element("bri") )
    vPrm.append( etree.Element("cle") )
    vPrm.append( etree.Element("gen") )
    vPrm.append( etree.Element("ope") )


    vVoice[0].text = str(vVoiceValue[0])
    vVoice[1].text = str(vVoiceValue[1])
    vVoice[2].text = etree.CDATA(str(vVoiceValue[2]))
    vVoice[3].text = etree.CDATA(str(vVoiceValue[3]))
    
    vPrm[0].text = str(vVoiceValue[4])
    vPrm[1].text = str(vVoiceValue[5])
    vPrm[2].text = str(vVoiceValue[6])
    vPrm[3].text = str(vVoiceValue[7])
    vPrm[4].text = str(vVoiceValue[8])
    
    #vVoice[0].text = str(0)
    #vVoice[1].text = str(0)
    #vVoice[2].text = etree.CDATA("BMGK9EC6G4RPWMB3")
    #vVoice[3].text = etree.CDATA("Yukari")
    #
    #vPrm[0].text = str(0)
    #vPrm[1].text = str(0)
    #vPrm[2].text = str(0)
    #vPrm[3].text = str(0)
    #vPrm[4].text = str(0)

    return vVoice

#===============================================
def vender():
    vender = etree.Element("vender")
    vender.text = etree.CDATA('Yamaha corporation')
    return vender

def version():
    version = etree.Element("version")
    version.text = etree.CDATA('4.0.0.3')
    return version

def vVoiceTable(vVoiceArray):
    """
    [n][9]

    """

    vVoiceTable = etree.Element("vVoiceTable")

    for a in vVoiceArray:
        vVoiceTable.append(vVoice(a))

    #vVoiceTable.append( etree.Element("vVoice") )
    #
    #vVoice = vVoiceTable[0]
    #vVoice.append( etree.Element("bs") )
    #vVoice.append( etree.Element("pc") )
    #vVoice.append( etree.Element("id") )
    #vVoice.append( etree.Element("name") )
    #vVoice.append( etree.Element("vPrm") )
    #
    #vPrm = vVoice[4]
    #vPrm.append( etree.Element("bre") )
    #vPrm.append( etree.Element("bri") )
    #vPrm.append( etree.Element("cle") )
    #vPrm.append( etree.Element("gen") )
    #vPrm.append( etree.Element("ope") )
    #
    #vVoice[0].text = str(0)
    #vVoice[1].text = str(0)
    #vVoice[2].text = etree.CDATA("BMGK9EC6G4RPWMB3")
    #vVoice[3].text = etree.CDATA("Yukari")
    #
    #vPrm[0].text = str(0)
    #vPrm[1].text = str(0)
    #vPrm[2].text = str(0)
    #vPrm[3].text = str(0)
    #vPrm[4].text = str(0)

    return vVoiceTable

def mixer(vsUnit_Number):

    mixer = etree.Element("mixer")

    # Mixer에 엘레멘트 추가
    mixer.append( etree.Element("masterUnit") )

    #for a in range(0, vsUnit_Number):
    #    mixer.append( vsUnit() )

    for acc in range(0,vsUnit_Number):
        mixer.append( vsUnit(acc) )

    mixer.append( etree.Element("monoUnit") )
    mixer.append( etree.Element("stUnit") )

    masterUnit = mixer[0]
    monoUnit = mixer[-2]
    stUnit = mixer[-1]

    # Mixer의 엘레멘트의 엘레멘트 추가
    masterUnit.append( etree.Element("oDev") )
    masterUnit.append( etree.Element("rLvl") )
    masterUnit.append( etree.Element("vol") )

    monoUnit.append( etree.Element("iGin") )
    monoUnit.append( etree.Element("sLvl") )
    monoUnit.append( etree.Element("sEnable") )
    monoUnit.append( etree.Element("m") )
    monoUnit.append( etree.Element("s") )
    monoUnit.append( etree.Element("pan") )
    monoUnit.append( etree.Element("vol") )

    stUnit.append( etree.Element("iGin") )
    stUnit.append( etree.Element("m") )
    stUnit.append( etree.Element("s") )
    stUnit.append( etree.Element("vol") )

    # Mixer의 엘레멘트의 엘레멘트의 값 변경
    masterUnit[0].text = str(0)
    masterUnit[1].text = str(0)
    masterUnit[2].text = str(0)

    monoUnit[0].text = str(0)
    monoUnit[1].text = str(-898)
    monoUnit[2].text = str(0)
    monoUnit[3].text = str(0)
    monoUnit[4].text = str(0)
    monoUnit[5].text = str(64)
    monoUnit[6].text = str(0)

    stUnit[0].text = str(0)
    stUnit[1].text = str(0)
    stUnit[2].text = str(0)
    stUnit[3].text = str(-129)

    return mixer

def masterTrack():

    masterTrack = etree.Element("masterTrack")

    # masterTrack에 엘레멘트 추가
    masterTrack.append( etree.Element("seqName") )
    masterTrack.append( etree.Element("comment") )
    masterTrack.append( etree.Element("resolution") )
    masterTrack.append( etree.Element("preMeasure") )
    masterTrack.append( etree.Element("timeSig") )
    masterTrack.append( etree.Element("tempo") )

    seqName = masterTrack[0]
    comment = masterTrack[1]
    resolution = masterTrack[2]
    preMeasure = masterTrack[3]
    timeSig = masterTrack[4]
    tempo = masterTrack[5]

    timeSig.append( etree.Element("m") )
    timeSig.append( etree.Element("nu") )
    timeSig.append( etree.Element("de") )

    tempo.append( etree.Element("t") )
    tempo.append( etree.Element("v") )

    # masterTrack의 엘레멘트의 값을 변경
    # */*/
    seqName.text = etree.CDATA("Untitled3")
    comment.text = etree.CDATA("New VSQ File")
    resolution.text = str(480)
    preMeasure.text = str(4)

    # */*/*/
    timeSig[0].text = str(0)
    timeSig[1].text = str(4)
    timeSig[2].text = str(4)

    tempo[0].text = str(0)
    tempo[1].text = str(30000)

    return masterTrack

def vsTrack(vsTrackArray, dfd = ""):
    """
    # vsTrack_tNo, cc_array, note_array \n
    vsTrack에는 vsPart가 들어간다. \n
    cc와 vsPart는 여러개가 들어갈 수 있다.

    """

    vsTrack_tNo, vsPartArray = vsTrackArray

    vsTrack = etree.Element("vsTrack") 

    # vsTrack의 엘레멘트를 추가
    vsTrack.append( etree.Element("tNo") )
    vsTrack.append( etree.Element("name") )
    vsTrack.append( etree.Element("comment") )
    for a in vsPartArray:
        vsTrack.append( vsPart(a) )

    #vsTrack.append( vsPart(note_array, cc_array, [7680,(1920*400)]) )

    # vsTrack의 엘레멘트의 값을 변경
    vsTrack[0].text = str(vsTrack_tNo)
    vsTrack[1].text = etree.CDATA("Track")
    vsTrack[2].text = etree.CDATA("Track")

    if vsTrack_tNo == 0:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 1:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 2:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 3:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 4:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 5:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 6:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 7:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 8:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 9:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 10:
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 11: 
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 12: 
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 13: 
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 14: 
        vsTrack[1].text = etree.CDATA(dfd)
    elif vsTrack_tNo == 15: 
        vsTrack[1].text = etree.CDATA(dfd)
 
    return vsTrack

def vsTrackMulti(root, vsTrackArray, dfd= "" ):
    
    """
    Array[0] => track Number\n
    Array[1] => cc Array\n
    Array[2] => note Array\n

    """

    for a in vsTrackArray :
        root.append( vsTrack(a,dfd) )
        #vsTrack(a)

def monoTrack():

    monoTrack = etree.Element("monoTrack")
    monoTrack.text = "NONENONENONE"

    return monoTrack

def stTrack():

    stTrack = etree.Element("stTrack")
    stTrack.text = "NONENONENONE"

    return stTrack

def aux():

    aux = etree.Element("aux")

    aux.append( etree.Element("id") )
    aux.append( etree.Element("content") )

    aux[0].text = etree.CDATA("AUX_VST_HOST_CHUNK_INFO")
    aux[1].text = etree.CDATA("VlNDSwAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")

    return aux

def MolderAndToString(root):
    
    String = str(etree.tostring(root, pretty_print=True))
    String = String.replace(
        "b'<vsq4>",
        """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <vsq4 xmlns="http://www.yamaha.co.jp/vocaloid/schema/vsq4/"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.yamaha.co.jp/vocaloid/schema/vsq4/ vsq4.xsd">"""
        )

    String = String.replace("</aux>\\n<","</aux>\n*<")
    String = String.replace("\\'","'")
    String = String.replace("\\\\","\\")
    String = String.replace("!@!@!@!!!","<![CDATA[")
    String = String.replace("!!!@!@!@!","]]>")
    String = String.replace(">\\n  <",">\n   *<")
    String = String.replace(">\\n    <",">\n       *<")
    String = String.replace(">\\n      <",">\n           *<")
    String = String.replace(">\\n        <",">\n               *<")
    String = String.replace(">\\n          <",">\n                   *<")
    String = String.replace(">\\n            <",">\n                       *<")
    String = String.replace(">\\n              <",">\n                           *<")
    String = String.replace(">\\n                <",">\n                               *<")
    String = String.replace("</vsq4>\\n'","</vsq4>")
    String = String.replace("*"," ")
    String = String.replace(">NONENONENONE<",">\n    <")

    return String

#########################################################
# Start
#########################################################

import numpy as np
import copy

def randomNote(NoteArraya, barNum):

    Pd = [" a"," i"," M"," e"," o"]

    Bright = [
                # 청음 (무성음)
                "k", "k'", 
                "s", "S", 
                "t", "t" + "'",
                "tS", "ts",
                "n", "J", 
                "h", "h"+chr(92), "C",
                "p"+chr(92), "p"+chr(92)+"'", 
                "m", "m'", 
                "j", 
                "4", "4'", 
                "w",

                # 탁음 (유성음)
                "g", "g'", 
                "dz", "z", "dZ", "z", 
                "d", "d'", 
                "b", "b'", 
                "p", "p'" 
             ]

    nn  =    [ "n", "J", "m", "m"+"'", "N", "N"+"'", "N"+chr(92) ]

    # 1 : 1920
    # 자투리 4개 + 기본 400개
    # 7680 + 728000

    Note = [0,0,60,100, "a","a", [0,0,0,0, 0,0,0,0, 0,[[0],[0]],[[0],[0]]]]
            # 위치, 길이, 음높이, 다이나믹스
    maxbar = 1920 * barNum

    c = 0

    while(1):

        s = np.random.randint( int(1920*1), int(1920*2) )

        asd = np.random.randint( 0,10 )
        ad = np.random.randint( 0,5 )

        Note[4] = str(Bright[asd] + Pd[ad])
        Note[5] = str(Bright[asd] + Pd[ad])

        Note[0] = c

        c = c + s

        if c > maxbar:

            Note[1] = s - (c-(maxbar))
            Note[2] = np.random.randint(60-7, 60+26)

            NoteArraya.append(copy.deepcopy(Note))

            break

        Note[1] = s
        Note[2] = np.random.randint(60-7, 60+26)

        NoteArraya.append(copy.deepcopy(Note))

def CCArrayToFile(ccArrays, barNum,Name = "", type = 0):
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

    datatype = [
        "dynamics",
        "breathiness",
        "brightness",
        "clearness",
        "opening",
        "gender_factor",
        "portamento_timing",
        "cross_synth",
        "growl",
        "pitch_bend",
        "pitch_bend_sensitivity"
    ]

    maxbar = 1920 * barNum

    String = []

    Time = 0

    ac = []

    for a in ccArrays:
        ac.append( [ a[1][0],a[1][1],a[2] ] )

    x = np.array(ac)

    np.save(Name +"_"+ datatype[type], x)

def NoteToFile(NoteArray, Name=""):

    ac = []

    for a in NoteArray:
        ac.append( a )

    x = np.array(ac)

    np.save(Name + ".score", x)


def TrackMaker(TargetArray, RepeatNum):

    import copy

    if(RepeatNum>16):
        RepeatNum = 16

    s = []

    #print(TargetArray[1][0][3])

    for ac in range(0, RepeatNum):

        # voice select
        TargetArray[1][0][3] = np.random.randint(low=0,high = 30)

        # track Number
        TargetArray[0]=ac
        s.append( copy.deepcopy(TargetArray) )

    return s


NoteArray = []

print("SetNOTE")
randomNote(NoteArray,800)

print("SetCC")
import Voca4py
#Dynamics    = Voca4py.BarSize1920.CCdynamics(800)
#Breathiness = Voca4py.BarSize1920.CCbreathiness(800)
#Brightness  = Voca4py.BarSize1920.CCbrightness(800)
#Clearness   = Voca4py.BarSize1920.CCclearness(800)
#Growl       = Voca4py.BarSize1920.CCgrwol(800)
Dynamics    = Voca4py.BarSize960.CCdynamics(800)
Breathiness = Voca4py.BarSize960.CCbreathiness(800)
Brightness  = Voca4py.BarSize960.CCbrightness(800)
Clearness   = Voca4py.BarSize960.CCclearness(800)
Growl       = Voca4py.BarSize960.CCgrwol(800)

# 트랙 어레이
# 파트 어레이
# 노트데이터 어레이[n], CC데이터 어레이[n], 설정데이터 어레이[n]

import VocaloidVoiceBank_List

vVoice__ = VocaloidVoiceBank_List.selected

TrackTargetArray =  [ # track 0
                        0,  [   # part
                                [   Dynamics
                                  + Breathiness 
                                  + Brightness
                                  + Clearness
                                  + Growl
                                  , NoteArray, [int(1920*4), int(1920*800)], 1
                                ]
                            ]
                    ]

vstrack__1  =   TrackMaker(TrackTargetArray,16)

    # [n * [ 0, [[ D+B+B+C+G, Note, [X,Y], VoiceBankNumber ]] ] ]

    # track
        # part{trackNumber(note[n],cc[n],setup[2])} 
        # part{trackNumber(note[n],cc[n],setup[2])}

    # track
        # part{trackNumber(note[n],cc[n],setup[2])} 
        # part{trackNumber(note[n],cc[n],setup[2])}

   #[
   #   [ # track 0
   #       0,  [   # part
   #               [   Dynamics
   #                 + Breathiness 
   #                 + Brightness
   #                 + Clearness
   #                 + Growl
   #                 , NoteArray, [int(1920*4), int(1920*800)], 1
   #               ]
   #           ]
   #   ],
   #]

def datasetMaker(Number=1):
    
    root = etree.Element("vsq4")

    root.append( vender() )
    root.append( version() )
    root.append( vVoiceTable(vVoice__) )
    root.append( mixer(len(vstrack__1)) )
    root.append( masterTrack() )
    vsTrackMulti( root, vstrack__1, )
    root.append( monoTrack() )
    root.append( stTrack() )
    root.append( aux() )

    name = str(Number)

    print("GOFile")
    NoteToFile(NoteArray,name)
    CCArrayToFile(Dynamics,     800, name, 0)
    CCArrayToFile(Breathiness,  800, name, 1)
    CCArrayToFile(Brightness,   800, name, 2)
    CCArrayToFile(Clearness,    800, name, 3)
    CCArrayToFile(Growl,        800, name, 8)

    f = open(str(Number)+".vsqx", 'w')
    f.write(MolderAndToString(root))
    f.close()

datasetMaker(4)