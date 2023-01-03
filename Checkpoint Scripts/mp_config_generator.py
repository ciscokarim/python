import string
from re import search
import re
import copy
from collections import OrderedDict
import xlwings as xw
import time
import sys
import os
import time


os.system("cls")


#==========================================================================================================================#
#Variables
loi=[] #list of interfaces
lobpi=[] #list of bootp interfaces
lorelay=[] #list of bootp relay IPs.
intns={

    "eth2.5":{"state":"off","name":"Network Mgmt - 5"},
    "eth2.100":{"state":"off","name":"Business - 100"},
    "eth2.105":{"state":"off","name":"WiFi-Infrastructure - 105"},
    "eth2.106":{"state":"off","name":"3M-Secure - 106"},
    "eth2.120":{"state":"off","name":"Process - 120()"},
    "eth2.121":{"state":"off","name":"Process1 - 121()"},
    "eth2.122":{"state":"off","name":"Process2 - 122()"},
    "eth2.123":{"state":"off","name":"Process3 - 123()"},
    "eth2.124":{"state":"off","name":"Process4 - 124()"},
    "eth2.125":{"state":"off","name":"Process5 - 125()"},
    "eth2.126":{"state":"off","name":"Process6 - 126()"},
    "eth2.127":{"state":"off","name":"Process7 - 127()"},
    "eth2.128":{"state":"off","name":"Process8 - 128()"},
    "eth2.129":{"state":"off","name":"Process9 - 129()"},
    "eth2.147":{"state":"off","name":"Cameras - 147"},
    "eth2.148":{"state":"off","name":"SecurityDevice - 148"},
    "eth2.201":{"state":"off","name":"VoIP - 201"},
    "eth2.282":{"state":"off","name":"3M-Visitor - 282"},
    "eth2.283":{"state":"off","name":"3M-DC - 283"},
    "eth2.284":{"state":"off","name":"3M-SecureGuest - 284"},
    "eth2.285":{"state":"off","name":"3M-BAS - 285"},
    "eth2.286":{"state":"off","name":"3M-Remediation - 286"},
    "eth2.287":{"state":"off","name":"3M-PCBuild - 287"}
}

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

domdata={

    "10":{"account_id":"6217907","name":"dms_site10.mmm.com","mgmt_svr_address":"169.12.132.166"},
    "11":{"account_id":"6277501","name":"dms_site11.mmm.com","mgmt_svr_address":"169.12.17.111"},
    "12":{"account_id":"6454177","name":"not_available","mgmt_svr_address":"169.12.17.112"},
    "perimeter":{"account_id":"5970594","name":"dms_perimeter.mmm.com","mgmt_svr_address":"169.12.132.154"},
    "post_prod":{"account_id":"6617423","name":"3M Post-Production Firewalls","mgmt_svr_address":"169.12.132.154"}
}

# ================================================================
# ####
# DMS_Site10 (Account ID: 6217907)
# Name:    dms_site10.mmm.com
# Addresses:  169.12.132.166
#           169.12.17.102 ***
# ####
# ================================================================
# ####
# > DMS_Site11 (Account ID: 6277501)
# Name:    dms_site11.mmm.com
# Address:  169.12.17.111
# ####
# ================================================================
# ####
# > DMS_Site12 (Account ID: 6454177)
# Name:    Not available
# Address:  169.12.17.112
# ####
# ================================================================
# ####
# > DMS_Perimeter (Account ID: 5970594)
# Name:    dms_perimeter.mmm.com
# Addresses:  169.12.132.154
#           169.12.17.175 ***
# ####
# ================================================================
# ####
# Account Name:    3M Post-Production Firewalls
# Account ID:    6617423
# ####
# ================================================================

datadict={}
datadict["b2-model"]="n/a"
intdict={}
timestring=time.strftime("%d%m%Y-%H%M%S")

#==========================================================================================================================#
#load the excel file and then load the correct tab of the file.
cwd=os.getcwd()
# print(cwd)
for file in os.listdir(cwd):
    # if file.endswith(".cfg") or file.endswith(".txt"):
    if "core" in file:
        core_config=file
    if "utm"  in file:
        utm_config=file
    if "sentry"  in file:
        fw_sentry=file        
        
wb=xw.Book('mp_cfg_gen_template.xlsx')
ws=wb.sheets['Configurations']

print("==========================================================================")
print("Loading UTM Configuration File (UTM-A)")
print("==========================================================================")

with open (utm_config) as fileholder01:
    utm_config_string=fileholder01.read() # this converts the file into a string
