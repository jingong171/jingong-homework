year=int(input("请输入年："))
month=int(input("请输入月份："))
#输入年月
months={1:'January',2:'Feburary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
#设置月份对应的英文
monthday={1:31,2:0,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#设置除2月外每月对应的天数
print("   \t"+str(months[month])+"\t"+str(year))
print("-"*40)
print("Sun\t"+"Mon\t"+"Tue\t"+"Wed\t"+"Thu\t"+"Fri\t"+"Sat\t")
def getRNnumber(year):
    RNnumber=0
    y=1990
    while y<year:
        if y%4==0:
            RNnumber+=1
        y+=1
    return RNnumber
#计算目前为止闰年的个数
def getyeardays(year,month):
    if month<2:
        return 31
    else:
        if year%4==0:
            mon=1
            yeardays=0
            while mon<month:
                yeardays+=monthday[mon]
                mon+=1
            return yeardays+29
        else:
            mon=1
            yeardays=0
            while mon<month:
                yeardays+=monthday[mon]
                mon+=1
            return yeardays+28
#计算本年到上个月为止的天数
def getMonthStartDay(year,month):
    a=1+getTotalDaysFrom1990(year,month)%7
    if a==7:
        return 0
    else:
        return a
#计算应该从周几开始本月日历
def getTotalDaysFrom1990(year,month):
    if month>2:
        return (year-1990)*365+getRNnumber(year)+getyeardays(year,month)
    else:
        return (year-1990)*365+getRNnumber(year)+getyeardays(year,month)-1
#计算当前到1990年1月1日一共多少天
def getspace(num):
    if num<10:
        return str(num)+"       "
    else:
        return str(num)+"      "
#打印不同数量的空格使万年历整齐
for n in range(1,8):
    if n<=getMonthStartDay(year,month):
        print(end=" "*8)
    elif n<7:
        num=n-getMonthStartDay(year,month)
        print(end=getspace(num))
    else:
        num=n-getMonthStartDay(year,month)
        print(getspace(num))
for n in range(8,15):
    if n<14:
        num=n-getMonthStartDay(year,month)
        print(end=getspace(num))
    else:
        num=n-getMonthStartDay(year,month)
        print(getspace(num))
for n in range(15,22):
    if n<21:
        num=n-getMonthStartDay(year,month)
        print(end=getspace(num))
    else:
        num=n-getMonthStartDay(year,month)
        print(getspace(num))
for n in range(22,29):
    if n<28:
        num=n-getMonthStartDay(year,month)
        print(end=getspace(num))
    else:
        num=n-getMonthStartDay(year,month)
        print(getspace(num))

if month==4 or month==6 or month==9 or month==11:
    m=31+getMonthStartDay(year,month)
elif month==2:
    if year%4!=0:
        m=29+getMonthStartDay(year,month)
    else:
        m=30+getMonthStartDay(year,month)
else:
    m=32+getMonthStartDay(year,month)
for n in range(29,m):
    if n<m<35:
        num=n-getMonthStartDay(year,month)
        print(end=getspace(num))
    elif n==35 or n==m:
        num=n-getMonthStartDay(year,month)
        print(getspace(num))
    else:
        num=n-getMonthStartDay(year,month)
        print(end=getspace(num))
        
#打印万年历
