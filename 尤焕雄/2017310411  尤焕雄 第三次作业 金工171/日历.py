def getdaysofcertainyear(year):
    """求某一年的天数"""
    if year%4==0 and year%100!=0:
        a=366
    elif year%100==0 and year%400==0:
        a=366
    else:
        a=365
    return a
def getdaysofyears(year):
    """求到1990年的整年部分的天数"""
    if year==1990:
        return 0
    else:
        return getdaysofcertainyear(year-1)+getdaysofyears(year-1)
def getdayswithmonth(year,month):
    """求某一年到某一月份之前的总天数"""
    sum=0
    if getdaysofcertainyear(year)==366:
        monthdays1=[31,29,31,30,31,30,31,31,30,31,30,31]
        for i in range(0,month-1):
            sum=sum+monthdays1[i]
    else:
        monthdays2=[31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(0,month-1):
            sum=sum+monthdays2[i]
    return sum
def getTotalDaysFrom1990(year,month):
    return getdaysofyears(year)+getdayswithmonth(year,month)
def getMonthStartDay(year,month):
    return 1+getTotalDaysFrom1990(year,month)%7
def print_calendar():
    year=input("请输入年份")
    month=input("请输入月份")
    year=int(year)
    month=int(month)
    print("Sun\tMon\tTue\tWed\tTur\tFri\tSat")
    if getMonthStartDay(year,month)==7:
        print("",end="")
    else:
        print((getMonthStartDay(year,month)*8)*" ",end="")
        """下面求该月总天数"""
    if getdaysofcertainyear(year)==366:
        monthdays1=[31,29,31,30,31,30,31,31,30,31,30,31]
        b=monthdays1[month-1]
    else:
        monthdays2=[31,28,31,30,31,30,31,31,30,31,30,31]
        b=monthdays2[month-1]
    for i in range(1,b+1):
        if (i+getMonthStartDay(year,month))%7==0:
            print(str(i),end="\n")
        elif i<10:
            print(str(i)+" "*7,end="")
        else:
            print(str(i)+" "*6,end="")
print_calendar()
        
    