with open (utm_config) as fileholder02:
    utm_config_list_dirty=fileholder02.readlines() # this converts the file into a string

#strip all the \n from the end of each line in the list.
utm_config_list= [lines.strip() for lines in utm_config_list_dirty]


#==========================================================================================================================#
#loading the FW Sentry UTM Database file as string and as a list
print("==========================================================================")
print("Loading UTM Configuration File (UTM-A)")
print("==========================================================================")

with open (fw_sentry) as fwsentryfileholder01:
    fwsentryfw_string=fwsentryfileholder01.read() # this converts the file into a string
with open (fw_sentry) as fwsentryfileholder02:
    fwsentryfw_list_dirty=fwsentryfileholder02.readlines() # this converts the file into a string

#strip all the \n from the end of each line in the list.
fwsentryfw_list= [lines.strip() for lines in fwsentryfw_list_dirty]


#==========================================================================================================================#

print("==========================================================================")
print("Ensure Template has no values pre-configured")
print("==========================================================================")

ws['b2'].value = ""
ws['b30'].value = ""
ws['b31'].value = ""
ws['b5'].value = ""
ws['c5'].value = ""
ws['c2'].value = ""
ws['b34'].value = ""
ws['c34'].value = ""
ws['b14'].value = ""
ws['b15'].value = ""
ws['b16'].value = ""
ws['b39'].value = ""
ws['c39'].value = ""
ws['d39'].value = ""
ws['e39'].value = ""
ws['a53:g121'].value = ""

print("==========================================================================")
print("filling DataDict with none Values")
print("==========================================================================")


datadict["b2-model"]="unknown"
datadict["b30-domain_account_id"]="unknown"
datadict["b31-mgt_server_address"]="unknown"
datadict["b5-hostname_a"]="unknown"
datadict["c5-hostname_b"]="unknown"
datadict["c2_location"]="unknown"
datadict["b34-primary_snmp_loc_str"]="unknown"
datadict["c34-secondary_snmp_loc_str"]="unknown"
datadict["b14-routerip"]="unknown"
datadict["b15-routerip"]="unknown"
datadict["b16-routerip"]="unknown"

# datadict=dict.fromkeys(datadict,"none") #set all values of a dict to a value of choice

print("==========================================================================")
print("search for items in files")
print("==========================================================================")

counter=0
c2_location="unknown"

for eachline in utm_config_list:



    if (re.search(r"set.*snmp.*loc",eachline)):
        print(f"snmp location >>> {eachline}")               
        c2value1=input("Enter the standardized snmp location string e.g. <utm-ukBRI-A Bridgend, UK>:")
        b34value1=c2value1
        c34value1=b34value1.replace("-A","-B")

        # c2value2=b5value1.strip()
        c2value2=c2value1.split(' ')[1]+" "+c2value1.split(' ')[2]
        # print(f"value of c2_location is {c2value2}")
        c2_location=c2value2
        datadict["c2_location"]=c2_location
        datadict["b34-primary_snmp_loc_str"]=b34value1
        datadict["c34-secondary_snmp_loc_str"]=c34value1


    # if (re.search(r"set.*snmp.*loc",eachline)):
    #     print(f"snmp location found in,# {eachline}#")               
    #     c2value1=eachline.split('"')[1]
    #     c2value2=c2value1.split(' ')[1]+" "+c2value1.split(' ')[2]
    #     b34value1=c2value1
    #     c34value1=b34value1.replace("-A","-B")

    #     # c2value2=b5value1.strip()
    #     c2_location=c2value2
    #     # print(f"value of c2_location is {c2value2}")
    #     datadict["c2_location"]=c2value2
    #     datadict["b34-primary_snmp_loc_str"]=b34value1
    #     datadict["c34-secondary_snmp_loc_str"]=c34value1
    
    if (re.search(r"set.*hostname",eachline)):
        print(f"hostname >>>> {eachline}")               
        b5value1=eachline.split(" ")[2]
        b5value2=b5value1.split("\\")[0]
        # print(f"b5 value i.e. hostname A  is, {b5value2}")  
        hostcnl=b5value2.split("-")[1]
        # print(f"value of hostnl is {hostcnl}")
        datadict["b5-hostname_a"]=b5value2
        # print(datadict)
        # datadict["b5-hostname"]=b5value
        c5value1=b5value2.replace("-A","-B")
        # print(f"c5 value i.e. hostname B is, {c5value1}")  
        datadict["c5-hostname_b"]=c5value1
        #print(datadict)


    if (re.search(r"set.*static.*default.*next.*gate.*on",eachline)):
        print(f"default route >>>> {eachline}")               
        b14value1=eachline.split(" ")[6]
        datadict["b14-routerip"]=b14value1
        datadict["b15-routerip"]=b14value1
        datadict["b16-routerip"]=b14value1


    # if (re.search(r"set.*int.*eth.*state.*on",eachline)): #find all live interfaces even duplicates
    if (re.search(r"set.*int.*eth.*state",eachline)): #find all live interfaces even duplicates
        # print(f"live interfaces found in,# {eachline}#")   
        loi.append(eachline.split(" ")[2])            


    if (re.search(r"set.*bootp.*int.*relay.*on",eachline)): #find all live interfaces even duplicates
        #print(f"hostname found in,# {eachline}#")   
        lorelay.append(eachline.split(" ")[5])            
    
