LeapYearMonthDays=[31,29,31,30,31,30,31,31,30,31,30,31]#闰年各月天数
MonthDays=[31,28,31,30,31,30,31,31,30,31,30,31]        #非闰年各月天数
Months=["Januray","February","March","April","May","June",
        "July","August","September","October","November","December"]#各月名称

def getMonthStartDay(TotalDays):#计算给定月第一天是星期几
    return 1+TotalDays%7

def getTotalDaysFrom1990(year,month):  #计算从1990.01.01到给定月份之前经历天数
    TotalDays=0
    for i in range(1990,year):         #找出给定年份以前的闰年和非闰年
        if i%4!=0:
            TotalDays += 365           #非闰年天数加365
            for j in range(1,month):
                TotalDays += MonthDays[j-1] #非闰年给定月前经历天数
        elif i%4==0 and i%100!=0:
            TotalDays += 366           #闰年天数加366
            for j in range(1,month):
                TotalDays += LeapYearMonthDays[j-1] #闰年给定月前经历天数
        elif i%100==0 and i%400==0:
            TotalDays += 366
            for j in range(1,month):
                TotalDays += LeapYearMonthDays[j-1]
        else:
            TotalDays += 365
            for j in range(1,month):
                TotalDays += MonthDays[j-1]
    return TotalDays

def getGivenMonthDays(year,month):     #根据给定年是否为闰年，计算给定月天数
    if year%4!=0:
        GivenMonthDays=MonthDays[month-1]
    elif year%4==0 and year%100!=0:
        GivenMonthDays=LeapYearMonthDays[month-1]
    elif year%100==0 and year%400==0:
        GivenMonthDays=LeapYearMonthDays[month-1]
    else:
        GivenMonthDays=MonthDays[month-1]
    return GivenMonthDays

year=input("year:")
month=input("month:")
TotalDays=getTotalDaysFrom1990(int(year),int(month))
FirstDay=getMonthStartDay(TotalDays)
GivenMonthDays=getGivenMonthDays(int(year),int(month))

print("The Calendar of "+Months[int(month)-1]+" "+year+":")
print("                    "+Months[int(month)-1]+"  "+year)
print("---------------------------------------------------------")
print("Monday Tuesday Wednesday Thursday Friday  Saturday Sunday")
print("         "*(FirstDay-1),end="") #日历中给定月1号之前位置用空格填充
for j in range(1,GivenMonthDays+1):    #给定月所有天遍历
    if (j-(1+7-FirstDay))%7!=0:        #日期与第一周最后一天的差不是7的整数倍
        if j<10:                       #美观设计：日期位数为个位数的多空一格
            print(j,end="        ")
        else:
            print(j,end="       ")
    else:                              #日期与第一个星期最后一天的差是7的整数倍
        print(j,end="\n")
