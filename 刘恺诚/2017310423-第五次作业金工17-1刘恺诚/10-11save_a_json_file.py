import json
number=int(input("请输入一个你喜欢的数字"))

filename='likehood.json'
with open(filename,'w') as obj:
    json.dump(number,obj)
    

