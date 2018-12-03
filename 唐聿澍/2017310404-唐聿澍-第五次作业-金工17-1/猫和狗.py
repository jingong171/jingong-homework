try:#try模块
    with open('cats.txt') as catsList:#打开猫文件
        cats = catsList.readlines()#逐行读取


    with open('dogs.txt') as dogsList:#打开狗文件
        dogs = dogsList.readlines()#逐行读取

except FileNotFoundError:#错误抓取
    print()#一言不发

else:
    for cat in cats:#打印猫
        print(cat.title())
    for dog in dogs:#打印狗
        print(dog.title())
