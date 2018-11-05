def getyear(theyear):
        theyear=int(theyear)
        if theyear%400==0:
                return 1
        else:
                if theyear%100==0:
                        return 0
                else:
                        if theyear%4==0:
                                return 1
                        else:
                                return 0
def getWeekday(year,month,day):
        sum=0
        year=int(year)
        month=int(month)
        day=int(day)
        for m in range(1990,year):
                if getyear(m)==1:
                        sum=366+sum
                else:
                        sum=sum+365
        if month==1:
                if day<=30:
                        sum=sum+day
        else:
                if month==2:
                        if getyear(year)==1:
                                if day<=29:
                                        sum=sum+31+day
                                else:
                                        return 1
                        else:
                                if day<=28:
                                        sum=sum+31+day
                                else:
                                        return 1
                else:
                        for m in range(1,month):
                                if m in[1,3,5,7,8,10,12]:
                                        sum=sum+31
                                else:
                                        if m in [4,6,9,11]:
                                                sum=sum+30
                                        else:
                                                if getyear(m)==1:
                                                        sum=sum+29
                                                else:
                                                        sum=sum+28
                        if month in [1,3,5,7,8,10,12]:
                                if day<=31:
                                        sum=sum+day
                                else:
                                        return 1
                        else:
                                if day<=30:
                                        sum=sum+day
                                else:
                                        return 1
        days=sum%7
        if days==0:
                return '星期天'
        if days==1:
                return'星期一'
        if days==2:
                return'星期二'
        if days==3:
                return'星期三'
        if days==4:
                return'星期四'
        if days==5:
                return'星期五'
        if days==6:
                return'星期六'
def column(year1,month1):
        year1=int(year1)
        month1=int(month1)
        print('星期天 ','    ','星期一 ','    ','星期二 ','    ','星期三 ','    ','星期四 ','    ','星期五 ','    ','星期六 ')
        day1=getWeekday(year1,month1,1)
        w1='星期天'
        w2='星期一'
        w3='星期二'
        w4='星期三'
        w5='星期四'
        w6='星期五'
        w7='星期六'
        s='           '         
        s1='          '
        s3='         '
        if day1==w1:
                print('    ','1',s1,end='')
        if day1==w2:
                print('    ',s,'1',s1,end='')
        if day1==w3:
                print('    ',s,s,'1',s1,end='')
        if day1==w4:
                print('    ',s,s,s,'1',s1,end='')
        if day1==w5:
                print('    ',s,s,s,s,'1',s1,end='')
        if day1==w6:
                print('    ',s,s,s,s,s,'1',s1end='')
        if day1==w7:
                print('    ',s,s,s,s,s,s,'1','\n',end='    ')
        for m in range(2,10):
                day2=getWeekday(year1,month1,m)
                if day2==w7:
                        print(m,'\n','    ',end='')
                else:
                        if day2 in[w1,w2,w3,w4,w5,w6]:
                                print(m,s1,end='')
        for m in range(10,32):
                day3=getWeekday(year1,month1,m)
                if day3==w7:
                        print(m,'\n','    ',end='')
                else:
                        if day3 in [w1,w2,w3,w4,w5,w6]:
                                print(m,s3,end='')
_year=input('请输入年份')
_month=input('请输入月份')
column(_year,_month)
    
            

