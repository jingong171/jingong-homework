import json

numbers=input("请输入您喜欢的数字：")
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj)
    print("我们已经记录您喜欢的数字！")
    
