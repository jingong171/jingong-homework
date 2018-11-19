year = int(input("请输入年份: "))
month = int(input("请输入月份: "))
#计算是否为闰年
def LeapYear(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False
    
#计算1990年以来的总天数
def TotalDaysFrom1990(year,month):
    Days=0
    for y in range (1990,year):
        if LeapYear(y):
            Days=Days+366
        else:
            Days=Days+365
#计算每个月有多少天
    Days/Month=0
    for m in range(1,month):
        if m==2:
            if LeapYear(year):
                Days/Month=Days/Month+29
            else:
                Days/Month=Days/Month+28
        elif i in [4,6,9,11]:
            Days/Month=Days/Month+30
        else:
            Days/Month=Days/Month+31
    TotalDays=Days+Days/Month
    return TotalDays
        
#计算周
def MonthStartDay(year,month):
    return 1+TotalDaysFrom1990(year,month)%7
print("\n"+"             "+str(month)+"          "+str(year)+"\n")
print("________________________________________________"+"\n")
print("日\t一\t二\t三\t四\t五\t六")
if MonthStartDay(year,month)!=7:
    for w in range(1,MonthStartDay(year,month)+1):
        print("\t",end='')
    for w in range(1,TotalDaysFrom1990(year,month+1)-TotalDaysFrom1990(year,month)+1):
        if MonthStartDay(year,month)==6:
            if w==1 or w%7==1:
                print(str(w)+"\n")
            else:
                print(str(w)+"\t",end="")
        else:
            if w==7-MonthStartDay(year,month)or (w+MonthStartDay(year,month))%7==0:
                print(str(w)+"\n")
            else:
                print(str(w)+"\t",end="")
if MonthStartDay(year,month)==7:
    for w in range(1,TotalDaysFrom1990(year,month+1)-TotalDaysFrom1990(year,month)+1):
        if w%7==0:
            print(str(w)+"\n")
        else:
            print(str(w)+"\t",end="")
