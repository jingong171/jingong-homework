#判断是否为闰年
def is_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        return True
    else:
        return False
#判断月份有多少天
def get_month_day(year,month):
    if month in [4,6,9,11]:
        days = 30
    elif month == 2:
        if is_leap_year(year):
            days = 29
        else:
            days = 28
    else:
        days = 31
    return days
#求输入年份和月份日期总天数
def get_days(year,month):
    totaldays = 0
    for i in range(1900,year):
        if is_leap_year(i):
            totaldays += 366
        else:
            totaldays += 365
    for i in range(1,month):
        totaldays += get_month_day(year,i)
    return totaldays
#主程序
year = input("请输入年份：")
year = int(year)
if year < 1900:
    print("输入年份有误")
else:
    month = input("请输入月份：")
    month = int(month)
    if month < 1 or month > 12:
        print("输入月份有误")
    else:
        print(str(year)+"年"+str(month)+"月"+"万年历")
        print('日\t一\t二\t三\t四\t五\t六')
        count = 0
        for i in range(0,(get_days(year,month)%7)+1):
            print('\t',end='')
            count += 1
        for i in range(1,get_month_day(year,month)+1):
            print(str(i)+'\t',end='')
            count += 1
            if count%7 == 0:
                print('\n',end='')
