try:
    with open('cats.txt') as file_cat:
        print('猫猫的名字')
        print(file_cat.read())
        #打印猫猫的名字
    with open('dogs.txt') as file_dog:
        print('狗狗的名字')
        print(file_dog. read())
        #打印狗狗的名字

except FileNotFoundError:
    pass
#找不到文件时一声不吭
