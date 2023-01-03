#module is just an external python program and you
#can pull functions , variables and everything else
#from that file by importing it. its just like a library
import greeter as gt
import themodule as tm

gt.greeter("oscar")

kms=int(input("enter the kms you want to conver to ms :"))
print ((tm.msINkms)*kms)

numb1=int(input("enter the first number :"))
numb2=int(input("enter the second number :"))

#product=themodule.proder(numb1,numb2)
print ("product of the numbers is: "+str(tm.proder(numb1,numb2)))
print ("sum of the numbers is: "+str(tm.adder(numb1,numb2)))
print ("square of the first numbers is: "+str(tm.square(numb1)))
