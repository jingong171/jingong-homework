w=float(input("请输入您的体重w（单位：公斤）="))
h=float(input("请输入您的身高h（单位：米）=" ))
t=w/(h*h)
if t<18:
    print("您为低体重")
elif t>=18 and t<=25:
          print("您为正常体重")
elif t>25 and t<=27:
          print("您为超重体重")
else:
          print("您为肥胖")

input("请输入回车键结束")
