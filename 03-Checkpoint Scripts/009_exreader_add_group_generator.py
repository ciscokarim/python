import string
from re import search
import re
import copy
from collections import OrderedDict
import xlwings as xw
import time
import sys
import os

os.system("cls")

#==========================================================================================================================#
#load the excel file and then load the correct tab of the file.
cwd=os.getcwd()
# print(cwd)
for file in os.listdir(cwd):

    if (re.search(r"(?i)utm",file)) or (re.search(r"(?i)form",file)) or (re.search(r"(?i)xls",file)):
    # if "UTM" in file or "utm" in file or "form" in file or "FORM" in file:
        utm_request_form=file
        print(utm_request_form)
    
    if (re.search(r"(?i)domain",file)) or (re.search(r"(?i)csv",file)):
    # if "csv"  in file or "objects" in file or "domain" in file:
        objects_csv_file=file
        print(objects_csv_file)
       
#-------------------------------------------------------------#

wb=xw.Book(utm_request_form)
ws=wb.sheets['UTM Form']

#-------------------------------------------------------------#

frow=int(input("Enter the firt data row :"))
lrow=0
while frow > lrow: #keep asking util the correct data is entered.
    lrow=int(input("Enter the last data row :"))
    if frow > lrow:
        lrow=int(input("Enter the last data row again (last row must be greater than first row):"))

ppkg_uinput=(input("Enter the name of the utm e.g. utm-plWAR(case-sensitive) :"))
# ppkg_uinput="utm-plWAR"
# ppkg_uinput="utm-ukAYC"
rule_name="Process Vlans"
rule_comment="CXXXXX AK XX/XX/2022"
rbasestrow=int(input(f"Enter the starting point in #{ppkg_uinput}# rulebase :"))
gpsttrow=int(input(f"Enter the starting row for groups: "))
gpendrow=0
while gpsttrow > gpendrow: #keep asking until the correct data is entered.
    gpendrow=int(input(f"Enter the ending row for groups: "))
    if gpsttrow > gpendrow:
        gpendrow=int(input("Enter the ending row for groupsagain (last row must be greater than first row):"))
# group_counter=number_of_groups
group_rows=[]
group_item_rows=[]
group_dict={'gpa999':{'gptype':"",'gpname':"",'gpmembers':[]}}

# if(number_of_groups > 0):
#     for i in range (1,group_counter+1):
#         group_row=int(input(f"Enter the row location for the group {i}: "))
#         group_first_item_row=int(input(f"Enter the first item row for the group {i}: "))
#         group_last_item_row=int(input(f"Enter the last item row for the group {i}: "))
#         group_data_string="gp"+str(i)
#         group_dict[group_data_string]={'gprow':group_row,'gpfrow':group_first_item_row,'gplrow':group_last_item_row,'gpname':"",'gpmembers':[]}




    
# rbasestrow=1


# frow=263
# lrow=266
# ppkg_uinput="utm-var"
# rbasefrow=5

#-------------------------------------------------------------#
#cols=["a","b"]
cols=["a","b","c","d"]

#-------------------------------------------------------------#
ppkg=ppkg_uinput+"_In_Line Security"
# print(ppkg)
ipwmcnr=""
portwmcnr=""
iplist=[]
iplistcnr=[]
# iplist
netlist=[]
netlistcnr=[]

fqdnlist=[]
fqdnlistcnr=[]

fqdn_host_tbcr_list=[]
fqdn_host_tbcr_list_cnr=[]

fqdn_net_tbcr_list=[]
fqdn_net_tbcr_list_cnr=[]

fqdn_dns_tbcr=[]
fqdn_dns_tbcr_list=[]
fqdn_dns_tbcr_list_cnr=[]

portlist=[]
portlistcnr=[]

actionlist=[]
actionlistcnr=[]

sectionlist=[]
sectionlistcnr=[]

actionfnl=[]
# celldict_unfmtd={999:{'srcs': [''], 'dsts': [''], 'ports': [''], 'action': ''}}
# celldict_fmtd={999:{'srcs': [''], 'dsts': [''], 'ports': [''], 'action': ''}}
celldict_unfmtd={999:{'srcs': [], 'dsts': [], 'ports': [], 'action':"", 'snegate':"", 'dnegate':""}}
celldict_fmtd={999:{'srcs': [], 'dsts': [], 'ports': [], 'action':"", 'snegate':"", 'dnegate':""}}
# print(celldict_unfmtd)

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
    # print(f"items in the list are ....")
    for items in x:
        print(items)

def dictprinter(x):
    for items in x:
        print(f"{items}:{x[items]}")

def dictprinter2(x):
    for l1keys in x:
        # print(l1keys)
        if str(l1keys) == "999":
            continue
        else:
            # print("no")
            print(f"========================================= l1key : {l1keys}")
            for l2keys,l2values in x[l1keys].items():
                # print(f"l2keys:{l2keys},l2values:{l2values}")
                print(f"{l2keys}:{l2values}")

def flatten(lst):
    for el in lst:
        if isinstance(el, list):  # N.B. this only works for lists, not general
                                  # collections e.g. sets, tuples, dicts, etc...
            # recurse
            yield from flatten(el)
        else:
            # generate
            yield el

# def list_cleaner(the_list):
#     {
#             #this function cleans the list and returns a list without
#             #None, bool and length objects.
#             # the_list=list(filter(None,the_list))
#             # the_list = list(filter(bool,the_list))
#             # the_list = list(filter(len,the_list))
#             return the_list
#     }

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

#-------------------------------------------------------------#

port_dict={

            "TCP102":"ICCP",
            "TCP123":"ntp-TCP",
            "TCP1234":"UltorsTrojan",
            "TCP139":"nbsession",
            "TCP1433":"MS-SQL-Server",
            "TCP1434":"MS-SQL-Monitor",
            "TCP1723":"pptp-TCP",
            "TCP2000":"SCCP",
            "TCP21":"ftp",
            "TCP22":"ssh",
            "TCP23":"telnet",
            "TCP25":"smtp",
            "TCP3001":"StoneBeat-Daemon",
            "TCP3389":"Remote_Desktop_Protocol",
            "TCP389":"ldap",
            "TCP443":"https",
            "TCP445":"microsoft-ds",
            "TCP514":"shell",
            "TCP53":"domain-tcp",
            "TCP5432":"PostgreSQL",
            "TCP636":"ldap-ssl",
            "TCP69":"tftp",
            "TCP80":"http",
            "TCP8080":"HTTP_proxy",
            "UDP123":"ntp-UDP",
            "UDP137":"nbname",
            "UDP138":"nbdatagram",
            "UDP1433":"MS-SQL-Server_UDP",
            "UDP1434":"MS-SQL-Monitor_UDP",
            "UDP1812":"NEW-RADIUS",
            "UDP161":"snmp",
            "UDP389":"ldap_UDP",
            "UDP445":"microsoft-ds-UDP",
            "UDP514":"syslog",
            "UDP53":"domain-udp",
            "TCP18191":"CPD",
            "TCP18264":"FW1_ica_services",
            "TCP18192":"CPD_amon",
            "TCP4000":"tcp4000",
            "TCP5000":"tcp5000",
            "TCP18208":"FW1_CPRID"



}
#-------------------------------------------------------------#
print("==========================================================================")
print("Loading objects file ")
print("==========================================================================")

with open (objects_csv_file) as fileholder01:
    objectsfile_string=fileholder01.read() # this converts the file into a string
with open (objects_csv_file) as fileholder02:
    objectsfile_list=fileholder02.readlines() # this converts the file into a string

print("==========================================================================")
print("Loading the script file to be created ")
print("==========================================================================")

with open('thescript.txt', 'w') as script:
        script.write(f"===========================================================\n")
        script.write(f"           Script to be pasted in mgmt-cli==\n")
        script.write(f"===========================================================\n")

#-------------------------------------------------------------#



print("=================================================================================")
print("Extracting the IP Addresses, Networks and Ports && Append them to lists ")
print("=================================================================================")
print("=================================================================================")
print("Add data to celldict_unfmtd ")
print("=================================================================================")


for row in range (frow,lrow+1):
    # celldict_unfmtd[row]={"srcs":[""],"dsts":[""],"ports":[""],"action":""}
    # celldict_fmtd[row]={"srcs":[""],"dsts":[""],"ports":[""],"action":""}
    celldict_unfmtd[row]={'srcs': [], 'dsts': [], 'ports': [], 'action':"", 'snegate':"no", 'dnegate':"no","section":"none"}
    celldict_fmtd[row]={'srcs': [], 'dsts': [], 'ports': [], 'action':"", 'snegate':"no", 'dnegate':"no","section":"none"}
# dictprinter(celldict_unfmtd)

for col in (cols):
    for row in range (frow,lrow+1):
        cell=str(col)+str(row)
    #  print(cell)
        cvalue=ws.range(cell).value
        ccolor=ws.range(cell).color
    #  print(f"cvalue:{cvalue}---ccolor:{ccolor}")
        itemlist=[]
     
    #  if(cvalue != None):

##########################################################################################################################

        if(cvalue != None and cvalue.find("any") == -1):
            # print(f"cvalue:\n{cvalue}")
            if re.search("(?i)ndns.*",cvalue):
                fqdn_dns_tbcr=re.findall(r'(?i)ndns.*',cvalue)
                # print(f"fqdn_dns_tbcr:\n{fqdn_dns_tbcr}")
                counter=0
                for lines in fqdn_dns_tbcr:
                    # clean_name=lines.split(":")[1]
                    # clean_name=clean_name.strip()
                    # fqdn_name_list.append(clean_name)
                    # fqdn[counter]=clean_name
                    # lines=lines.replace("ndns:","")
                    lines=lines.lower()
                    # print(f"{lines}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    # ndns_str_to_search=lines.replace("ndns:","")
                    # objectsfile_string_lower_case=objectsfile_string.lower()
                    # print(f"ndns string to search is {ndns_str_to_search}")
                    # if ndns_str_to_search in objectsfile_string_lower_case:
                        # continue
                        # print(f"string to search {ndns_str_to_search} not found in objects file string lower case")
                        # continue
                        # fqdn_dns_tbcr[counter]=lines
                        # counter+=1
                    # fqdn_dns_tbcr[counter]=lines
                    # counter+=1
                # print(fqdn)
                if fqdn_dns_tbcr:
                    fqdn_dns_tbcr_cnr=str(col)+str(row)+":"+str(fqdn_dns_tbcr)
                    
                # print(f"ipwmcnr:{ipwmcnr}")
                    if col == "a" or col == "A":
                        celldict_unfmtd[row]["srcs"]=fqdn_dns_tbcr
                    if col == "b" or col == "B":
                        celldict_unfmtd[row]["dsts"]=fqdn_dns_tbcr
                    if col == "c" or col == "C":
                        celldict_unfmtd[row]["ports"]=fqdn_dns_tbcr

                fqdn_dns_tbcr_list_cnr.append(fqdn_dns_tbcr_cnr)
                fqdn_dns_tbcr_list.append(fqdn_dns_tbcr)            
                continue

