print("Enter 'q' to stop.")
while True: #输入'q'退出
    a=input("Please enter the first number: ")
    if a=='q':
        break
    if a=='q':
        break
    b=input("Please enter the second number: ")
    try:
        c=int(a)+int(b)
    except ValueError:
        print("Please enter two integers!")
    else:
        print("The total number is "+c+".")
