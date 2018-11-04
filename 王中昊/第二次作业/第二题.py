m=18
n=27
list_1=[]
list_2=[]
if m>n:
	for value in range(1,n):
		t=n % int(value)
		s=m % int(value)
		if t==0 and s==0:
			list_1.append(int(value))
	print("最大公约数为"+"%d"%(max(list_1)))
else:
	for value in range(1,m):
		t=n % int(value)
		s=m % int(value)
		if t==0 and s==0:
			list_1.append(int(value))
	print("最大公约数为"+"%d"%(max(list_1)))
if m>n:
        for value_2 in range(m,n*m):
                p=int(value_2)%n
                q=int(value_2)%m
                if p==0 and q==0:
                        list_2.append(int(value_2))
        print("最小公倍数为"+"%d"%(min(list_2)))
else:
        for value_2 in range(n,n*m):
                p=int(value_2)%n
                q=int(value_2)%m
                if p==0 and q==0:
                        list_2.append(int(value_2))
        print("最小公倍数为"+"%d"%(min(list_2)))

