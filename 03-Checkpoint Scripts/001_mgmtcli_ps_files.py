import subprocess
import codecs
import chardet
import time


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
        print(f"**{str(cmd)}**  command executed successfully!")
    
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
    
    run("del login_output*")
    run(f'mgmt_cli.exe login -u {uname} -p {pwd} -d {dn} -m {ioms} > login_output.txt')
    
    print(f"Login Result >>>")
    cat_result = run("cat login_output.txt")
    # print(cat_result)





'''
##################################################################################
==================================================================================
this function converts the utf16 files to ascii, which are readable by python
==================================================================================
##################################################################################
'''

def ascii_encoder():

    # with open("login_output.txt") as scr_out:
    #     sos=scr_out.read()
    #     encoding = chardet.detect(sos.encode())["encoding"]R=6L3L)!zu5VO2lG)TaI
    #     print(encoding)

    with codecs.open("login_output.txt","r", encoding="utf-16") as scr_out:
        sos=scr_out.read()


    with codecs.open("login_output_tgt.txt","w", encoding="ascii") as scr_out:
        scr_out.write(sos)


    # with open("login_output.txt") as scr_out:
    #     sos=scr_out.read()
    #     encoding = chardet.detect(sos.encode())["encoding"]
    #     print(encoding)
    

    run("ren login_output.txt login_output_utf.txt")
    run("ren login_output_tgt.txt login_output.txt")


'''
##################################################################################
==================================================================================
this function converts the utf16 files to ascii, which are readable by python
==================================================================================
##################################################################################
'''

def ascii_encoder2():

    # with open("logout_output.txt") as scr_out:
    #     sos=scr_out.read()
    #     encoding = chardet.detect(sos.encode())["encoding"]R=6L3L)!zu5VO2lG)TaI
    #     print(encoding)

    with codecs.open("logout_output.txt","r", encoding="utf-16") as scr_out:
        sos=scr_out.read()


    with codecs.open("logout_output_tgt.txt","w", encoding="ascii") as scr_out:
        scr_out.write(sos)


    # with open("logout_output.txt") as scr_out:
    #     sos=scr_out.read()
    #     encoding = chardet.detect(sos.encode())["encoding"]
    #     print(encoding)
    

    run("ren logout_output.txt logout_output_utf.txt")
    run("ren logout_output_tgt.txt logout_output.txt")

'''
##################################################################################
==================================================================================
this function gets the sid by reading the login_result file which is gneerated 
by the login function.
==================================================================================
##################################################################################
'''


def sid_getter():

    sid=""


    with open("login_output.txt") as sot:
        sot=sot.readlines()
        for lines in sot:
            if "sid" in lines:
                sid=lines
                # print(lines)

    # print(type(sid))
    # print(sid)
    sid.strip()
    sidlist = sid.split(' ')
    # print(sidlist)
    sid=sidlist[1]
    # print(sid)
    sid=sid.replace('"','')
    sid=sid.strip()
    print(f"sid for this session is = {sid}")
    return sid


'''
##################################################################################
==================================================================================
Following function logs the user out of the current session
==================================================================================
##################################################################################
'''


def logout(ioms,sid):
    
    run("del logout_output*")
    run(f'mgmt_cli.exe logout -m {ioms} --session-id {sid} >> logout_output.txt')
    
    print(f"Logout Result >>>")
    cat_result = run("get-content logout_output.txt")
    print(cat_result)





'''
##################################################################################
==================================================================================
Following is the main program Run.
==================================================================================
##################################################################################
'''


if __name__ == '__main__':

    # ioms=input("Enter the ip address of the managment server: ")        #ioms = ip of management server
    ioms="169.12.17.102"
    # dn=input("Enter the domain name: ")
    dn="Site10_Domain"
    # uname=input("Enter the username :")
    # pwd=input("Enter the password :")
    uname='"adfwyzzad"'
    pwd='"R=6L3L)!zu5VO2lG)TaI"'

    # run("del login_output.txt")
    # run(f'mgmt_cli.exe login -u {uname} -p {pwd} -d {dn} -m {ioms} > login_output.txt')
    
    
    print(f"============================================================================")
    print(f"=======================  Initiating Login  =================================")
    print(f"============================================================================")

    login(uname,pwd,dn,ioms)

    ascii_encoder()

    print("\n")
    print(f"============================================================================")
    print(f"=======================  Getting SID For the Session  ======================")
    print(f"============================================================================")

    sid = sid_getter()

    print("\n")
    print(f"============================================================================")
    print(f"=======================  Initiating Logout =================================")
    print(f"============================================================================")

    logout(ioms,sid)

    ascii_encoder2()

    with open("logout_output.txt") as scr_out:
        sos=scr_out.read()
        encoding = chardet.detect(sos.encode())["encoding"]
        print(encoding)

    test1=run("cat logout_output.txt")
    print(test1)
    test2=run("dir")
    print(test2)
