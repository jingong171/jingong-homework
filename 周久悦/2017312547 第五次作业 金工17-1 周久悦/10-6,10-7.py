print("请输入两个数字，我们会对其进行加法运算：")

flag_1=flag_2=1

while flag_1==1:
    try:
        a=int(input("请输入第一个数字：\t"))
    except ValueError:
        print("请输入数字")
    else:
        flag_1=0

while flag_2:
    try:
        b=int(input("请输入第二个数字：\t"))
    except ValueError:
        print("请输入数字")
    else:
        flag_2=0

a=float(a)
b=float(b)

print("两数字之和为"+str(a+b))