if  c2_location == "unknown":
    print("location could not be established")
    manual_location=input("Do you want to enter it manually, (y/n):")
    if (manual_location=="y"):
        c2_location=input("Enter the location. e.g. Milano,Italy :")
        datadict["c2_location"]=c2_location
        datadict["b34-primary_snmp_loc_str"]=b5value2+" "+c2_location
        datadict["c34-secondary_snmp_loc_str"]=c5value1+" "+c2_location

loi=list(dict.fromkeys(loi)) #removed all the duplicates from the list.
lorelay=list(dict.fromkeys(lorelay)) #removed all the duplicates from the list.

print("==========================================================================")
print(f"live interfaces are ....")
for ints in loi:
    print (f"{ints}")
print("==========================================================================")
print(f"helper addresses are ....")
for helpers in lorelay:
    print (f"{helpers}")
print("==========================================================================")

# print("====================================================: Interface dictionary")

# for keys,items in intdict.items():
#     print(f"{keys} : {items}")
# print("==========================================================================")



for ints in loi:
    
    if ints=="eth2":
        continue

    intdict[ints]={"vip":"none","aip":"none","bip":"none","mask":"none","bootp":"none","comment":"none"}

    bootpline="set bootp interface "+ints+" on"


    for eachline in utm_config_list:
        
        if (re.search(rf"int.*{ints}.*add",eachline)): #find all live interfaces even duplicates
            #print(f"hostname found in,# {eachline}#")
            aip=eachline.split(" ")[4]
            lastoctetplus1=int(aip.split(".")[3])+1
            lastoctetminus1=int(aip.split(".")[3])-1
            bip=str(aip.split(".")[0])+"."+str(aip.split(".")[1])+"."+str(aip.split(".")[2])+"."+str(lastoctetplus1)
            vip=str(aip.split(".")[0])+"."+str(aip.split(".")[1])+"."+str(aip.split(".")[2])+"."+str(lastoctetminus1)
            slashmask=eachline.split(" ")[6]
            dotmask=maskdict[slashmask]
            # intdict[ints]={"vip":vip,"aip":aip,"bip":bip,"mask":dotmask,"bootp":"none"}
            intdict[ints]={"vip":vip,"aip":aip,"bip":bip,"mask":dotmask,"bootp":"none","comment":"none"}

        if bootpline in eachline: #find all live interfaces even duplicates
            intdict[ints]["bootp"]="yes"
            lobpi.append(ints)

        if (re.search(rf"int.*{ints}.*comments",eachline)): #find all live interfaces even duplicates
            #print(f"hostname found in,# {eachline}#")
            int_comment=eachline.split('"')[1]
            int_comment=int_comment.strip()
            # print(f"intdict value is ...{intdict}")
            print(f"interface is {ints} and comment is {int_comment}")
            # intdict[ints]["comment"]=int_comment
            # intdict[ints]["comment"]="test123"
            # intdict[ints]["bootp"]="yes"
            # print(intdict[ints]["comment"])
            # print(int_comment)
            # intdict[ints]["comment"]=int_comment

    # for x,y in intdict.items():
    #     print(f"{x}:{y}")

# for x,y in intdict.items():
#     print(f"{x}:{y}")

print("==========================================================================")
print(f"list of bpis is ....")
for bpi in lobpi:
    print(f"{bpi}")
print("==========================================================================")

print("==========================================================================")
print("Establish Domain for the UTM Device")
print("==========================================================================")


print(f"hostname found in ....#")

for eachline in fwsentryfw_list: 
    if (hostcnl in eachline and "luster" in eachline): #find all live interfaces even duplicates
        print(eachline)
        domain=eachline.split(",")[1]
        domain=domain.split("ite")[1]
        

happy_with_domain_value=input(f"domain value is {domain}, are you happy: (y/n):")  #happy with domain value
if happy_with_domain_value=="n":
    domain=input("Enter the domain value manually: ")


