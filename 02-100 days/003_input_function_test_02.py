#greeting for the program
from functools import total_ordering

print ("\n this is the tip calculator\n")
total_bill=input("what is the total bill : ")
split=input("how many people did split the bill : ")
percentage=input("what percentage of the bill do you want to pay as tip: ")
bill_for_each=int(total_bill)/int(split)
# print(str(bill_for_each))
percentage_final=int(100)*(int(percentage)/100)
# print(str(percentage_final))
percentage_final_split=int(percentage_final)/int(split)
#print(str(percentage_final_split))
total_for_each=int(bill_for_each)+int(percentage_final_split)
print("Total for each person including tip is :"+str(total_for_each))