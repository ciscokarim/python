# ##printing a table with while loop

# counter=0
# while counter!=10:
#     counter=counter+2
#     print(counter)

### input a list using while loop

#===========================================================================#

data=""
mylist=[]

while (data!="finish"):
    data=str(input("Enter the objects you want to put into the list :"))

    if(data!="finish"):
        mylist.append(data)

print(*mylist,sep=",")    


