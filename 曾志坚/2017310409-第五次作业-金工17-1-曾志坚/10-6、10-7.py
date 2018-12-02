while True:
    m=input("请输入两个数字\n")
    m=int(m)
    n=input()
    n=int(n)
    try:
        print(m+n)
    except ValueError:
        print("您输入的不是数字")


    if m=='q':
        break
