from lxml import etree

class vender:

    def __init__(self, Array = "Yamaha corporation"):
    
        vender = etree.Element("vender")

        vender.text = etree.CDATA(Array)

        self.data = vender

class version:

    def __init__(self, Array = "4.0.0.3"):
    
        version = etree.Element("version")

        version.text = etree.CDATA(Array)

        self.data = version

class vVoiceTable:

    def __vPrm(self, Array):
        
        vPrm = etree.Element("vPrm")

        vPrm.append( etree.Element("bre") )
        vPrm.append( etree.Element("bri") )
        vPrm.append( etree.Element("cle") )
        vPrm.append( etree.Element("gen") )
        vPrm.append( etree.Element("ope") )
        
        bre = vPrm[0]
        bri = vPrm[1]
        cle = vPrm[2]
        gen = vPrm[3]
        ope = vPrm[4]

        bre.text = str(0)
        bri.text = str(0)
        cle.text = str(0)
        gen.text = str(0)
        ope.text = str(0)

        return vPrm
        
    def _vVoice(self, Array):
        
        vVoice = etree.Element("vVoice")

        vVoice.append( etree.Element("bs") )
        vVoice.append( etree.Element("pc") )
        vVoice.append( etree.Element("id") )
        vVoice.append( etree.Element("name") )

        bs = vVoice[0]
        pc = vVoice[1]
        _id = vVoice[2]
        name = vVoice[3]

        bs.text = str( Array[0] )
        pc.text = str( Array[1] )
        _id.text = etree.CDATA( Array[2] )
        name.text = etree.CDATA( Array[3] )

        vVoice.append( self.__vPrm(Array[4]) )

        return vVoice

    def __init__(self, Array):

        vVoiceTable = etree.Element("vVoiceTable")

        for _Array in Array:
            vVoiceTable.append( self._vVoice(_Array) )

        self.data = vVoiceTable

class mixer:
    
    def _masterUnit(self, Array):
        
        masterUnit = etree.Element("masterUnit")
        
        masterUnit.append( etree.Element("oDev") )
        masterUnit.append( etree.Element("rLvl") )
        masterUnit.append( etree.Element("vol") )

        oDev = masterUnit[0]
        rLvl = masterUnit[1]
        vol = masterUnit[2]

        oDev.text = str(Array[0])
        rLvl.text = str(Array[1])
        vol.text = str(Array[2])

        return masterUnit

    def _vsUnit(self, Array):
        
        vsUnit = etree.Element("vsUnit")
        
        vsUnit.append( etree.Element("tNo") )
        vsUnit.append( etree.Element("iGin") )
        vsUnit.append( etree.Element("sLvl") )
        vsUnit.append( etree.Element("sEnable") )
        vsUnit.append( etree.Element("m") )
        vsUnit.append( etree.Element("s") )
        vsUnit.append( etree.Element("pan") )
        vsUnit.append( etree.Element("vol") )

        tNo = vsUnit[0]
        iGin = vsUnit[1]
        sLvl = vsUnit[2]
        sEnable = vsUnit[3]
        m = vsUnit[4]
        s = vsUnit[5]
        pan = vsUnit[6]
        vol = vsUnit[7]

        tNo.text = str(Array[0])
        iGin.text = str(Array[1])
        sLvl.text = str(Array[2])
        sEnable.text = str(Array[3])
        m.text = str(Array[4])
        s.text = str(Array[5])
        pan.text = str(Array[6])
        vol.text = str(Array[7])

        return vsUnit

    def _monoUnit(self, Array):
        
        monoUnit = etree.Element("monoUnit")

        monoUnit.append( etree.Element("iGin") )
        monoUnit.append( etree.Element("sLvl") )
        monoUnit.append( etree.Element("sEnable") )
        monoUnit.append( etree.Element("m") )
        monoUnit.append( etree.Element("s") )
        monoUnit.append( etree.Element("pan") )
        monoUnit.append( etree.Element("vol") )

        iGin = monoUnit[0]
        sLvl = monoUnit[1]
        sEnable = monoUnit[2]
        m = monoUnit[3]
        s = monoUnit[4]
        pan = monoUnit[5]
        vol = monoUnit[6]

        iGin.text = str(Array[0])
        sLvl.text = str(Array[1])
        sEnable.text = str(Array[2])
        m.text = str(Array[3])
        s.text = str(Array[4])
        pan.text = str(Array[5])
        vol.text = str(Array[6])
        
        return monoUnit

    def _stUnit(self, Array):
        
        stUnit = etree.Element("stUnit")

        stUnit.append( etree.Element("iGin") )
        stUnit.append( etree.Element("m") )
        stUnit.append( etree.Element("s") )
        stUnit.append( etree.Element("vol") )

        iGin = stUnit[0]
        m = stUnit[1]
        s = stUnit[2]
        vol = stUnit[3]
        
        iGin.text = str(Array[0])
        m.text = str(Array[1])
        s.text = str(Array[2])
        vol.text = str(Array[3])

        return stUnit

    def __init__(self, Array):
    
        mixer = etree.Element("mixer")
        
        mixer.append( self._masterUnit(Array[0]) )
        for _Array in Array[1]:
            mixer.append( self._vsUnit(_Array) )
        mixer.append( self._monoUnit(Array[2]) )
        mixer.append( self._stUnit(Array[3]) )

        self.data = mixer

