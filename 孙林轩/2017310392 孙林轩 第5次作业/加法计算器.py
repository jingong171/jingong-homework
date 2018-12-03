while True:
    """完成让用户重复输入"""
    try:
        a = int(input('Please enter a number:   '))
        b = int(input('Please enter another one:   '))
    except ValueError:
        print("You can only use numbers!")
    else:
        print(a + b)