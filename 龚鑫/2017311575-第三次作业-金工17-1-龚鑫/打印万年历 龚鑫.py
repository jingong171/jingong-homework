def getMonthStart(year,month): #返回该月第一天是周几
    return 1+getTotalDaysFrom1990(year,month)%7  
def getTotalDaysFrom1990(year,month): #返回该月第一天距离1990年月一日的天数
    day=0
    for years in range(1990,year): 
        if years % 100 != 0 and years % 4 == 0: #该年是闰年
            day=day+366
        elif years % 100 != 0 and years % 4 != 0: #该年不是闰年
            day=day+365
        elif years % 100 ==0 and years % 400 == 0: #该年是闰年
            day=day+366
        else: #该年不是闰年
            day=day+365
    for months in range(1,month):
        day=day+returnDay(year,months) #将该年一月一日直到该月1日的天数加总
    return day

def judge(year): #该函数用于判断该年是否是闰年，返回布尔值
        if year%100 != 0 and year%4 == 0:
            flag = 1
        elif year%100 != 0 and year%4 != 0:
            flag = 0
        elif year%100 ==0 and year%400 == 0:
            flag = 1
        else:
            flag = 0
        return flag
    

def returnDay(year,month): #返回该月的天数
    day=0
    flag=judge(year)
    if month in [1,3,5,7,8,10,12]:
        day=31
    elif month in [4,6,9,11]:
        day=30
    elif month == 2:
        if flag:
            day=29
        else:
            day=28
    return day

week=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

def outPut(start,day): #输出日历
    print(start)
    for i in range(1,8):
        print(week[i-1],end="    ") #打印日历第一行
    print("")
    count=0 #count用于识别每打印七个日期时就跳到下一行
    for i in range(0,start):
        print("   ",end="    ") #用来打印该月1日前的空白部分
        count=count+1
    for i in range(1,day+1):
        if count >=7:
            print("")
            count=0
        print("{:<3}".format(i),end="    ") #通过format方法格式化数字，使每个数字均占3个字符，排版整齐
        count=count+1
year = eval(input("请输入年份："))
month = eval(input("请输入月份： "))
start = getMonthStart(year,month)
day = returnDay(year,month)
outPut(start,day)
