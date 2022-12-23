from multiprocessing.reduction import steal_handle
import random

lom=["terminator","rocky","topgun","madmax","breakingbad","superman","spiderman"] 
print(f"list of movies is  {lom}")
mov=random.choice(lom)

mstrlist = list(mov)
gstrlist=[]
charloc=0
charlocall=0
correct_counter=0    
counter=0
correct=0
strholder1=""

print(f"movie picked is {mov}")
lom.remove(mov)
print(f"new list of movies is {lom}")
movstr=str(mov)
print(f"the movie string is {movstr}")
lenmovstr=len(movstr)
print(f"length of movie string is {lenmovstr}")

for i in range (lenmovstr):
    gstrlist.append("-")

#while ((counter!= (lenmovstr*2)) and (gstrlist!=mstrlist)):
while (gstrlist!=mstrlist):    
    counter=counter+1
    print(f"\n\n\n\nYou have {((lenmovstr*2)+1)-counter} attemps left")
    print(f"you got <<{correct}>> correct so far")
    print(f"value of gstrlist is {gstrlist}")
    print(f"value of mstrlist is {mstrlist}")
    char=input("Enter the letter you think there is in the movie : ")
    
    if (char not in mstrlist):
        print("Wrong! Let's Try again")

    for eachletter in mstrlist:
        #print(f"character is {char}")
        if (char == eachletter):
            charloc=mstrlist.index(char)
            charlocall = [ i for i in range(len(mstrlist)) if mstrlist[i] == char ]
            #print(f"value of char is {char} location of character is {mstrlist.index(char)}")
            print(f"value of char is {char} location/s of character is {charlocall}")
            
            for item in charlocall:
                 gstrlist=gstrlist[:int(item)]+[char]+gstrlist[item+1:]
            
            #gstrlist=gstrlist[:int(charlocall)]+[char]+gstrlist[charloc+1:]
            correct=correct+1
            # print(f"value of correct is {correct}")
    
    if gstrlist==mstrlist:
        print("you nailed it")
        break
    
    
