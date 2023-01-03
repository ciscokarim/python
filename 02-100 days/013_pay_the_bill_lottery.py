import random

lop=[]
nop=int(input("Enter the total number of people : "))
for i in range (1,nop+1):
    people=input("Enter the name of the person number: "+str(i)+" :")
    lop.append(people)

randperson=random.randint(1,5)
print(randperson)

print("Person to pay the bill would be : "+str(lop[randperson-1]))