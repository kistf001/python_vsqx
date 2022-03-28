from lxml import etree

def _masterUnit(Array):
    
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

def _vsUnit(Array):
    
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

def _monoUnit(Array):
    
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

def _stUnit(Array):
    
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

def mixer(Array):
    
    mixer = etree.Element("mixer")
    
    mixer.append( _masterUnit(Array[0]) )
    for _Array in Array[1]:
        mixer.append( _vsUnit(_Array) )
    mixer.append( _monoUnit(Array[2]) )
    mixer.append( _stUnit(Array[3]) )

    return mixer

#root = mixer()

#print(etree.tostring(root, pretty_print=False))

