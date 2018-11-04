MonthsOf31=[1,3,5,7,8,10,12]
MonthsOf30=[4,6,9,11]
#将除2月之外的月份划分为两个列表

days = 0
#表示所给月份1日离1999年1月1日（周一）的天数

y = input ('请输入年份:')
y = int(y)
for year in range(1990,int(y)):
    if year%100 ==0:
        if year%400 ==0:
            days = days + 366
        else:
            days = days + 365
    elif year%4 ==0:
        days = days + 366
    else:
        days = days + 365
#计算年份之间的天数（分闰年平年讨论）

m = input ('请输入月份：')
for month in range(1,int(m)):
    if month in MonthsOf31:
        days = days +31
    elif month in MonthsOf30:
        days = days +30
    elif month == 2:
         if year%100 ==0:
             if year%400 ==0:
                 days = days +29
             else:
                 days = days + 28
         elif year%4 ==0:
             days = days + 29
         else:
             days = days + 28
#按月计算当年剩余未算入总天数的部分


W = days%7
#除以7取余

def calender_topline(t):
    k=t
    while t != -1:
        print('     ',end='')
        t=t-1
    else:
        for d in range(1,7-k):
            print (str(d)+'    ',end='')
    print('\n')
#日历第一行专用函数
    
#日历剩余行专用函数
def calender_rest(t,v,year):
    v=int(v)
#将月份分为3类—31天类
    if v in MonthsOf31:
        if t+7<32:
            for w in range(t,t+7):
                if w <10:
                    print(str(w)+'    ',end='')
                else:
                    print(str(w)+'   ',end='')
            print('\n')
            calender_rest(t+7,v,year)
        else:
            for w in range(t,32):
                print(str(w)+'   ',end='')

#将月份分为3类—30天类
    elif v in MonthsOf30:
        if t+7<31:
            for w in range(t,t+7):
                if w <10:
                    print(str(w)+'    ',end='')
                else:
                    print(str(w)+'   ',end='')
            print('\n')
            calender_rest(t+7,v,year)
        else:
            for w in range(t,31):
                print(str(w)+'   ',end='')

#将月份分为3类—2月类（再次分闰年平年讨论）
    else:
        if year%100 ==0:
            if year%400 ==0:
                if t+7<30:
                    for w in range(t,t+7):
                        if w <10:
                            print(str(w)+'    ',end='')
                        else:
                            print(str(w)+'   ',end='')
                    print('\n')
                    calender_rest(t+7,v,year)
                else:
                    for w in range(t,30):
                        print(str(w)+'   ',end='')
            else:
                if t+7<29:
                    for w in range(t,t+7):
                        if w <10:
                            print(str(w)+'    ',end='')
                        else:
                            print(str(w)+'   ',end='')
                    print('\n')
                    calender_rest(t+7,v,year)
                else:
                    for w in range(t,29):
                        print(str(w)+'   ',end='')
        elif year%4 ==0:
            if t+7<30:
                for w in range(t,t+7):
                    if w <10:
                        print(str(w)+'    ',end='')
                    else:
                        print(str(w)+'   ',end='')
                print('\n')
                calender_rest(t+7,v,year)
            else:
                for w in range(t,30):
                    print(str(w)+'   ',end='')
        else:
            if t+7<29:
                for w in range(t,t+7):
                    if w <10:
                        print(str(w)+'    ',end='')
                    else:
                        print(str(w)+'   ',end='')
                print('\n')
                calender_rest(t+7,v,year)
            else:
                for w in range(t,29):
                    print(str(w)+'   ',end='')

print('   '+str(m) +'月'+'   '+str(y)+'年')
print('------------------------------------')
print('Sun'+'  '+'Mon'+'  '+'Tue'+'  '+'Wen'+'  '+'Thu'+'  '+'Fri'+'  '+'Sat')
#打印表头

calender_topline(W)
calender_rest(7-W,m,y)
#最后运行首行函数和余行函数


