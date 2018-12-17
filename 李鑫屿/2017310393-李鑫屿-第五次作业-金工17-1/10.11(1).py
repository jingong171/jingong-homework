import json
numbers=input("输入一个你喜欢的数字")
filename="number.json"
with open(filename,"w") as f_obj:
    json.dump(numbers, f_obj)
