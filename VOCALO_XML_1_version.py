from lxml import etree

def version():
    
    version = etree.Element("version")

    version.text = etree.CDATA("4.0.0.3")

    return version