year=input("enter the year")
year=int(year)
month=input("enter the month")
month=int(month)
def getTotalDaysFrom1990(year,month):
    """得到距离1990年1月1日有多少天"""
    num=0
    number_of_years=year-1990
    for cout_year in range(1990,year):
        if ((cout_year%4==0 and cout_year%100!=0)or(cout_year%400==0)):
            num+=1
    normal_months=[31,28,31,30,31,30,31,31,30,31,30,31]
    leap_year_months=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=0
    if ((year%4==0 and year%100!=0)or(year%400==0)):
        for month_day in leap_year_months[0:month-1]:
            days+=month_day
    else:
        for month_day in normal_months[0:month-1]:
            days+=month_day

    number_of_days=num*366+(number_of_years-num)*365+days
    return number_of_days

def getMonthStartDay(year,month):
    """得到所给定的月份的第一天是周几"""
    return (1+getTotalDaysFrom1990(year,month))%7

#开始打印日历表头
all_month=("January","February","March","April","May","June","July","August","September","October","Novewmber","December")
print("\t"+all_month[month-1]+"\t",end='')
print(year)
for i in range(0,40):
    print("-",end='')
print('')
all_week=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
for week in all_week:
    print(week+"\t",end='')
print('')
a=getMonthStartDay(year,month)
#开始打印日历，按照2月、有31天的月和有30天的月分类，分别打印

#2月类
if (month==2):
    if (year%400==0 or (year%4==0 and year%100!=0)):
            print("\t"*(a-1),end='')
            for d in range(1,8-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(8-a,15-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(15-a,22-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(22-a,29-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(29-a,30):
                print(str(d)+"\t",end='')
            print('')

    else:
        if (a==0):
            print("\t"*a,end='')
            for d in range(1,8-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(8-a,15-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(15-a,22-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(22-a,29):
                print(str(d)+"\t",end='')
            print('')
        else:
            print("\t"*a,end='')
            for d in range(1,8-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(8-a,15-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(15-a,22-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(22-a,29-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(29-a,29):
                print(str(d)+"\t",end='')
            print('')
#有31天的月
elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    if (a<=4):
            print("\t"*a,end='')
            for d in range(1,8-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(8-a,15-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(15-a,22-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(22-a,29-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(29-a,32):
                print(str(d)+"\t",end='')
            print('')
    else:
            print("\t"*a,end='')
            for d in range(1,8-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(8-a,15-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(15-a,22-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(22-a,29-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(29-a,36-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(36-a,32):
                print(str(d)+"\t",end='')
            print('')
#有30天的月
elif (month==4 or month==6 or month==9 or month==11):
    if (a<=5):
            print("\t"*a,end='')
            for d in range(1,8-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(8-a,15-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(15-a,22-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(22-a,29-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(29-a,31):
                print(str(d)+"\t",end='')
            print('')
    else:
            print("\t"*a,end='')
            for d in range(1,8-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(8-a,15-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(15-a,22-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(22-a,29-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(29-a,36-a):
                print(str(d)+"\t",end='')
            print('')
            for d in range(36-a,31):
                print(str(d)+"\t",end='')
            print('')