#########################################################################################################################

        if(cvalue != None and cvalue.find("any") == -1):
            # print(f"cvalue:\n{cvalue}")
            if re.search("(?i)nho.*",cvalue):
                fqdn_host_tbcr=re.findall(r'(?i)nho.*',cvalue)
                # print(f"fqdn_host_tbcr:\n{fqdn_host_tbcr}")
                counter=0
                for lines in fqdn_host_tbcr:
                    # clean_name=lines.split(":")[1]
                    # clean_name=clean_name.strip()
                    # fqdn_name_list.append(clean_name)
                    # fqdn[counter]=clean_name
                    lines=lines.replace("nho:","")
                    fqdn_host_tbcr[counter]=lines
                    counter+=1
                # print(fqdn)
                if fqdn_host_tbcr:
                    fqdn_host_tbcr_cnr=str(col)+str(row)+":"+str(fqdn_host_tbcr)
                    
                # print(f"ipwmcnr:{ipwmcnr}")
                    if col == "a" or col == "A":
                        celldict_unfmtd[row]["srcs"]=fqdn_host_tbcr
                    if col == "b" or col == "B":
                        celldict_unfmtd[row]["dsts"]=fqdn_host_tbcr
                    if col == "c" or col == "C":
                        celldict_unfmtd[row]["ports"]=fqdn_host_tbcr

                fqdn_host_tbcr_list_cnr.append(fqdn_host_tbcr_cnr)
                fqdn_host_tbcr_list.append(fqdn_host_tbcr)            
                continue
 
        if(cvalue != None and cvalue.find("any") == -1):
            # print(f"cvalue:\n{cvalue}")
            if re.search("(?i)nno.*",cvalue):
                fqdn_net_tbcr=re.findall(r'(?i)nno.*',cvalue)
                # print(f"fqdn_net_tbcr:\n{fqdn_net_tbcr}")
                counter=0
                for lines in fqdn_net_tbcr:
                    # clean_name=lines.split(":")[1]
                    # clean_name=clean_name.strip()
                    # fqdn_name_list.append(clean_name)
                    # fqdn[counter]=clean_name
                    lines=lines.replace("nno:","")
                    fqdn_net_tbcr[counter]=lines
                    counter+=1
                # print(fqdn)
                if fqdn_net_tbcr:
                    fqdn_net_tbcr_cnr=str(col)+str(row)+":"+str(fqdn_net_tbcr)
                    
                # print(f"ipwmcnr:{ipwmcnr}")
                    if col == "a" or col == "A":
                        celldict_unfmtd[row]["srcs"]=fqdn_net_tbcr
                    if col == "b" or col == "B":
                        celldict_unfmtd[row]["dsts"]=fqdn_net_tbcr
                    if col == "c" or col == "C":
                        celldict_unfmtd[row]["ports"]=fqdn_net_tbcr

                fqdn_net_tbcr_list_cnr.append(fqdn_net_tbcr_cnr)
                fqdn_net_tbcr_list.append(fqdn_net_tbcr)            
                continue


        if(cvalue != None and cvalue.find("any") == -1):
            # print(f"cvalue:\n{cvalue}")
            if re.search("(?i)fqdn.*",cvalue):
                fqdn=re.findall(r'(?i)fqdn.*',cvalue)
                # print(f"fqdn:\n{fqdn}")
                counter=0
                for lines in fqdn:
                    # clean_name=lines.split(":")[1]
                    # clean_name=clean_name.strip()
                    # fqdn_name_list.append(clean_name)
                    # fqdn[counter]=clean_name
                    fqdn[counter]=lines
                    counter+=1
                # print(fqdn)
                if fqdn:
                    fqdncnr=str(col)+str(row)+":"+str(fqdn)
                    
                # print(f"ipwmcnr:{ipwmcnr}")
                    if col == "a" or col == "A":
                        celldict_unfmtd[row]["srcs"]=fqdn
                    if col == "b" or col == "B":
                        celldict_unfmtd[row]["dsts"]=fqdn
                    if col == "c" or col == "C":
                        celldict_unfmtd[row]["ports"]=fqdn

                fqdnlistcnr.append(fqdncnr)
                fqdnlist.append(fqdn)            
                continue
    
        if(cvalue != None and cvalue.find("any") == -1):
            # print(f"cvalue is #######################{cvalue}")
            if re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",cvalue):
                ipwm=re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\/..',cvalue)

                if ipwm:
                    ipwmcnr=str(col)+str(row)+":"+str(ipwm)
                    # print(f"ipwmcnr:{ipwmcnr}")
                
                if ipwm:
                    
                    if col == "a" or col == "A":
                        celldict_unfmtd[row]["srcs"]=ipwm
                    
                    if col == "b" or col == "B":
                        celldict_unfmtd[row]["dsts"]=ipwm
                # print(f"cvalue:{cvalue}")        
                # print(f"ipwm:{ipwm}")
                netlist.append(ipwm)
                # print(f"ipwmcnr:{ipwmcnr}")
                netlistcnr.append(ipwmcnr)
                # itemlist.append(net_good)
            
            # if re.search("(?i)tcp.\d+|udp.\d+|ip.\d+|icmp.\d+|tcp\d+|udp\d+|ip\d+|icmp\d+",cvalue):
            if re.search("(?i)tcp.\d+-\d+|udp.\d+-\d+|tcp.\d+|udp.\d+|ip.\d+|icmp.\d+|tcp\d+|udp\d+|ip\d+|icmp\d+",cvalue):
                portwm=re.findall(r'(?i)tcp.\d+-\d+|udp.\d+-\d+|tcp.\d+|udp.\d+|ip.\d+|icmp.\d+|tcp\d+|udp\d+|ip\d+|icmp\d',cvalue)
                # print(f"portwm={portwm}")
                if portwm:
                    portwmcnr=str(col)+str(row)+":"+str(portwm)
                # print(f"ipwmcnr:{ipwmcnr}")
                
                    if col == "c" or col == "C":
                        celldict_unfmtd[row]["ports"]=portwm

                portlistcnr.append(portwmcnr)
                # itemlist.append(net_good)           
            
                portlist.append(portwm)
                # itemlist.append(portwm)


            if re.search("(?i)section.*",cvalue):
                # section_line=re.findall(r'(?i)section.*',cvalue)
                section_title=cvalue.split("ection:")[1]
                section_title=section_title.strip()
                # print(f"section_title:{section_title}#######################")
                # print(section_line)
                # section_line=section_line.split(":")(1)
                # section_line=section_line.strip()
                if section_title:
                    section_title_cnr=str(col)+str(row)+":"+str(section_title)
                # print(f"ipwmcnr:{ipwmcnr}")
                
                    if col == "a" or col == "A":
                        celldict_unfmtd[row]["section"]=section_title
                        celldict_fmtd[row]["section"]=section_title

                sectionlistcnr.append(section_title_cnr)
                # itemlist.append(net_good)           
            
                sectionlist.append(section_title)
                # itemlist.append(portwm)



            # if "ny" in cvalue:
            #     print(f"portwm cvalue:{cvalue}")
            #     portwm=cvalue
            #     if portwm:
            #         portwmcnr=str(col)+str(row)+":"+str(portwm)
            #     # print(f"ipwmcnr:{ipwmcnr}")
                
            #         if col == "c" or col == "C":
            #             celldict_unfmtd[row]["ports"]=portwm

            #     portlistcnr.append(portwmcnr)
            #     # itemlist.append(net_good)           
            
            #     portlist.append(portwm)
            #     # itemlist.append(portwm)

            if re.search("(?i)any",cvalue):
                portwm=re.findall(r'(?i)any',cvalue)
                if portwm:
                    portwmcnr=str(col)+str(row)+":"+str(portwm)
                # print(f"ipwmcnr:{ipwmcnr}")
                
                    if col == "c" or col == "C":
                        celldict_unfmtd[row]["ports"]=portwm

                portlistcnr.append(portwmcnr)



                # itemlist.append(net_good)           
            
                portlist.append(portwm)
                # itemlist.append(portwm)

            if re.search("(?i)accept|deny|drop|any",cvalue):
                #actionwm=[]
                actionwm=re.findall(r'(?i)accept|deny|drop|any',cvalue)
                if actionwm:
                    actionwmcnr=str(col)+str(row)+":"+str(actionwm)
                    if "cept" in actionwmcnr or "CEPT" in actionwmcnr:
                        actionwmcnr="Accept"
                        actionwm="Accept"
                    if "eny" in actionwmcnr or "ENY" in actionwmcnr:
                        actionwmcnr="Deny"
                        actionwm="Deny"    
                    if "rop" in actionwmcnr or "ROP" in actionwmcnr:
                        actionwmcnr="Drop"
                        actionwm="Drop"    
                    if col == "d" or col == "D":
                        celldict_unfmtd[row]["action"]=actionwm
                
                # print(f"ipwmcnr:{ipwmcnr}")
                
                actionlistcnr.append(actionwmcnr)
                #print(actionwm[0])
                # print(type(actionwm))
                actionlist.append(actionwm)
                # itemlist.append(actionwm)    

            # if(cvalue != None and cvalue.find("any") == -1 and cvalue.find("/") == -1 ) or :

            # if(cvalue != None and cvalue.find("any") == -1):
                                
            # if "/" not in cvalue:
            if re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",cvalue):
                # print(f"ip:{ip}")
                # print(f"{cvalue}")
                ip=re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b',cvalue)
                # print(f"ip:{ip}")
                if "/" not in cvalue and "gated" not in cvalue:
                    if ip:
                        ipcnr=str(col)+str(row)+":"+str(ip)
                    # print(f"ipwmcnr:{ipwmcnr}")
                        if col == "a" or col == "A":
                            celldict_unfmtd[row]["srcs"]=ip
                        if col == "b" or col == "B":
                            celldict_unfmtd[row]["dsts"]=ip

                    # print(f"cvalue:{cvalue}")        
                    # print(f"ip:{ip}")
                    iplistcnr.append(ipcnr)
                    iplist.append(ip)
                    # itemlist.append(ip)

            # if(cvalue != None and cvalue.find("any") == -1):
            # # if(cvalue != None and cvalue.find("any")):
            #     if re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",cvalue):
            #         # print(f"ip:{ip}")
            #         # print(f"{cvalue}")
            #         ip=re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b',cvalue)
            #         # print(f"{ip}########################")
            #         if ip:
            #             ipcnr=str(col)+str(row)+":"+str(ip)
            #         # print(f"ipwmcnr:{ipwmcnr}")
            #             if col == "a" or col == "A":
            #                 celldict_unfmtd[row]["srcs"]=ip
            #             if col == "b" or col == "B":
            #                 celldict_unfmtd[row]["dsts"]=ip
            #         print(f"ip:{ip}")
            #         iplistcnr.append(ipcnr)
            #         iplist.append(ip)
            #         # itemlist.append(ip)

            #  fqdn_name_list=[]
            
            if(cvalue != None and cvalue.find("any") == -1 and cvalue.find("/") == -1 ):
                # print(cvalue)
                if re.search("(?i)fqdn.*",cvalue):
                    fqdn=re.findall(r'(?i)fqdn.*',cvalue)
                    # print(fqdn)
                    counter=0
                    for lines in fqdn:
                        # clean_name=lines.split(":")[1]
                        # clean_name=clean_name.strip()
                        # fqdn_name_list.append(clean_name)
                        # fqdn[counter]=clean_name
                        fqdn[counter]=lines
                        counter+=1
                    # print(fqdn)
                    if fqdn:
                        fqdncnr=str(col)+str(row)+":"+str(fqdn)
                    # print(f"ipwmcnr:{ipwmcnr}")
                        if col == "a" or col == "A":
                            celldict_unfmtd[row]["srcs"]=fqdn
                        if col == "b" or col == "B":
                            celldict_unfmtd[row]["dsts"]=fqdn

                    fqdnlistcnr.append(fqdncnr)
                    fqdnlist.append(fqdn)            



