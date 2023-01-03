#when you split a string and store it in a variable.
#it by default gets stored into a list.
names=input("Enter the names separated by commas :")
names_separated=names.split(",")
print(type(names_separated))
print(names_separated)