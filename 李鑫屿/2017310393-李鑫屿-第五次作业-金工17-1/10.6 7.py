while True:
    num1=input("请输入第一个数字")
    num2=input("请输入第二个数字")
    try:
        num1=int(num1)
        num2=int(num2)
    except ValueError:
        print("只可以输入数字")
        continue
    else:
        print(num1+num2)
        break
