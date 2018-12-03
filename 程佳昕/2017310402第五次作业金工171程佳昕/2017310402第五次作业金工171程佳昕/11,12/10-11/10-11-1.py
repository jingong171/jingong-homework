#要求用户输入一个最喜欢的数字并把这个数字储存起来
import json

fav_num=input("请输入一个你最喜欢的数字：")

filename='favorite_number.json'
with open(filename,'w')as f_obj:
    json.dump(fav_num,f_obj)
