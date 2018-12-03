import json

file="number.json"
try:
    with open(file) as num:
        x=json.load(num)
except FileNotFoundError:
    with open(file,'w') as num:
        x=input("请输入你喜欢的数字")
        json.dump(x,num)
else:
    with open(file) as num:
        print("喜欢的数字是"+x)
