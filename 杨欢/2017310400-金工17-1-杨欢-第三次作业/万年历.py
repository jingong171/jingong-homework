year=int(input("请输入年："))
month=int(input("请输入月："))

#一个月第一天的星期
def getMonthStartDay(year,month):
    return 1+getTotalDaysFrom1990(year,month)%7

#本年本月1日距本年元旦的天数（不算今年2月天数与30的差）
def getTotalDaysFrom1990_m(year,month):
    if (month==1):
        return 0
    else:
        if (((month-1)<=7 and (month-1)%2==1)or((month-1)>=8 and (month-1)%2==0)):
            day_m=getTotalDaysFrom1990_m(year,month-1)+31
        else:
            day_m=getTotalDaysFrom1990_m(year,month-1)+30
        return day_m

#验证平年闰年函数，闰年返回true
def judge(year):
    if ((year%4==0 and year%100!=0) or year%400==0):
        return True
    else:
        return False
#本年1月1日距1990年1月1日的天数减去今年2月（如果有）天数与30的差
def getTotalDaysFrom1990_y(year,month):
    if (year==1990):
        return 0
    else:
        #闰年366天，上一年为闰年，且月份小于2的，经历了闰年2月；大于2的，经历了平年二月
        #本年为闰年，且月份大于二的，经历了闰年二月；小于二的，经历了平年二月
        if (judge(year-1)):
            day_y=getTotalDaysFrom1990_y(year-1,1)+366
            if(month>2):
                day_y=day_y-2
        #非闰年（平年）365天
        else:
            day_y=getTotalDaysFrom1990_y(year-1,1)+365
            #减去二月天数与30的差
            if(month>2):
                day_y=day_y-2
                if (judge(year)):
                    day_y=day_y+1
        return day_y

#本月1日距1990年1月1日的天数
def getTotalDaysFrom1990(year,month):
    return getTotalDaysFrom1990_y(year,month)+getTotalDaysFrom1990_m(year,month)

#firstday为本月第一天的星期数
firstday=getMonthStartDay(year,month)

#计算该月的天数
if (month<12):
    monthdays=getTotalDaysFrom1990(year,month+1)-getTotalDaysFrom1990(year,month)
else:
    monthdays=getTotalDaysFrom1990(year+1,1)-getTotalDaysFrom1990(year,month)

def switch(month):
    if (month==1):
        m_output="January"
    elif (month==2):
        m_output="February"
    elif (month==3):
        m_output="March"
    elif (month==4):
        m_output="April"
    elif (month==5):
        m_output="May"
    elif (month==6):
        m_output="June"
    elif (month==7):
        m_output="July"
    elif (month==8):
        m_output="August"
    elif (month==9):
        m_output="September"
    elif (month==10):
        m_output="October"
    elif (month==11):
        m_output="Noveber"
    elif (month==12):
        m_output="December"
    return m_output

#打出抬头
print("%27s"%switch(month)+"%7d"%year)
#打出分割线
for line in range(55):
    print("-",end='')
print('')
#日历表的第一行
print("%7s"%"Sun"+"%7s"%"Mon"+"%7s"%"Tue"+"%7s"%"Wed"+"%7s"%"Thu"+"%7s"%"Fri"+"%7s"%"Sat")

#打出本月第一天
def printDays(dayInWeeks):
    i=0
    while (i<dayInWeeks and dayInWeeks<7):
        print("%7s"%'',end='')
        i=i+1
    print("%7d"%1,end='')
    if (dayInWeeks==6):
        print('')
printDays(firstday)

#addDays储存本月递加的天数
addDays=1
#以第一天为基础通过循环实现日历的打印
while (addDays<monthdays):
    dayNow=addDays+firstday
    if (dayNow%7==6):
        print("%7d"%(addDays+1))
    else:
        print("%7d"%(addDays+1),end='')
    addDays=addDays+1
