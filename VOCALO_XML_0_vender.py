from lxml import etree

def vender(Array):
    
    vender = etree.Element("vender")

    vender.text = etree.CDATA(Array)

    return vender