import json
filename = 'numbers.json'
try:
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
except FileNotFoundError:
    numbers = input("请输入您喜欢的数字：")
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)
        print("我们已经记录您喜欢的数字！")
else:     
    print("I konw your favorite number,it's:" + numbers + "!")
