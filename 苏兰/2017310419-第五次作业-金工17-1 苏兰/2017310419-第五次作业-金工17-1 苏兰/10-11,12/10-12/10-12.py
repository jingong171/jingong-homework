#使用json格式
import json

filename='favorite_number_2.json'

#将10-11中的程序合并起来
try:
    with open(filename)as f_obj:
        fav_num=json.load(f_obj)
#利用try_expect结构捕获异常
except FileNotFoundError:
    fav_num=input("请输入你最喜欢的数字：")
    with open(filename,'w')as f_obj:
        json.dump(fav_num,f_obj)
        print("我们会记住你最喜欢的数字!")
else:
    print("你最喜欢的数字是 "+fav_num)
        
