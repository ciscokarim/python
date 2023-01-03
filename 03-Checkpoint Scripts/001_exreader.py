import string
from re import search
import re
import copy
from collections import OrderedDict
import xlwings as xw
import time
import sys

#-------------------------------------------------------------#

wb=xw.Book('utmform.xlsm')
ws=wb.sheets['UTM Form']

#-------------------------------------------------------------#

# frow=int(input("Enter the firt row :"))
# lrow=int(input("Enter the last row :"))
# ppkg_uinput=(input("Enter the name of the policy pakage (case-sensitive) :"))
# rbasefrow=int(input(f"Enter the row starting point in #{ppkg_uinput}# rulebase :"))

frow=263
lrow=266
ppkg_uinput="utm-var"
rbasefrow=5

#-------------------------------------------------------------#
#cols=["a","b"]
cols=["a","b","c","d"]

#-------------------------------------------------------------#
ppkg=ppkg_uinput+"_In_Line Security"
# print(ppkg)
iplist =[]
netlist=[]
portlist=[]
actionlist=[]
actionfnl=[]
celldict={}

#-------------------------------------------------------------#

def depth_of_list(l):
    if isinstance(l, list):
        return 1 + max(depth_of_list(item) for item in l)
    else:
        return 0

def progress_bar_printer():

    toolbar_width = 20
    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    #loop it.
    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()
    #print it
    sys.stdout.write("]\n") # this ends the #progress bar

def listprinter(x):
    for items in x:
        print(items)

def dictprinter(x):
    for items in x:
        print(f"{items}:{x[items]}")


def flatten(lst):
    for el in lst:
        if isinstance(el, list):  # N.B. this only works for lists, not general
                                  # collections e.g. sets, tuples, dicts, etc...
            # recurse
            yield from flatten(el)
        else:
            # generate
            yield el
#-------------------------------------------------------------#

with open('thescript.txt', 'w') as script:
        script.write(f"===========================================================\n")
        script.write(f"           Script to be pasted in mgmt-cli==\n")
        script.write(f"===========================================================\n")

#-------------------------------------------------------------#

print("=================================================================================")
print("Extracting the IP Addresses, Networks and Ports && Append them to a list ")
print("=================================================================================")

for col in (cols):
    for row in range (frow,lrow+1):
     cell=str(col)+str(row)
     cvalue=ws.range(cell).value
     itemlist=[]
     #print(f"Cell number is ###{cell}###")
     #print(f"Cell number is ###{col}{row}###")
     
     if(cvalue != None and cvalue.find("any") == -1):
        if re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",cvalue):
            ipwm=re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\/..',cvalue)
            netlist.append(ipwm)
            itemlist.append(ipwm)
        if re.search("(?i)tcp.\d+|udp.\d+|ip.\d+|icmp.\d+|tcp\d+|udp\d+|ip\d+|icmp\d+",cvalue):
            portwm=re.findall(r'(?i)tcp.\d+|udp.\d+|ip.\d+|icmp.\d+|tcp\d+|udp\d+|ip\d+|icmp\d+',cvalue)
            portlist.append(portwm)
            itemlist.append(portwm)
        if re.search("(?i)accept|deny",cvalue):
            #actionwm=[]
            actionwm=re.findall(r'(?i)accept|deny',cvalue)
            #print(actionwm[0])
            # print(type(actionwm))
            actionlist.append(actionwm)
            itemlist.append(actionwm)    

     if(cvalue != None and cvalue.find("any") == -1 and cvalue.find("/") == -1 ):
        if re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",cvalue):
            ip=re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b',cvalue)
            iplist.append(ip)
            itemlist.append(ip)

     flat_itemlist=list(flatten(itemlist))
    #  flat2_itemlist=list(flatten(flat1_itemlist))
    #  flat3_itemlist=list(flatten(flat2_itemlist))
     celldict[cell]=[]
     for eachitem in flat_itemlist:
        celldict[cell].append(eachitem)

#print(celldict)

# for items in celldict:
#     print(f"{items}={celldict[items]}")  

# print(celldict)
# progress_bar_printer()

print("==========================================================================")
print("Cleaning the lists ")
print("==========================================================================")

#create a function for below
iplist = list(filter(None, iplist))
iplist = list(filter(bool, iplist))
iplist = list(filter(len, iplist))

netlist = list(filter(None, netlist))
netlist = list(filter(bool, netlist))
netlist = list(filter(len, netlist))

portlist = list(filter(None, portlist))
portlist = list(filter(bool, portlist))
portlist = list(filter(len, portlist))

itemlist = list(filter(None, itemlist))
itemlist = list(filter(bool, itemlist))
itemlist = list(filter(len, itemlist))

#progress_bar_printer()

print("==========================================================================")
print("Flattening the lists 2D to 1D ")
print("==========================================================================")

