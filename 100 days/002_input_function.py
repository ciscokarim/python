#when you want to use the input from the user 
print ("\n===================================\n")
name_string=input("what is your name: ")
print("your name is "+name_string)


#printing the input without storing it into a variable
print ("\n===================================\n")
print(input("Enter your name if you want it to be printed : "))


# use numbers as input
print ("\n===================================\n")
num1=input("enter the first number :")
num2=input("enter the second number :")
result=int(num1)+int(num2)
print("The sum of two number is : "+str(result))
print ("\n===================================\n")

#printing the input without storing it into a variable and process it.
print ("\n===================================\n")
print("length of this string is :"+str(len(input("Enter the string to find its length : "))))

#switch variables
v1=input("enter the value of the first variable :")
v2=input("enter the value of the second variable :")
v3=v1
v1=v2
v2=v3
print("V1 is *"+str(v1)+"* and V2 is *"+str(v2)+"* after switching")
