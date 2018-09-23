Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> w=56
>>> h=1.63
>>> t=w/h**2
>>> if t < 18:
	a="低体重"
elif t >= 18 and t <= 25:
	a="正常体重"
elif t > 25 and t <= 27:
	a="超重体重"
elif t > 27:
	a="肥胖"

	
>>> print("您的体重指数为"+str(t)+"，是"+str(a))
您的体重指数为21.077195227520797，是正常体重
>>> 
