try:
    with open("dogs.txt") as fileobj:
        print("there are dogs:")
        for line in fileobj :
            print(line.rstrip())
    with open("cats.txt") as fileobj:
        print("there are cats:")
        for line in fileobj :
            print(line.rstrip())
except FileNotFoundError:
    """如果文件不存在则提示"""
    print("sorry,the file doesn't exit.")

try:
    with open("dogs.txt") as fileobj:
        print("there are dogs:")
        for line in fileobj :
            print(line.rstrip())
    with open("cats.txt") as fileobj:
        print("there are cats:")
        for line in fileobj :
            print(line.rstrip())
except FileNotFoundError:
    """找不到文件时一言不发"""
    pass