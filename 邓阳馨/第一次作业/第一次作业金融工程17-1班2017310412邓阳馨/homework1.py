w=47
h=1.55
t=w/(h**2)
if t<18:
    print("低体重"+str(t))
elif t<=25:
    print("正常体重"+str(t))
elif t<=27:
    print("超重体重"+str(t))
elif t>27:
    print("肥胖"+str(t))