print(f"########################### fqdn dns tbcr list  ####################################")
# listprinter(fqdn_dns_tbcr_list_cnr)
# listprinter(fqdn_dns_tbcr_list)
# listprinter(fqdnlistcnr)

print(f"########################### fqdn host tbcr list  ####################################")
# listprinter(fqdn_host_tbcr_list_cnr)
# listprinter(fqdn_host_tbcr_list)
# listprinter(fqdnlistcnr)

print(f"########################### fqdn net tbcr list  ####################################")
# listprinter(fqdn_host_tbcr_list_cnr)
# listprinter(fqdn_net_tbcr_list)
# listprinter(fqdnlistcnr)

print(f"########################### fqdn list ###########################################")
# listprinter(fqdnlist)

print(f"########################### ip list #############################################")
# listprinter(iplist)
print(f"#################################################################################")

# listprinter(netlist)
# listprinter(fqdnlist)
# listprinter(fqdnlistcnr)
print(f"\n")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>>>> ")
print(f"  <<<<<<< Your Un-formatted Cell dictionary >>>>>>>>>> ")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>>>> ")
print(f"\n")
# dictprinter(celldict_unfmtd)
dictprinter2(celldict_unfmtd)
# print(f"celldict_fmtd out of the loop after filling up data is :")
# dictprinter(celldict_fmtd)

print("==========================================================================")
print("Formatting the data in celldict, create celldict_fmtd ")
print("==========================================================================")

asrcs=[]
bdsts=[]
cports=[]
daction=""

for keys,values in celldict_unfmtd.items():
    
    if keys==999:
        continue
    asrcs=(celldict_unfmtd[keys]["srcs"])
    bdsts=(celldict_unfmtd[keys]["dsts"])
    cports=(celldict_unfmtd[keys]["ports"])
    daction=(celldict_unfmtd[keys]["action"])

    # print(f"key is {keys}")
    # counter=0

    for eachitem in asrcs:
        # print(f"start loop counter={counter}")
        # print(f"eachitem in loop={eachitem}")

        if re.search("(?i)fqdn",eachitem):
            # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem.split(":")[1]
            # print(item_formatted)
            # print("########################################")
            # item_formatted=item_formatted.replace(")",",")
            # item_formatted=item_formatted.split(",")[1]
            # item_formatted="negated,"+item_formatted
            # print(f"eachitem:{eachitem},formatted_item={item_formatted}")

            if re.search("(?i)fqdn:negate",item_formatted):
                item_formatted=eachitem.replace("(",",")
                item_formatted=item_formatted.replace(")",",")
                item_formatted=item_formatted.split(",")[1]
                # item_formatted="negated,"+item_formatted
                # print(f"eachitem:{eachitem},formatted_item={item_formatted}")
                celldict_fmtd[keys]["srcs"].append(item_formatted)
                celldict_fmtd[keys]["snegate"]="yes" 
                continue
            
            celldict_fmtd[keys]["srcs"].append(item_formatted)
            # celldict_fmtd[keys]["snegate"]="yes" 
            continue

        if re.search("(?i)fqdn:negate",eachitem):
            # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem.replace("(",",")
            item_formatted=item_formatted.replace(")",",")
            item_formatted=item_formatted.split(",")[1]
            # item_formatted="negated,"+item_formatted
            # print(f"eachitem:{eachitem},formatted_item={item_formatted}")
            celldict_fmtd[keys]["srcs"].append(item_formatted)
            celldict_fmtd[keys]["snegate"]="yes" 

        elif "/" in eachitem:
            # print(eachitem)
            eachitem_mask_cidr=eachitem.split("/")[1]
            eachitem_net=eachitem.split("/")[0]
            item_formatted="n-"+eachitem_net+"-"+eachitem_mask_cidr
            # print(f"formatted item is {item_formatted}")
            # print(f"item to be updated is {celldict_fmtd[keys]['srcs']}")
            celldict_fmtd[keys]["srcs"].append(item_formatted)
            # counter+=1
       

            
        # if ("g_" in eachitem) or ("G_" in eachitem) or ("gr-" in eachitem) or ("GR-" in eachitem) or ("gr_" in eachitem) or ("GR_" in eachitem): 
        elif re.search("(?i)^g.*",eachitem):
            # print(f"eachitem is :{eachitem}")
            # eachitem_mask_cidr=eachitem.split("/")[1]
            # eachitem_net=eachitem.split("/")[0]
            # item_formatted=eachitem # no change to the fqdn name.
            # print(f"formatted item is {item_formatted}")
            # print(f"item to be updated is {celldict_fmtd[keys]['srcs']}")
            celldict_fmtd[keys]["srcs"].append(eachitem)
            # counter+=1


#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################

        elif re.search("(?i)^ndns.*",eachitem):
        # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem.replace("ndns:","")
            celldict_fmtd[keys]["srcs"].append(item_formatted)
        
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################


        elif re.search("(?i)^h.*",eachitem):
        # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem
            celldict_fmtd[keys]["srcs"].append(item_formatted)
        
        elif re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",eachitem):
        # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted="h-"+eachitem
            celldict_fmtd[keys]["srcs"].append(item_formatted)

        elif re.search("(?i)egated",eachitem):
            # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem.replace("(",",")
            item_formatted=item_formatted.replace(")",",")
            item_formatted=item_formatted.split(",")[1]
            # item_formatted="negated,"+item_formatted
            # print(f"eachitem:{eachitem},formatted_item={item_formatted}")
            celldict_fmtd[keys]["srcs"].append(item_formatted)
            celldict_fmtd[keys]["dnegate"]="yes" 


        # else:
        #     # eachitem_mask_cidr=eachitem.split("/")[1]
        #     # eachitem_net=eachitem.split("/")[0]
        #     item_formatted="h-"+eachitem
        #     # print(f"formatted item is {item_formatted}")
        #     # print(f"item to be updated is {celldict_fmtd[keys]['dsts']}")
        #     celldict_fmtd[keys]["srcs"].append(item_formatted)
        #     # counter+=1

    for eachitem in bdsts:
        # print(f"start loop counter={counter}")
        # print(f"eachitem in loop={eachitem}")
        
        if re.search("(?i)fqdn",eachitem):
            # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem.split(":")[1]
            # print(item_formatted)
            # print("########################################")
            # item_formatted=item_formatted.replace(")",",")
            # item_formatted=item_formatted.split(",")[1]
            # item_formatted="negated,"+item_formatted
            # print(f"eachitem:{eachitem},formatted_item={item_formatted}")

            if re.search("(?i)negate",item_formatted):
                item_formatted=eachitem.replace("(",",")
                item_formatted=item_formatted.replace(")",",")
                item_formatted=item_formatted.split(",")[1]
                # item_formatted="negated,"+item_formatted
                # print(f"eachitem:{eachitem},formatted_item={item_formatted}")
                celldict_fmtd[keys]["dsts"].append(item_formatted)
                celldict_fmtd[keys]["dnegate"]="yes" 
                continue
            
            celldict_fmtd[keys]["dsts"].append(item_formatted)
            # celldict_fmtd[keys]["snegate"]="yes" 
            continue
        
        if re.search("(?i)fqdn:negate",eachitem):
            # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem.replace("(",",")
            item_formatted=item_formatted.replace(")",",")
            item_formatted=item_formatted.split(",")[1]
            # item_formatted="negated,"+item_formatted
            # print(f"eachitem:{eachitem},formatted_item={item_formatted}")
            celldict_fmtd[keys]["dsts"].append(item_formatted)
            celldict_fmtd[keys]["dnegate"]="yes" 

        elif "/" in eachitem:
            # print(eachitem)
            eachitem_mask_cidr=eachitem.split("/")[1]
            eachitem_net=eachitem.split("/")[0]
            item_formatted="n-"+eachitem_net+"-"+eachitem_mask_cidr
            # print(f"formatted item is {item_formatted}")
            # print(f"item to be updated is {celldict_fmtd[keys]['dsts']}")
            celldict_fmtd[keys]["dsts"].append(item_formatted)
            # counter+=1
       

            
        # if ("g_" in eachitem) or ("G_" in eachitem) or ("gr-" in eachitem) or ("GR-" in eachitem) or ("gr_" in eachitem) or ("GR_" in eachitem): 
        elif re.search("(?i)^g.*",eachitem):
            # print(f"eachitem is :{eachitem}")
            # eachitem_mask_cidr=eachitem.split("/")[1]
            # eachitem_net=eachitem.split("/")[0]
            # item_formatted=eachitem # no change to the fqdn name.
            # print(f"formatted item is {item_formatted}")
            # print(f"item to be updated is {celldict_fmtd[keys]['dsts']}")
            celldict_fmtd[keys]["dsts"].append(eachitem)
            # counter+=1

