#store a list of numbers separated by spaces in a list
nums=input("enter the numbers separated by commas : ") #1,2,3
num_list=nums.split(",")
holder=0

for items in num_list:
    if (int(items) > holder):
        holder=int(items)
       
print(f"the highest number is {holder}")