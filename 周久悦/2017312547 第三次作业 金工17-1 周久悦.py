Year=int(input("请输入年："))
Month=int(input("请输入月："))
print("——————"+str(Year)+"年"+str(Month)+"月"+"——————")
print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")

#判断闰年
def leap(year):
    if year%400==0:
        return True
    else:
        if year%100==0:
            return False
        else:
            if year%4==0:
                return True
            else:
                return False

#计算闰年个数
count=0

for Year in list(range(1990,Year+1)):
    if leap(Year)==1:
        count+=1

#计算某一月到该年1月1日已经历多少天
def dayahead(month):
    if month==1:
        return 0
    elif month==2:
        return 31
    elif month==3:
        return 59
    elif month==4:
        return 90
    elif month==5:
        return 120
    elif month==6:
        return 151
    elif month==7:
        return 181
    elif month==8:
        return 212
    elif month==9:
        return 243
    elif month==10:
        return 273
    elif month==11:
        return 304
    elif month==12:
        return 334

#计算某一特定年月前距1990年1月1日已经历多少天
def getDayFrom1990(Year,Month):
    day=(Year-1990)*365+dayahead(Month)+count
    if leap(Year) and Month<=2:
       day=day-1
    return day;

#计算某一特定年月1号开始前有几个空格
def getspace(year,month):
    space=(getDayFrom1990(year,month)%7+1)%7
    return space

#一个月中有多少天
def day(month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    elif month==4 or month==6 or month==9 or month==11:
        return 30
    else:
        if(leap(Year)):
            return 29
        else:
            return 28

#输出日历
for i in range(getspace(Year,Month)):
    print("   \t",end='')

for i in range(1,1+day(Month)):
    print(" "+str(i)+" \t",end='')
    if (i+getspace(Year,Month))%7==0:
        print("")


    
