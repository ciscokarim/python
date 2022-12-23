###########################################################################
# leap year using functions, with doc string ..
# the string appears when using the function as help.
# to show what the function does.
# its the string enclosed in the ''' '''
###########################################################################

def is_leap_year(year): #lyc=leap year check
    '''
    Takes year as input and return true
    or false for its leap year check
    '''
    if year%4==0:
        return True
    else:
        return False

def dom(year,month): #dom = days of month
    '''
    Takes year and month as input and return
    the number of days you have in a month
    for that particular year and month
    '''
    domlist=["31","28","31","30","31","30","31","31","30","31","30","31"]
    if is_leap_year(year) and month==2:
        return "29"
    if is_leap_year(year) and month!=2:
        return domlist[month-1]
    if not is_leap_year(year):
        return domlist[month-1]


year=int(input("Enter the year :"))
month=int(input("Enter the month :"))
print(f"year {year} has {dom(year,month)} number of days in month {month}")
