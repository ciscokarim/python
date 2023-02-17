'''
################################################################################################
================================================================================================
Version Highlights

* This version takes input of username,password,domain,mds ip and command
* It logs in the user, captures "show command" in json format and logs the user out
* It also creates a show_command.txt user output where multiple outputs are combined.

================================================================================================
################################################################################################
'''


import subprocess
import codecs
import chardet
import time
import json
import sys
import time as t #because the time and datetime.time are interfering with each other.
from datetime import *

'''
##################################################################################
==================================================================================
Following line starts moniting the time at the start ot the script
==================================================================================
##################################################################################
'''

start_time = t.perf_counter()

'''
##################################################################################
==================================================================================
following function executes commands in powershell and let us know 
if the command was successfull of note.
==================================================================================
##################################################################################
'''

def run(cmd):
    
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

    if completed.returncode != 0:
        # print("An error occured: %s", completed.stderr)
        print("------------------------------")
        
        if "del login_output" in cmd:
            print(f"No prevoius login_output.txt files found")

        print(f"**{str(cmd)}**  command execution FAILED!!!!")
        print("------------------------------")
    
    else:
        print(f"<< {str(cmd)} >>  command executed successfully!")
    
    return completed.stdout

'''
##################################################################################
==================================================================================
Following function lets a user login after inputting their login details.
it takes username, password, domain-name and ip address of management server
as input. It also generates a login_input log.
==================================================================================
##################################################################################
'''


def login(uname,pwd,dn,ioms):
    
    # run("del login_output*")
    login_output=run(f'mgmt_cli.exe login -u {uname} -p {pwd} -d {dn} -m {ioms}')
    
    # print(f"Login Result >>>")
    print(f"{login_output}")


    if "sid:" in login_output:
        print("login Successful")
    else:
        print("Unsuccessful Login")
        sys.exit()

    return login_output
    # cat_result = run("cat login_output.txt")
    # print(cat_result)


'''
##################################################################################
==================================================================================
this function gets the sid by reading the login_result file which is gneerated 
by the login function.
==================================================================================
##################################################################################
'''


def sid_getter(login_output):

    sid=""

    login_output=login_output.split("\n")

    for lines in login_output:
        if "sid:" in lines:
            sid=lines
    
    sid=sid.strip()
    sid=sid.split(" ")
    sid=sid[1]
    sid=sid.replace('"',"")
    sid=sid.replace(" ","")
    sid=sid.strip()

    print(sid)

    return sid

'''
##################################################################################
==================================================================================
Following function logs the user out of the current session
==================================================================================
##################################################################################
'''

def logout(ioms,sid):
    
    logout_output = run(f'mgmt_cli.exe logout -m {ioms} --session-id {sid}')
    # print(f"Logout Result >>>")
    print(logout_output)
    
    if "OK" in logout_output:
        print("logout Successful")
    else:
        print("Unsuccessful Logout")

'''
##################################################################################
==================================================================================
Following function gets the output for long show commands
==================================================================================
##################################################################################
'''

def show_cmd_getter(show_cmd):

    total = "0"

    total_extractor=run(f"mgmt_cli.exe {show_cmd} offset 0 limit 10 -f json -d {dn} -m {ioms} --session-id {sid}")

    total_extractor=total_extractor.split("\n")

    for lines in total_extractor:
        if "total" in lines:
            total = lines

    total = total.split(':')
    total = total[1]
    total = total.strip()
    total = int(total)
    # print(type(total))

    limit = 500
    # total = 2706
    # total=int(input("Enter the total: "))
    offset = 0
    show_items=""
    show_items_holder=""
    objects_batch_ctr=0
    list_holder = []

    while  (total >=  0):
        
        counter = 0

        if total <= 500:
            limit = 500
            objects_batch_ctr+=1
            print(f"total = {total}, offset = {offset} and limit = {limit}")
            show_items_holder=run(f"mgmt_cli.exe {show_cmd} offset {offset} limit {limit} -f json -d {dn} -m {ioms} --session-id {sid}")
            show_items += show_items_holder
            show_items.replace("objects",f"objects_batch_{objects_batch_ctr}")
            
            py_data_dict = json.loads(show_items_holder)
            # for items in py_data_dict:
            #     print(f"{items} ###############################")
            
            print(py_data_dict["total"])
            list_holder = list_holder + py_data_dict["objects"]
            
            counter+=1
            print(f"counter under 500 is  {counter}")
            
            break

        # counter = 0
        if total >= 500: 
            
            print(f"total = {total}, offset = {offset} and limit = {limit}")
            show_items_holder=run(f"mgmt_cli.exe {show_cmd} offset {offset} limit {limit} -f json -d {dn} -m {ioms} --session-id {sid}")
            
            py_data_dict = json.loads(show_items_holder)
            # for items in py_data_dict:
            #     print(f"{items} ###############################")
            
            print(py_data_dict["total"])
            list_holder = list_holder + py_data_dict["objects"]
            counter+=1

            print(f"counter over 500 is {counter}")

            limit = 500
            total = total - 500
            offset += 500

            show_items+=show_items_holder
            show_items.replace("objects",f"objects_batch_{objects_batch_ctr}")
        
        # if total >= 500:
        #     limit = 10
        #     objects_batch_ctr+=1
        #     print(f"total = {total}, offset = {offset} and limit = {limit}")
        #     show_items_holder=run(f"mgmt_cli.exe {show_cmd} offset {offset} limit {limit} -f json -d {dn} -m {ioms} --session-id {sid}")
        #     show_items += show_items_holder
        #     show_items.replace("objects",f"objects_batch_{objects_batch_ctr}")
            
        #     py_data_dict = json.loads(show_items_holder)
        #     # for items in py_data_dict:
        #     #     print(f"{items} ###############################")
            
        #     print(py_data_dict["total"])
        #     list_holder = list_holder + py_data_dict["objects"]
            
        #     counter+=1
        #     print(f"counter under 500 is  {counter}")
            
        #     break

    # print(show_hosts)
    print(type(list_holder))
    print(len(list_holder))
    print("Items Extraction Process Completed")
    # return show_items
    return list_holder


