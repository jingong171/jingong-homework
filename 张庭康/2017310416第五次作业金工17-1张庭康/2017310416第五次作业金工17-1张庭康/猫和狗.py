#文件引用声明
firstfile = 'cats.txt'
lastfile = 'dogs.txt'

try:
    with open(firstfile) as first_object:
        content = first_object.read()
    with open(lastfile) as last_object:
        contents = last_object.read()
except FileNotFoundError:
    pass     #不做任何处理
else:
    print("文件cats.txt中内容为：\n"+content)
    print("文件dogs.txt中内容为：\n"+contents)
