##10-6&10-7
#输入提示信息
print("请输入两个数字，我会对它们做加法。")
print("输入字母'q'停止计算。")

#可多次使用的加法计算器
while True:
    
    #用户输入q时可以停止运行
    first_num = input("\n第一个数：")
    if first_num == 'q':
        break
    second_num = input("第二个数：")
    if second_num == 'q':
        break

    #捕捉ValueError异常并打印错误提示信息
    try:
        answer = int(first_num)+int(second_num)
    except ValueError:
        result="输入错误"
        print("您的输入中含有不是数字的内容，请输入数字")
    else:
        result=str(first_num)+"+"+str(second_num)+"="+str(answer)
        print(result)
    #将完成的加法运算写入文件
    filename='加法计算器运行结果.txt'

    #使用附加到文件的方法保证历史记录不消失
    with open(filename,'a') as file_object:
        file_object.write(result+"\n")
