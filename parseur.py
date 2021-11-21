import xml.etree.ElementTree as ET
from lxml import etree
import lxml.etree

##############################PARSEUR##############################
def parse_date():
    tree = ET.parse("./xml/all.xml")
    root_node = tree.getroot()
    #tableau pour stocker les valeurs de TestDate
    tab=[]
    return tab, root_node

def parse_totalram():
    tree2 = ET.parse("./xml/all.xml")
    root_node2 = tree2.getroot()
    #tableau pour stocker les valeurs de TotalRam
    tab_totalram=[]
    return tab_totalram, root_node2

def parse_UsedRam():
    tree3 = ET.parse("./xml/all.xml")
    root_node3 = tree3.getroot()
    #tableau pour stocker les valeurs de TotalRam
    tab_UsedRam=[]
    return tab_UsedRam, root_node3

def parse_SwapUsage():
    tree4 = ET.parse("./xml/all.xml")
    root_node4 = tree4.getroot()
    #tableau pour stocker les valeurs de SwapUsage
    tab_SwapUsage=[]
    return tab_SwapUsage, root_node4

def parse_Server():
    tree5 = ET.parse("./xml/all.xml")
    root_node5 = tree5.getroot()
    #tableau pour stocker les valeurs de Server
    tab_Server=[]
    return tab_Server, root_node5

#########################Client1 RAM#########################
def parse_date_client1_ram():
    tree_client1_date_ram = ET.parse("./xml/client1_ram.xml")
    root_node_client1_date_ram = tree_client1_date_ram.getroot()
    #tableau pour stocker les valeurs de TestDate
    tab_client1_date_ram=[]
    return tab_client1_date_ram, root_node_client1_date_ram

def parse_totalram_client1():
    tree_client1_totalram = ET.parse("./xml/client1_ram.xml")
    root_node2_client1_totalram = tree_client1_totalram.getroot()
    #tableau pour stocker les valeurs de TotalRam
    tab_client1_totalram=[]
    return tab_client1_totalram, root_node2_client1_totalram

def parse_UsedRam_client1():
    tree_client1_UsedRam = ET.parse("./xml/client1_ram.xml")
    root_node2_client1_UsedRam = tree_client1_UsedRam.getroot()
    #tableau pour stocker les valeurs de TotalRam
    tab_client1_UsedRam=[]
    return tab_client1_UsedRam, root_node2_client1_UsedRam
#########################Client1 SWAP#########################

def parse_date_client1_swap():
    tree_client1_date_swap = ET.parse("./xml/client1_swap.xml")
    root_node_client1_date_swap = tree_client1_date_swap.getroot()
    #tableau pour stocker les valeurs de TestDate
    tab_client1_date_swap=[]
    return tab_client1_date_swap, root_node_client1_date_swap

def parse_SwapUsage_client1():
    tree_client1_SwapUsage = ET.parse("./xml/client1_swap.xml")
    root_node_client1_SwapUsage = tree_client1_SwapUsage.getroot()
    tab_client1_SwapUsage=[]
    return tab_client1_SwapUsage, root_node_client1_SwapUsage

#########################Client2 RAM#########################

def parse_date_client2_ram():
    tree_client2_date_ram = ET.parse("./xml/client2_ram.xml")
    root_node_client2_date_ram = tree_client2_date_ram.getroot()
    #tableau pour stocker les valeurs de TestDate
    tab_client2_date_ram=[]
    return tab_client2_date_ram, root_node_client2_date_ram

def parse_totalram_client2():
    tree_client2_totalram = ET.parse("./xml/client2_ram.xml")
    root_node2_client2_totalram = tree_client2_totalram.getroot()
    tab_client2_totalram=[]
    return tab_client2_totalram, root_node2_client2_totalram

def parse_UsedRam_client2():
    tree_client2_UsedRam = ET.parse("./xml/client2_ram.xml")
    root_node2_client2_UsedRam = tree_client2_UsedRam.getroot()
    tab_client2_UsedRam=[]
    return tab_client2_UsedRam, root_node2_client2_UsedRam

#########################Client2 SWAP#########################
def parse_date_client2_swap():
    tree_client2_date_swap = ET.parse("./xml/client2_swap.xml")
    root_node_client2_date_swap = tree_client2_date_swap.getroot()
    #tableau pour stocker les valeurs de TestDate
    tab_client2_date_swap=[]
    return tab_client2_date_swap, root_node_client2_date_swap
    
def parse_SwapUsage_client2():
    tree_client2_SwapUsage = ET.parse("./xml/client2_swap.xml")
    root_node_client2_SwapUsage = tree_client2_SwapUsage.getroot()
    tab_client2_SwapUsage=[]
    return tab_client2_SwapUsage, root_node_client2_SwapUsage