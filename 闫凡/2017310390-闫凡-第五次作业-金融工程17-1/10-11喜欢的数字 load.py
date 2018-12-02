#导入json模块
import json
filename='favorite_num.json'
#读取数字
with open(filename) as file:
    favorite_num=json.load(file)
    print('I know your favorite number! It\'s '+favorite_num)