class masterTrack:

    def _timeSig(self, Array):

        timeSig = etree.Element("timeSig")
        timeSig.append( etree.Element("m") )
        timeSig.append( etree.Element("nu") )
        timeSig.append( etree.Element("de") )

        m = timeSig[0]
        nu = timeSig[1]
        de = timeSig[2]
        
        m.text = str(Array[0])
        nu.text = str(Array[1])
        de.text = str(Array[2])

        return timeSig

    def _tempo(self, Array):

        tempo = etree.Element("tempo")
        
        tempo.append( etree.Element("t") )
        tempo.append( etree.Element("v") )

        t = tempo[0]
        v = tempo[1]

        t.text = str(Array[0])
        v.text = str(Array[1])

        return tempo

    def __init__(self, Array = list()):

        masterTrack = etree.Element("masterTrack")

        masterTrack.append( etree.Element("seqName") )
        masterTrack.append( etree.Element("comment") )
        masterTrack.append( etree.Element("resolution") )
        masterTrack.append( etree.Element("preMeasure") )

        seqName = masterTrack[0]
        comment = masterTrack[1]
        resolution = masterTrack[2]
        preMeasure = masterTrack[3]

        seqName.text = etree.CDATA( Array[0] )
        comment.text = etree.CDATA( Array[1] )
        resolution.text = str(Array[2])
        preMeasure.text = str(Array[3])

        masterTrack.append( self._timeSig(Array[4]) )
        masterTrack.append( self._tempo(Array[5]) )

        self.data = masterTrack

