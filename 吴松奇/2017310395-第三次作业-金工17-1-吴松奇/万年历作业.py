def getMonthStartDay(year,month):
    def getMonthDaysFrom1990(year,month):
        numbers1=0
        #m,n,p均为判断某年是否是闰年的参数
        year_=year
        #存储year的数值
        while year>=1990:
            year=year-1
            m=year%100
            n=year%400
            p=year%4
            if m==0 and n==0:
                numbers1=numbers1+1
            if m!=0 and p==0:
                numbers1=numbers1+1
        year=year_
        #判断从1990年到该年(不算概念)共有几个闰年(numbers1 个闰年)
        numbers2=year-numbers1-1990
        #从1990年到该年共有几个平年(numbers2个平年)
        days=(numbers1)*366+numbers2*365
        #从1990到该年其中的整年共有的天数
        if month>2:
            m=year%100
            n=year%400
            p=year%4
            if (m==0 and n==0) or (m!=0 and p==0):
                days=days+1
        #增加该年为闰年时2月多出来的一天
        if month==2:
            days=days+31
        if month==3:
            days=days+31+28
        if month==4:
            days=days+31+28+31
        if month==5:
            days=days+31+28+31+30
        if month==6:
            days=days+31+28+31+30+31
        if month==7:
            days=days+31+28+31+30+31+30
        if month==8:
            days=days+31+28+31+30+31+30+31
        if month==9:
            days=days+31+28+31+30+31+30+31+31
        if month==10:
            days=days+31+28+31+30+31+30+31+31+30
        if month==11:
            days=days+31+28+31+30+31+30+31+31+30+31
        if month==12:
            days=days+31+28+31+30+31+30+31+31+30+31+30
        #加上该年过去的天数
        return days
    return 1+getMonthDaysFrom1990(year,month)%7
#返回值为星期数
year=int(input("请输入年"))
month=int(input("请输入月"))
number=getMonthStartDay(year,month)
number_=number
#存储number的数字
print("    ",end="")
print(month,end="")
print("    ",end="")
print(year)
#打印日历年月
print("--------------------------------")
print("Sun".center(8," ")+"Mon".center(8," ")+"Tue".center(8," ")+"Wed".center(8," ")+"Thu".center(8," ")+"Fri".center(8," ")+"Sat".center(8," "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    d=31
    #判断该月是否为大月
if month==4 or month==6 or month==9 or month==11:
    d=30
numbers1=0
if month==2:
    numbers=0
    m=year%100
    n=year%400
    p=year%4
    if m==0 and n==0:
        numbers1=numbers1+1
    if m!=0 and p==0:
        numbers1=numbers1+1
    if numbers1==1:
        d=29
    else:
        d=28
date=1
#该月起始日的日期
while number>0:
    print(str().center(8," "),end="")
    number=number-1
#使得开始日期对应所在星期数
while d>0:
    print("  ",end="")
    print(str(date).center(6," "),end="")
    m=(number_+date)%7
    #判断是否开始新的一周
    if m==0:
        print("")
    date=date+1
    d=d-1
        
