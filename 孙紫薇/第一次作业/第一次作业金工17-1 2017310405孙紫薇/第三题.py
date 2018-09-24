Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> numbers=[]
>>> for a in range(1,10):
	for b in range(1,10):
		for c in range(1,10):
			if a**3+b**3+c**3==a*100+b*10+c:
				numbers.append(a*100+b*10+c)
				print(numbers)

				
[153]
[153, 371]
>>> 
