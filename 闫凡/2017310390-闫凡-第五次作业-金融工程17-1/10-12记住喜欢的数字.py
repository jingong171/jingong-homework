#导入json模块
import json
filename='favorite_num.json'
#尝试打开文件
try:
    with open(filename) as file:
        favorite_num=json.load(file)
#没有文件时提示用户存储数字
except FileNotFoundError:
    favorite_num=input('请输入你喜欢的数字')
    filename='favorite_num.json'
#存储数字
    with open(filename,'w') as file:
        json.dump(favorite_num,file)
#输出数字
else:
    print('I know your favorite number! It\'s '+favorite_num)
