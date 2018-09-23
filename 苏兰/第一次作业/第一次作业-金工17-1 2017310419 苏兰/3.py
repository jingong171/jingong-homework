Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			if 100*a+10*b+c == a**3+b**3+c**3:
				print(100*a+10*b+c)

				
153
370
371
407
>>> 
