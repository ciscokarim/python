###########################################################################
# ceasar cipher. You shift abcdefg ... to right the number of keys
###########################################################################
from module_with_printers import clistprinter
from module_with_printers import rlistprinter
from module_with_printers import cdictprinter
from module_with_printers import rdictprinter

#org_charset=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
#ext_charset=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
# org_charset=["a","b","c","d","e"," "]
# ext_charset=["a","b","c","d","e"," "]
chardef={"a":"ae","b":"bee"}

mode=input("\n\ndo you want to cipher, decipher or quit: ")

while (mode != "quit"):
    org_charset=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    ext_charset=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    if (mode=="cipher"):
        str_to_cipher=input("Enter the string :")
        shift=int(input("Enter the shift :"))
        lc=(len(org_charset))

        #extend the list to accomodated extra members due to shift

        for i in range (1,shift+1):
            ext_charset.append("-")
            #print(i,end="")

        print ("\n==================1")

        print("value of i is ...  ")
        for i in range (lc,lc+shift):
            print(f"{i}",end="")
            ext_charset[i]=org_charset[i-lc]

        print ("\n==================2")

        print("original charset")
        rlistprinter(org_charset)

        print ("\n==================3")

        print("extended charset")
        rlistprinter(ext_charset)

        print ("\n==================3")
        # listprinter(charset)
        # listprinter(charset)
        # dictprinter(chardef)
        # print("\n"+str_to_cipher)
        # print("\n")
        print(f"string to cipher is **{str_to_cipher}**")
        the_cipher=str_to_cipher
        the_cipher2=""
        
        in_in_cipher=-1
        for eachletter in str_to_cipher:
            in_in_cipher+=1
            #print(in_in_cipher)            
            #print (eachletter,end=" ")
            index_in_org=org_charset.index(eachletter)
            corr_letter_in_ext=ext_charset[index_in_org+shift]
            #print(f"index of *{eachletter}* in original is *{index_in_org}*, corr letter in ext is *{corr_letter_in_ext}*")
            index_in_cipher=str_to_cipher.index(eachletter)
            #print(f"index of letter in *{eachletter} in cipher is *{index_in_cipher}*")
            #the_cipher2=the_cipher.replace(eachletter,corr_letter_in_ext)
            #print(f"each letter = {eachletter} & corr_letter = {corr_letter_in_ext} & abc=cipher2={the_cipher2}, original cipher={the_cipher}")
            the_cipher = the_cipher[:in_in_cipher] + corr_letter_in_ext + the_cipher[in_in_cipher+1:]
            #print(the_cipher)
            #print(f"abc={the_cipher2}, original cipher={the_cipher}") 
                # new_character = 'k'
                # mastr = mastr[:index] + new_character + mastr[index+1:]
                # print(mastr)
                
        print ("==================4")

        print(f"the_cipher is *{the_cipher}*")


    if (mode=="decipher"):

        str_to_decipher=input("Enter the string to decipher:")
        shift=int(input("Enter the shift :"))
        lc=(len(org_charset))

        #extend the list to accomodated extra members due to shift

        
        for i in range (1,shift+1):
            ext_charset.append("-")
            #print(i,end="")

        print ("\n==================1")

        print("value of i is ...  ")
        for i in range (lc,lc+shift):
            print(f"{i}",end="")
            ext_charset[i]=org_charset[i-lc]

        print ("\n==================2")

        print("original charset")
        rlistprinter(org_charset)

        print ("\n==================3")

        print("extended charset")
        rlistprinter(ext_charset)

        print ("\n==================3")
        # listprinter(charset)
        # listprinter(charset)
        # dictprinter(chardef)
        # print("\n"+str_to_cipher)
        # print("\n")
        print(f"string to decipher is **{str_to_decipher}**")
        the_decipher=str_to_decipher
        
        in_in_cipher=-1
        for eachletter in str_to_decipher:
            #print (eachletter,end=" ")
            in_in_cipher+=1
            #print(in_in_cipher)  
            index_in_ext=ext_charset.index(eachletter)
            index_in_org=index_in_ext - shift
            #index_in_ext=ext_charset.index(eachletter)
            #print(f"letter is **{eachletter}** index in ext is **{index_in_ext}**, index in org is **{index_in_org}**")
            # corr_letter_in_ext=ext_charset[index_in_org+shift]
            corr_letter_in_org=org_charset[index_in_ext-shift]
            #print(corr_letter_in_org)
            #print(f"index of *{eachletter}* in original is *{index_in_org}*, corr letter in ext is *{corr_letter_in_ext}*")
            index_in_decipher=str_to_decipher.index(eachletter)
            #print(f"index of letter in *{eachletter} in cipher is *{index_in_cipher}*")
            the_decipher = the_decipher[:in_in_cipher] + corr_letter_in_org + the_decipher[in_in_cipher+1:]
                # new_character = 'k'
                # mastr = mastr[:index] + new_character + mastr[index+1:]
                # print(mastr)
                
        print ("==================4")

        print(f"the_decipher is *{the_decipher}*")
    
    mode=input("\n\ndo you want to cipher, decipher or quit: ")





#shift 2
#Enter the string :i am good
#the_cipher is *kbco iqof*
#Enter the string :go and fuck yourself
#the_cipher is *iqbcpf hwem  outugnf*

#shift 9
# Enter the string :baby come home
# the_cipher is *kjbgilxvn qome*
# Enter the string :fuck off
# the_cipher is *ocltixff*