#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################

        elif re.search("(?i)^ndns.*",eachitem):
        # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem.replace("ndns:","")
            celldict_fmtd[keys]["dsts"].append(item_formatted)
        
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################

        elif re.search("(?i)^h.*",eachitem):
        # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted=eachitem
            celldict_fmtd[keys]["dsts"].append(item_formatted)
        
        elif re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])",eachitem):
        # fqdn=re.findall(r'(?i)fqdn.*',cvalue)
            item_formatted="h-"+eachitem
            celldict_fmtd[keys]["dsts"].append(item_formatted)
        

    for eachitem in cports:
        # print(f"eachitem:{eachitem}&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        # print(f"start loop counter={counter}")
        if "Any" in eachitem or "any" in eachitem:
            celldict_fmtd[keys]["ports"].append("Any")
            continue

        if re.search("(?i)fqdn", eachitem):
            service_fmtd=eachitem.split(":")[1]
            celldict_fmtd[keys]["ports"].append(service_fmtd)
            continue

        port_prot=re.search("^[a-zA-Z]+", eachitem).group()
        port_num=re.search("\d+-\d+|\d+", eachitem).group() 
        service_fmtd=port_prot.upper()+port_num
        print(f"services formated are {service_fmtd}")
        service_replaced=""
        for portitem in port_dict:
            # print(f"port items are {portitem}")
            if service_fmtd == portitem:
                print (f"formatted service {service_fmtd} found in port_dict@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                # print (f"replaced service for {service_fmtd} will be {service_replaced}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                service_replaced=port_dict[service_fmtd]
                print (f"replaced service for {service_fmtd} will be {service_replaced}")
                service_fmtd=service_replaced
        celldict_fmtd[keys]["ports"].append(service_fmtd)

   
    celldict_fmtd[keys]["action"]=daction.lower()
    celldict_fmtd[keys]["action"]=daction.replace("accept","Accept")
    celldict_fmtd[keys]["action"]=daction.replace("deny","Deny")


# dictprinter(celldict_fmtd)




print("==========================================================================")
print("Cleaning the lists ")
print("==========================================================================")

#create a function for below

# def list_cleaner(a_list):
# iplist=list_cleaner(iplist)
iplist = list(filter(None, iplist))
iplist = list(filter(bool, iplist))
iplist = list(filter(len, iplist))
# iplistcnr=list_cleaner(iplistcnr)
iplistcnr = list(filter(None, iplistcnr))
iplistcnr = list(filter(bool, iplistcnr))
iplistcnr = list(filter(len, iplistcnr))
# sectionlist=list_cleaner(sectionlist)
sectionlist = list(filter(None, sectionlist))
sectionlist = list(filter(bool, sectionlist))
sectionlist = list(filter(len, sectionlist))
# sectionlistcnr=list_cleaner(sectionlistcnr)
sectionlistcnr = list(filter(None, sectionlistcnr))
sectionlistcnr = list(filter(bool, sectionlistcnr))
sectionlistcnr = list(filter(len, sectionlistcnr))


# fqdn_dns_tbcr_list=list_cleaner(fqdn_dns_tbcr_list)
fqdn_dns_tbcr_list = list(filter(None, fqdn_dns_tbcr_list))
fqdn_dns_tbcr_list = list(filter(bool, fqdn_dns_tbcr_list))
fqdn_dns_tbcr_list = list(filter(len, fqdn_dns_tbcr_list))

# fqdn_dns_tbcr_listcnr=list_cleaner(fqdn_dns_tbcr_listcnr)
fqdn_dns_tbcr_listcnr = list(filter(None, fqdn_dns_tbcr_list_cnr))
fqdn_dns_tbcr_listcnr = list(filter(bool, fqdn_dns_tbcr_list_cnr))
fqdn_dns_tbcr_listcnr = list(filter(len, fqdn_dns_tbcr_list_cnr))


# fqdn_host_tbcr_list=list_cleaner(fqdn_host_tbcr_list)
fqdn_host_tbcr_list = list(filter(None, fqdn_host_tbcr_list))
fqdn_host_tbcr_list = list(filter(bool, fqdn_host_tbcr_list))
fqdn_host_tbcr_list = list(filter(len, fqdn_host_tbcr_list))

# fqdn_host_tbcr_listcnr=list_cleaner(fqdn_host_tbcr_listcnr)
fqdn_host_tbcr_listcnr = list(filter(None, fqdn_host_tbcr_list_cnr))
fqdn_host_tbcr_listcnr = list(filter(bool, fqdn_host_tbcr_list_cnr))
fqdn_host_tbcr_listcnr = list(filter(len, fqdn_host_tbcr_list_cnr))


# fqdn_net_tbcr_list=list_cleaner(fqdn_net_tbcr_list)
fqdn_net_tbcr_list = list(filter(None, fqdn_net_tbcr_list))
fqdn_net_tbcr_list = list(filter(bool, fqdn_net_tbcr_list))
fqdn_net_tbcr_list = list(filter(len, fqdn_net_tbcr_list))


# fqdn_net_tbcr_listcnr=list_cleaner(fqdn_net_tbcr_listcnr)
fqdn_net_tbcr_listcnr = list(filter(None, fqdn_net_tbcr_list_cnr))
fqdn_net_tbcr_listcnr = list(filter(bool, fqdn_net_tbcr_list_cnr))
fqdn_net_tbcr_listcnr = list(filter(len, fqdn_net_tbcr_list_cnr))

# fqdnlist=list_cleaner(fqdnlist)
fqdnlist = list(filter(None, fqdnlist))
fqdnlist = list(filter(bool, fqdnlist))
fqdnlist = list(filter(len, fqdnlist))

# fqdnlistcnr=list_cleaner(fqdnlistcnr)
fqdnlistcnr = list(filter(None, fqdnlistcnr))
fqdnlistcnr = list(filter(bool, fqdnlistcnr))
fqdnlistcnr = list(filter(len, fqdnlistcnr))

# netlist=list_cleaner(netlist)
netlist = list(filter(None, netlist))
netlist = list(filter(bool, netlist))
netlist = list(filter(len, netlist))

# netlistcnr=list_cleaner(netlistcnr)
netlistcnr = list(filter(None, netlistcnr))
netlistcnr = list(filter(bool, netlistcnr))
netlistcnr = list(filter(len, netlistcnr))

# portlist=list_cleaner(portlist)
portlist = list(filter(None, portlist))
portlist = list(filter(bool, portlist))
portlist = list(filter(len, portlist))

# portlistcnr=list_cleaner(portlistcnr)
portlistcnr = list(filter(None, portlistcnr))
portlistcnr = list(filter(bool, portlistcnr))
portlistcnr = list(filter(len, portlistcnr))

# actionlistcnr=list_cleaner(actionlistcnr)
actionlistcnr = list(filter(None, actionlistcnr))
actionlistcnr = list(filter(bool, actionlistcnr))
actionlistcnr = list(filter(len, actionlistcnr))

# itemlist=list_cleaner(itemlist)
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

fqdn_dns_tbcr_list_flat = []
for items in fqdn_dns_tbcr_list:
  for values in items:
    fqdn_dns_tbcr_list_flat.append(values)

fqdn_host_tbcr_list_flat = []
for items in fqdn_host_tbcr_list:
  for values in items:
    fqdn_host_tbcr_list_flat.append(values)

fqdn_net_tbcr_list_flat = []
for items in fqdn_net_tbcr_list:
  for values in items:
    fqdn_net_tbcr_list_flat.append(values)


fqdnlist_flat = []
for items in fqdnlist:
  for values in items:
    fqdnlist_flat.append(values)


sectionlist_flat = []
for items in sectionlist:
  for values in items:
    sectionlist_flat.append(values)

# #progress_bar_printer()

print("==========================================================================")
print("Removing Duplicates ")
print("==========================================================================")

# print("----------------------------------- IP Addresses ---------------------------------------")
iplist_nondup=list(dict.fromkeys(iplist_flat))
iplistcnr_nondup=list(dict.fromkeys(iplistcnr))


# print("----------------------------------- Networks ---------------------------------------")
netlist_nondup=list(dict.fromkeys(netlist_flat))
netlistcnr_nondup=list(dict.fromkeys(netlistcnr))



# print("----------------------------------- Ports ---------------------------------------")
portlist_nondup=list(dict.fromkeys(portlist_flat))
portlistcnr_nondup=list(dict.fromkeys(portlistcnr))


# print("----------------------------------- fqdns_new_dns ---------------------------------------")
fqdn_dns_tbcr_list_nondup=list(dict.fromkeys(fqdn_dns_tbcr_list_flat))
# fqdn_dns_tbcr_list_cnr_nondup=list(dict.fromkeys(fqdn_dns_tbcr_list_cnr_flat))


# print("----------------------------------- fqdns_new_host ---------------------------------------")
fqdn_host_tbcr_list_nondup=list(dict.fromkeys(fqdn_host_tbcr_list_flat))
# fqdn_host_tbcr_list_cnr_nondup=list(dict.fromkeys(fqdn_host_tbcr_list_cnr_flat))

# print("----------------------------------- fqdns_new_host ---------------------------------------")
fqdn_net_tbcr_list_nondup=list(dict.fromkeys(fqdn_net_tbcr_list_flat))
# fqdn_host_tbcr_list_cnr_nondup=list(dict.fromkeys(fqdn_host_tbcr_list_cnr_flat))


# print("----------------------------------- fqdns ---------------------------------------")
fqdnlist_nondup=list(dict.fromkeys(fqdnlist_flat))
fqdnlistcnr_nondup=list(dict.fromkeys(fqdnlistcnr))

# print("----------------------------------- Hosts -- ---------------------------------------")
sectionlist_nondup=list(dict.fromkeys(sectionlist_flat))
sectionlistcnr_nondup=list(dict.fromkeys(sectionlistcnr))

print("==========================================================================")
print("Comparing the requested host objects against the existing objects ")
print("Create list of objects to be created and associated CLI script ")
print("==========================================================================")

print("\n")
print("======================")
print("iplist_nondup is >>>")
print("======================")

listprinter(iplist_nondup)

if not iplist_nondup:
    print("Empty ")

print("\n")
print("==============================")
print("fqdn_dns_tbcr_list_nondup is >>>")
print("==============================")

listprinter(fqdn_dns_tbcr_list_nondup)

if not fqdn_dns_tbcr_list_nondup:
    print("Empty ")

print("\n")
print("==============================")
print("fqdn_host_tbcr_list_nondup is >>>")
print("==============================")

listprinter(fqdn_host_tbcr_list_nondup)

if not fqdn_host_tbcr_list_nondup:
    print("Empty ")

print("\n")

print("==============================")
print("fqdn_net_tbcr_list_nondup is >>>")
print("==============================")

listprinter(fqdn_net_tbcr_list_nondup)

if not fqdn_net_tbcr_list_nondup:
    print("Empty ")

print("\n")
print("==============================")
print("fqdnlist_nondup is >>>")
print("==============================")

listprinter(fqdnlist_nondup)

if not fqdnlist_nondup:
    print("Empty ")

# print("iplistcnr_nondup is")
print("\n")
print("==============================")
# listprinter(iplistcnr_nondup)
print("netlist_nondup is >>> ")
print("==============================")
# print("================")
listprinter(netlist_nondup)

if not netlist_nondup:
    print("Empty ")

# print("netlist with cnr is")
print("\n")
# listprinter(netlistcnr_nondup)
print("==============================")
print("portlist_nondup is >>> ")
print("==============================")
# print("=====================")
# listprinter(portlistcnr_nondup)
listprinter(portlist_nondup)

if not portlist_nondup:
    print("Empty ")

print("\n")
print("=====================")
print("actionlistcnr is >>> ")
print("=====================")
# print("================")
listprinter(actionlistcnr)

if not actionlistcnr:
    print("Empty ")

print("\n")
# print("dictionary is ..")
# print(celldict_unfmtd)
#dictprinter(celldict_unfmtd)
# print(f"each matching item is")


########################################################################################################
###  Section below finds if required host objects are not in the local database (objectsfile_string) ###
###  and if they are not they are simply appended to the lists.                                      ###                                         
########################################################################################################

hoststbcr=[] # hosts to be created
hostsaddcmds=[] #hosts add commands batch

object_list=[]
local_host_object_list=[]

for ips in iplist_nondup:
    #print(f"printing IPs =  {ips}")
    ips_with_commas=","+ips+"," #improve this section with a list of prefixes and loop through them to append.
    hostname="h-"+ips
    hostaddcmd='add host name '+hostname+" ip-address "+ips+' color "forest green" ignore-warnings true'    
   
  
    if ips_with_commas not in objectsfile_string:
        # print(f"\n{ips} , requested host object doesnt exist it will be created")
        hoststbcr.append(hostname)
        hostsaddcmds.append(hostaddcmd)
        continue
    
    # regex_ip_pattern="r'(?i)g.(?i)h."+ips+"\\b.*,'"
    # regex_ip_pattern2="(?i)g.(?i)h."+ips+"\\b.*,"
    # print(regex_ip_pattern)
    #(?i)g.(?i)h.1.1.1.1\b.*,
    
    h_ip_exists="n/a"
    g_ip_exists="n/a"
    
        
    ########################################################################################################
    ###  Section below gets a list of hosts which need creating but already exist in the local database  ###
    ########################################################################################################

    for eachline in objectsfile_list:
        # if "1.1.1.1" in eachline:
            # print (eachline)
        if ips_with_commas in eachline:
            # print(f"=========================================================================")
            # print(f"\n{ips_with_commas} found in following line \n{eachline}")
            object_list.append(eachline.split(",")[0])
            # print(f"list of host objects already configured are \n{object_list}")
            if (re.search(r"(?i)^h[^r ]",eachline)):
            # print(f"==========================================================================")
                local_host_object_list.append(eachline.split(",")[0]+","+eachline.split(",")[1])
                # local_network_object_list.append(eachline.split(",")[1])


    #####################################################################################################
    ###   Section below establishes if the h-x.x.x.x 's local version is missing. And If it is        ###
    ###   it will go ahead and append the hostname to the list to be created and also update          ###
    ###   the list of cli commands. It                                                                ###
    #####################################################################################################
    
    for eachhost in object_list:
        h_ip_exists=""
        g_ip_exists=""
        print(f"eachhost:{eachhost}")
        if (re.search(r"(?i)^h[^r ]",eachhost)):
            print(f"local object exists, {eachhost}")               
            h_ip_exists="true"                
        if (re.search(r"(?i)^g[^r ]",eachhost)):
            print(f"global object exists, {eachhost}")
            g_ip_exists="true"
    print(f"g_ip_exists:{g_ip_exists}, h_ip_exists:{h_ip_exists}")

    if (g_ip_exists == "true" and h_ip_exists != "true"):
        print(f"{ips} , requested IP has global version but needs a local version ****")
        hoststbcr.append(hostname)
        hostsaddcmds.append(hostaddcmd)

print("==========================================================")
print("Required host objects currently present in local DB are ..")
print("==========================================================")
listprinter(local_host_object_list)
print("==========================================================")
print("\n\n")
print("==========================================================================")
print("Printing the CLI to add hosts && add them to a text file ")
print("==========================================================================")

#listprinter(hostsaddcmds)

with open('thescript.txt', 'w') as script:
    script.write(f"\n### ---------------------------  ###")
    script.write(f"\n### CLI to add new host objects  ###")
    script.write(f"\n### ---------------------------  ###\n\n")
    for each in hostsaddcmds:
        script.write(f'{each}\n')

non_existing_ips=[]

print("==========================================================================")
print("Comparing the requested network objects against the existing objects ")
print("Create list of objects to be created and associated CLI script ")
print("==========================================================================")


###############################################################################
###  Section below finds if required network objects are not in the local   ###
###  database (objectsfile_string)                                          ###
###  and if they are not they are simply appended to the lists.             ###                                         
###############################################################################

netstbcr=[]  # nets to be created
netsaddcmds=[] #nets add commands batch
local_network_object_list=[]

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
    netaddcmd="add network name "+netname+" subnet "+broken_net[0]+" mask-length "+broken_net[1]+' color "forest green" ignore-warnings true'    
    #print(f"COMMAND:>  {netaddcmd}")
    
    
    if comma_network_comma_mask_comma not in objectsfile_string:
        # print(f"{net} , requested network object doesnt exist ###################")
        netstbcr.append(netname)
        netsaddcmds.append(netaddcmd)
        #print(netsaddcmds)
        #print("test")
        object_list=[]

    ########################################################################################################
    ###  Section below gets a list of nets which need creating but already exist in the local database  ###
    ########################################################################################################

    for eachline in objectsfile_list:
        # if "1.1.1.1" in eachline:
            # print (eachline)
        if comma_network_comma_mask_comma in eachline:
            # print(f"=========================================================================")
            # print(f"\n{ips_with_commas} found in following line \n{eachline}")
            # object_list.append(eachline.split(",")[0])
            # print(f"list of net objects already configured are \n{object_list}")
            if (re.search(r"(?i)^n[^r ]",eachline)):
            # print(f"==========================================================================")
                local_network_object_list.append(eachline.split(",")[0]+","+eachline.split(",")[1])
                # local_network_object_list.append(eachline.split(",")[1])
                
    #####################################################################################################
    ###   Section below establishes if the n-x.x.x.x 's local version is missing. And If it is        ###
    ###   it will go ahead and append the network object name to the list to be created and also      ###
    ###   update the of the CLI commands. Search will be m                                                             ###
    #####################################################################################################
   
    n_net_exists="n/a"
    g_net_exists="n/a"
    for eachline in objectsfile_list:
        if comma_network_comma_mask_comma in eachline:
            # print(f"\n{comma_network_comma_mask_comma} found in following line \n{eachline}")
            object_list.append(eachline.split(",")[0])
            # print(f"list of host objects already configured are \n{object_list}")

            for eachnet in object_list:
                if (re.search(r"(?i)^n[^r ]",eachnet)):
                    # print(f"local object exists, {eachnet}")               
                    n_net_exists="true"
                if (re.search(r"(?i)^g[^r ]",eachnet)):
                    # print(f"global object exists, {eachnet}")               
                    g_net_exists="true"                 
            
            # print(f"n={n_net_exists},g={g_net_exists}")

        if (g_net_exists == "true" and n_net_exists != "true"):
            # print(f"{ips} , requested IP has global version but needs a local version ****")
            # hoststbcr.append(netname)
            # hostsaddcmds.append(netaddcmd)
            netstbcr.append(netname)
            netsaddcmds.append(netaddcmd)


print("=============================================================")
print("Required network objects currently present in local DB are ..")
print("=============================================================")
listprinter(local_network_object_list)
print("=============================================================")

print("==========================================================================")
print("Print the CLI to add nets && add them to a text file ")
print("==========================================================================")

with open('thescript.txt', 'a+') as script:
    script.write(f"\n### ------------------------------  ###")
    script.write(f"\n### CLI to add new network objects  ###")
    script.write(f"\n### ------------------------------  ###\n\n")
    for each in netsaddcmds:
        script.write(f'{each}\n')


print("==========================================================================")
print("Loading the list of ports ")
print("==========================================================================")

non_existing_ips=[]

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
    # print(f"port:{port}#################")
    if "Any" in port:
        continue
    port_prot=re.search("^[a-zA-Z]+", port).group()
    port_num=re.search("\d+-\d+|\d+", port).group()
    service=port_prot.upper()+port_num
    # print(f"port_num={port_num}")
    # print(f"service={service}")
    built_in_service="none"
    if service in port_dict:
        built_in_service=port_dict[service]
        # print(f"{built_in_service}#########")
    # print(f"service:{service}###############")
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
    portaddcmd="add service-"+port_prot.lower()+" name "+port_prot.upper()+port_num+" port "+port_num+' color "forest green" ignore-warnings true'    
    # print(f"##################portaddcmd:{portaddcmd}")
    #print(f"COMMAND:>  {portaddcmd}")

#print(len(objectsfile_list))
# listprinter(objectsfile_list)
    # if comma_port_comma not in objectsfile_string:
        #print(f"{port} , requested port object doesnt exist")
    # portstbcr.append(service)
    # portsaddcmds.append(portaddcmd)
        #print(portsaddcmds)

    if comma_port_comma not in objectsfile_string:
        #print(f"{port} , requested port object doesnt exist")
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
                # print(f"gport_exists:{gport_exists}, comma_port_comma:{comma_port_comma}")
                #print(f"{port} , requested port object exists as  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG g{gport_exists}")
            #     # print("gport exists")
            else:
                #print(f"port {comma_port_comma} exists in following line \n{lines}")
                #print(f"{port} , requested port object exists as  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> n{port_exists}")
                # print(f"port_exists:{port_exists}, comma_port_comma:{comma_port_comma}")
                nportctr+=1
                port_exists="yes"
                # print("port exists")
            
            #print (f"values of g and n {gport_exists},{port_exists}")

      

            #if(gport_exists=="yes" and port_exists!="yes"):
            #print(f"port count is g{gportctr} and n{nportctr}")
        #print(linectr)

        service_object_to_search=service+","+port_num

        if(linectr==(len(objectsfile_list))):
            #print (f"for {service} the ncounter={nportctr} and gcounter={gportctr}")
            if(gportctr!=0 and nportctr==0):
            #     print("no")
                portstbcr.append(service)
                portsaddcmds.append(portaddcmd)
 
            if(nportctr>0 and built_in_service=="none" and service_object_to_search not in objectsfile_string):
                portstbcr.append(service)
                portsaddcmds.append(portaddcmd)


            # if(nportctr>0):
            #     # print(f"portaddcmd:{portaddcmd}")
            #     # print(f"service:{service}")
            #     # print(f"port:{port}")
            #     service_object_to_search=service+","+port_num
            #     if(service_object_to_search not in objectsfile_string):
            #         # print(f"added")
            #         portstbcr.append(service)
            #         portsaddcmds.append(portaddcmd)

print("==========================================================================")
print("Print the CLI to add ports && add them to a text file ")
print("==========================================================================")

with open('thescript.txt', 'a+') as script:
    script.write(f"\n### ------------------------------  ###")
    script.write(f"\n### CLI to add new service objects  ###")
    script.write(f"\n### ------------------------------  ###\n\n")
    for each in portsaddcmds:
        script.write(f'{each}\n')

print("==========================================================================")
print("Existing Local object insertion into the formatted cell dict ")
print("==========================================================================")

#add access-rule layer "utm-ukGOR_In_Line Security" name "Process Vlans" source.1 h-169.4.98.13 source.2 h-169.4.98.11 source.3 h-169.4.98.15 destination.1 h-10.0.14.190 destination.2 h-10.0.15.71 destination.3 h-169.4.10.2 service.1 TCP135 action "Accept" position 11 track.type log comments "CR12345 - AK - 07/12/2022"


for keys,values in celldict_fmtd.items():
    
    if keys==999:
        continue
    # total_items_in_source_list=len(celldict_fmtd["srcs"])    
    # print(f"key is {keys}")
    counter=1
    # source_list_for_rule=[]
    #now#
    for eachitem in celldict_fmtd[keys]["srcs"]:   ### change here for network replacements ####
        # print(f"item is {eachitem}")
        if "h-" in eachitem:
            # print(f"ip items are {eachitem}")
            itemcounter=1
            for local_host in local_host_object_list:
                # print(f"local_host={local_host}")
                if itemcounter==2:
                    continue
                if (local_host.split(",")[1]) in eachitem:
                    # print(f'local_host.split(",")"={local_host.split(",")[1]}') 
                    # print(f"{eachitem} needs replacing with {local_host.split(',')[0]}")
                    local_host_object=local_host.split(',')[0]
                    print(f"{eachitem} needs replacing with {local_host_object}")
                    if local_host_object==eachitem:
                        # print(f"no replacement needed, same objects")
                        continue
                    index_of_object_in_dict_list=celldict_fmtd[keys]['srcs'].index(eachitem)
                    # print(f"location of {eachitem} in list is {index_of_object_in_dict_list}")
                    celldict_fmtd[keys]['srcs'][index_of_object_in_dict_list]=local_host_object
                    # print(f"location of {eachitem} in list is {celldict_fmtd[keys]['srcs'].index(eachitem)}")
                    itemcounter+=1
    
    
    for eachitem in celldict_fmtd[keys]["dsts"]:
        # print(f"item is {eachitem}")
        if "h-" in eachitem:
            # print(f"ip items are {eachitem}")
            itemcounter=1
            for local_host in local_host_object_list:
                # print(f"local_host={local_host}")
                if itemcounter==2:
                    continue
                if (local_host.split(",")[1]) in eachitem:
                    # print(f'local_host.split(",")"={local_host.split(",")[1]}') 
                    # print(f"{eachitem} needs replacing with {local_host.split(',')[0]}")
                    local_host_object=local_host.split(',')[0]
                    print(f"{eachitem} needs replacing with {local_host_object}")
                    if local_host_object==eachitem:
                        # print(f"no replacement needed, same objects")
                        continue
                    index_of_object_in_dict_list=celldict_fmtd[keys]['dsts'].index(eachitem)
                    # print(f"location of {eachitem} in list is {index_of_object_in_dict_list}")
                    celldict_fmtd[keys]['dsts'][index_of_object_in_dict_list]=local_host_object
                    # print(f"location of {eachitem} in list is {celldict_fmtd[keys]['dsts'].index(eachitem)}")
                    itemcounter+=1          
    
    for eachitem in celldict_fmtd[keys]["srcs"]:   ### change here for network replacements ####
        # print(f"item is {eachitem}")
        if "n-" in eachitem:
            # print(f"network items in sources are {eachitem}")
            itemcounter=1
            for local_net in local_network_object_list:
                # print(f"local_net={local_net}")
                if itemcounter==2:
                    continue
                if (local_net.split(",")[1]) in eachitem:
                    # print(f'local_net.split(",")"={local_net.split(",")[1]}') 
                    # print(f"{eachitem} needs replacing with {local_net.split(',')[0]}")
                    local_net_object=local_net.split(',')[0]
                    print(f"{eachitem} needs replacing with {local_net_object}")
                    if local_net_object==eachitem:
                        # print(f"no replacement needed, same objects")
                        continue
                    index_of_object_in_dict_list=celldict_fmtd[keys]['srcs'].index(eachitem)
                    # print(f"location of {eachitem} in list is {index_of_object_in_dict_list}")
                    celldict_fmtd[keys]['srcs'][index_of_object_in_dict_list]=local_net_object
                    # print(f"location of {eachitem} in list is {celldict_fmtd[keys]['srcs'].index(eachitem)}")
                    itemcounter+=1
    counter=1
    # source_list_for_rule=[]

    for eachitem in celldict_fmtd[keys]["dsts"]:
        # print(f"item is {eachitem}")
        if "n-" in eachitem:
            # print(f"network items in destinations are {eachitem}")
            itemcounter=1
            for local_net in local_network_object_list:
                # print(f"local_net={local_net}")
                if itemcounter==2:
                    continue
                if (local_net.split(",")[1]) in eachitem:
                    # print(f'local_net.split(",")"={local_net.split(",")[1]}') 
                    # print(f"{eachitem} needs replacing with {local_net.split(',')[0]}")
                    local_net_object=local_net.split(',')[0]
                    print(f"{eachitem} needs replacing with {local_net_object}")
                    if local_net_object==eachitem:
                        # print(f"no replacement needed, same objects")
                        continue
                    index_of_object_in_dict_list=celldict_fmtd[keys]['dsts'].index(eachitem)
                    # print(f"location of {eachitem} in list is {index_of_object_in_dict_list}")
                    celldict_fmtd[keys]['dsts'][index_of_object_in_dict_list]=local_net_object
                    # print(f"location of {eachitem} in list is {celldict_fmtd[keys]['dsts'].index(eachitem)}")
                    itemcounter+=1      

                
print(f"\n")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>> ")
print(f"  <<<<<<< Your formatted  Cell dictionary >>>>>>>>>> ")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>> ")
print(f"\n")
dictprinter2(celldict_fmtd)

        # source_number="source."+str(counter)
        # source_number=source_number+" "+eachitem
        # source_list_for_rule.append(source_number)
        # counter=counter+1
    # source_list_string=""    
    # for eachitem in source_list_for_rule:
        # source_list_string=source_list_string+eachitem+" "
    # 
    # print(source_list_string)






def row_browser_list_returner(frow,lrow,cols_range):
    
    list_of_items=[]
    for col in (cols_range):
        for row in range (frow,lrow+1):
            cell=str(col)+str(row)
        #  print(cell)
            cvalue=ws.range(cell).value
            ccolor=ws.range(cell).color
        #  print(f"cvalue:{cvalue}---ccolor:{ccolor}
       
            if(cvalue != None and cvalue.find("any") == -1):
                # print(f"cvalue:\n{cvalue}")
                # print(f"cvalueType:\n{type(cvalue)}")
                list_of_items.append(cvalue)        
        
    return list_of_items


def row_browser_dict_returner(frow,lrow,cols_range):
    
    # list_of_items=[]
    dict_of_items={}
    datatype=""
    cell_and_purpose=""
    cell_and_type=""
    cell_type_string=""
    
    # for col in (cols_range):
    for row in range (frow,lrow+1):
        dict_of_items[row]={}
        # dict_of_items={row:{"src":[],"dst":[],"ports":[],"action":""}}

        # print(f"#######value of dictionary at the beginning of col loop")
        # print(f"{dict_of_items}")
        # list_of_items=[]
        cvalue_list=[]
        # for row in range (frow,lrow+1):
        for col in (cols_range):
            datatype=""
            
            cvalue_list=[]
            cell=str(col)+str(row)
            if col=="a":
                cell_and_purpose=cell+".src"
                cell_type_string=cell+".type"
            if col=="b":
                cell_and_purpose=cell+".dst"
                cell_type_string=cell+".type"
            if col=="c":
                cell_and_purpose=cell+".ports"
                cell_type_string=cell+".type"
            if col=="d":
                cell_and_purpose=cell+".action"    
                cell_type_string=cell+".type"       
            # print(cell)
            cvalue=ws.range(cell).value
            ccolor=ws.range(cell).color
        #  print(f"cvalue:{cvalue}---ccolor:{ccolor}")

            if(cvalue != None and cvalue.find("any") == -1):
                # print(f"cvalue:\n{cvalue}")
                # print(f"cvalueType:\n{type(cvalue)}")
                if(re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])", cvalue)) and (re.search("(?i)ngp.*", cvalue)) and (re.search("/", cvalue)):
                    datatype="ngp_nets"
                elif(re.search("(?i)(fqdn:h|fqdn:n).*", cvalue)) and (re.search("(?i)ngp.*", cvalue)):
                    datatype="ngp_fqdn"
                elif(re.search("(?i)(fqdn).*", cvalue)) and (re.search("(?i)pgp.*", cvalue)):
                    datatype="pgp_fqdn"
                elif(re.search("(?i)fqdn.*", cvalue)) and (re.search("(?i)port", cvalue)):
                    datatype="pgp_fqdn"
                elif(re.search("(?i)tcp.\d+|udp.\d+|ip.\d+|icmp.\d+|tcp\d+|udp\d+|ip\d+|icmp\d+", cvalue) and (re.search("(?i)pgp.*", cvalue))):
                    datatype="pgp_ports"
                elif(re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])", cvalue)) and (re.search("(?i)ngp.*", cvalue)):
                    datatype="ngp_ips"
                elif(re.search("(?i)(fqdn).*", cvalue)):
                    datatype="fqdn"
                elif(re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])", cvalue)) and (re.search("/", cvalue)):
                    datatype="nets"                 
                elif(re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])", cvalue)) and (re.search("n-", cvalue)):
                    datatype="n_nets"                  
                elif(re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])", cvalue)) and (re.search("(?i)h-.*", cvalue)):
                    datatype="h_ips" 
                #anything not matched by above will fall down to below 
                elif(re.search("(?i)tcp.\d+|udp.\d+|ip.\d+|icmp.\d+|tcp\d+|udp\d+|ip\d+|icmp\d+", cvalue)):
                    datatype="ports"
                # elif(re.search("(?i)(fqdn).*", cvalue)):
                #     datatype="fqdn"
                elif(re.search("(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])", cvalue)):
                    datatype="ips"   
                else:
                    datatype="unknown"                   

                cvalue=cvalue.strip()
                if "\n" in cvalue:
                    cvalue_list=cvalue.split("\n")
                    # continue
                elif "\n" not in cvalue:
                    cvalue_list.append(cvalue)
                    # continue
                else:
                    cvalue_list.append(cvalue)

                # print(f"value of cell on each row iteration")   
                # print(f"{cell}")  
                # print(f"value of cvalue on each row iteration")   
                # print(f"{cvalue}")  
                # print(cvalue_list)
                # print(f"cell:{cell}")
                # print(f"cvalue_list:{cvalue_list}")
                # dict_of_items[cell]=cvalue_list 
                
                # dict_of_items[row][cell]=cvalue_list 
                dict_of_items[row][cell_and_purpose]=cvalue_list 
                dict_of_items[row][cell_type_string]=datatype 
                # print(f"dict_of_items_in_loop\n{dict_of_items}")
            
            else:
            #    print("Nothing in the cell")
            #    print(f"cell:{cell}")
            #    print(f"cvalue_list:{cvalue_list}")
               dict_of_items[row][cell_and_purpose]="none"
               dict_of_items[row][cell_type_string]="none"
            #    print(f"dict_of_items_in_loop\n{dict_of_items}")

        # print(f"cell:{cell}############ each cell")
        # print(f"list_of_items:{cvalue_list}")
        # dict_of_items[cell]=cvalue_list   
        # print(f"value of dictionary on each column iteration")   
        # print(f"{dict_of_items}")
    return dict_of_items

