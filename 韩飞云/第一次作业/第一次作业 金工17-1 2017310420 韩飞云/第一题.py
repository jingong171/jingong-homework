w = 70
h = 1.87
t = w/h**2#w(体重，单位：公斤)，h(身高，单位：米)
if t < 18:
    print("低体重")
elif t <= 25:
    print("正常体重")
elif t <= 27:
    print("超重体重")
else:
    print("肥胖")
