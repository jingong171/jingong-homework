while True:

    number_a=input("请输入一个数字：")
    number_b=input("请再输入一个数字：")
    #提示用户输入两个数字

    try:
        answer=int(number_a)+int(number_b)
    except ValueError:
        print("请输入数字！")
        #如果输入的不是数字，则给出提示
    else:
        print(answer)
        #如果是数字就给出答案
