print("Give me two numbers, and I'll plus them.")
print("Enter 'q' to quit.")
#while循环
while True:
    number1=input("Please enter the first number:")
    if number1=='q':
        break
    number2=input("Please enter another number:")
    if number2=='q':
        break
#try模块处理异常
    try:
        number1=int(number1)
        number2=int(number2)      
#抓取valueerror异常    
    except ValueError:
        print("You cannot input string message.")
    else:
        sum=number1+number2
        print("The result is "+str(sum)+".")
