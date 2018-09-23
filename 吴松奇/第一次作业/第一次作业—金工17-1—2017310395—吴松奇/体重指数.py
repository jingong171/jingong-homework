w=53
h=1.66
t=w/h**2
print("您的体重指数为"+str(t))
if t<18:
    print("低体重")
elif t<=25:
    print("正常体重")
elif t<=27:
    print("超重体重")
else:
    print("肥胖")
