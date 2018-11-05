def Leap_year(year):#判断一年是否是闰年
    if ((year%4==0 and year%100!=0) or (year%400==0)):
            return True
    else:
            return False
def getTotalDaysFrom1990(year,month):#得到1990年以来总天数（不包含当前月份）
    years=year-1990
    Days_in_one_year=[0,31,59,90,120,151,181,212,243,273,304,334,365]#平年每个月之前的天数
    num1=years*365+int(years/4)-int(years/100)+int(years/400)+Days_in_one_year[month-1]
    if (Leap_year(year) and month>2):
        return num1+1
    else:
        return num1
def getMonthStartDay(year,month,date=0):#date这个默认参数后面会在输出日历回车问题用到
    return 1+(date+getTotalDaysFrom1990(year,month))%7
def print_Month_start_weekday(year,month):
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
    return week[getMonthStartDay(year,month)-1]
def get_Month(month):
    month1=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month1[month-1]
def get_date(year,month):#每个月有多少天
    la_month=[1,3,5,7,8,10,12]
    li_month=[4,6,9,11]
    if month in la_month:
        return 31
    if month in li_month:
        return 30
    if month==2:
        if Leap_year(year):
            return 29
        if not Leap_year(year):
            return 28
def print_calender():#输出万年历（主函数）
    week = ["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    i=0
    day=1
    year=int(input("Please enter the year:  "))
    month=int(input("Please enter the month:  "))
    print(get_Month(month),"\n"+"-"*52)#输出月份
    print(week[0]+"\t"*2+week[1]+"\t"*2+week[2]+"\t"*2+week[3]+"\t"*2+week[4]+"\t"*2+week[5]+"\t"*2+week[6])#输出表头
    while print_Month_start_weekday(year,month)!=week[i]:#通过循环确定一个月第一天是星期几
        i+=1
    print("\t"*(i*2)+str(day),'\t'*2,end='')#输出这个月的第一天
    for m in list(range(day+1,get_date(year,month)+1)):#输出剩余的天数并利用制表符进行对齐
        if getMonthStartDay(year,month,m-1)==7:
            print()
        print(m,"\t"*2,end='')
print_calender()