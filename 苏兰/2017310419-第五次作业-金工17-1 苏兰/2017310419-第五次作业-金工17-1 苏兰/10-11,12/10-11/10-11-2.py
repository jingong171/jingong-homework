#读取上一个文件中用户储存的数字并打印出来
import json

filename='favorite_number.json'
with open(filename) as f_obj:
    fav_num=json.load(f_obj)
    print("Your favorite number is "+fav_num)
