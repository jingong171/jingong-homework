num=[]
a=int(input('a:'))
b=int(input('b:'))
if a<b:
	for i in range(b,a*b+1):
		if i%a ==0:
			if i%b==0:
				num.append(i)
	print(min(num))
if a==b:
	print(b)
else:
	for i in range(a,a*b+1):
		if i%a ==0:
			if i%b==0:
				num.append(i)
	print(min(num))