#create a function for below.
iplist_flat = []
for items in iplist:
  for values in items:
    iplist_flat.append(values)

netlist_flat = []
for items in netlist:
  for values in items:
    netlist_flat.append(values)

portlist_flat = []
for items in portlist:
  for values in items:
    portlist_flat.append(values)

# #progress_bar_printer()

print("==========================================================================")
print("Removing Duplicates ")
print("==========================================================================")

# print("----------------------------------- IP Addresses ---------------------------------------")
iplist_nondup=list(dict.fromkeys(iplist_flat))

# print ("printing flat list of ips without dups")
# for ips in iplist_nondup:
#     print(ips)

# print("----------------------------------- Networks ---------------------------------------")
netlist_nondup=list(dict.fromkeys(netlist_flat))

# print ("printing flat list of networks without dups")
# for nets in netlist_nondup:
#     print(nets)

# print("----------------------------------- Ports ---------------------------------------")
portlist_nondup=list(dict.fromkeys(portlist_flat))

# print ("printing flat list of ports without dups")
# for ports in portlist_nondup:
#     print(ports)

# print("----------------------------------- Hosts -- ---------------------------------------")

#progress_bar_printer()

print("==========================================================================")
print("Loading objects file ")
print("==========================================================================")

with open ("07-objects_on_domain10_14-11-2022_14-22.csv") as fileholder01:
    objectsfile_string=fileholder01.read() # this converts the file into a string
with open ("07-objects_on_domain10_14-11-2022_14-22.csv") as fileholder01:
    objectsfile_list=fileholder01.readlines() # this converts the file into a string

hoststbcr=[] # hosts to be created
hostsaddcmds=[] #hosts add commands batch

print("==========================================================================")
print("Comparing the requested host objects against the existing objects ")
print("Create list of objects to be created and associated CLI script ")
print("==========================================================================")

print("iplist_nondup is")
listprinter(iplist_nondup)
print("dictionary is ..")
print(celldict)
#dictprinter(celldict)
print(f"each matching item is")
for ips in iplist_nondup:
    #print(f"printing IPs =  {ips}")
    ips_with_commas=","+ips+"," #improve this section with a list of prefixes and loop through them to append.
    h_ip_exists=""
    g_ip_exists=""
    hostname="h-"+ips
    hostaddcmd='add host name '+hostname+" ip-address "+ips+' color "forest green"'    
   
    for eachlist in celldict.values():
        #print(f"the list is {eachlist}")
        #print(f"ips are {ips}")
        #print(f"items in celldcit are {eachitem}")
        #print(f"depth of the list is {depth_of_list(eachlist)}")
        for eachitem in eachlist:
            if ips == eachitem:
                print(f"ip is {ips} and item is {eachitem}")
                #print(ips)
                #ipinlistform="['"+ips+"']"
                # ipinlistform=ips
                # print(ipinlistform)
                celldictkey=list(celldict.keys())[list(celldict.values()).index([ips])]
                print(celldictkey)
                # print (f"key is {celldictkey} and list item is {eachitem} and list is {eachlist}")
        # if ips == str(celldict[eachitem]):
        #     print(ips)
            #print(list(celldict.keys())[list(celldict.values()).index([ips])])
    
    if ips_with_commas not in objectsfile_string:
        #print(f"{ips} , requested host object doesnt exist #############################")
        hoststbcr.append(hostname)
        hostsaddcmds.append(hostaddcmd)
    
    if (("\ng_h-"+ips+",") in objectsfile_string) or (("\ng-h-"+ips+",") in objectsfile_string or (("\nG_H-"+ips+",") in objectsfile_string) or (("\nG-H-"+ips+",") in objectsfile_string) or (("\nG-h-"+ips+",") in objectsfile_string) or (("\nG_h-"+ips+",") in objectsfile_string)):
        # print(f"{ips} , requested host object exists already >>>>>>>>>>>>>>>>>>>>>g_h/g-h/G_H/G-H.X.X.X.X")
        g_ip_exists="true"       

    if (("\nh-"+ips+",") in objectsfile_string) or (("\nh_"+ips+",") in objectsfile_string) or (("\nH-"+ips+",") in objectsfile_string) or (("\nH_"+ips+",") in objectsfile_string):
        # print(f"{ips} , requested host object exists already >>>>>>>>>>>>>>>>>>>>>H-X.X.X.X")
        h_ip_exists="true"

    if (g_ip_exists=="true" and h_ip_exists!="true"):
        # print(f"{ips} , requested IP has global version but needs a local version ****")
        hoststbcr.append(hostname)
        hostsaddcmds.append(hostaddcmd)
    
print("==========================================================================")
print("Print the CLI to add hosts && add them to a text file ")
print("==========================================================================")

#listprinter(hostsaddcmds)

