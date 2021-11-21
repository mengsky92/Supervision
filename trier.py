import xml.etree.ElementTree as ET
import numpy

def trier_ram():
    i=0
    elem1=[]
    tree = ET.parse("xml.xml")
    root_node6 = tree.getroot()
    #Server=create_table()
    elem2 = root_node6.findall("generic/ramUsage/Server")
    for x in elem2:
        # elem1 contient une liste avec tous les clients dans /ramUsage/Server
            elem1.append(x.text)
            print('elem1',elem1)
            #elem1=elem1_modify.txt
    #on enlève le premier element de la liste
    elem1.pop(0)
    #On trie elem1 pour ne garder qu'une seule fois un nom de serveur
    unique_client_ram=numpy.unique(elem1)
    print('unique_client_ram', unique_client_ram)
    #create_table_trier_ram()
    #general_trier_ram()
    return unique_client_ram

"""
def trier_swap():
    i=0
    elem1=[]
    tree = ET.parse("./xml/client1_swap.xml")
    root_node6 = tree.getroot()
    #Server=create_table()
    elem2 = root_node6.findall("generic/swapUsage/Server")
    for x in elem2:
        # elem1 contient une liste avec tous les clients dans /ramUsage/Server
            elem1.append(x.text)
            print('elem1',elem1)
            #elem1=elem1_modify.txt
    #on enlève le premier element de la liste
    elem1.pop(0)
    #On trie elem1 pour ne garder qu'une seule fois un nom de serveur
    unique_client_ram=numpy.unique(elem1)
    print('unique_client_ram', unique_client_ram)
    #create_table_trier_ram()
    #general_trier_ram()
    return unique_client_ram
    """