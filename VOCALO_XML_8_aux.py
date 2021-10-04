from lxml import etree

def aux():

    aux = etree.Element("aux")

    aux.append(etree.Element("id"))
    aux.append(etree.Element("content"))

    _id = aux[0]
    content = aux[1]
    
    _id.text = etree.CDATA("AUX_VST_HOST_CHUNK_INFO")
    content = etree.CDATA("VlNDSwAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")

    return aux

    
    
#root = aux()

#print(etree.tostring(root, pretty_print=False))