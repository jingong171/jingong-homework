import json

filename='favorite_Num.json'

##首先尝试直接打印文件'favorite_Num.json'里的数字（如果该文件存在的话）
try:
    with open(filename) as f_obj:
        favorite_num=f_obj.read()
        print("I know your favorite number!It's "+favorite_num+".")

##若不存在，则作如下解答
except FileNotFoundError:
    print("You haven't enter your favorite number.")
    favorite_num=input("Please enter：")

    filename='favorite_Num.json'

    with open(filename,'w') as f_obj:
        json.dump(favorite_num,f_obj)
    print("I know your favorite number!It's "+favorite_num+".")

