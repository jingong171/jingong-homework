#之前有多少个闰年
def runnianshu(year,month):
    n=0
    while (year-1990 >= 0):
        if ((year-1)%4 == 0 and (year-1)%100 != 0) or (year-1)%400 == 0:
            n=n+1
        year = year-1
    return n

#今年是不是闰年
def jinnian(year,month):
    m=0
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        m=1
    return m

#今年过了多少天
def lingshu(year,month):
    zongshu = 0
    tianshu = 0
    yueshus = list(range(1,month))
    for yueshu in yueshus:
        if yueshu == 1 or  yueshu ==  3 or  yueshu ==  5 or  yueshu == 7 or  yueshu == 8 or  yueshu == 10 or  yueshu == 12:
            jiashu = 31
        else:
            jiashu = 30
        zongshu = zongshu+jiashu
    if month > 2:
        if (jinnian(year,month)==1):
            tianshu = zongshu-1
        else: 
            tianshu = zongshu-2
    else:
        tianshu = zongshu
    return tianshu
           
#这个月有几天
def benyue(year,month):
        if month == 1 or  month ==  3 or  month ==  5 or  month == 7 or  month== 8 or  month == 10 or  month== 12:
            return 31
        elif month == 2:
            if jinnian(year,month) == 0:
                return 28
            else:
                return 29
        else:
            return 30

#从1990为止过了多少天
def gettotledaysfrom1990(year,month):
    howmanyyear = year-1990
    zhengshu = 365*howmanyyear + runnianshu(year,month)
    suoyou = zhengshu + lingshu(year,month)
    return suoyou

#返回星期几
def getmonthstartday(year,month):
    return  (1 + gettotledaysfrom1990(year,month)%7)


year=int(input("请输入年,在1990年之后："))
while year < 1990:
    print("输入错误请重新输入")
    year=int(input("请输入年,在1990年之后："))
month=int(input("请输入月份："))
while month > 12:
    print("输入错误请重新输入：")
    month=int(input("请输入月份："))
diyitian = getmonthstartday(year,month)
diyitianzhiqian = getmonthstartday(year,month)-1
print("星期天\t一\t二\t三\t四\t五\t六")
yushu = 7-diyitian
if diyitian == 7:
    xs = list(range(1,benyue(year,month)+1))
    for x in xs:
        print(str(x)+"\t",end=" ")
        if (diyitian + x)%7 == 0:
            print("\n")
else:
    while diyitian > 0:
        print("\t",end=" ")
        diyitian = diyitian-1
    xs = list(range(1,benyue(year,month)+1))
    for x in xs:
        print(str(x)+"\t",end=" ")
        if (diyitian + x)%7 == yushu:
            print("\n")
        
