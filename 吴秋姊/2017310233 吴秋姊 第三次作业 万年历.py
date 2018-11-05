def leapyearornot(year):#判断是否为闰年
    if (year%4==0 and year%100!=0):
        return True

def getmonthday(year,month):#判断当前月的天数
    monthday=[31,28,31,30,31,30,31,31,30,31,30,31]
    if (leapyearornot(year)==True):
        monthday[1]=29
    return monthday[month-1]

def getTotalDaysFrom1990(year,month):#距1990年1月1日的天数
    days=0
    for index_year in range(1990,year):
        if leapyearornot(index_year):
            days+=366
        else:
            days+=365
    for index_month in range(1,month):
        days+=getmonthday(year,index_month)
    return days
        
def getMonthStartDay(year,month):#判断给定月的1号是星期几
    return 1+getTotalDaysFrom1990(year,month)%7

def show():#显示当前月份
    year=input("请输入年:")
    year=int(year)
    month=input("请输入月份:")
    month=int(month)
    print("\t%4d"%year+"\t%2d"%month)
    space_num=getMonthStartDay(year,month)
    print("\tSun\tMon\tTue\tWed\tThu\tFri\tSat")
    for i in range(1,getmonthday(year,month)+1):
        if (i==1):
            for j in range(space_num%7):
                print("\t",end="")        
        print("\t%2d"%i,end="")
        if ((i+space_num)%7==0):
            print()

show()
            
    
    





    
