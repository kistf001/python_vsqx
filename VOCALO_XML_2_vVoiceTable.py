from lxml import etree

def __vPrm(Array):
    
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

    bre.text = str(Array[0])
    bri.text = str(Array[1])
    cle.text = etree.CDATA( Array[2] )
    gen.text = etree.CDATA( Array[3] )

    return vPrm
    
def _vVoice(Array):
    
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

    vVoice.append(__vPrm( Array[4] ))

    return vVoice

def vVoiceTable(Array):

    vVoiceTable = etree.Element("vVoiceTable")

    for _Array in Array:
        vVoiceTable.append( _vVoice(_Array) )

    return vVoiceTable
