catsFile='cats.txt'
#储存文件名
dogsFile='dogs.txt'
#储存文件名

print("10-8")
#10-8的代码

try:
    with open(catsFile) as catsNames:
        #打开猫文件
        print("There are three cats:")
        cats=catsNames.read()
        print(cats)
        catsNames.close()
        #关闭文件
except FileNotFoundError:
    #找不到文件时打印提示语
    print("未找到文件"+catsFile)

try:
    with open(dogsFile) as dogsNames:
        #打开狗文件
        print("There are three dogs:")
        dogs=dogsNames.read()
        print(dogs)
        dogsNames.close()
        #关闭狗文件
except FileNotFoundError:
    #找不到文件时打印提示语
    print("未找到文件"+dogsFile)


print("\n10-9")
#10-9的代码
try:
    with open(catsFile) as catsNames:
        #打开猫文件
        print("There are three cats:")
        cats=catsNames.read()
        print(cats)
        catsNames.close()
        #关闭文件
except FileNotFoundError:
    #找不到文件时一言不发
    pass

try:
    with open(dogsFile) as dogsNames:
        #打开狗文件
        print("There are three dogs:")
        dogs=dogsNames.read()
        print(dogs)
        dogsNames.close()
        #关闭狗文件
except FileNotFoundError:
    #找不到文件时一言不发
    pass