print("==========================================================================")
print("Loading domain data")
print("==========================================================================")

if domain=="10":
    b30value=domdata["10"]["account_id"]
    b31value=domdata["10"]["mgmt_svr_address"]
    datadict["b30-domain_account_id"]=b30value
    datadict["b31-mgt_server_address"]=b31value

if domain=="11":
    b30value=domdata["11"]["account_id"]
    b31value=domdata["11"]["mgmt_svr_address"]
    datadict["b30-domain_account_id"]=b30value
    datadict["b31-mgt_server_address"]=b31value

if domain=="12":
    b30value=domdata["12"]["account_id"]
    b31value=domdata["12"]["mgmt_svr_address"]
    datadict["b30-domain_account_id"]=b30value
    datadict["b31-mgt_server_address"]=b31value

if domain=="perimeter":
    b30value=domdata["perimeter"]["account_id"]
    b31value=domdata["perimeter"]["mgmt_svr_address"]
    datadict["b30-domain_account_id"]=b30value
    datadict["b31-mgt_server_address"]=b31value

if domain=="post_prod":
    b30value=domdata["post_prod"]["account_id"]
    b31value=domdata["post_prod"]["mgmt_svr_address"]
    datadict["b30-domain_account_id"]=b30value
    datadict["b31-mgt_server_address"]=b31value

    # "10":{"account_id":"6217907","name":"dms_site10.mmm.com","mgmt_svr_address":"169.12.132.166"},
    # "11":{"account_id":"6277501","name":"dms_site11.mmm.com","mgmt_svr_address":"169.12.17.111"},
    # "12":{"account_id":"6454177","name":"not_available","mgmt_svr_address":"169.12.17.112"},
    # "perimeter":{"account_id":"5970594","name":"dms_perimeter.mmm.com","mgmt_svr_address":"169.12.132.154"},
    # "post_prod":{"account_id":"6617423","name":"3M Post-Production Firewalls","mgmt_svr_address":"169.12.132.154"}

print("===================================: dictionary of items")
for keys,items in datadict.items():
    print(f"{keys} : {items}")

print("==========================================================================")
print("Insert gathered data into the spreadsheet")
print("==========================================================================")

dhs="""
{}
""".format("\n".join(lorelay[0:]))
# print(f"value of dhs is {dhs}")

# ws['b2'].value = "none"
# ws['b30'].value = "none"
# ws['b31'].value = "none"
# ws['b5'].value = "none"
# ws['c5'].value = "none"
# ws['c2'].value = "none"
# ws['b34'].value = "none"
# ws['c34'].value = "none"
# ws['b14'].value = "none"
# ws['b15'].value = "none"
# ws['b16'].value = "none"
# ws['b39'].value = "none"
# ws['c39'].value = "none"
# ws['d39'].value = "none"
# ws['e39'].value = "none"

ws['b2'].value = "n/a"
# ws['b2'].value = datadict["b2-model"]
ws['b30'].value = datadict["b30-domain_account_id"]
ws['b31'].value = datadict["b31-mgt_server_address"]
ws['b5'].value = datadict["b5-hostname_a"]
ws['c5'].value = datadict["c5-hostname_b"]
# print(f"value of c2_location is {c2_location}")
ws['c2'].value = datadict["c2_location"]
ws['b34'].value = datadict["b34-primary_snmp_loc_str"]
ws['c34'].value = datadict["c34-secondary_snmp_loc_str"]
ws['b14'].value = datadict["b14-routerip"]
ws['b15'].value = datadict["b15-routerip"]
ws['b16'].value = datadict["b16-routerip"]
ws['b39'].value = intdict["eth1"]["vip"]
ws['c39'].value = intdict["eth1"]["aip"]
ws['d39'].value = intdict["eth1"]["bip"]
ws['e39'].value = intdict["eth1"]["mask"]
if "eth4" in intdict:
    ws['b42'].value = intdict["eth4"]["vip"]
    ws['c42'].value = intdict["eth4"]["aip"]
    ws['d42'].value = intdict["eth4"]["bip"]
    ws['e42'].value = intdict["eth4"]["mask"]
if "eth5" in intdict:
    ws['b43'].value = intdict["eth5"]["vip"]
    ws['c43'].value = intdict["eth5"]["aip"]
    ws['d43'].value = intdict["eth5"]["bip"]
    ws['e43'].value = intdict["eth5"]["mask"]

ws.range('c54').api.WrapText = False
ws.range('c55').api.WrapText = True


