w=72
h=1.83
t=w/(h*h)
print("我的体重指数t="+ str(t))
if t < 18:
    print("我是低体重")
elif t <= 25:
    print("我是正常体重")
elif t <= 27:
    print("我是超重体重")
elif t >27:
    print("我是肥胖")
    
