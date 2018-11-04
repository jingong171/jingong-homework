#判断1990年至该年有多少个闰年
def judgenumber(year):
    leap = 0
    for year in range(1990, year) :
        if (year%4 == 0 and (year%100 != 0 or year%400 == 0) ) :
            leap += 1
    return leap

#判断该年是不是闰年
def judge(year):
    judgement=0
    if (year%4 == 0 and (year%100 != 0 or year%400 == 0) ) :
        judgement=1
    return judgement

#判断一年的各个月有多少天
def daysofmonth(year,month):
    days=0
    if month in (1,3,5,7,8,10,12):
        days = 31
    elif month in (4,6,9,11):
        days = 30
    else:
        if judge(year) == 1:
            days = 29
        else :
            days = 28
    return days

#计算该年中该月前有多少天
def DaysofOneyear(year,month):
    Days=0
    t=1
    while t<month:
        Days += daysofmonth(year,t)
        t += 1
    return Days

#计算从1990年1月1日至该年该月过了多少天
def getTotalDaysFrom1990(year,month):
    days = 365*(year-1990)+judgenumber(year)+DaysofOneyear(year,month)
    return days

#返回给定月的1日是星期几，由1990.01.01是星期一推算
def getMonthStartDay(year,month):
	return 1+getTotalDaysFrom1990(year,month)%7

#打印日历
def printRiLi(year,month):
    print('\t'+str(year)+"年"+'\t'+str(month)+"月")
    print('Sun\t'+'Mon\t'+'Tue\t'+'Wed\t'+'Thu\t'+'Fri\t'+'Sat')
    N = getMonthStartDay(year,month)
    n=0
    while n<N:
        print(' \t',end='')
        n += 1
    m=1
    D=daysofmonth(year,month)
    while m < D+1:
        print(str(m)+'\t',end='')
        m += 1
        n += 1
        if n%7==0:
            print('\n')
        
Y=int(input('请输入您要查询的年份（1990—）：\t'))
while Y<1990:
    Y=int(input('年份输入错误，请重新输入：\t'))
M=int(input('请输入您要查询的月份：\t'))
while M not in range(1,13):
    M=int(input('月份输入错误，请重新输入：\t'))
year=Y
month=M
printRiLi(year,month)