# print(f"value of intns dictionary is ....\n")
# for keys,values in intns.items():
#     print(f"{keys}:{values}")

# print(f"value of intdict dictionary is ....\n")
# for keys,values in intdict.items():
#     print(f"{keys}:{values}")

startrow=53
for eachint in loi:
    
    # if eachint == "eth1" or eachint == "eth2" or eachint == "eth3" or eachint == "eth4" or eachint == "eth5" or eachint == "eth6":
    if eachint == "eth1" or eachint == "eth2" or (re.search(rf"eth[3-8]",eachint)):
        continue
    nextrow=startrow+1
    cella="a"+str(startrow)
    cellanr="a"+str(nextrow)
    cellb="b"+str(startrow)
    # cellbnr="b"+str(nextrow)
    cellc="c"+str(startrow)
    cellcnr="c"+str(nextrow)
    celld="d"+str(startrow)
    celldnr="d"+str(nextrow)
    celle="e"+str(startrow)
    # cellenr="e"+str(nextrow)
    cellf="f"+str(startrow)
    # cellfnr="f"+str(nextrow)
    cellg="g"+str(startrow)
    # cellgnr="g"+str(nextrow)
    # print(cella)
    ws[cella].value = eachint
    ws[cellanr].value = "DHCP helpers"
    ws[cellb].value = intdict[eachint]["vip"]
    ws[cellc].value = intdict[eachint]["aip"]
    ws[cellcnr].value = "n/a"
    ws[celld].value = intdict[eachint]["bip"]
    ws[celldnr].value = "n/a"
    ws[celle].value = intdict[eachint]["mask"]
    ws[cellf].value = intns[eachint]["state"]
    ws[cellg].value = intns[eachint]["name"]
    
    bpstartrow=startrow
    # print(f"bpstartrow now at the beginning is {bpstartrow}")
    
    if eachint in lobpi:
        
        # if eachint == "eth1" or eachint == "eth2" or eachint == "eth3" or eachint == "eth4" or eachint == "eth5" or eachint == "eth6":
        if eachint == "eth1" or eachint == "eth2" or (re.search(rf"eth[3-8]",eachint)):
            continue

        bpstartrow+=1
        # print(f"bpstartrow now in the loop is {bpstartrow}")
        print(f"loop begin: startrow:{bpstartrow}, eachint:{eachint} ")
        cella="a"+str(bpstartrow)
        cellc="c"+str(bpstartrow)
        celld="d"+str(bpstartrow)
        # print(f"cella {cella}, cellc {cellc}, celld {celld}")
        ws[cella].value = "DHCP helpers"
        ws[cellc].value = dhs
        ws[celld].value = dhs
        print(f"loop end: startrow:{bpstartrow}, eachint:{eachint} ")
    startrow=startrow+3
    
    # print(startrow)



# b2-model : n/a
# b30-domain_account_id : 6617423
# b31-mgt_server_address : 169.12.132.154
# b5-hostname_a : utm-itMAR-A
# c5-hostname_b : utm-itMAR-B
# c2_location : Marcallo,Italy
# b34-primary_snmp_loc_str : utm-itMAR-A Marcallo,Italy
# c34-secondary_snmp_loc_str : utm-itMAR-B Marcallo,Italy
# b14-routerip : 169.5.229.20
# b15-routerip : 169.5.229.20
# b16-routerip : 169.5.229.20

# print("===================================: dictionary of items")
# for keys,items in datadict.items():
#     print(f"{keys} : {items}")

# print("===================================: List of interfaces")

# for lines in loi:
#     print(lines)
# print("===================================: list of bootp interfaces")

# for lines in lobpi:
#     print(lines)

# print("===================================: list of relay IPs")

# for lines in lorelay:
#     print(lines)
        
print("===================================: Interface dictionary")

for keys,items in intdict.items():
    print(f"{keys} : {items}")

print("==========================================================================")
print("Save a copy of template file")
print("==========================================================================")
#name format
# print(f"{c2_location}")
wb.save(fr'C:\Users\adfwyzz\OneDrive - 3M\Documents\automation\python_scripts\mp-config-generator\{c2_location} - 3M UTM Build Template for midpoint AK_{timestring}.xlsx')
#IT-Milano - 3M TUM Build Template for midpoint AK_30112022.xlsx

print("==========================================================================")
print("All done")
print("Critical: Remember to check and verify the cable type!!!!")
print("Search for <<unknown>> in resultant spreadsheet, and address the issue if there")
print("Remember to check the router ip is upto the latest standards (show run int vlan 109, on core) !!!!")
print("==========================================================================")

