def leap_year(year):
    if year%4==0:
        return True
    else:
        return False
def monthdays(year,month):
    days = 31
    if month == 2 :
        if leap_year(year):
            days=29
        else:
            days=28
    elif month==4 or month==6 or month==9 or month==11:
        days=30
    return days
def totaldays(year,month):
    totaldays=0
    for i in range(1990,year):
        if leap_year(i):
            totaldays+=366
        else:
            totaldays+=365
    for i in range(1,month):
        totaldays+=monthdays(year,month)
    return totaldays
year=input("please input the year:")
year=int(year)
month=input("please input the month:")
month=int(month)
primarycount=0
print('日\t一\t二\t三\t四\t五\t六')
i=1
for i in range((totaldays(year,month)%7)+1):
    print("\t")
    primarycount+=1
for i in range(1,monthdays(year,month)):
    print( i,"\t",end='')
    primarycount+=1
    if primarycount%7==0:
        print ("\n")

    
