w=52
h=1.68
t=w/h**2
print("你的体重指数是"+str(t))
if t<18:
    print("你是低体重")
elif t<=25:
    print("你是正常体重")
elif t<=27:
    print("你是超重体重")
else:
    print("你肥胖")
