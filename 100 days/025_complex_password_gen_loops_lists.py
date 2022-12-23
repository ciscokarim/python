import random

#### password generator input
num_letters=int(input("Enter the number of letters you want in your password :"))
num_numbers=int(input("Enter the number of numbers you want in your password :"))
num_specials=int(input("Enter the number of specials you want in your password :"))

### lists of letters, numbers and specials to choose from
list_letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
list_numbers=[0,1,2,3,4,5,6,7,8,9]
list_specials=["!",'"',"£","$","%","^","&","*","(",")"]

### lists of letters, numbers and specials to choose from
random.shuffle(list_letters)
random.shuffle(list_numbers)
random.shuffle(list_specials)

### print the list
# print(list_letters)
# print(list_numbers)
# print(list_specials)

pwd=[]

for i in range (1,num_letters+1):
    pwd.append(list_letters[i])

for i in range (1,num_numbers+1):
    pwd.append(list_numbers[i])

for i in range (1,num_specials+1):
    pwd.append(list_specials[i])

### randomize the list again, withotu any commas, brackets or enclosed commas
print("the pwd before the shuffle")
print(*pwd, sep='')

### print the list without brackets,commas and enclosed commas, after the shuffle
random.shuffle(pwd)
print("the pwd after the shuffle")
print(*pwd, sep='')
