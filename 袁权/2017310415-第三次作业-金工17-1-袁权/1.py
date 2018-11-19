def getTotalDaysFrom1990(year,month):
    """返回1990年1月1日的天数"""
    for month in range(1,month):
        m=month
        y=year
        if(m==4 or m==6 or m==9 or m==11):
            d=30
        elif(m==2):
            d=28
        else:
            d=31
        sum=0
        sum=sum+d
    if((y-1990)%4==0):
        day=(y-1990)*365+sum+int((y-1990)/4)+1
    else:
        day=(y-1990)*365+sum+int((y-1990)/4)
    return day
year=input("请输入年份：")
month=input("请输入月份：")
year=int(year)
month=int(month)
m=month
y=year
d=getTotalDaysFrom1990(year,month)
t=d%7
print("Sun"+"   "+"Mon"+"   "+"Tue"+"   "+"Wed"+"   "+"Thu"+"   "+"Fri"+"   "+"Sat")
if(m==4 or m==6 or m==9 or m==11):
    for n in range(0,t):
        print("   ",end="   ")
    for n in range(1,7-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(7-t+1,14-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(14-t+1,21-t+1):
        print(n,end="    ")
    print(" ")
    for n in range(21-t+1,28-t+1):
        print(n,end="    ")
    print(" ")
    if(t>5):
        for n in range(28-t+1,35-t+1):
            print(n,end="    ")
        print(" ")
        for n in range(35-t+1,31):
            print(n,end="    ")
    else:
        for n in range(28-t+1,31):
            print(n,end="    ")
elif(m==2 and (y-1990)%4==0):
    for n in range(0,t):
        print("   ",end="   ")
    for n in range(1,7-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(7-t+1,14-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(14-t+1,21-t+1):
        print(n,end="    ")
    print(" ")
    for n in range(21-t+1,28-t+1):
        print(n,end="    ")
    print(" ")
    if(t>6):
        for n in range(28-t+1,35-t+1):
            print(n,end="    ")
        print(" ")
        for n in range(35-t+1,30):
            print(n,end="    ")
    else:
        for n in range(28-t+1,30):
            print(n,end="    ")
elif(m==0 and (y-1990)%4!=0):
    for n in range(0,t):
        print("   ",end="   ")
    for n in range(1,7-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(7-t+1,14-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(14-t+1,21-t+1):
        print(n,end="    ")
    print(" ")
    for n in range(21-t+1,28-t+1):
        print(n,end="    ")
    print(" ")        
    for n in range(28-t+1,29):
        print(n,end="    ")
else:
    for n in range(0,t):
        print("   ",end="   ")
    for n in range(1,7-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(7-t+1,14-t+1):
        print(n,end="     ")
    print(" ")
    for n in range(14-t+1,21-t+1):
        print(n,end="    ")
    print(" ")
    for n in range(21-t+1,28-t+1):
        print(n,end="    ")
    print(" ")        
    if(t>4):
        for n in range(28-t+1,35-t+1):
            print(n,end="    ")
        print(" ")
        for n in range(35-t+1,32):
            print(n,end="    ")
    else:
        for n in range(28-t+1,32):
            print(n,end="    ")
        
        


    





    
