print("请输入两个数字：")
while True:
    number1=input("数字1:")
    number2=input("数字2:")
    try:
        s=int(number1)+int(number2)
    except ValueError:
        print("请您输入数字而不是字符！")
        print("请您再次输入数字:")
    else:
        print(s)
            
        
            
    
