import json
filename="love_number.json"

try:#如果有则执行
    with open(filename)as obj:
        love_number=json.load(obj)
except FileNotFoundError:
    love_number=input("请输入您喜欢的数字：")#如果没有则输入
    with open(filename,'w')as obj:
        json.dump(love_number,obj)
else:
    print("I know your farivate number!It's "+love_number+".")#输出
