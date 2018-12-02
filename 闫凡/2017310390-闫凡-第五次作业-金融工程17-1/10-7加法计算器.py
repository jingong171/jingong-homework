#使用while循环让代码可以在出错后继续运行
while True:
#使用try-excpet代码块来处理异常
    try:
#输入第一个数
        num1=input('请输入两个数字，计算他们的和，请输入第一个数字')
#输入第二个数
        num2=input('请输入第二个数字')
#执行计算并打印
        num=float(num1)+float(num2)
        print('他们的和为'+str(num))
#处理异常
    except ValueError:
        print('请输入两个数字，不要输入文本')
