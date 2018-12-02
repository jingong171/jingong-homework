try:#尝试打开第一个文件
    with open('cat.txt') as cats:
        contents=cats.read()
except FileNotFoundError:
    print( "The file 'cat.txt' does not exist")
    pass#如果第一个文件打开失败就打印出语句并跳过，打开第二个文件
else:
    print(contents)

try:#尝试打开第二个文件
    with open('dog.txt') as dogs:
        contents=dogs.read()
except FileNotFoundError:
    print( "The file 'dog.txt' does not exist")
    pass#如果第一个文件打开失败就打印出语句并跳过，打开第二个文件
else:
    print(contents)
