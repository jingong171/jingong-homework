import json
filename='favorite_number.json'
try:
    with open(filename) as f_obj:
        favorite_number=json.load(f_obj)
except FileNotFoundError:
    #如果没有存储就发出提醒
    print("Can not find favorite number.")
else:
    #如果存储就打印
    mgs="I know your favorite number!It's "+favorite_number
    print(mgs)