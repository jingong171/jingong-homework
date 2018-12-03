

while True:
    
    num_1=input("请输入一个数字(输入q退出）：")
    if num_1=='q':
        break
    num_2=input("请输入另一个数字（输入q退出）：")
    if num_2=='q':
        break
    try:
        answer=int(num_1)+int(num_2)
    except ValueError:
        print("请输入一个整数")
    else:
        filename='add.txt'
        with open(filename,'w') as obj:
            obj.write(str(answer))
            break
        
    
    
