while True: #循环
    num_1 = input("第一个数字：") #输入两个数字
    num_2 = input("第二个数字：")

    try:
        sum0 = int(num_1) + int(num_2) #加法运算

    except ValueError: #捕获错误
        print("这不是数字！") #错误提示

    else:
        print("结果是：" + str(sum0)) #无错误情况下的输出
