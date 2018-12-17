try:
    with open('C:/Users/孙林轩/Desktop/Dogs') as d:
        for line in d.readlines():
            print(line,end='')
    print()
    #令猫的名字和狗的名字之间有空行
    with open('C:/Users/孙林轩/Desktop/Cats') as c:
        for line in c.readlines():
            print(line,end='')
except FileNotFoundError:
    print('Cannot find file!')