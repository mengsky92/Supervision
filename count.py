import lxml.etree
#############################################################
###Compter le nombre de balise <ramUsage>, <SwapSize> dans le fichier xml
def count():
    doc = lxml.etree.parse('./xml/all.xml')
    countlxml_ramUsage = int(doc.xpath('count(//ramUsage)'))
    countlxml_TotalRam = int(doc.xpath('count(//TotalRam)'))
    countlxml_Server_ram = int(doc.xpath('count(//generic/ramUsage/Server)'))
    return countlxml_TotalRam
    return countlxml_Server_ram
"""       
    i=0
    elem1=[]
    tree = ET.parse("./xml/all.xml")
    root_node6 = tree.getroot()
    elem2 = root_node6.findall("generic/ramUsage/Server")
    print('elem2',elem2)
    for x in elem2:
        # elem1 contient une liste avec tous les clients dans /ramUsage/Server
            elem1.append(x.text)
            print('elem1',elem1)
            #elem1=elem1_modify.txt
    #on enlève le premier element de la liste
    elem1.pop(0)
    print('elem1 2',elem1)
    #On trie elem1 pour ne garder qu'une seule fois un nom de serveur
    unique_client_ram=numpy.unique(elem1)
    print('unique_client',unique_client_ram)


    return unique_client_ram
"""
def count2():
    doc = lxml.etree.parse('./xml/all.xml')
    countlxml_SwapUsage = int(doc.xpath('count(//SwapUsage)'))
    countlxml_SwapSize = int(doc.xpath('count(//SwapSize)'))
    countlxml_Server_swap = int(doc.xpath('count(//Server)'))
    return countlxml_SwapUsage
    return countlxml_SwapSize
    return countlxml_Server_swap


def count_client1_ram():
    doc_client1_ram = lxml.etree.parse("./xml/client1_ram.xml")
    countlxml_ramUsage_client1 = int(doc_client1_ram.xpath('count(//ramUsage)'))
    countlxml_RamUsed_client1 = int(doc_client1_ram.xpath('count(//RamUsed)'))
    countlxml_TotalRam_client1 = int(doc_client1_ram.xpath('count(//TotalRam)'))
    return countlxml_ramUsage_client1
    return countlxml_RamUsed_client1
    return countlxml_TotalRam_client1
    
def count_client1_swap():
    doc_client1_swap = lxml.etree.parse("./xml/client1_swap.xml")
    countlxml_SwapUsage_client1 = int(doc_client1_swap.xpath('count(//SwapUsage)'))
    countlxml_SwapSize_client1 = int(doc_client1_swap.xpath('count(//SwapSize)'))
    return countlxml_SwapUsage_client1
    return countlxml_SwapSize_client1

def count_client2_ram():
    doc_client2_ram = lxml.etree.parse("./xml/client2_ram.xml")
    countlxml_ramUsage_client2 = int(doc_client2_ram.xpath('count(//ramUsage)'))
    countlxml_RamUsed_client2 = int(doc_client2_ram.xpath('count(//RamUsed)'))
    countlxml_TotalRam_client2 = int(doc_client2_ram.xpath('count(//TotalRam)'))
    return countlxml_ramUsage_client2
    return countlxml_RamUsed_client2
    return countlxml_TotalRam_client2
    
def count_client2_swap():
    doc_client2_swap = lxml.etree.parse("./xml/client2_swap.xml")
    countlxml_SwapUsage_client2 = int(doc_client2_swap.xpath('count(//SwapUsage)'))
    countlxml_SwapSize_client2 = int(doc_client2_swap.xpath('count(//SwapSize)'))
    return countlxml_SwapUsage_client2
    return countlxml_SwapSize_client2