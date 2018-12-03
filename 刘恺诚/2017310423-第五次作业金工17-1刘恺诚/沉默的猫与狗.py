
try:
    objcat=open("cat.txt","r")
    objdog=open("dog.txt","r")


    print(objcat.read()),
    print(objdog.read()),
except FileNotFoundError:
    pass#什么都不做，沉默不语
