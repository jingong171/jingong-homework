digits=[]
for value in range (3,31,3):
	square=value**2
	digits.append(square)#将平方数放入空列表中
	a=sum(digits)#对列表中的数求和

	
print(a)
