import random

choice=input("Which side do you think the coin landed on, heads/tail : ")
toss=random.randint(1,2)

if (toss == 1):
    result="heads"
if (toss == 2):
    result="tail"

print (f"choice is {choice}, toss is {toss}, result is {result}")
if (choice == result):
    print(f" you are right, the result is, {result}")
else: 
    print(f" you are wrong, the result is, {result}")