# new_list=row_browser_list_returner(gpsttrow,gpendrow,"b")
# listprinter(new_list)

# new_list=row_browser_list_returner(gpsttrow,gpendrow,cols)
# print(f"#################### list final value #######################")
# listprinter(new_list)

groups_dict_unfmtd=row_browser_dict_returner(gpsttrow,gpendrow,cols)
groups_dict_fmtd=row_browser_dict_returner(gpsttrow,gpendrow,cols)

print(f"\n")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>>>> ")
print(f"  <<<<<<< Your Un-formatted Group dictionary >>>>>>>>>> ")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>>>> ")
print(f"\n")

dictprinter2(groups_dict_unfmtd)

print("==========================================================================")
print("List formatter ")
print("==========================================================================")

def list_formatter(the_list,list_type):

    if list_type=="pgp_fqdn" or list_type=="ngp_fqdn":
        list_len=len(the_list)
        formatted_string=""
        for i in range (0,list_len):
            if "pgp" not in the_list[i] or "ngp" not in the_list[i]:
                formatted_string=re.sub(r"(?i)fqdn:","",the_list[i])
                # formatted_string=the_list[i].replace("fqdn:","")
                # formatted_string=the_list[i].replace("FQDN:","")
                the_list[i]=formatted_string
    
    # BUG.X the section below should replace the host object with the existing object.

    if list_type=="ngp_ips":
        list_len=len(the_list)
        formatted_string=""
        for i in range (0,list_len):
            # if "ngp" not in the_list[i]:
            #     formatted_string="h-"+the_list[i]
            #     the_list[i]=formatted_string
            if "ngp" not in the_list[i]:
                formatted_string = the_list[i]
                # print(f"formatted string before formatting = {formatted_string}")
                host_string_to_search_in_objects_file = "," + formatted_string + ","
                # print(f"host_string_to_search = {host_string_to_search_in_objects_file}")
                # print(f"host string to search = >> {host_string_to_search_in_objects_file} << ")
                # print(f"{the_list[i]}")
                # print(f"{formatted_string}")
                # if host_string_to_search_in_objects_file in objectsfile_string:
                #     for eachline in objectsfile_list:
                #         if eachline.startswith("g") or eachline.startswith("G"):
                #             continue
                #         if host_string_to_search_in_objects_file in eachline:
                #             existing_host_name = eachline.split(",")
                #             existing_host_name = existing_host_name[0]
                #             # print(f"existing host found = {existing_host_name}")
                #             formatted_string=existing_host_name

                lo_counter=0

                if host_string_to_search_in_objects_file in objectsfile_string:
                    for eachline in objectsfile_list:
                        if host_string_to_search_in_objects_file in eachline:
                            if eachline.startswith("g") or eachline.startswith("G"):
                                print("global object found")
                                continue
                            existing_host_name = eachline.split(",")
                            existing_host_name = existing_host_name[0]
                            print(f"existing host object name = {existing_host_name}")
                            formatted_string=existing_host_name
                            lo_counter+=1


                # if net_string_to_search_in_objects_file in objectsfile_string:
                #     for eachline in objectsfile_list:
                #         if net_string_to_search_in_objects_file in eachline:
                #             if eachline.startswith("g") or eachline.startswith("G"):
                #                 continue
                #             existing_network_name = eachline.split(",")
                #             existing_network_name = existing_network_name[0]
                #             print(f"existing network name = {existing_network_name}")
                #             formatted_string=existing_network_name                
                
                
                if lo_counter == 0:   
                    print(f"else initiated")
                    formatted_string = "h-"+the_list[i]
                               
                # print(f"formatted string after formatting = {formatted_string}") 
                the_list[i]=formatted_string


    if list_type=="ngp_nets":
        list_len=len(the_list)
        formatted_string=""
        net_string_to_search_in_objects_file = ""
        for i in range (0,list_len):
            if "ngp" not in the_list[i]:
                formatted_string=the_list[i].split("/")
                net_string_to_search_in_objects_file = "," + formatted_string[0] + "," + maskdict[formatted_string[1]]
                print(f"net string to search = {net_string_to_search_in_objects_file}")
                # print(f"{the_list[i]}#######################")
                # print(f"{formatted_string}#######################")
                if net_string_to_search_in_objects_file in objectsfile_string:
                    for eachline in objectsfile_list:
                        if net_string_to_search_in_objects_file in eachline:
                            if eachline.startswith("g") or eachline.startswith("G"):
                                continue
                            existing_network_name = eachline.split(",")
                            existing_network_name = existing_network_name[0]
                            print(f"existing network name = {existing_network_name}")
                            formatted_string=existing_network_name
                else:   
                    formatted_string="n-"+formatted_string[0]+"-"+formatted_string[1]
                                
                the_list[i]=formatted_string

    if list_type=="pgp_ports":
        list_len=len(the_list)
        formatted_string=""
        for i in range (0,list_len):
            if "pgp" not in the_list[i]:
                formatted_string=the_list[i].upper()
                formatted_string=re.sub(r"(?i)tcp-|(?i)tcp_","TCP",formatted_string)
                formatted_string=re.sub(r"(?i)udp-|(?i)udp_","UDP",formatted_string)
                # formatted_string=formatted_string.replace("TCP-","")
                # formatted_string=formatted_string.replace("_","")
                # print(f"formatted string for port = {formatted_string}")
                if formatted_string in port_dict:
                    formatted_string=port_dict[formatted_string]
                # formatted_string="n-"+formatted_string[0]+"-"+formatted_string[1]
                the_list[i]=formatted_string   
    
    return the_list

