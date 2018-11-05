year = int(input("请输入年份: "))
month = int(input("请输入月份: "))
def isLeap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False
    
def getTotalDaysFrom1990(year,month):
    Days=0
    for i in range (1990,year):
        if isLeap(i):
            Days=Days+366
        else:
            Days=Days+365
    MonthDays=0
    for i in range(1,month):
        if i==2:
            if isLeap(year):
                MonthDays=MonthDays+29
            else:
                MonthDays=MonthDays+28
        elif i in [4,6,9,11]:
            MonthDays=MonthDays+30
        else:
            MonthDays=MonthDays+31
    TotalDays=Days+MonthDays
    return TotalDays
        
def getMonthStartDay(year,month):
    return 1+getTotalDaysFrom1990(year,month)%7
print("\n"+"             "+str(month)+"          "+str(year)+"\n")
print("________________________________________________"+"\n")
print("日\t一\t二\t三\t四\t五\t六")
if getMonthStartDay(year,month)!=7:
    for i in range(1,getMonthStartDay(year,month)+1):
        print("\t",end='')
    for i in range(1,getTotalDaysFrom1990(year,month+1)-getTotalDaysFrom1990(year,month)+1):
        if getMonthStartDay(year,month)==6:
            if i==1 or i%7==1:
                print(str(i)+"\n")
            else:
                print(str(i)+"\t",end="")
        else:
            if i==7-getMonthStartDay(year,month)or (i+getMonthStartDay(year,month))%7==0:
                print(str(i)+"\n")
            else:
                print(str(i)+"\t",end="")
if getMonthStartDay(year,month)==7:
    for i in range(1,getTotalDaysFrom1990(year,month+1)-getTotalDaysFrom1990(year,month)+1):
        if i%7==0:
            print(str(i)+"\n")
        else:
            print(str(i)+"\t",end="")
            
                