with open('thescript.txt', 'w') as script:
    script.write(f"\n### ---------------------------  ###")
    script.write(f"\n### CLI to add new host objects  ###")
    script.write(f"\n### ---------------------------  ###\n\n")
    for each in hostsaddcmds:
        script.write(f'{each}\n')


print("==========================================================================")
print("Loading the list of nets ")
print("==========================================================================")

# non_existing_ips=[]

# with open ("02_networks on domain-10_13-10-2022_14-57.txt") as fileholder01:
#     netsfile_string=fileholder01.read() # this converts the file into a string
# with open ("02_networks on domain-10_13-10-2022_14-57.txt") as fileholder01:
#     netsfile_list=fileholder01.readlines() # this converts the file into a string

# print(netsfile_string,type(netsfile_string))
# print(netsfile_list,type(netsfile_list))



print("==========================================================================")
print("Comparing the requested network objects against the existing objects ")
print("Create list of objects to be created and associated CLI script ")
print("==========================================================================")

netstbcr=[]  # nets to be created
netsaddcmds=[] #nets add commands batch
maskdict={
            "8":"255.0.0.0",
            "9":"255.128.0.0",
            "10":"255.192.0.0",
            "11":"255.224.0.0",
            "12":"255.240.0.0",
            "13":"255.248.0.0",
            "14":"255.252.0.0",
            "15":"255.254.0.0",
            "16":"255.255.0.0",
            "17":"255.255.128.0",
            "18":"255.255.192.0",
            "19":"255.255.224.0",
            "20":"255.255.240.0",
            "21":"255.255.248.0",
            "22":"255.255.252.0",
            "23":"255.255.254.0",
            "24":"255.255.255.0",
            "25":"255.255.255.128",
            "26":"255.255.255.192",
            "27":"255.255.255.224",
            "28":"255.255.255.240",
            "29":"255.255.255.248",
            "30":"255.255.255.252",
            "31":"255.255.255.254",
            "32":"255.255.255.255"
}

