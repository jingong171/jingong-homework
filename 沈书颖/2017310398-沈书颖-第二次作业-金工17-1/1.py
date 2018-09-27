numbers=[]#创建一个空列表
for x in range(1,11):#取1~10
    y=(x*3)**2#用y表示3^2+6^2……
    numbers.append(y)#在列表中添加
    
sum_numbers=sum(numbers)#对列表求和
print(sum_numbers)#打印
