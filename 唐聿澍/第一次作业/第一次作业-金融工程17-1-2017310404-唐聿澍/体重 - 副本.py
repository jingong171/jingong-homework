w = 65
h = 1.82
t = w / h**2
if t < 18  :
    a = "低体重"
elif t <= 25 :
    a = "正常体重"
elif t <= 27 :
    a = "超重体重"
else:
    a ="肥胖"
print(a)