print("==========================================================================")
print("dictionary formatter for the groups ")
print("==========================================================================")

def group_dict_formatter(the_dict): 
    #takes a dictionary as an input and returns a formatted dictionary.
    for l1keys,l1values in the_dict.items():
        # print(f"keys:{keys[]}###############")
        #print("!!!!!")  ## loop runs same number as the number of rows e.g. 2 rows , 2 times
        # print(l1keys)       
        srckeyl2string="a"+str(l1keys)+".src"
        typekeyl2srcstring="a"+str(l1keys)+".type"
        dstkeyl2string="b"+str(l1keys)+".dst"
        typekeyl2dststring="b"+str(l1keys)+".type"
        
        # print(srckeyl2string)
        # print(typekeyl2srcstring)
        # print(dstkeyl2string)
        # print(typekeyl2dststring)

        src_list_unfmtd=the_dict[l1keys][srckeyl2string]   
        dst_list_unfmtd=the_dict[l1keys][dstkeyl2string]   
        src_type=the_dict[l1keys][typekeyl2srcstring]
        dst_type=the_dict[l1keys][typekeyl2dststring] 
         
        # print(src_list_unfmtd)
        # print(dst_list_unfmtd)
        # print(src_type)
        # print(dst_type)

        # print(f"l2ks_row_dot_srcORdst={l2ks_row_dot_srcORdst}")
        # print(f"l2ks_row_dot_type={l2ks_row_dot_type}")

        if src_list_unfmtd != "none":

            # print(src_type)
            old_list=src_list_unfmtd
            # print(f"list before formatting\n{old_list}")
            new_list=list_formatter(src_list_unfmtd,src_type)
            # print(f"list after formatting\n{new_list}")

        if  dst_list_unfmtd !="none":
            
            # print(dst_type)
            old_list=dst_list_unfmtd
            # print(f"list before formatting\n{old_list}")
            new_list=list_formatter(dst_list_unfmtd,dst_type)
            # print(f"list after formatting\n{new_list}")


    # print(the_dict[l1ks_row][l2ks_row_dot_srcORdst])
    # print(the_dict[l1ks_row][l2ks_row_dot_type])
    return the_dict

