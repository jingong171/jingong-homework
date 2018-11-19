def daysofmonth(year,month):
    dayofmonth={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if year%4==0 and year%100!=0 or year%400==0:
        dayofmonth[2]=29
    return dayofmonth[month]
def getMonthStartDay(year,month):
    TotalDaysFrom1990=0
    for thisyear in range(1990,year):
        yeardays=356
        if thisyear%4==0 and thisyear%100!=0 or thisyear%400==0:
            yeardays+=1
        TotalDaysFrom1990+=yeardays        
    for thismonth in range(1,month):
        monthdays=daysofmonth(year,thismonth)
        TotalDaysFrom1990+=monthdays        
    return 1+(TotalDaysFrom1990%7)
year=int(input('请输入年:'))
month=int(input('请输入月:'))
monthname=('january','february','march','april','May','June','July','August','September','October','November','December')
print('          '+monthname[month-1]+'          '+str(year)+'\n'+'-'*50)
daynames=['sun','mon','tue','wed','thu','fri','sat']
for dayname in daynames:
    print(dayname,'\t',end='')
print('\n',end='')
if getMonthStartDay(year,month)!=7:
    print(getMonthStartDay(year,month)*'\t',end='')
for j in range(1,daysofmonth(year,month)+1):
    print  (str(j),'\t',end='')
    if (j+getMonthStartDay(year,month))%7==0:
        print('\n',end='')

