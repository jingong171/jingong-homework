Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for a in range(1,2001):
	s=0
	for b in range(1,a):
		if a%b==0:
			s=s+b
	if a==s:
		print(a)

		
6
28
496
>>> 
