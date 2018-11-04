#计算出输入日期距1990年1月1日的天数
def getTotalDaysFrom1990(year,month):
    leapyear=0
    commonyear=0
    for everyyear in range(1990,year):
        if everyyear%4==0:
            leapyear+=1
        else:
            commonyear+=1
    Part1=leapyear*366+commonyear*365#Part1表示计算总天数的第一部分：年包含的天数
    assistance1=0#辅助数字1
    assistance2=0#辅助数字2
    bigmonth=0
    smallmonth=0
    #将一年月份分为1月、2月、3到7月、8到12月共四个部分
    #3到7月的奇数月为大月，偶数月为小月
    if month<=7 and month>=3:
        for everymonth in range(1,month):
            if everymonth%2==0:
                smallmonth+=1
            else:
                bigmonth+=1
    #8到12月与3到7月相反
    elif month>=8:
        for everymonth in range(8,month):
            if everymonth%2==0:
                assistance1+=1
            else:
                assistance2+=1
            bigmonth=4+assistance1
            smallmonth=3+assistance2
    if year%4==0 and month>=3:
        #Part2表示计算总天数的第二部分：月包含的天数
        Part2=bigmonth*31+smallmonth*30-1
    #由于计算的天数是输入的月份之前的天数，所以输入1月，则今年还没开始，Part2=0,二月同理
    elif month==1:
        Part2=0
    elif month==2:
        Part2=31
    elif year%4!=0 and month>=3:
        Part2=bigmonth*31+smallmonth*30-2
    TotalDaysFrom1990=Part1+Part2
    return TotalDaysFrom1990

#将月份转化成日历上的英语
def Month(month):
    if month==1:
        print("January",end='')
    elif month==2:
        print("February",end='')
    elif month==3:
        print("March",end='')
    elif month==4:
        print("April",end='')
    elif month==5:
        print("May",end='')
    elif month==6:
        print("June",end='')
    elif month==7:
        print("July",end='')
    elif month==8:
        print("August",end='')
    elif month==9:
        print("September",end='')
    elif month==10:
        print("October",end='')
    elif month==11:
        print("November",end='')
    elif month==12:
        print("December",end='')
    return " "

#输出日历
def Calendar(TotalDaysFrom1990,year,month):
    startday=1+TotalDaysFrom1990%7
    space3=''
    space4=''
    space5=''
    for i in range(8):
        space3+=' '
    for i in range(7):
        space4+=' '#每月前9天之间的空格
    for i in range(6):
        space5+=' '#每月两位数之间的空格
    if startday<=6:
        leftspace=str(space3*startday)
    else:
        leftspace=''
    print(leftspace,end='')
    for i in range(1,8-startday):
        print(str(i)+space4,end='')
    print('\n',end='')
    #区分10和15-startday的大小以确定数字之间的空格是7个或6个
    if 10>15-startday:
        for i in range(8-startday,15-startday):
            print(str(i)+space4,end='')
        print('\n',end='')
        for i in range(15-startday,10):
            print(str(i)+space4,end='')
        for i in range(10,22-startday):
            print(str(i)+space5,end='')
    else:
        for i in range(8-startday,10):
            print(str(i)+space4,end='')
        for i in range(10,15-startday):
            print(str(i)+space5,end='')
        print('\n',end='')
        for i in range(15-startday,22-startday):
            print(str(i)+space5,end='')
    print('\n',end='')
    for i in range(22-startday,29-startday):
        print(str(i)+space5,end='')
    print('\n',end='')
    #最后一行日历根据平年2月、闰年2月、大月、小月四种情况需进行讨论
    if year%4!=0 and month==2:
        for i in range(29-startday,29):
            print(str(i)+space5,end='')
    elif year%4==0 and month==2:
        for i in range(29-startday,30):
            print(str(i)+space5,end='')
    elif month==1:
        for i in range(29-startday,32):
            print(str(i)+space5,end='')
    elif month>=3 and month<=7 and month%2!=0:
        for i in range(29-startday,32):
            print(str(i)+space5,end='')
    elif month>=3 and month<=7 and month%2==0:
        for i in range(29-startday,31):
            print(str(i)+space5,end='')
    elif month>=8 and month<=12 and month%2!=0:
        for i in range(29-startday,31):
            print(str(i)+space5,end='')
    elif month>=8 and month<=12 and month%2==0:
        for i in range(29-startday,32):
            print(str(i)+space5,end='')
    return ''

year=input("请输入年：")
year=int(year)
month=input("请输入月份：")
month=int(month)
TotalDays=getTotalDaysFrom1990(year,month)
space1=""
space2=""
for i in range(12):
    space1+=" "
for i in range(5):
    space2+=" "
print(space1,end='')
print(str(Month(month))+space2+str(year))
print("----------------------------------------------------")
print("Sun.    Mon.    Tue.    Wed.    Thu.    Fri.    Sat.")
print(Calendar(TotalDays,year,month))