'''
##################################################################################
==================================================================================
The Script Itself - Putting it all together
==================================================================================
##################################################################################
'''

# if __name__ == "__main__":

# ioms=input("Enter the ip address of the managment server: ")        #ioms = ip of management server
ioms="169.12.17.102"
# ioms="169.12.17.111"
# dn=input("Enter the domain name: ")
dn="Site10_Domain"
# dn="Site11_Domain"
# uname=input("Enter the username :")
# pwd=input("Enter the password :")
uname='"adfwyzzad"'
pwd='"c}LMJ*sE)Rb4x%F0W3m="' #keep two sets of quotes around password
show_cmd="show services-tcp"
# show_cmd="show services-tcp"


print(f"============================================================================")
print(f"=======================  Initiating Login  =================================")
print(f"============================================================================")
print("\n")

login_data=login(uname,pwd,dn,ioms)

print("\n")
print(f"============================================================================")
print(f"=======================  Getting SID For the Session  ======================")
print(f"============================================================================")
print("\n")

sid = sid_getter(login_data)

print("\n")
print(f"============================================================================")
print(f"=======================  Getting output for << {show_cmd} >>")
print(f"============================================================================")
print("\n")

show_cmd_output=show_cmd_getter(show_cmd)


print("\n") 
print(f"============================================================================")
print(f"=======================  Initiating Logout =================================")
print(f"============================================================================")
print("\n")

logout(ioms,sid)


print("\n")
print("==========================================================================")
print("Deleting any existing show_hosts files ")
print("==========================================================================")
print("\n")

# run("del show*")


print("\n")
print("==========================================================================")
print("Creating the output file name")
print("==========================================================================")
print("\n")

# show_items_filename = "show_hosts"
show_items_filename = show_cmd
show_items_filename = show_items_filename.strip()
show_items_filename = show_items_filename.replace(" ","_")
show_items_filename = show_items_filename + "_" + (f'{datetime.now().strftime("%H-%M-%S_%d-%m-%Y")}')
print("File name is ...")
print(show_items_filename)


# print("\n")
# print("==========================================================================")
# print("Creating the output PYTHON file")
# print("==========================================================================")
# print("\n")

# with open(f'{show_items_filename}.py', 'a+') as show_items_file:
#     show_items_file.write(str(show_cmd_output))

# file_checker = run("dir")

# if show_items_filename in file_checker:
#     print(f"{show_items_filename} python file created successfully")
# else:
#     print(f"{show_items_filename} python file COULD NOT be created")

    # print("\n")


print("\n")
print("==========================================================================")
print("Creating the output JSON file")
print("==========================================================================")
print("\n")


show_cmd_output_json = json.dumps(show_cmd_output, indent=4)
# data_json_string = json.dumps(user_dict, indent=4)


with open(f'{show_items_filename}.json', 'a+') as show_items_file:
    show_items_file.write(str(show_cmd_output_json))

file_checker = run("dir")

if str(show_items_filename+".json") in file_checker:
    print(f"{show_items_filename} json file created successfully")
else:
    print(f"{show_items_filename} json file COULD NOT be created")



print("==========================================================================")
print("Creating the output CSV file")
print("==========================================================================")
print("\n")

print("type of show items file")
print (type(show_cmd_output))
print("length of show items file")
print(len(show_cmd_output))

csvlist=[]

for each_dict in show_cmd_output:
  # print(f'name: {each_dict["name"]}  ,,,,  ip: {each_dict["ipv4-address"]}   ')
#   if "subnet4" in each_dict:
    csvlist.append(f'{each_dict["name"]},{each_dict["port"]},{each_dict["type"]},npf,\n')
#   csvlist.append(f'{each_dict["name"]},{each_dict["subnet4"]},{each_dict["subnet-mask"]},{each_dict["mask-length4"]},\n')



with open(f'{show_items_filename}.csv', 'a+') as show_items_file:
    for eachitem in csvlist: 
        show_items_file.write(eachitem)
    

file_checker = run("dir")

if str(show_items_filename+".csv") in file_checker:
    print(f"{show_items_filename} csv file created successfully")
else:
    print(f"{show_items_filename} csv file COULD NOT be created")



'''
##################################################################################
==================================================================================
Following line starts moniting the time at the start ot the script
==================================================================================
##################################################################################
'''

end_time = t.perf_counter()



print("\n")
print("==========================================================================")
print("Total time the script took to execute")
print("==========================================================================")
print("\n")

print(f"Time of Execution = {end_time - start_time} Seconds")
