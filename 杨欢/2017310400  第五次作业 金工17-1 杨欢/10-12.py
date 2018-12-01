import json
#载入json

filename='favor.json'

try:
    with open(filename,'r') as favor_numbers:
        #读取文件
        number=json.load(favor_numbers)
except FileNotFoundError:
    #找不到文件则创建
    number=input("请输入你最喜欢的数字:")
    with open(filename,'w') as favor_numbers:
        json.dump(number,favor_numbers)
        print("I know your favorite number!It's " + str(number))
        #创建文件并读取
else:
    with open(filename) as favor_numbers:
        #若文件存在，则读取
        print("I know your favorite number!It's " + str(number))
