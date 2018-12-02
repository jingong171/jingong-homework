#输入年月
year = input('请先输入年份：')
year = int(year)
month = input('请输入月份：')
month = int(month)
#打印日历第一行
def translate_month(month):
    if month == 1:
        return 'January'
    elif month == 2:
        return 'February'
    elif month == 3:
        return 'March'
    elif month == 4:
        return 'April'
    elif month == 5:
        return 'May'
    elif month == 6:
        return 'June'
    elif month == 7:
        return 'July'
    elif month == 8:
        return 'August'
    elif month == 9:
        return 'September'
    elif month == 10:
        return 'October'
    elif month == 11:
        return 'November'
    else :
        return 'December'
#一年有几天
def year_days(year):
    if year % 100 == 0 and year % 400 == 0:
        return 366
    elif year % 100 != 0 and year % 4 == 0:#闰年
        return 366
    else:
        return 365
#一个月有几天
def month_days(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif year_days(year) == 366:#闰年
        return 29
    else:
        return 28
#得到总天数
def gettotaldays(year,month):
    days = 0
    for i1 in range(1900,year):
        days = days + year_days(i1)
    for i1 in range(1,month):
        days = days + month_days(year,i1)
    return days
#该月的第一天是星期几
def getmonthstartday(year,month):
    return gettotaldays(year,month) % 7 +1
    

def print_month(year,month):
    print('\t',translate_month(month),'\t',year)
    print('Sun\tMon\tTues\tWed\tThu\tFri\tSat')
    for i2 in range(1,month_days(year,month)+getmonthstartday(year,month)+1):
        if i2<=getmonthstartday(year,month):
            print("\t",end="")
            continue
        print(i2-getmonthstartday(year,month),end="")
        print("\t",end="")
        if i2%7==0:
            print()

print_month(year,month)