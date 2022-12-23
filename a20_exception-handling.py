#exception handling using wrong data input as an example
# my_number=int(input("enter a number (enter string on purpose to see the effect): "))
# print ("number you entered is: "+str(my_number))
# print ("result of my_number/my_number is: "+ str(my_number/0))

# try:
#     my_number=int(input("enter a number (enter string on purpose to see the effect): "))
#     print ("number you entered is: "+str(my_number))
#     print ("result of my_number/my_number is: "+ str(my_number/0))
#
# except:
#     print ("one or the other type of error")

# the above except statement catches all types of errors
# it is a catch all error statement
# if we want to catch specific types of errors then we will have to use a
# different technique. problem with first is you will never know what
# went wrong

# try:
#     my_number=int(input("enter a number (enter string on purpose to see the effect): "))
#     print ("number you entered is: "+str(my_number))
#
# except ValueError:
#     print ("Value Error")
#
# try:
#     my_number=int(input("enter a number to see effect of number/0: "))
#     print ("result of my_number/my_number is: "+ str(my_number/0))
#
# except ZeroDivisionError:
#     print ("divide by zero error")
#
# print ("rest of the program continues to run")


# storing errors as variables

try:
    my_number=int(input("enter a number (enter string on purpose to see the effect): "))
    print ("number you entered is: "+str(my_number))

except ValueError as err1:
    print (err1)

try:
    my_number=int(input("enter a number to see effect of number/0: "))
    print ("result of my_number/my_number is: "+ str(my_number/0))

except ZeroDivisionError as err2:
    print (err2)

print ("rest of the program continues to run")
