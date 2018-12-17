while True:
    try:
        a=int(input("请输入第一个数字"))
        b=int(input("请输入第二个数字"))
    except ValueError:
        print("输入文本是无法计算的哦~请重新输入")
    else:
        print(str(a+b))
