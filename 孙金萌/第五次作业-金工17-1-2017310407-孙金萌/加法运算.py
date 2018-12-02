while True:
    A = input("Please enter the first number:")
    if A == 'q':
        break
    B = input("Please enter the second number:")
    if B == 'q':
        break
    try:
        sum=int(A)+int(B)
    except ValueError:
        print("请输入数字！")
    else:
        print(sum)
