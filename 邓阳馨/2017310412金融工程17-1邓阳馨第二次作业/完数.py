for i in range(1,2001):
	digits_1=[]#用于储存i的因子
	for j in range(1,i):	
		if i%j==0:
			digits_1.append(j)
	a=sum(digits_1)#对i的因子j求和
	if i==a:#判断完数
		print(i)
