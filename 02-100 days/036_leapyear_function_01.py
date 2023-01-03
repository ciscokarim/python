###########################################################################
# leap year using functions
###########################################################################

def dom(year,month): #dom = days of month
    if year%4==0:
        domlist=["31","29","31","30","31","30","31","31","30","31","30","31"]
        if month=="jan":
            return domlist[0]
        if month=="feb":
            return domlist[1]
        if month=="mar":
            return domlist[2]            
        if month=="apr":
            return domlist[3]
        if month=="may":
            return domlist[4]
        if month=="jun":
            return domlist[5]
        if month=="jul":
            return domlist[6]
        if month=="aug":
            return domlist[7]
        if month=="sep":
            return domlist[8]
        if month=="oct":
            return domlist[9]
        if month=="nov":
            return domlist[10]
        if month=="dec":
            return domlist[11]

    if year%4!=0:
        domlist=["31","28","31","30","31","30","31","31","30","31","30","31"]
        if month=="jan":
            return domlist[0]
        if month=="feb":
            return domlist[1]
        if month=="mar":
            return domlist[2]            
        if month=="apr":
            return domlist[3]
        if month=="may":
            return domlist[4]
        if month=="jun":
            return domlist[5]
        if month=="jul":
            return domlist[6]
        if month=="aug":
            return domlist[7]
        if month=="sep":
            return domlist[8]
        if month=="oct":
            return domlist[9]
        if month=="nov":
            return domlist[10]
        if month=="dec":
            return domlist[11]


year=int(input("Enter the year :"))
month=input("Enter the month :")
print(f"year {year} has {dom(year,month)} number of days in {month}")