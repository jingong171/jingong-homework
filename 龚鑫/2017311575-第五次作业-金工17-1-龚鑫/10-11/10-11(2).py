import json
filename='fav_number.json'

try:
    with open(filename) as f_obj:
        number=json.load(f_obj)
except FileNotFoundError:
    print("没找到文件")
else:
    print(number)

