##10-6&10-7
#要求用户输入两个需要做加法的数字，并且告诉用户退出程序的方法
print("请输入两个需要做加法的数字")
print("输入字母'q'退出计算")

#用while循环构建加法计算器
while True:
    
    #用户输入‘q’时程序即停止运行
    first_num = input("\n第一个数字为：")
    if first_num == 'q':
        break
    second_num = input("第二个数字为：")
    if second_num == 'q':
        break

    #捕捉ValueError异常并打印错误提示信息
    try:
        outcome = int(first_num)+int(second_num)
    except ValueError:
        result="输入错误"
        print("您的输入中含有不是数字的内容，请输入数字")
    else:
        result=str(first_num)+"+"+str(second_num)+"="+str(outcome)
        print(result)
    #将运行完成的加法运算结果写入文件
    filename='outcome.txt'

    #使用附加到文件的方法保证历史记录不消失
    with open(filename,'a') as file_object:
        file_object.write(result+"\n")