groups_dict_fmtd=group_dict_formatter(groups_dict_unfmtd)

print(f"\n")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>>>> ")
print(f"  <<<<<<< Your formatted Groups dictionary >>>>>>>>>> ")
print(f"  <<<<<<<|||||||||||||||||||||||||||||||||>>>>>>>>>>>> ")
print(f"\n")

dictprinter2(groups_dict_fmtd)


print("==========================================================================")
print("New FQDN-DNS Objects Generator")
print("==========================================================================")

# ndnso_ip=""
ndnso_name=""
ndnso_add_cmds=[]

for eachdnsline in  fqdn_dns_tbcr_list_nondup:
    # ndnso_ip=eachhostline.split(",")[0]
    ndnso_name=eachdnsline.replace("ndns:","")
    ndnso_name=ndnso_name.lower()
    if ndnso_name in objectsfile_string.lower(): #these two lines ensure existing objects dont get created again.
        continue
    #print(f"new host ip is {ndnso_ip} and new host name is {ndnso_name}")
    ndnso_add_cmd = 'add dns-domain name '+ndnso_name+' is-sub-domain False color "forest green" ignore-warnings true'
    # print(f"{ndnso_add_cmd}")
    ndnso_add_cmds.append(ndnso_add_cmd)

listprinter(ndnso_add_cmds)



print("==========================================================================")
print("New HOST Objects, with custom names - FQDN Generator")
print("==========================================================================")

nho_ip=""
nho_name=""
nho_add_cmds=[]

for eachhostline in  fqdn_host_tbcr_list_nondup:
    nho_ip=eachhostline.split(",")[0]
    nho_name=eachhostline.split(",")[1]
    #print(f"new host ip is {nho_ip} and new host name is {nho_name}")
    nho_add_cmd = 'add host name '+nho_name+' ip-address '+nho_ip+' color "forest green" ignore-warnings true'
    # print(f"{nho_add_cmd}")
    nho_add_cmds.append(nho_add_cmd)

listprinter(nho_add_cmds)


print("==========================================================================")
print("New NET Objects, with custom names - FQDN Generator")
print("==========================================================================")

nno_net_and_mask=""
nno_net=""
nno_mask=""
nno_name=""
nno_add_cmds=[]

for eachnetline in  fqdn_net_tbcr_list_nondup:
    nno_net_and_mask=eachnetline.split(",")[0]
    nno_net=nno_net_and_mask.split("-")[0]
    nno_mask=nno_net_and_mask.split("-")[1]
    nno_name=eachnetline.split(",")[1]

    # print(f"network and mask is {nno_net_and_mask} , network is {nno_net} , mask is {nno_mask} , name is {nno_name}")
    nno_add_cmd = 'add network name '+nno_name+' subnet '+nno_net+' mask-length '+nno_mask+' color "forest green" ignore-warnings true'
    # print(f"{nno_add_cmd}")
    nno_add_cmds.append(nno_add_cmd)

listprinter(nno_add_cmds)