class vsTrack:

    def __sPlug(self, Array):
        
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

    def __pStyle(self, Array):

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

    def __singer(self, Array):

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

    def __cc(self, Array):

        cc = etree.Element("cc")
        cc.append( etree.Element("t") )
        cc.append( etree.Element("v", id=Array[1]) )

        t = cc[0]
        v = cc[1]

        t.text = str(Array[0])
        v.text = str(Array[2])
        
        return cc

    def ____seq(self, Array):

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

    def ___nStyle(self, Array):

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

    def __note(self, Array):

        note = etree.Element("note")

        note.append(etree.Element("t"))
        note.append(etree.Element("dur"))
        note.append(etree.Element("n"))
        note.append(etree.Element("v"))
        note.append(etree.Element("y"))
        note.append(etree.Element("p"))
        note.append( self.___nStyle(Array[6]) )

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
        y.text = etree.CDATA(str(Array[4]))     # visible
        p.text = etree.CDATA(str(Array[5]))     # to engine

        return note

    def _vsPart(self, Array):
        
        vsPart = etree.Element("vsPart") 
        
        vsPart.append( etree.Element("t") )
        vsPart.append( etree.Element("playTime") )
        vsPart.append( etree.Element("name") )
        vsPart.append( etree.Element("comment") )

        vsPart.append( self.__sPlug(Array[4]) )
        vsPart.append( self.__pStyle(Array[5]) )
        vsPart.append( self.__singer(Array[6]) )

        for _Array in Array[7]:
            vsPart.append( self.__cc(_Array) )
            
        for _Array in Array[8]:
            vsPart.append( self.__note(_Array) )

        vsPart.append( etree.Element("plane") )

        t = vsPart[0]
        playTime = vsPart[1]
        name = vsPart[2]
        comment = vsPart[3]
        plane = vsPart[-1]

        t.text = str(Array[0])
        playTime.text = str(Array[1])
        name.text = etree.CDATA(Array[2])
        comment.text = etree.CDATA(Array[3])
        plane.text = str(1)

        return vsPart

    def __init__(self, Array):

        vsTrack = etree.Element("vsTrack") 
        
        vsTrack.append( etree.Element("tNo") )
        vsTrack.append( etree.Element("name") )
        vsTrack.append( etree.Element("comment") )

        for _Array in Array[3]:
            vsTrack.append( self._vsPart(_Array) )

        tNo = vsTrack[0]
        name = vsTrack[1]
        comment = vsTrack[2]

        tNo.text = str(Array[0])
        name.text = etree.CDATA(Array[1])
        comment.text = etree.CDATA(Array[2])
        
        self.data = vsTrack

class monoTrack:

    def __init__(self, Array = ""):

        monoTrack = etree.Element("monoTrack")

        monoTrack.text = str()
        
        self.data = monoTrack

class stTrack:

    def __init__(self, Array = ""):

        stTrack = etree.Element("stTrack")
        stTrack.text = str()
        
        self.data = stTrack

class aux:

    def __init__(self, Array = ""):

        aux = etree.Element("aux")

        aux.append(etree.Element("id"))
        aux.append(etree.Element("content"))

        _id = aux[0]
        content = aux[1]
        
        _id.text = etree.CDATA("AUX_VST_HOST_CHUNK_INFO")
        content.text = etree.CDATA("VlNDSwAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")

        self.data = aux

class list2vsqx:

    def to_file(self, directory):

        s1 = """<?xml version="1.0" encoding="UTF-8" standalone="no"?> """
        s2 = """\n<vsq4 xmlns="http://www.yamaha.co.jp/vocaloid/schema/vsq4/" """
        s3 = """\n      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" """
        s4 = """\n      xsi:schemaLocation="http://www.yamaha.co.jp/vocaloid/schema/vsq4/ vsq4.xsd"> """
        
        s0 = s1 + s2 + s3 + s4

        my_tree = self.vsq4

        data = etree.tostring(my_tree, pretty_print=True).decode('utf-8')

        sfo = s0 + data[6:]

        with open( directory + '.vsqx', 'wb') as f:
            arr = bytes(sfo, 'utf-8')
            f.write(arr)

    def fill_vsq4(self, Array):

        self.vsq4.append(vender(Array[0]).data)
        self.vsq4.append(version(Array[1]).data)
        self.vsq4.append(vVoiceTable(Array[2]).data)
        self.vsq4.append(mixer(Array[3]).data)
        self.vsq4.append(masterTrack(Array[4]).data)
        
        for a in Array[5]:
            self.vsq4.append(vsTrack(a).data)
        
        self.vsq4.append(monoTrack(Array[6]).data)
        self.vsq4.append(stTrack(Array[7]).data)
        self.vsq4.append(aux(Array[8]).data)

    def __init__(self, Array = ""):

        self.vsq4 = etree.Element("vsq4")

        if(len(Array) == 9):
            self.fill_vsq4(Array)
        else:
            print("Fail")
