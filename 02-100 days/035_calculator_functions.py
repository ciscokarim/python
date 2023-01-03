###########################################################################
# calculator using functions
###########################################################################

def calc(a,b,c):
    if c=="plus":
        result=a+b
    if c=="minus":
        result=a-b
    if c=="mult":
        result=a*b
    if c=="div":
        result=a/b
    return result

def adder(a,b):
    return(a+b)

def subtractor(a,b):
    return(a-b)

def multiplier(a,b):
    return(a*b)

def divider(a,b):
    return(a/b)

more=""

fnum=int(input("Enter the first number :"))

while (more!="no"):
    
    op=input("Enter the operation (plus,minus,mult,div) :")
    snum=int(input("Enter the second number :"))
    result=calc(fnum,snum,op)
    print(f"{fnum} {op} {snum} = {result}")

    more=input("more?? (yes/no): ")

    if (more=="yes"):
        holdvalue=input("result as first number (yes/no): ")
        if holdvalue=="yes":
            fnum=result
            print(f"First number is {fnum}")
        else:
            fnum=int(input("Enter the first number :"))
