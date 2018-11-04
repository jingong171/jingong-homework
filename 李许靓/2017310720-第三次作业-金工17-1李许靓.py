def leapnum(year):          #设置函数计算这一年之前一共有几个闰年
    sum=0
    for i in range(1990,year):
        if (i % 100 != 0 and i % 4 == 0) or i % 400 == 0:
            sum=sum+1
    return sum


def is_leap_year(year):                 #判断这一年是不是闰年
    if (year % 100 != 0 and year%4==0)or year%400==0:
        return True
    else:
        return False


def getTotalDaysFrom1990(year,month):  #返回距1990年1月1日的天数
    if year!=1990:
        sum=leapnum(year)              #计算这一年之前（包括这一年）一共有几个闰年
    else:
        sum=0
    if is_leap_year(year):                  #计算这一年有几天
        if month==1:
            days=0
        elif month==2:
            days=31
        elif month==3:
            days=60
        elif month==4:
            days=91
        elif month==5:
            days=121
        elif month==6:
            days=152
        elif month==7:
            days=182
        elif month==8:
            days=213
        elif month==9:
            days=244
        elif month==10:
            days=274
        elif month==11:
            days=305
        elif month==12:
            days=335
    else:
        if month==1:
            days=0
        elif month==2:
            days=31
        elif month==3:
            days=59
        elif month==4:
            days=90
        elif month==5:
            days=120
        elif month==6:
            days=151
        elif month==7:
            days=181
        elif month==8:
            days=212
        elif month==9:
            days=243
        elif month==10:
            days=273
        elif month==11:
            days=304
        elif month==12:
            days=334
    totaldays=sum*366+(year-sum-1990)*365+days
    return totaldays

#返回给定月的1日是星期几，由1990.01.01是星期一推算
def getMonthStartDay(year,month):
    return getTotalDaysFrom1990(year,month)%7+1


#判断这个月一共有几天
def getday(year,month):
    if is_leap_year(year):
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            day=31
        elif month==2:
            day=29
        else:
            day=30
    else:
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            day=31
        elif month==2:
            day=28
        else:
            day=30
    return day


year=input("请输入年份:")
month=input("请输入月份:")
year=int(year)
month=int(month)
day=getday(year,month)
startday=getMonthStartDay(year,month)
print(startday)      #计算该月第一天是星期几
print("Sun"+'\t'+"Mon"+'\t'+'Tue'+'\t'+"Wed"+'\t'+"Thu"+'\t'+'Fri'+'\t'+"Sat")

count=0   #用来控制换行
for i in range(1,startday+1):
    print(" "+"\t",end="")
    count+=1
p=1   #打印日期
while p<=day:
    print(str(p) +'\t',end="")
    count+=1
    p+=1
    if count%7==0:
        print("\n")
print('\n')
