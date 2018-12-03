while True:
    m=input("输入两个数字\n")
    m=int(m)
    n=input()
    n=int(n)
    try:
        print(m+n)
    except ValueError:
        print("输入的不是数字")


    if m=='q':
        break
