from lxml import etree

def __sPlug(Array):
    
    sPlug = etree.Element("sPlug")

    sPlug.append( etree.Element("id") )
    sPlug.append( etree.Element("name") )
    sPlug.append( etree.Element("version") )

    _id = sPlug[0]
    name = sPlug[1]
    version = sPlug[2]

    _id.text = etree.CDATA(Array[0])
    name.text = etree.CDATA(Array[1])
    version.text = etree.CDATA(Array[2])

    return sPlug

def __pStyle(Array):

    pStyle = etree.Element("pStyle")

    pStyle.append( etree.Element("v", id = "accent") )
    pStyle.append( etree.Element("v", id = "bendDep") )
    pStyle.append( etree.Element("v", id = "bendLen") )
    pStyle.append( etree.Element("v", id = "decay") )
    pStyle.append( etree.Element("v", id = "fallPort") )
    pStyle.append( etree.Element("v", id = "opening") )
    pStyle.append( etree.Element("v", id = "risePort") )

    accent = pStyle[0]
    bendDep = pStyle[1]
    bendLen = pStyle[2]
    decay = pStyle[3]
    fallPort = pStyle[4]
    opening = pStyle[5]
    risePort = pStyle[6]

    accent.text = str(Array[0])
    bendDep.text = str(Array[1])
    bendLen.text = str(Array[2])
    decay.text = str(Array[3])
    fallPort.text = str(Array[4])
    opening.text = str(Array[5])
    risePort.text = str(Array[6])

    return pStyle

def __singer(Array):

    singer = etree.Element("singer")

    singer.append( etree.Element("t") )
    singer.append( etree.Element("bs") )
    singer.append( etree.Element("pc") )

    t = singer[0]
    bs = singer[1]
    pc = singer[2]

    t.text = str(Array[0])
    bs.text = str(Array[1])
    pc.text = str(Array[2])

    return singer

def __cc(Array):

    cc = etree.Element("cc")

    cc.append( etree.Element("t") )

    t = cc[0]

    t.text = str(Array[0])

    _Array = Array[0]

    if   _Array == "P":                       # pitchband
        cc.append( etree.Element("v", id="P") )
        cc[1].text = str(Array[1])

    elif _Array == "R":                       # Bright
        cc.append( etree.Element("v", id="R") )
        cc[1].text = str(Array[1])

    elif _Array == "W":                         # Grawol
        cc.append( etree.Element("v", id="W") )
        cc[1].text = str(Array[1])

    elif _Array == "X" :                        # XrossSynth
        cc.append( etree.Element("v", id="X") )
        cc[1].text = str(Array[1])

    elif _Array == "S" :                        # PitchBend Sense
        cc.append( etree.Element("v", id="S") )
        cc[1].text = str(Array[1])
        
    elif _Array == "C" :                        # Clearance
        cc.append( etree.Element("v", id="C") )
        cc[1].text = str(Array[1])
        
    elif _Array == "T" :                        # Portamento Timing
        cc.append( etree.Element("v", id="T") )
        cc[1].text = str(Array[1])
        
    elif _Array == "B" :                        # Breath
        cc.append( etree.Element("v", id="B") )
        cc[1].text = str(Array[1])
        
    elif _Array == "G" :                        # gender
        cc.append( etree.Element("v", id="G") )
        cc[1].text = str(Array[1])
        
    elif _Array == "D" :                        # dynamic
        cc.append( etree.Element("v", id="D") )
        cc[1].text = str(Array[1])
    
    return cc

def ____seq(Array):

    seq = etree.Element("seq", id = "vibRate")

    seq.append(etree.Element("cc"))

    cc = seq[0]

    cc.append(etree.Element("p"))
    cc.append(etree.Element("v"))

    p = cc[0]
    v = cc[1]

    p.text = str(Array[0])
    v.text = str(Array[1])

    return seq

def ___nStyle(Array):

    nStyle = etree.Element("nStyle")

    nStyle.append( etree.Element("v", id="accent") )
    nStyle.append( etree.Element("v", id="bendDep") )
    nStyle.append( etree.Element("v", id="bendLen") )
    nStyle.append( etree.Element("v", id="decay") )
    nStyle.append( etree.Element("v", id="fallPort") )
    nStyle.append( etree.Element("v", id="opening") )
    nStyle.append( etree.Element("v", id="risePort") )
    nStyle.append( etree.Element("v", id="vibLen") )
    nStyle.append( etree.Element("v", id="vibType") )

    accent = nStyle[0]
    bendDep = nStyle[1]
    bendLen = nStyle[2]
    decay = nStyle[3]
    fallPort = nStyle[4]
    opening = nStyle[5]
    risePort = nStyle[6]
    vibLen = nStyle[7]
    vibType = nStyle[8]

    accent.text = str(Array[0]) 
    bendDep.text = str(Array[1]) 
    bendLen.text = str(Array[2]) 
    decay.text = str(Array[3]) 
    fallPort.text = str(Array[4]) 
    opening.text = str(Array[5]) 
    risePort.text = str(Array[6]) 
    vibLen.text = str(Array[7]) 
    vibType.text = str(Array[8]) 

    return nStyle

def __note(Array):

    note = etree.Element("note")

    note.append(etree.Element("t"))
    note.append(etree.Element("dur"))
    note.append(etree.Element("n"))
    note.append(etree.Element("v"))
    note.append(etree.Element("y"))
    note.append(etree.Element("p"))

    note.append( ___nStyle(Array[6]) )

    t = note[0]
    dur = note[1]
    n = note[2]
    v = note[3]
    y = note[4]
    p = note[5]

    t.text = str(Array[0])
    dur.text = str(Array[1])
    n.text = str(Array[2])
    v.text = str(Array[3])
    y.text = etree.CDATA(Array[4])     # visible
    p.text = etree.CDATA(Array[5])     # to engine

    return note

def _vsPart(Array):
    
    vsPart = etree.Element("vsPart") 
    
    vsPart.append( etree.Element("t") )
    vsPart.append( etree.Element("playTime") )
    vsPart.append( etree.Element("name") )
    vsPart.append( etree.Element("comment") )

    vsPart.append( __sPlug(Array[5]) )
    vsPart.append( __pStyle(Array[6]) )
    vsPart.append( __singer(Array[7]) )

    for _Array in Array[8]:
        vsPart.append( __cc(_Array) )
        
    for _Array in Array[9]:
        vsPart.append( __note(_Array) )

    vsPart.append( etree.Element("plane") )


    t = vsPart[0]
    playTime = vsPart[1]
    name = vsPart[2]
    comment = vsPart[3]
    # __sPlug, __pStyle, __singer, __cc, __note
    plane = vsPart[-1]

    t.text = str(Array[0])
    playTime.text = str(Array[1])
    name.text = etree.CDATA(Array[2])
    comment.text = etree.CDATA(Array[3])
    # __sPlug, __pStyle, __singer, __cc, __note
    plane.text = str(Array[4])

    return vsPart

def vsTrack(Array):

    vsTrack = etree.Element("vsTrack") 
    
    vsTrack.append( etree.Element("tNo") )
    vsTrack.append( etree.Element("name") )
    vsTrack.append( etree.Element("comment") )

    vsTrack.append( _vsPart(Array[3]) )

    tNo = vsTrack[0]
    name = vsTrack[1]
    comment = vsTrack[2]

    tNo.text = str(Array[0])
    name.text = etree.CDATA(Array[1])
    comment.text = etree.CDATA(Array[2])
    
    return vsTrack

#root = vsTrack()

#print(etree.tostring(root, pretty_print=False))