x=input("请输入一个数字")
y=input("请再输入一个数字")
try:
    x=int(x)
    y=int(y)
except ValueError:
    print("请不要输入文本")
else:
    print(x+y)