for net in netlist_nondup:
    broken_net=net.split("/")
    maskvalue=str(maskdict[broken_net[1]])
    #print(f"current net is {net} and network is {broken_net[0]} and mask is {maskvalue}")
    comma_network_comma_mask_comma=","+broken_net[0]+","+maskvalue+","
    #print(f"\n\nformatted network to search for doesnot exist is {comma_network_comma_mask_comma}")
    #print(f"formatted network to search for n-x.x.x. exists is n-"+broken_net[0]+"-"+broken_net[1])
    net_exists=""
    g_net_exists=""
    n_net_exists=""
    netname="n-"+broken_net[0]+"-"+broken_net[1]
    #print(f"formatted netname is {netname}")
    #print("\nn-"+broken_net[0]+"-"+broken_net[1])
    netaddcmd="add network name "+netname+" subnet "+broken_net[0]+" mask-length "+broken_net[1]+' color "forest green"'    
    #print(f"COMMAND:>  {netaddcmd}")

    if comma_network_comma_mask_comma not in objectsfile_string:
        #print(f"{net} , requested network object doesnt exist")
        netstbcr.append(netname)
        netsaddcmds.append(netaddcmd)
        #print(netsaddcmds)
        #print("test")
    if (("\ng_n-"+broken_net[0]+"-"+broken_net[1])) in objectsfile_string or ( ("\ng-n-"+broken_net[0]+"-"+broken_net[1])in objectsfile_string or (("\nG_N-"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string) or (("\nG-N-"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string) or ("\ng_n_"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string) or (("\ng-n_"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string or (("\nG_N_"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string) or (("\nG-N_"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string) or (("\nG-n-"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string) or (("\nG_n-"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string)):
        # print(f"{net} , requested network object exists already >>>>>>>>>>>>>>>>>>>>>g_h/g-h/G_H/G-N.X.X.X.X")
        g_net_exists="true"

    if (("\nn-"+broken_net[0]+"-"+broken_net[1])) in objectsfile_string or ( ("\nN-"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string or (("\nn_"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string) or (("\nN_"+broken_net[0]+"-"+broken_net[1]) in objectsfile_string)):
        # print(f"{net} , requested network object exists already >>>>>>>>>>>>>>>>>>>>>N-X.X.X.X")
        n_net_exists="true"

    if (g_net_exists=="true" and n_net_exists!="true"):
        # print(f"{net} , requested net has global version but needs a local version ****")
        netstbcr.append(netname)
        netsaddcmds.append(netaddcmd)

    if (g_net_exists!="true" and n_net_exists!="true" and comma_network_comma_mask_comma in objectsfile_string ):
        # print(f"{net} , requested net needs a local version ****")
        netstbcr.append(netname)
        netsaddcmds.append(netaddcmd)

print("==========================================================================")
print("Print the CLI to add nets && add them to a text file ")
print("==========================================================================")

# listprinter(netstbcr)

with open('thescript.txt', 'a+') as script:
    script.write(f"\n### ------------------------------  ###")
    script.write(f"\n### CLI to add new network objects  ###")
    script.write(f"\n### ------------------------------  ###\n\n")
    for each in netsaddcmds:
        script.write(f'{each}\n')


#======================================================================================================================#


print("==========================================================================")
print("Loading the list of ports ")
print("==========================================================================")

# non_existing_ips=[]

# with open ("04_services on domain-10_13-10-2022_14-57.txt") as fileholder01:
#     objectsfile_string=fileholder01.read() # this converts the file into a string
# with open ("04_services on domain-10_13-10-2022_14-57.txt") as fileholder01:
#     objectsfile_list=fileholder01.readlines() # this converts the file into a string

# print(objectsfile_string,type(objectsfile_string))
# print(objectsfile_list,type(objectsfile_list))

print("==========================================================================")
print("Comparing the requested service objects against the existing objects ")
print("Create list of objects to be created and associated CLI script ")
print("==========================================================================")

portstbcr=[]  # ports to be created
portsaddcmds=[] #ports add commands batch
gport_exists=""
port_exists=""
comma_port_comma=""
gport_exists=""
port_exists=""
gportctr=0
portctr=0
linectr=0

for port in portlist_nondup:
    port_prot=re.search("^[a-zA-Z]+", port).group()
    port_num=re.search("\d+", port).group()
    service=port_prot.upper()+port_num
    #print(f"port is <{port}>, protocol is {port_prot},port number is {port_num}, service is {service}") 
#     broken_port=port.split("/")
#     maskvalue=str(maskdict[broken_port[1]])
#     #print(f"current port is {port} and portwork is {broken_port[0]} and mask is {maskvalue}")
    comma_port_comma=","+port_num+","
    #print(f"formatted service to search is {comma_port_comma}")
#     #print(f"formatted portwork to search is {comma_portwork_comma_mask_comma}")

#     portname="n-"+broken_port[0]+"-"+broken_port[1]
#     #print(f"formatted portname is {portname}")
    # if port_prot="tcp"
    portaddcmd="add service-"+port_prot.lower()+" name "+port_prot.upper()+port_num+" port "+port_num+' color "forest green"'    
    #print(f"COMMAND:>  {portaddcmd}")


#print(len(objectsfile_list))
# listprinter(objectsfile_list)
    if comma_port_comma not in objectsfile_string:
        #print(f"{port} , requested port object doesnt exist ##############################")
        portstbcr.append(service)
        portsaddcmds.append(portaddcmd)
        #print(portsaddcmds)
    
    linectr=0
    gportctr=0
    nportctr=0
    
    for lines in objectsfile_list:
        linectr+=1
        #sprint(linectr)
        # print(comma_port_comma)
        if (comma_port_comma in lines):
            #print(lines)
            if(re.search("(?i)^g.*", lines)):
            #     print(lines)
            # # if(re.search("^g.*", lines)):
            #     print(lines)
            #     #print(f"g_port {comma_port_comma} exists in following line \n{lines}")
                gportctr+=1
                gport_exists="yes"
                #print(f"{port} , requested port object exists as  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG g{gport_exists}")
            #     # print("gport exists")
            else:
                #print(f"port {comma_port_comma} exists in following line \n{lines}")
                #print(f"{port} , requested port object exists as  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> n{port_exists}")
                nportctr+=1
                port_exists="yes"
                # print("port exists")
            
            #print (f"values of g and n {gport_exists},{port_exists}")
            

            #if(gport_exists=="yes" and port_exists!="yes"):
            #print(f"port count is g{gportctr} and n{nportctr}")
        #print(linectr)
        
        if(linectr==(len(objectsfile_list))):

            #print (f"for {service} the ncounter={nportctr} and gcounter={gportctr}")
            if(gportctr!=0 and nportctr==0):
            #     print("no")
                portstbcr.append(service)
                portsaddcmds.append(portaddcmd)

# print("\n")
# print (f"{linectr} = linecounter")
# print (f"{len(objectsfile_list)} = length of list")
# print("\n**** port objects to be created are as follows***")
# print("=================================================")
# listprinter(portstbcr)
# print("\ncommands to be created are as follows")
# print("=================================================")
# listprinter(portsaddcmds)


print("==========================================================================")
print("Print the CLI to add hosts && add them to a text file ")
print("==========================================================================")

# listprinter(portstbcr)

with open('thescript.txt', 'a+') as script:
    script.write(f"\n### ------------------------------  ###")
    script.write(f"\n### CLI to add new service objects  ###")
    script.write(f"\n### ------------------------------  ###\n\n")
    for each in portsaddcmds:
        script.write(f'{each}\n')


