def isLeapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def getTotalDaysFrom1990(year,month):
    days=0
    for y in range(1990,year):
        if isLeapYear(y):
            days += 366
        else:
            days += 365
    for m in range(1,month):
        if m in [1,3,5,7,8,10,12]:
            days += 31
        elif m in [4,6,9,11]:
            days += 30
        elif m==2:
            if isLeapYear(year):
                days += 29
            else:
                days += 28
    return days

def getMonthStartDay(year,month):
    return 1+getTotalDaysFrom1990(year,month)%7

year = int(input("请输入年份: "))
month = int(input("请输入月份: "))
print("\n"+"             "+str(month)+"          "+str(year)+"\n")
print("________________________________________________"+"\n")
print("日\t一\t二\t三\t四\t五\t六")
if getMonthStartDay(year,month)!=7:
    for i in range(1,getMonthStartDay(year,month)+1):
        print("\t",end='')
    for i in range(1,getTotalDaysFrom1990(year,month+1)-getTotalDaysFrom1990(year,month)+1):
        if getMonthStartDay(year,month)!=6:
            if i==7-getMonthStartDay(year,month)or (i+getMonthStartDay(year,month))%7==0:
                print(str(i)+"\n")
            else:
                print(str(i)+"\t",end="")
        else:
            if i==1 or i%7==1:
                print(str(i)+"\n")
            else:
                print(str(i)+"\t",end="")
if getMonthStartDay(year,month)==7:
    for i in range(1,getTotalDaysFrom1990(year,month+1)-getTotalDaysFrom1990(year,month)+1):
        if i%7==0:
            print(str(i)+"\n")
        else:
            print(str(i)+"\t",end="")


