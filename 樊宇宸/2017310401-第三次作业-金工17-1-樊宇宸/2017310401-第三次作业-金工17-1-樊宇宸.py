#建立函数Ruinian用于判断是否为闰年，返回值为bool型
def Runnian(year):                       
    if (year%400)==0:
        return True
    elif (year%100)==0:
        return False
    elif (year%4)==0:
        return True
    else:
        return False
#建立函数days_per_month用于计算每个月的天数
def days_per_month(year,month):
    if month==2:
        if Runnian(year):
            return 29
        else:
            return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
#建立函数getTotalDaysFrom1990用于计算该月1号与1990年1月1日的距离天数    
def getTotalDaysFrom1990(year,month):
    Days=0
    for i in range(1990,year):
        if Runnian(i):
            Days=Days+366
        else:
            Days=Days+365
    for i in range(1,month):
        Days=Days+days_per_month(year,i)
    return Days
#建立函数getMonthStartDay用于计算该月1号为星期几
def getMonthStartDay(year,month):
	return 1+getTotalDaysFrom1990(year,month)%7
    
year=int(input("请输入年:"))
month=int(input("请输入月:"))
#打印年份月份以及下面一道横线
Month=["January","Feburary","March","April","May","June","July","August","September","Octomber","November","December"]
print(" "*18,Month[month-1],year)
print("-"*51)
#打印星期几的栏
for date in ["Sun","Mon","Tue","Wed","Thu","Fri"]:
    print(date+"     ",end="")
print("Sat"+"    ")
#根据该月1号为星期几提前留好1号前的空白位置，每一天的间隔为8个空格
print(" "*(getMonthStartDay(year,month)%7)*8,end="")
#从1号一直打印到最后一天，遇到周六便换行
for i in range (1,days_per_month(year,month)+1):
    if ((i-1+getMonthStartDay(year,month))%7)==6:
        print(i,'\t','\n')
    else:
        print(i,'\t',end='')



      
            
    
        
    

    
    
        
    
