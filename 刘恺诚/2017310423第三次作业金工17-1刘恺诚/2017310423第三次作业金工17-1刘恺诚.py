def getTotalDaysFrom1990(year,month):
    county=-1 #普通年
    countx=0 #闰年
    for i in list(range(1990,year+1)):
        if (i%4==0 and i%100!=0):
            countx+=1
        elif (i%400==0):
            countx+=1
        else:
            county+=1
    
    m31=[1,3,5,7,8,10,12]
    m30=[4,6,9,11]
    day=0
    if ((year%4==0 and year%100!=0)or year%400==0):
        for j in range(1,month):
            if j in m31:
                day=day+31
            if j in m30:
                day=day+30
            if j==2 :
                day=day+29
    else:
        for j in range(1,month):
            if j in m31:
                day=day+31
            if j in m30:
                day=day+30
            if j==2 :
                day=day+28

    return int(county*365+countx*366+day)

def getMonthStartDay(year,month):
    
    return int(1+getTotalDaysFrom1990(year,month)%7)

year=int(input('请输入年：'))
month=int(input('请输入月：'))
FirstDay=getMonthStartDay(year,month)
m31=[1,3,5,7,8,10,12]
m30=[4,6,9,11]

if month in m31:
    day=31
elif month in m30:
    day=30
else:
    if ((year%4==0 and year%100!=0)or year%400==0):
        day=29
    else:
        day=28
print(day,FirstDay)
monthName=['January\t','February\t','March\t','April\t','May\t','June\t','July\t','Augest\t','September\t','October\t','November\t','December\t']
dayName=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

print('   ',monthName[month-1],'  ',year)
print('-----------------------------------')
for i in range(0,7):
    print(dayName[i],end='\t')

print('\n')
k=0
for j in range(0,45):
    if (j<=FirstDay or j>day+FirstDay):
        print(' ',end='\t')
    if (FirstDay<j<day+FirstDay+1):
        k+=1
        print(k,end='\t')
    
    if j%7==0:
        print('\n')
    
        

