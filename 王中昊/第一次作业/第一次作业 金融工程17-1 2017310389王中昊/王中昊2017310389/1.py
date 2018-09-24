w=56.50
h=1.75
t=w/h**2

if t<18:
	print('t='+str(t)+',为低体重')
elif t<=25:
	print('t='+str(t)+',为正常体重')
elif t<=27:
	print('t='+str(t)+',为超重体重')
elif t>27:
	print('t='+str(t)+',为肥胖')
	
