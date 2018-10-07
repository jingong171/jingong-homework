Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> squares=[]
>>> for x in range(1,11):
	y=(3*x)**2
	squares.append(y)
	print(squares)

	
[9]
[9, 36]
[9, 36, 81]
[9, 36, 81, 144]
[9, 36, 81, 144, 225]
[9, 36, 81, 144, 225, 324]
[9, 36, 81, 144, 225, 324, 441]
[9, 36, 81, 144, 225, 324, 441, 576]
[9, 36, 81, 144, 225, 324, 441, 576, 729]
[9, 36, 81, 144, 225, 324, 441, 576, 729, 900]
>>> sum(squares)
3465
>>> 
