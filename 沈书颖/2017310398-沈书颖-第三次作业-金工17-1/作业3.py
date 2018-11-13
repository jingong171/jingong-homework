def leap_year(year):
    if year%4==0 and year%100!=0:
	    return True
    elif year%400==0:
            return True
    else:
	    return False


def getMonthDays(year,month):
    if month==2:
	    if leap_year(year):
		    return 29
	    else:
		    return 28
    elif month==4 or month==6 or month==9 or month==11:
	    return 30
    else:
            return 31

		
def getTotalDays(year,month):
    totaldays=0
    for i in range(1990,year):
	    if leap_year(i):
		    totaldays+=366
	    else:
		    totaldays+=365
		    
    for i in range(1,month):
    	totaldays+=getMonthDays(year,i)
    	
    return totaldays

def getMonthStartDay(year,month):
    return 1+getTotalDays(year,month)%7

year=int(input("请输入年份："))
month=int(input("请输入月份："))


daycount=0

print("日\t一\t二\t三\t四\t五\t六")
      
i=1
for i in range(getMonthStartDay(year,month)):
      print(end='\t')
      daycount+=1

for i in range(1,getMonthDays(year,month)+1):
      print(i,end='\t')
      daycount+=1
      if daycount%7==0:
          print('')

