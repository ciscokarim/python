# #python-functions
#
# #function that greets users
#
# #function definition
# def greeter():
#     print "good morning sir"
# #call the function to execute it
#
# print "Oh he is here"
# greeter()
# #print "\n"
# print "how are you doing today"
#
# #parameters and variables in functions
# def greeter2(name):
#     print "good morning, " + name
#
# greeter2("kala")
# greeter2("neela")
# greeter2("peela")
#
# #function printing age,sex and location of a person
# def asl(age,sex,location):
#     print "The new comer is "+str(age)+" years old, is "+str(sex)+ " and from "+str(location)+"."
#
# asl(15,"male","aus")
# asl(31,"female","can")
# asl(23,"male","usa")
#
# #function that adds three numbers
#
# def adder(one,two,three):
#     sum=one+two+three
#     print "sum of "+str(one)+ ", "+str(two)+", "+str(three)+" is ="+str(sum)
#
# adder(1,2,3)
# adder(1,1,1)
# adder(2,2,2)
#
# #function that returns a cube but this functions
# #can only print a number
# #which cannot be used for anything or with another operator
#
# def cuber(cnum):
#     cube=cnum*cnum*cnum
#     print "cube of the number is: "+str(cube)
#
#
# usercnum=input ("enter the number to get the cube: ")
# cuber(usercnum)
#
#
# #using return rather than print in the functions
# #this way we can use the result as a variable or
# #store it in a variables
#
#
# def cuber2(cnum2):
#     return cnum2*cnum2*cnum2
#     #after return no more code be put in.
#     #this is going to be the last line
#     #in the function definition
#
# cuber2input=input ("enter the number you want the cube for: ")
# print str(cuber2(cuber2input))

# #build an exponent functions x^y functions
# num=int(input("please enter the number: "))
# power=int(input("please enter the desired power: "))
#
# def powfinder(num,power):
#     result=1
#     for i in range (1,power+1):
#         result=result*num
#     return result
#
#
# print (str(num)+"^"+str(power)+"= "+str((powfinder(num,power))))

def varprinter(a,b,c):
 print(f"value of a is {a}, b is {b} and c is {c}")

x=1
y=2
z=3

varprinter(a=3,b=3,c=3) # you can specify the a,b,c here but not a different variable name.
varprinter(c=2,b=2,a=2) # you can even change the order and it wont matter anymore.