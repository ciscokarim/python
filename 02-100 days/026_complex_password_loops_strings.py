import random

#### password generator input
num_letters=int(input("Enter the number of letters you want in your password :"))
num_numbers=int(input("Enter the number of numbers you want in your password :"))
num_specials=int(input("Enter the number of specials you want in your password :"))

### lists of letters, numbers and specials to choose from
list_letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
list_numbers=[0,1,2,3,4,5,6,7,8,9]
list_specials=["!",'"',"£","$","%","^","&","*","(",")"]

#define password variable as an empty string
pwd=""

for i in range (1,num_letters+1):
    pwd=pwd+str(random.choice(list_letters))

for i in range (1,num_numbers+1):
    pwd=pwd+str(random.choice(list_numbers))

for i in range (1,num_specials+1):
    pwd=pwd+str(random.choice(list_specials))

# you will have to convert a string to list to randomize

pwd_rnd=list(pwd)
print(*pwd_rnd, sep='')
random.shuffle(pwd_rnd)
print(*pwd_rnd, sep='')