print("==========================================================================")
print("Group Generator")
print("==========================================================================")

def group_generator(the_formatted_dict):
    
    gp_add_cmds=[]
    for l1keys,l1values in the_formatted_dict.items():
    
        srckeyl2string="a"+str(l1keys)+".src"
        typekeyl2srcstring="a"+str(l1keys)+".type"
        dstkeyl2string="b"+str(l1keys)+".dst"
        typekeyl2dststring="b"+str(l1keys)+".type"
        
        src_list_fmtd=the_formatted_dict[l1keys][srckeyl2string]   
        dst_list_fmtd=the_formatted_dict[l1keys][dstkeyl2string]   
        
        # if (src_list_fmtd != "none" or dst_list_fmtd != "none"):
        #     print(src_list_fmtd)
        #     print(dst_list_fmtd)

        items_list=["src","dst"]
        list_of_lists=[src_list_fmtd,dst_list_fmtd]

        for eachlist in list_of_lists:
            
            # # print(type(eachlist))
            # list_type=type(eachlist)
            # print(list_type)
            if isinstance(eachlist, list):
                # print(eachlist)
                counter=0
                member_string=""
                for item in eachlist:
                    # print(item)
                    ## remove the pgp or ngp from the group name ##
                    if ("pgp"  in item or "ngp" in item):
                        # print("each item is ...")
                        # print(item)
                        eachlist[0]=eachlist[0].split(":")
                        eachlist[0]=eachlist[0][1]
                        eachlist[0]=eachlist[0].strip()
                        
                        # if "pgp" not in eachlist[0] or "ngp" not in eachlist[0]:
                        #     break # this ensure no unnecessary groups are generated.
                        
                        # print(eachlist[0])
                        # print(item)
                    
                    ## start at 1 and avoid 0 to miss the group name and start at a member ##
                    if (counter!=0):
                        # member_string=eachlist[0]
                        member_string=member_string+"members."+str(counter)+" "+item+" "

             
                    counter+=1
                
                
                if (re.search("(?i)( h-| n-).*", member_string)):
                    final_string="add group name"+" "+eachlist[0]+' color "forest green"'+" "+member_string+" ignore-warnings true"
                else:
                    final_string="add service-group name"+" "+eachlist[0]+' color "forest green"'+" "+member_string+" ignore-warnings true"

                # print("test=======")
                gp_add_cmds.append(final_string)
            # print(member_string)        

    return gp_add_cmds            

group_add_cmds=group_generator(groups_dict_fmtd)
# listprinter(group_add_cmds)

print("==========================================================================")
print("Rule Generator ")
print("==========================================================================")

#add access-rule layer "utm-ukGOR_In_Line Security" name "Process Vlans" source.1 h-169.4.98.13 source.2 h-169.4.98.11 source.3 h-169.4.98.15 destination.1 h-10.0.14.190 destination.2 h-10.0.15.71 destination.3 h-169.4.10.2 service.1 TCP135 action "Accept" position 11 track.type log comments "CR12345 - AK - 07/12/2022"

rule_add_cmds=[]
for keys,values in celldict_fmtd.items():
   
    if keys==999:
        continue
    # if not celldict_fmtd[keys]["action"] and not celldict_fmtd[keys]["srcs"] and celldict_fmtd[keys]["section"]=="none":
    if not celldict_fmtd[keys]["action"] and celldict_fmtd[keys]["section"]=="none":

        continue
    # if not celldict_fmtd[keys]["dsts"] and not celldict_fmtd[keys]["ports"]:
    #     continue
    # total_items_in_source_list=len(celldict_fmtd["srcs"])    
    # print(f"key is {keys}")
    counter=1
    source_list_for_rule=[]
    for eachitem in celldict_fmtd[keys]["srcs"]:
        # print(f"item is {eachitem}")
        source_number="source."+str(counter)
        source_number=source_number+" "+eachitem
        source_list_for_rule.append(source_number)
        counter=counter+1
    source_list_string=""    
    for eachitem in source_list_for_rule:
        source_list_string=source_list_string+eachitem+" "

    if celldict_fmtd[keys]["snegate"]=="yes":
        source_list_string='source-negate "True"'+" "+source_list_string    
    # print(source_list_string)

    counter=1
    destination_list_for_rule=[]
    for eachitem in celldict_fmtd[keys]["dsts"]:
        # print(f"item is {eachitem}")
        destination_number="destination."+str(counter)
        destination_number=destination_number+" "+eachitem
        destination_list_for_rule.append(destination_number)
        counter=counter+1
    destination_list_string=""    
    for eachitem in destination_list_for_rule:
        destination_list_string=destination_list_string+eachitem+" "    
    
    if celldict_fmtd[keys]["dnegate"]=="yes":
        destination_list_string='destination-negate "True"'+" "+destination_list_string
    # print(destination_list_string)

    counter=1
    port_list_for_rule=[]
    for eachitem in celldict_fmtd[keys]["ports"]:
        # print(f"item is {eachitem}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        port_number="service."+str(counter)
        port_number=port_number+" "+eachitem
        port_list_for_rule.append(port_number)
        counter=counter+1
    port_list_string=""    
    for eachitem in port_list_for_rule:
        port_list_string=port_list_string+eachitem+" "    
    
    # print(port_list_string)
    
    action_string=celldict_fmtd[keys]["action"]
    #add access-rule layer "utm-ukGOR_In_Line Security" name "Process Vlans" source.1 h-169.4.98.13 destination.1 h-10.0.14.190 service.1 TCP135 action "Accept" position 11 track.type log comments "CR12345 - AK - 07/12/2022"
    
    # print(keys)
    if celldict_fmtd[keys]["section"]=="none":
        # print("empty")
        rule_string='add access-rule layer "'+ppkg+'" name "'+rule_name+'" '+source_list_string+' '+destination_list_string+' '+port_list_string+' '+"action"+' "'+action_string+'"'+' position '+str(rbasestrow)+' track.type log comments "'+rule_comment+'"'
    if celldict_fmtd[keys]["section"]!="none":
        # print("not empty")
        rule_string='add access-section layer "'+ppkg+'" name "'+celldict_fmtd[keys]["section"]+'"'+' position '+str(rbasestrow)
    
    rule_add_cmds.append(rule_string)
    rbasestrow=rbasestrow+1
# listprinter(rule_add_cmds)
    # listprinter(source_list_for_rule)
# listprinter(source_list_for_rule)



print("==========================================================================")
print("Print the CLI commands to be added to the script file ")
print("==========================================================================")

print("## HOSTS  ##")
listprinter(hostsaddcmds)
print("\n")

print("## DNS FQDNs   ##")
listprinter(ndnso_add_cmds)
print("\n")

print("## Custom HOSTs & FQDNs  ##")
listprinter(nho_add_cmds)
print("\n")

print("## Custom NETs& FQDNs  ##")
listprinter(nno_add_cmds)
print("\n")

print("## NETs  ##")
listprinter(netsaddcmds)
print("\n")

print("## PORTs  ##")
listprinter(portsaddcmds)
print("\n")

print("## GROUPs  ##")
listprinter(group_add_cmds)
print("\n")

print("## RULES  ##")
listprinter(rule_add_cmds)

# listprinter(portstbcr)


print("==========================================================================")
print("Adding CLI Commands to Add DNS FQDNS")
print("==========================================================================")
print("\n")
with open('thescript.txt', 'a+') as script:
    script.write(f"\n### --------------------------------  ###")
    script.write(f"\n### CLI Commands to Add DNS FQDNs     ###")
    script.write(f"\n### --------------------------------  ###\n\n")
    for each in ndnso_add_cmds:
        script.write(f'{each}\n')


print("==========================================================================")
print("Adding CLI Commands to Add Custom Hosts and FQDNs  to the script ")
print("==========================================================================")
print("\n")
with open('thescript.txt', 'a+') as script:
    script.write(f"\n### ------------------------------------------  ###")
    script.write(f"\n### CLI Commands to Add Custom Hosts and FQDNs  ###")
    script.write(f"\n### ------------------------------------------  ###\n\n")
    for each in nho_add_cmds:
        script.write(f'{each}\n')

print("==========================================================================")
print("Adding CLI Commands to Add Custom Nets and FQDNs  to the script ")
print("==========================================================================")
print("\n")
with open('thescript.txt', 'a+') as script:
    script.write(f"\n### -----------------------------------------  ###")
    script.write(f"\n### CLI Commands to Add Custom Nets and FQDNs  ###")
    script.write(f"\n### -----------------------------------------  ###\n\n")
    for each in nno_add_cmds:
        script.write(f'{each}\n')


print("==========================================================================")
print("Adding Groups addition commands to the script ")
print("==========================================================================")
print
with open('thescript.txt', 'a+') as script:
    script.write(f"\n### ----------------------------------  ###")
    script.write(f"\n### CLI Commands to Add New Groups      ###")
    script.write(f"\n### ------------------------------  ###\n\n")
    for each in group_add_cmds:
        script.write(f'{each}\n')


print("==========================================================================")
print("Add rules to the script file ")
print("==========================================================================")

with open('thescript.txt', 'a+') as script:
    script.write(f"\n### ------------------------------  ###")
    script.write(f"\n### CLI Commands to Add New Rules   ###")
    script.write(f"\n### ------------------------------  ###\n\n")
    for each in rule_add_cmds:
        script.write(f'{each}\n')



    
#TODO1.lmt1: existing networks cnanot be replaced.
#TODO2.lmt2: mixing of networks/ips ips/fqdns doesnt work currently.
#TODO3.lmt3: negate will only work for the object_name rather than ip i.e 1.1.1.1 will not work but h-1.1.1.1 will as it already exists
#TODO4.at the time of the rule creation`
#TODO5.lmt5: it cannot create the groups yet.
#TODO6.lmt6: script cannot add hosts to group yet.
#TODO7.lmt7: script still takes static fw name
#TODO8.lmt8: script still takes static comments
#TODO9.bug1: "any" is not being picked up by the script as port.
#TODO10.bug2: groups are generated for lines where they arent required. 
##169.5.5.126 script did not create this host?? row 64
####  script could not create 10.120.101.110 row 22


'''
CODES
=====

1.1.1.1                         no code needed, auto pick up

2.2.2.0/24                      no code needed, auto pick up

nho:1.1.1.1,1.1.1.1-h1          nho: for new ip host object with custom name. Notice ip comma name.

nno:2.2.2.0-24,2.2.2.0-24-n1    nno: for new network object with custom name. Notice network comma name.

fqdn:3.3.3.0-h3                 for pre-existing objects with that name. If you are sure object exists use fqdn:
                                this can be used for anything, host, network, dns etc.

ndns:.abc.xyz.com               this code is needed for a dns domain object.

section: my new section         section: And text of your choice, this will add a new section for you.

ngp:mynewnetworkgroup           it can contain host ips or host nets, all auto picked.

pgp:mynewportgroup              it can contain ports like tcp445 udp61 etc.


'''
