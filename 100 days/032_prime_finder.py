###########################################################################
# find if a number is prime
###########################################################################

def primefinder(num):

    counter=0

    for i in range (1,number+1):
        tester=number%i
        if(tester==0):
            counter+=1

    if counter>2:
        print(f"number is not prime")
    else:
        print(f"number is prime")


        
number=int(input("Enter the number you want to check : "))
primefinder(number)