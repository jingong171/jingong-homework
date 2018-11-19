#计算该月的天数
def daysOfMonth(year,month):
    year=int(year)
    month=int(month)
    if (year%4==0 and year%100!=0) or (year%400==0):
        flag=1
    else:
        flag=0
    j=month
    if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
        days=31
    if j==4 or j==6 or j==8 or j==11:
        days=30
    if flag==1 and j==2:
        days=29
    if flag==0 and j==2:
        days=28
    return days
#计算输入年份到90年1月1日的天数
def getTotalDaysFrom1990(year,month):
    #计算输入年份到90年中有多少个闰年
    n=0
    totaldays=0
    year=int(year)
    month=int(month)
    for i in range(1990,int(year)+1):
        if (i%4==0 and i%100!=0) or (i%400==0):
            n=n+1
    if (year%4==0 and year%100!=0) or (year%400==0):
        flag=1
    else:
        flag=0
    m=year-1990-n#除了闰年的年数        
    #除了本年距离1990的总天数
    totaldays=m*365+n*366
    for  j in range(1,month+1):
        if j==1 or j==3 or j==5 or j==7 or j==8 or j==10 or j==12:
            days=31
        if j==4 or j==6 or j==9 or j==11:
            days=30
        if flag==1 and j==2:
            days=29
        if flag==0 and j==2:
            days=28
        totaldays=totaldays+days#加上本年到所求月的天数
    return totaldays
#计算每月的一号是星期几
def getMonthStartDay(year,month):
    return 1+(getTotalDaysFrom1990(year,month)-daysOfMonth(year,month))%7

#g构造日历
def Calendar(year,month):
    year=int(year)
    month=int(month)
    print(str(month)+"  "+str(year))
    print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
    
    #打出初始星期之前的空格
    b=0
    for m in range(1,getMonthStartDay(year,month)+1):
        if m==7:
            break
        if m!=7:
            print("\t",end="")
        b=b+1
    #打出这个月的天数
    for k in range(1,daysOfMonth(year,month)+1):                     
        
        if (k+b-1)%7==0:
            print("\n")
        print(str(k)+"\t",end=" ")
def show():
    year=input("请输入年份:\t")
    month=input("请输入月份:\t")
    Calendar(year,month)

show()        
        
    
