#提示用户输入喜欢的数字并储存
import json

fav_num=input("请输入你最喜欢的数字：")

filename='favorite_number.json'
with open(filename,'w')as f_obj:
    json.dump(fav_num,f_obj)
