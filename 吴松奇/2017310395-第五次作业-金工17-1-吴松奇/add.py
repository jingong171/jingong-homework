print("这是一个加法程序，我们会将你提供的两个数字相加并输出结果")
flag=True
while flag:
    try:
        m=int(input("请输入第一个数字"))
        """m为将进行相加的两个数字中的第一个数字"""
        n=int(input("请输入第二个数字"))
        """n为将进行相加的两个数中的第二个数字"""
    except ValueError:
        show="您输入的不是数字哦~请重新输入"
        print(show)
    else:
        break
print(m+n)
        

