#引入json模块
import json

filename = 'number.json'
try:
    with open(filename) as f_object:
        number = json.load(f_object)
except FileNotFoundError:
    #提示用户输入喜欢的数字
    number = input("请您输入一个喜欢的数字")
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)
        print("I know your favorite number! It's "+number+".")
else:
    print("I know your favorite number! It's "+number+".")
