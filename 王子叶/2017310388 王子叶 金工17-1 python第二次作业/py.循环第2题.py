Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> m=35
>>> n=14
>>> squares=[]
>>> for x in range(1,m+1):
	if(m%x==0 and n%x==0):
		squares.append(x)
		max(squares)

		
1
7
>>> m=35
>>> n=14
>>> squares2=[]
>>> for y in range(1,m*n+1):
	if(y%m==0 and y%n==0):
		squares2.append(y)

		min(squares2)




		
70
70
70
70
70
70
70
>>> 
