
import json
filename = "number.json"
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except   FileNotFoundError:
    print("请创建一个你喜欢的数字")
    import json
    numbers=input("输入一个你喜欢的数字")
    filename="number.json"
    with open(filename,"w") as f_obj:
        json.dump(numbers, f_obj)
else:
    print(number)
