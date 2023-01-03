#this program uses a module which was created as "module_with_data"
#it is currently in the same directory as this program. you can now
#simply import and use the data stored in its variables. The variables
#used below are defined in the module and the program simply prints them.

import module_with_data

#access variables with predefined values
print (module_with_data.name)
print (module_with_data.age)
print (module_with_data.address)

#access a function which prints a name
print(module_with_data.greeting("aftab"))

#access a function which adds two numbers
#by passing them variables.

a=3
b=2

print(str(module_with_data.adder(a,b)))


#access a dictionary

print(module_with_data.personx["name"])
print(module_with_data.personx["age"])
print(module_with_data.personx["country"])