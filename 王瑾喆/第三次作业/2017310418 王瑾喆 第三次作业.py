year=input("输入年份")
month=input("输入月份")
year=int(year)
month=int(month)


#编写判断是否为闰年的函数
def judge_leap_year(a):
    if a%4==0 & a%100!=0 or a%400==0:
        return 0
    else:
        return 1


#编写计算所输入的年份月份距离1990年1月1日有多少天的函数
def get_total_days_from1990(year,month):
    normal=[31,28,31,30,31,30,31,31,30,31,30,31]
    leap_year=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=0
    num=0
    number_of_years=year-1990
    for cout_year in range(1990,year):
        if ((cout_year%4==0 and cout_year%100!=0)or(cout_year%400==0)):
            num+=1
    if ((year%4==0 and year%100!=0)or(year%400==0)):
        for month_day in leap_year[0:month-1]:
            days+=month_day
    else:
        for month_day in normal[0:month-1]:
            days+=month_day

    number_of_days=num*366+(number_of_years-num)*365+days
    return number_of_days



#编写计算所输入的月份的1号是周几的函数
def get_month_start_day(year,month):
    
    return (1+ get_total_days_from1990(year,month))%7


#编写计算输入月份有几天的函数
def get_total_day_of_the_month(month):
    the_day_of_the_month=0;
    if month in[1,3,5,7,8,10,12]:
        the_day_of_the_month=31
    if month in[4,6,9,11,]:
        the_day_of_the_month=30
    if judge_leap_year(year)==0 & month==2:
        the_day_of_the_month=29
    if judge_leap_year(year)==1 & month==2:
        the_day_of_the_month=28
    return the_day_of_the_month


#打印日历表头
all_month=("January","Febuary","March","April","May","June","July","August","September","November","December")
print("\t"+all_month[month-1]+"\t",end='')
print(year)
for i in range(0,40):
    print("-",end='')
print('')
all_week=("Sun","Mon","Tue","Wed","Thr","Fri","Sat")
for week in all_week:
    print(week+" \t",end='')
print('')


a=get_month_start_day(year,month)


#根据该月份有几天进行数字打印
if get_total_day_of_the_month(month)==31:
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
if get_total_day_of_the_month(month)==30:
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


