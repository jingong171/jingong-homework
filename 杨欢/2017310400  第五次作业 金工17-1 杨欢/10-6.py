def sum(fNum,sNum):
    #定义加法函数
    try:
        return int(fNum)+int(sNum)
    except ValueError:
        #发生错误时可以提示
        print("请输入数字")
        pass
    
for i in range(2):
    #程序需要运行两遍以检验
    firstNumber=input("请输入第一个数字：")
    secondNumber=input("请输入第二个数字：")
    sumTwo=sum(firstNumber,secondNumber)
    print(sumTwo)
