from lxml import etree

def _timeSig(Array):

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

def _tempo(Array):

    tempo = etree.Element("tempo")
    
    tempo.append( etree.Element("t") )
    tempo.append( etree.Element("v") )

    t = tempo[0]
    v = tempo[1]

    t.text = str(Array[0])
    v.text = str(Array[1])

    return tempo

def masterTrack(Array):

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

    masterTrack.append( _timeSig(Array[4]) )
    masterTrack.append( _tempo(Array[5]) )

    return masterTrack

#root = masterTrack()

#print(etree.tostring(root, pretty_print=False))