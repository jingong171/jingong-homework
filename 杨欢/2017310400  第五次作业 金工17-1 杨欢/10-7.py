
def sum(fNum,sNum):
    #定义加法函数
    try:
        return int(fNum)+int(sNum)
        #保证需要的是数字型，才能调用TypeError
    except ValueError:
        print("请输入数字")
        pass
Flag=True    
while Flag:
    #程序需要运行两遍以检验
    firstNumber=input("输入'q'退出，请输入第一个数字：")
    if firstNumber=='q':
        Flag=False
        break;
    secondNumber=input("请输入第二个数字：")
    sumTwo=sum(firstNumber,secondNumber)
    print(sumTwo)
