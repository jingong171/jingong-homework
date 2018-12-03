input1=input("请输入第一个数字")#input1用于暂时储存用户输入的值
try:
    number1=float(input1)#尝试将用户输入的值转化为整数
except ValueError:
    print("输入的不是数字")
else:        #如果第一个数字正确就输入第二个数字
    input2=input("请输入另一个数字")
    try:
        number2=float(input2)
    except ValueError:
        print("输入的不是数字")
    else:
        print(number1+number2)

