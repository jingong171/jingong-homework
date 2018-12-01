import json
#载入json

number=input("请输入你最喜欢的数字:")
filename='favor.json'

try:
    with open(filename,'w') as favor_numbers:
        #若无文件，则创建一个，若有，则修改
        json.dump(number,favor_numbers)
    with open(filename) as favor_numbers:
        number=json.load(favor_numbers)
        print("I know your favorite number!It's " + str(number))
except FileNotFoundError:
    #找不到文件错误处理
    print("未找到文件!")
