def clistprinter(l):
    for eachitem in l:
        print(eachitem)

def rlistprinter(l):
    for eachitem in l:
        print(eachitem,end="")       

def cdictprinter(d):
    for eachitem in d:
        print(f"{eachitem}:{d[eachitem]}") 

def rdictprinter(d):
    for eachitem in d:
        print(f"{eachitem}:{d[eachitem]},",end="") 