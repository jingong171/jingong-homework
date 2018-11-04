year=input('请输入年份：')
year=int(year)
month=input('请输入月份：')
month=int(month)
months=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
print("\t"+ months[month-1] + "\t" + str(year))
print("------------------------------")
print("Sun  Mon  Tue  Wed  Thu  Fri  Sat")#日历标头
def leapyear(y):#判断某一年是否为闰年
    if y%4==0:
        if y%100==0:
            if y%400==0:
                a=1
            else:
                a=0
        else:
            a=1
    else:
        a=0
    return a
def month_days(y,m):#判断某一月有多少天
    if m==0:
        days=0
    if m==1 or m==3 or m==5  or m==7 or m==8 or m==10 or m==12:
        days=31
    if m==2:#判断该年是否为闰年,由此判断二月份有多少天
        b=leapyear(y)
        if b==1:
            days=29
        if b==0:
            days=28
    if m==4 or m==6 or m==9 or m==11:
        days=30
    return days
def getTotalDaysFrom1990(y,m):#定义一个函数，计算从1990年到该年一共有多少天
    start_year=1990#定义初始年为1990年
    getTotalDaysFrom1990=0#定义一个表示该年距1990年1月1日有多少天的变量
    while start_year != y:#把完整的年的天数加起来
        c=leapyear(start_year)
        if c==1:
            getTotalDaysFrom1990=getTotalDaysFrom1990 + 366
        if c==0:
            getTotalDaysFrom1990=getTotalDaysFrom1990 + 365
        start_year=start_year + 1
    start_month=1#定义该年的初始月份
    while start_month <= m:#把完整的月的天数加起来
        i=month_days(y,start_month-1)
        getTotalDaysFrom1990=getTotalDaysFrom1990+i
        start_month=start_month + 1
    return getTotalDaysFrom1990#返回值为该年该月第一天到1990.01.01的天数
def getMonthStartDay(y,m):
    return 1+getTotalDaysFrom1990(y,m)%7
firstday=getMonthStartDay(year,month)#这个值为该年该月第一天的星期
ds=month_days(year,month)#这个值为该月的天数
count=0#定义一个逢7必回车的变量
k=0#定义一个从头开始计数的变量
while k< firstday:#计算第一周有几天是空格
    k=k+1
    print("     ",end="")
    count=count+1
    if count%7==0:
        print("\n")
day=1#开始显示这个月的第一天
while day <= ds:#开始形成日历
    if day < 10:
        print(str(day) + "    ",end="")
    else:
        print(str(day) + "   ",end="")
    day=day+1
    count=count+1
    if count%7==0:
        print("\n")
