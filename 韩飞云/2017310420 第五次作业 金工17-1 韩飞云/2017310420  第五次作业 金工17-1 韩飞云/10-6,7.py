print("这是一个对两个数相加的计算器。")
condition=input("若想停止，请您输入“q”。")#判断是否继续
while (condition!='q'):
    first_number=input("请您输入第一个数字：")#输入第一个数字
    try:
        fir_num=int(first_number)
    except ValueError:
        print("请您重新输入数字。\n")
    else:
        second_number=input("请您输入第二个数字：")#输入第二个数字
        try:
            sec_num=int(second_number)
        except ValueError:
            print("请您重新输入数字。\n")
        else:
            result=fir_num+sec_num
            print(first_number+"+"+second_number+"="+str(result)+'\n')#输出并进行循环
            condition=input("若想停止，请您输入“q”。")

            
