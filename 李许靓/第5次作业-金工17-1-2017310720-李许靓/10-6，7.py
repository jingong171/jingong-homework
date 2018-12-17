while 1:
    try:
        num1=input("please enter a number(enter q to quit):")
        if num1=='q':
            """设置循环退出条件"""
            break
        num1=int(num1)
        num2=input("please enter another number(enter q to quit):")
        if num2=='q':
            """设置循环退出条件"""
            break
        num2=int(num2)
        add=num1+num2
        print("the sum of the two numbers is "+str(add)+" .")
        with open("add.txt",'a') as fileobj:
            """将结果写入文件"""
            fileobj.write("the sum of the two numbers is "+str(add)+" .\n")
    except ValueError:
        """如果出现错误则提示"""
        print("sorry,you can't enter a string")