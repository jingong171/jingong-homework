
w=49
h=1.65
t=w/(h**2)
if t<18:
    print("轻体重"+str(t))
elif t<=25:
    print("正常体重"+str(t))
elif t<=27:
    print("超重体重"+str(t))
else:
    print("肥胖体重"+str(t))
    
