"""编写一个程序使用户输入的两个数相加并打印结果"""
"""设置循环使用户输入错误后能继续输入"""
while True:
    try:
        m=int(input("请输入第一个数字: "))
        n=int(input("请输入第二个数字: "))
        digits=m+n
        print("两个数的和为: "+str(digits))
    except ValueError:
        print("您的输入有误，请输入数字哦")
    else:
        break
