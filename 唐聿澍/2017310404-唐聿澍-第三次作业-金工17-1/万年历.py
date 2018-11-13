def leapYear(year):#判断是否闰年
    if year % 400 == 0:
        return 1
    elif year % 4 == 0 and year % 100 != 0:
        return 1
    else:
        return 0

def getTotalDaysFrom1990(year,month):#计算从1990.01.01开始的日数
    
    totalDays = 0 #加和天数
    for y in range(1991,year+1):#计算年数中的日数
        if leapYear(y-1) == 1:
            totalDays = 366 + totalDays
        else:
            totalDays = 365 + totalDays

    for m in range(2,month+1):#计算月数中的日数
        if m-1 in month31List:
            totalDays = 31 + totalDays
        elif m-1 == 2 and leapYear(year) == 0:
            totalDays = 28 + totalDays
        elif m-1 == 2 and leapYear(year) == 1:
            totalDays = 29 + totalDays
        else:
            totalDays = 30 + totalDays
    return totalDays

def getMonthStartDay(year,month):#判断星期几
    return 1 + getTotalDaysFrom1990(year,month) % 7

def getMonthDays(month):#本月的日数
    if month in month31List:
        return 31
    elif month == 2 and leapYear(year) == 1:
        return 29
    elif month == 2 and leapYear(year) == 0:
        return 28
    else:
        return 30


numberOfMonth = ['January','February','March','April','May','June','July','August','September','October','November','December']
month31List = [1,3,5,7,8,10,12]#31天月份的列表

year = int(input("请输入年："))
month = int(input("请输入月份："))
print("\t" + str(numberOfMonth[month-1]) + "\t" + str(year))#打印抬头
print("——————————————————————————")
print("Sun" + "\t" + "Mon" + "\t" + "Tue" + "\t" + "Wed" + "\t" + "Thu" + "\t" + "Fri" + "\t" + "Sat")

n = 0#计数换行

if getMonthStartDay(year,month) != 7:#解决周日（7）在周一（1）前的问题
    for blank in range(1,getMonthStartDay(year,month) + 1):
        print("\t" , end = '')
        n += 1

for num in range(1,getMonthDays(month) + 1):
    print(str(num) + "\t" , end = '')
    n += 1
    if n % 7 == 0:
        print('\n')#计数换行
