import json
filename = "number.json"
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except   FileNotFoundError:
    print("请创建一个你喜欢的数字")
else:
    print(number)
