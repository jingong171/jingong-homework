
try:
    objcat=open("cat.txt","r")
    objdog=open("dog.txt","r")


    print(objcat.read()),
    print(objdog.read()),
except FileNotFoundError:
    print("FileNotFoundError:找不到文件")#做一个友好的声明
