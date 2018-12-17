import json

file="number.json"
with open(file,'w') as num:
    x=input("请输入你喜欢的数字")
    json.dump(x,num)
