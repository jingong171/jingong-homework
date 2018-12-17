while True:
    a=input("请输入数字")
    b=input("请输入数字")
    try:
        a=float(a)
        b=float(b)
        c=a+b
    except ValueError:
        print("提示用户输入两个数字")
    else:
        print(c)
    

