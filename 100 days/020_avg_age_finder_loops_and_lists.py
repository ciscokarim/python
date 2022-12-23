tp=int(input("number of people you want the avg age for : "))
agelist=[]

adder=0
for i in range (1,tp+1):
    age=int(input(f"enter the age for the person number {i} :"))
    agelist.append(age)
    adder=adder+age

avg_age=adder/tp
print(f"the average is : {avg_age}")
