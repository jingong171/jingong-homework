year=int(input("请输入年份:"))
month=int(input("请输入月份:"))
def leap_year(year):#判断是否为闰年
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
def getMonthTotalDays(year,month):#计算当月有几天
    if month==2:
        if leap_year(year):
            days =29
        else:
            days =28
    elif month==4 or month==6 or month==9 or month==11:
        days= 30
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        days= 31
    return days
def getTotalDaysFrom1990(year,month):
    TotalDaysFrom1990=0
    for a in range(1990,year):
        if leap_year(a):
            YearDays=366 
        else:
            YearDays=365
        TotalDaysFrom1990+=YearDays
    for b in range(1,month):
        TotalDaysFrom1990+=getMonthTotalDays(year,b)
    return TotalDaysFrom1990
StartDay=1+getTotalDaysFrom1990(year,month)%7
print("一\t二\t三\t四\t五\t六 \t日")
print(" ",end="")
for m in range(1,StartDay):#日历初始空格
    print("\t",end="")
a=0
for n in range(1,getMonthTotalDays(year,month)+1):
    print(n,"\t",end="")
    a+=1
    if a==8-StartDay or a==15-StartDay or a==22-StartDay or a==29-StartDay or a==36-StartDay:
        print("")
        print(" ",end="")
    


