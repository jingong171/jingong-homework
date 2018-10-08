w=60
h=1.7
t=w/h**2
if t<18:
    print("低体重")
elif t<=25:
    print("正常体重")
elif t<=27:
    print("超重")
else:
    print("肥胖")
