 #定义一个函数判断是否为闰年
def Leapyear(year):
    if (year%4 == 0 and year != 0) or (year%400 == 0):
        return True
    else:
        return False
#定义一个函数判断每一个月份有多少天
def get_month_day(year,month):
    solar_month = [1,3,5,7,8,10,12]
    lunar_month = [4,6,9,11]
    if month in solar_month:
        return 31
    elif month in lunar_month:
        return 30
    elif month == 2:
        if Leapyear(year):
            return 29
        else:
            return 28
#计算总的天数
def getTotalDaysFrom1990(year,month):
    totaldays=0
    #计算完整的年的天数
    for y in range(1990,year):
        if Leapyear(y):
            totaldays += 366
        else:
            totaldays += 365
    for m in range(1,month):
        totaldays = totaldays + get_month_day(year,m)
    return totaldays

#计算打印月份的第一天是星期几
def getMonthStartDay(year,month):
    return getTotalDaysFrom1990(year,month)%7+1
#主函数
flag = True
while flag:
    year = input("输入年份")
    month = input("输入月份")
    year =  int(year)
    month = int(month)
    if month not in range(1,13):
        print("输入的月份无效，请重新输入")
        continue
    if year <1990:
        print\
               ("输入的年份无效，请重新输入")
        continue
    else:
        flag = False
        print("\t"+str(year)+" 年 "+str(month)+ " 月")
        print("Sun\tMon\tTue\tWed\tTue\tFri\tSat")
        iCount = 0
        for i in range(0,getMonthStartDay(year,month)):
            print (" ",end="\t")
            iCount = iCount+1
            if iCount%7 == 0:
                print("\n")
        for i in range(1,get_month_day(year,month)+1):
            print (str(i),end="\t")
            iCount = iCount+1
            if iCount%7 == 0:
                print("\n")
                
                
            
            

















