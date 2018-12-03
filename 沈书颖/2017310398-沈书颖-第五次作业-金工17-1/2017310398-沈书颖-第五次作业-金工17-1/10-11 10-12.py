import json

filename='favorite_number.json'
try:
    with open(filename) as f_obj:
        favorite_number=json.load(f_obj)
        print("I know your favorite number is "+str(favorite_number))
        #读取文件中的数值，并打印信息
except FileNotFoundError:
    favorite_number=input("What's your favorit number?")
    with open(filename,'w') as f_obj:
        json.dump(favorite_number,f_obj)
        #如果没有输入过数字，则提示用户输入
