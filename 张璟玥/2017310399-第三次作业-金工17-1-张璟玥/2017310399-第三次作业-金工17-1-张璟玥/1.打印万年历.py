def start():
    year = input("请输入年：")
    month = input("请输入月份:")

def year_days(year):
    if year % 100 == 0 and year % 400 == 0:
        return 366
    elif year % 100 != 0 and year % 4 == 0:
        return 366
    else:
        return 365

def month_days(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif year_days(year) == 366:
        return 29
    else:
        return 28

def gettotaldaysfrom1990(year,month):
    days = 0
    for i1 in range(1900,year):
        days = days + year_days(i1)
    for i1 in range(1,month):
        days = days + month_days(year,i1)
    return days

def getmonthstartday(year,month):
    return 1+gettotaldaysfrom1990(year,month)%7

def print_month(year,month):
    print('Sun       Mon       Tues      Wed       Thu       Fri       Sat')
    print((10 * getmonthstartday(year,month) - 10) * ' ',end = '')
    for i2 in range(1,month_days(year,month)+1):
        print('',i2, (8 - len(str(i2))) * ' ', end='')
        if getmonthstartday(year,month) == 7:
            print('\t')
