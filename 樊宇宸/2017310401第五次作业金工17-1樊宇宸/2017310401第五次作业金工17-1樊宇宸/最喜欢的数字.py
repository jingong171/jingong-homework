import json
#如果已经存储了数字，就读取它
# 否则，就提示用户输入数字再加载它
filename='favorite_name.json'
try:
    """打开最喜欢的数字文本并读取其中的数字"""
    with open(filename) as f_obj:
        favorite_number=json.load(f_obj)
        #利用jason.load将数字读取出来
except FileNotFoundError:
    """如果文本不存在，即出现异常，就新建文本并输入最喜欢的数字写入进去"""
    favorite_number=input("What's your favorite number?")
    with open(filename,'w') as f_obj:
        json.dump(favorite_number,f_obj)
        #利用jason.dump写入数字
        print("We will remember your favorite number.")
else:
    """如果文本存在，即未出现异常，就显示出其中的数字"""
    print("I know your favorite number!It's "+favorite_number+".")
