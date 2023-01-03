#simple boolean condition

condition1=True
if condition1:
    print "print something"  #this will only print if True

condition2=False
if condition2:
    print "something"        #this will only print if True


#if and else

condition2=True
if condition2:
    print "condition is True"
else:
    print "condition is Flase"

condition3=False
if condition3:
    print "condition is True"
else:
    print "condition is Flase"

#if and else with OR and AND
#but using or statement cannot be deterministic

is_the_car_fast=True
is_the_car_big=True

if is_the_car_fast or is_the_car_big:
    print "car is fast or big or both"
else:
    print "car is neither fast nor big"

if is_the_car_fast and is_the_car_big:
    print "car is both fast and big"
else:
    print "car is either fast or big or none"

# determination with single if statements

if is_the_car_fast:
    print "car is fast"
else:
    print "car is slow"

if is_the_car_big:
    print "car is big"
else:
    print "car is small"

#determination with AND statements

if   is_the_car_fast and is_the_car_big:
    print "car is fast, car is big"

elif is_the_car_fast and not(is_the_car_big):
    print "car is fast, car is not big"

elif not(is_the_car_fast) and is_the_car_big:
    print "car is no fast, car is big"

else:
    print "car is not fast, car is not big"

#comparisons
#   == equal
#   != not equal
#   >= greater or equal
#   <= less or equal

num1= input ("enter the first number: ")
num2= input ("enter the second number: ")
num3= input ("enter the third number: ")

def maxfinder(num1,num2,num3):
    if   num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    elif num3>=num2 and num3>=num1:
        return num3

print maxfinder(num1,num2,num3)

#basic calculator
#must run in python3 not 2
#python will need () in print statements.
#python 2 doesnt recognize the string input
n1= int(input ("enter the first number: "))
n2= int(input ("enter the second number: "))
operation= str(input ("enter the operation:add,sub,mul,div: "))
sum=n1+n2
prod=n1*n2
diff12=n1-n2
diff21=n2-n1
div12=n1/n2
div21=n2/n1

if operation=="add":
    print ("sum of numbers is: "+str(sum))

elif operation=="mul":
    print ("product of numbers is: "+str(prod))

elif operation=="sub":
    if n1>=n2:
        print("difference of numbers is :"+str(diff12))
    if n2>=n1:
        print("difference of numbers is :"+str(diff21))

elif operation=="div":
    if n1>=n2:
        print("quotient of numbers is :"+str(div12))
    if n2>=n1:
        print("quotient of numbers is :"+str(div21))


#if statement to look for a character in string

mystring="the quick brown fox jumps right over the lazy dog"
for character in mystring:
    if character in "AEIOUaeiou": ##instaed of using many character=="a" or etc etc
        print (character, end=",")
print ("")
