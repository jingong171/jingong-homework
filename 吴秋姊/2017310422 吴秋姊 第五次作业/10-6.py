
filename="10-6.txt"
#用append方式写入文件
with open(filename,'a') as file_object:
    number1=input("Please enter the first number:")
    number2=input("Please enter another number:")
    file_object.write("The first number is "+number1+".\n")
    file_object.write("The second number is "+number2+".\n")        
#处理文件异常用try模块
    try:
        number1=int(number1)
        number2=int(number2)      
    
    except ValueError:
        print("You cannot input string message.")
    else:
        sum=number1+number2
        file_object.write("The result is "+str(sum)+".\n")

