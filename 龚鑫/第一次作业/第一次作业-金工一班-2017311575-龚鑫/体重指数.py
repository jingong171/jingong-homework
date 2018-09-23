w=eval(input("请输入你的体重： "))
h=eval(input("请输入你的身高： "))
t=w/(h**2)
if t<18:
    k="低体重"
if t>=18 and t<=25:
    k= "正常体重"
if t>27:
    k= "肥胖"
print("你的体重指数为{}，属于{}".format(int(t),k))
