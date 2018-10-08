h=1.88
w=72.01
m=h*h
t=w/m
if t<18:
    print("为低体重")
elif t<=25:
    print("为正常体重")
elif t<=27:
    print("为超重体重")
else:
    print("为肥胖")
