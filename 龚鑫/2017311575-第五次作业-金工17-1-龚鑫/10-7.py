while True:#对于输入第一个数字的while循环
    input1=input("请输入第一个数字")
    try:
        number1=float(input1)
    except ValueError:
        print("输入的不是数字")
        continue#如果错误就重新开始这个循环
    else:
        break#如果没问题就是跳出第一个循环进入第二个循环
    
while True:#对于输入第二个数字的循环
    input2=input("请输入另一个数字")
    try:
        number2=float(input2)
    except ValueError:
        print("输入的不是数字")
        continue#如果错误就重新开始这个循环
    print(number1+number2)
    break#打印后程序结束

