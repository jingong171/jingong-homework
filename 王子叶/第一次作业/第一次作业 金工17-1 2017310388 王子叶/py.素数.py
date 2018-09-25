Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for x in range(100):
	if x <2:        continue
	for i in range(2,x):
		if x % i == 0:
		break
	else: print(x)


	

--------------------
